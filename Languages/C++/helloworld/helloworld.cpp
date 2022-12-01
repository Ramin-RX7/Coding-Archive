// C++ program to demonstrate working of regex_match() 
#include <iostream> 
#include <regex> 
#include <string.h>
#include <fstream>
#include <cstdlib>
#include <string>
#include <iterator>
using namespace std; 

string execute( string cmd, string file_name=""){
 if (file_name=="")
    system( ( cmd ).c_str() ) ; 
 else 
    system( ( cmd + " > " + file_name ).c_str() ) ; ifstream file(file_name) ;
 return { istreambuf_iterator<char>(file), istreambuf_iterator<char>() } ;
 }


int main(){

cout<< execute("whoami","xxx");






} 












// g++ -Wall -pedantic helloworld.cpp

// CMD Get Mac
/*
GETMAC
GETMAC /s computername
GETMAC /s 192.168.1.1 
GETMAC /s localhost
*/


// cmd output //
/*
#include <fstream>
#include <cstdlib>
#include <string>
#include <iterator>
string execute( string cmd, string file_name="Result.txt")
{
 system( ( cmd + " > " + file_name ).c_str() ) ; 
 ifstream file(file_name) ;
 return { istreambuf_iterator<char>(file), istreambuf_iterator<char>() } ;
}
*/


/*
#include <cstdlib> 
#include <ctime>
srand(time(0));
for (int x=0;x<5;x++){cout << rand() % 7 << ' ';};
*/