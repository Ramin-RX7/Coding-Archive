#include <iostream>
using namespace std;
#include <chrono>
using namespace std::chrono;
#include "json.hpp"
using json = nlohmann::json;




int main(){

    const auto START = high_resolution_clock::now();
    
    json database;
    database["bubbles"]["1000"] = false;
    cout << database << endl;
    
    const auto STOP = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(STOP - START);
    cout << "Proccess Finished in " << duration.count() << " milliseconds" << endl;


    return 0;
}