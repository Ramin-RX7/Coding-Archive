#include <iostream>
#include <memory>
#include <filesystem>

using namespace std;


string get_cmd_output(const char* cmd) {
    array<char, 128> buffer;
    string result;
    unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}


class Files{
    public:
        static void mkdir(string name){
            filesystem::create_directories(name);
        };
        static void write(string filename,string content){
            //fstream f(to_string())
        };
        static string read(string filename);
};


template <typename T>
void print(T inp,string end="\n"){
    cout << inp << end;
}




#include "./json.hpp"
using json = nlohmann::json;
static json get_database(){
    ifstream f("test.json");
    json j;
    f >> j;
    return j;
};




