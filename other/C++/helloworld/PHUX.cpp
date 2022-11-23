#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <iterator>
#include <bits/stdc++.h>
using namespace std;


string execute( string cmd, string file_name=""){
 if (file_name=="")
   system( ( cmd ).c_str() ) ; 
 else 
   system( (cmd + " > " + file_name).c_str() ); ifstream file(file_name);
 return { istreambuf_iterator<char>(file), istreambuf_iterator<char>()};
 }



int main()
{clock_t start, end; start = clock(); 
 printf("Getting Wifi Passwords...\n");
/*
 regex exp(": .*");
 smatch res;
 string GET_NAMES= execute("netsh wlan show profile");
 string NAMES="";
 string arr[1]={"Test"};int i=0;
 while (regex_search(GET_NAMES, res, exp)) {
    string NAME= res[0].str().substr(2,20);
    NAMES+= NAME + "  -  ";
    GET_NAMES = res.suffix();

    arr[i]=NAME;i++;
    }
 cout << NAMES;
 cout << NAMES.length();
    //
*/

/*
 string NAME_PASS="";   //string arr[]={};int i=0;
 regex exp("Key Content.*");
 smatch res;
 for (string out: arr){
  string GET_PASS= execute("netsh wlan show profile "+out+" key=clear");
  
  while (regex_search(GET_PASS, res, exp)) {
     string PASSWORD= res[0].str().substr(11,20);
     NAME_PASS+= out+": "+PASSWORD+"\n";
     GET_PASS = res.suffix();
     } 
   }
 cout<<NAME_PASS
*/
 printf("Done.\n");

 cout << endl;

 printf("Getting System Information...\n");
  execute("systeminfo","SystemINFO");
 printf("Done.\n");

 cout << endl;

 printf("Getting INFO...\n");
  string result;
  result+= "Mac Addresses:" + execute("GETMAC")+"\n\n";
  ofstream Info("Info") ;
  Info << result;
  Info.close();
 printf("Done.");



end = clock(); 

double time_taken = double(end - start) / double(CLOCKS_PER_SEC); 
cout << "\n" << time_taken; 
string x;
cin >>x;
}
