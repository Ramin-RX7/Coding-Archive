#include "RX7.hpp"
#include <iostream>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <memory>
#include <vector>

#include "json.hpp"
using json = nlohmann::json;


using namespace std;




#include <tuple>
tuple<string,int> get_pers(){
    return {"Ramin",18};
}


int main(){
    cout << "Start" << endl;


    auto[name,age] = get_pers();
    print(name);
    print(age);
    

    
    




    cout << "End";
}

























/*
// Get cmd output
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

*/

/*
template <typename T>
void print(T arr){
    int n = sizeof(arr) / sizeof(arr[0]);
    int i =0;
    while (i<n) {
    cout<<arr[i]<<endl;
    i++;
  }
}
}
*/

