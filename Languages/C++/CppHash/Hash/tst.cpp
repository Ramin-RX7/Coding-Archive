#include <iostream>
using namespace std;
#include <chrono>
using namespace std::chrono;
#include <vector>
#include "json.hpp"
using json = nlohmann::json;


#include "md5.h"

template <typename T>
void print(T value){
    cout << value << endl;
}


vector<vector<char>> table_creator(string alphabet, string key="", int width=5){
    // Remove duplicate chars from key
    for ( std::string::size_type i = 0; i < key.size(); i++ ){
        std::string::size_type j = i + 1;
        while (j < key.size()) {
            if ( key[i] == key[j] ){key.erase( j, 1 );}
            else {++j;}
        }
    }
    
    vector<char> alpha;  // this will be used to make the table
    // Adding key to beginning of "alpha"
    for (int i=0; i<=key.size();i++){
        alpha.push_back(key[i]);
        // print(key[i]);
    }
    // Adding rest of alphabet to alpha
    for (int i=0; i<=alphabet.size();i++){
        if (!(std::count(key.begin(),key.end(), alphabet[i]))) {
            alpha.push_back(alphabet[i]);
            // print(alphabet[i]);
        }
    }

    vector<vector<char>> table;
    for (int i=0;i<=width;i++){
        table.push_back(vector<char>());
        for (int j=0;j<=width;j++){
            table[i].push_back(alpha[width*i + j]);
        }
    }
    return table;

}





string adfgx_encrypt(){

}









int main(){

    const auto START = high_resolution_clock::now();
    


    auto mytable = table_creator("abcdefghijklmnopqrstuvwxyz","ramin");
    for (vector<char> row: mytable){
        for (auto cell: mytable){
            for (auto fcell: cell){
                print(fcell);
            }
        }
    }
    /*
    int myi = 100;
    while (myi<5000000){
        table_creator("abcdefghijklmnopqrstuvwxyz",".raaminram");
        // string s = table_creator("abcdefghijklmnopqrstuvwxyz","raaminram");
        // cout << s << endl;
        break;
        myi++;
    }
    */




    const auto STOP = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(STOP - START);
    cout << "Proccess Finished in " << duration.count() << " milliseconds" << endl;


    return 0;
}