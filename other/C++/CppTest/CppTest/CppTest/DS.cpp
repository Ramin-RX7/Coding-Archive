#include <iostream>
#include <string>
using namespace std;
#include <chrono>
using namespace std::chrono;
#include <algorithm>
#include <vector>
#include <fstream>
#include <filesystem>

#include "json.hpp"
using json = nlohmann::json;


void print(string str){
    cout << str << endl;
}


void bubbleSortV(vector<int>& a)
{
      bool swapp = true;
      while(swapp){
        swapp = false;
        for (size_t i = 0; i < a.size()-1; i++) {
            if (a[i]>a[i+1] ){
                a[i] += a[i+1];
                a[i+1] = a[i] - a[i+1];
                a[i] -=a[i+1];
                swapp = true;
            }
        }
    }
}


void insertionSort (vector<int>& data, int n){
    int i, j, tmp;

    for (i=1; i<n; i++){
        j=i;
        tmp=data[i];
        while (j>0 && tmp<data[j-1]){
            data[j]=data[j-1];
            j--;
        }
        data[j]=tmp;
    }
}


void MergeSortedIntervals(vector<int>& v, int s, int m, int e) {
	
    // temp is used to temporary store the vector obtained by merging
    // elements from [s to m] and [m+1 to e] in v
	vector<int> temp;

	int i, j;
	i = s;
	j = m + 1;

	while (i <= m && j <= e) {

		if (v[i] <= v[j]) {
			temp.push_back(v[i]);
			++i;
		}
		else {
			temp.push_back(v[j]);
			++j;
		}

	}

	while (i <= m) {
		temp.push_back(v[i]);
		++i;
	}

	while (j <= e) {
		temp.push_back(v[j]);
		++j;
	}

	for (int i = s; i <= e; ++i)
		v[i] = temp[i - s];

}
void MergeSort(vector<int>& v, int s, int e) {
	if (s < e) {
		int m = (s + e) / 2;
		MergeSort(v, s, m);
		MergeSort(v, m + 1, e);
		MergeSortedIntervals(v, s, m, e);
	}
}


void swap(vector<int>& v, int x, int y) {
    int temp = v[x];
    v[x] = v[y];
    v[y] = temp;
}
void quicksort(vector<int> &vec, int L, int R) {
    int i, j, mid, piv;
    i = L;
    j = R;
    mid = L + (R - L) / 2;
    piv = vec[mid];

    while (i<R || j>L) {
        while (vec[i] < piv)
            i++;
        while (vec[j] > piv)
            j--;

        if (i <= j) {
            swap(vec, i, j); //error=swap function doesnt take 3 arguments
            i++;
            j--;
        }
        else {
            if (i < R)
                quicksort(vec, i, R);
            if (j > L)
                quicksort(vec, L, j);
            return;
        }
    }
}







void printVector(vector<int> a, int n=0){
    if (n == 0){ n=a.size();}
    for (size_t i=0;  i<n  ;i++)
        cout<<a[i]<<" ";
    cout<<endl;
}


vector<int> make_random_vector(int n){
    vector<int> values(n); 
    auto f = []() -> int { return rand() % 100000; };
    generate(values.begin(), values.end(), f);
    return values;
}


vector<int> make_length(int start, int last, int step){
    vector<int> ret;
    int m = start;
    while (m<=last){
        ret.push_back(m);
        m += step;
    }
    return ret;
}








int main(){
    const auto START = high_resolution_clock::now();


    auto bubbles    =   make_length(1000   ,20000  ,10000);
    auto insertions =   make_length(4000   ,60000  ,4000);
    auto merges     =   make_length(250000 ,4000000,250000);
    auto quicks     =   make_length(500000 ,7500000,500000);
    vector<int> sorts[] = {bubbles,insertions,merges,quicks};
    string sorted_names[] = {"bubble","insertion","merge","quick"};

    json database;
    int i = 0;
    vector<int> values;    
    for (auto sort_len_list: sorts){
        print(sorted_names[i]);
        for(int len:sort_len_list){
            values = make_random_vector(len);
    
            auto start = high_resolution_clock::now();
            switch (i){
                case 0:  bubbleSortV(values);break;
                case 1:  insertionSort(values,len);break;
                case 2:  MergeSort(values,0,len-1);break;
                case 3:  quicksort(values,0,len-1);break;
                default: break;
            }
            quicksort(values,0,len-1);
            auto stop = high_resolution_clock::now();

            auto duration = duration_cast<microseconds>(stop - start);
            cout << "Time taken by " << len << ": " << duration.count() << " microseconds" << endl;
            database[sorted_names[i]][to_string(len)] = duration.count();
            // printVector(values, 5);
        }
        i += 1;

    }
    
    std::ofstream f("database.json");
    f << std::setw(4) << database << std::endl;

    const auto STOP = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(STOP - START);
    cout << "Proccess Finished in " << duration.count() << " milliseconds" << endl;

    return 0;
}




//> JSON
/*
#include "./json.hpp"
using json = nlohmann::json;
static json get_database(){
    ifstream f("test.json");
    json j;
    f >> j;
    return j;
};

json database = get_database();

std::ofstream f("pretty.json");
f << std::setw(4) << database << std::endl;
*/