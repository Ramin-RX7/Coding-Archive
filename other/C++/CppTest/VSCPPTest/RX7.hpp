#include <iostream>
#include <memory>
#include <chrono>
#include <thread>
#include <unistd.h>
#include <time.h>
using namespace std;



template <typename T>
void print(T inp,string end="\n"){
    cout << inp << end;
}

template <typename T,typename... Ts>
void repeat(T f,int n,Ts... args){
    for (int i=1;i<=n;i++){
        f(args...);
    }
}

void wait(unsigned int seconds){ //<unistd.h>
    //<chrono,thread>
    //this_thread::sleep_for(chrono::seconds(seconds));
    sleep(seconds);
}
#define sleep wait

void clear(){
    #ifdef _WIN32
    "CLS"
    #else
    "clear"
    #endif
;}
#define cls clear

void progressbar();

void wait_for();

template <typename T>
void call_later(T func,float delay);
#define call call_later

string convert_bytes(int nom);

// template <typename T>
void restart_app(string filename);

string active_window_title();

void open_image(string path);

void download();

void extract();

void screenshot();

void func_info();

template <typename T>
T Progressbar();

int* pixel_color()
    //int* arr = new int[2];
    //static int arr[2];
;

void include_lib(string path);




template <typename T>
T* force(T arr[],T item){
    int size = sizeof(*arr)/sizeof(T);
    T newarr[size+1];
    for (int i=0;i<size;i++){
        newarr[i] = arr[i];
    }
    newarr[size] = item; 
    return newarr;
};

template <typename T>
T* erase(T arr[],T item);

template <typename T>
T* replace(T arr[],int index,T item);

template <typename T>
T* insert(T arr[],int index,T item);

template <typename T>
T* pop(T arr[],int index);



class Random{
    public:
        static void seed(int s=time(NULL)){
            srand(s);
        };

        template <typename T>
        static void choose(T iter[]){
            int size = sizeof(*iter)/sizeof(T);
            print(sizeof(iter));
            //return iter[]iter[rand()%size];
        };

        static int integer(int first_nom,int last_nom){
            return rand()%(last_nom-first_nom+1)+first_nom;
        }
};















/*




string get_cmd_output(const char* cmd) { //<memory>
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

*/