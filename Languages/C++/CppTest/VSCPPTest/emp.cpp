#include <iostream>
#include <ctime>
#include <fstream>
#include <filesystem>

#include <unistd.h>

using namespace std;



//#include <cstdio>
#include <memory>
#include "./json.hpp"
using json = nlohmann::json;

#include "EmpLib.hpp"



int today_mday = 1;

json database = get_database();











// class Time;  //Declaring "Time" bcz it's used in "Employee"  (!:: No, Not used)=>(Commented)



class Employee{ 
    private:
        //friend class Time; 
        string name;
        int salary;
        static int id;

    public:
        Employee(string Name,int Salary):
            name(Name),salary(Salary){
            print("Estekhdaame \"" + name + "\"" + "  (Hoghoogh:\"" + to_string(salary) + "\")");
        };
        string get_name(){
            return name;
        };
        int get_salary(){
            return salary;
        };
        void enter();
        void leave();
};



// Set Employee Check in/out 
enum move_type{Enter,Leave};
class Set_Check{
    public:
        static void set_enter_leave(Employee *emp,move_type type_);//string type_){
        static void set_enter(Employee *emp); //
        static void set_leave(Employee *emp);
};



class Time{
    public:
        Time(){
            time_t epoch = time(NULL);
            tm *t = localtime(&epoch);
            int year = t->tm_year;int month = t->tm_mon;int day = t->tm_mday;
            int hour = t->tm_hour;int minute= t->tm_min;int second = t->tm_sec;
            set_time(year,month,day,hour,minute,second);
        };
        void print_time(){
            cout << second << endl;
        };
        
    private:
        int year,month,day,hour,minute,second;
        void set_time(int year,int month,int day,int hour,int minute,int second){
            this->year   =  year;
            this->month  =  month;
            this->day    =  day;
            this->hour   =  hour;
            this->minute =  minute;
            this->second =  second;
        };
        //friend void Employee::set_enter();
        friend void Set_Check::set_enter_leave(Employee *emp,move_type type_);//string type_){
};



void Set_Check::set_enter_leave(Employee *emp,move_type type_){//string type_){
    Time t;
    if (today_mday>t.day){
        //Backup
        today_mday = t.day;
        print("New Day");    
    }

    char fmt_buf[100];
    sprintf(fmt_buf,"%d:%d:%d",t.hour,t.minute,t.second);
    database[to_string(t.month)][to_string(t.day)][type_][emp->get_name()] = fmt_buf;

    std::ofstream f("pretty.json");
    f << std::setw(4) << database << std::endl;
    string msg;
    if (type_==Enter){
        msg = "Vorood"  ;}
    else if (type_==Leave){
        msg = "Khorooj" ;}
    else { throw 1;}

    print(msg+"e "+emp->get_name()+" Sabt Shod ("+fmt_buf+")");

};



void Employee::enter(){
    Set_Check::set_enter_leave(this,Enter);
};
void Employee::leave(){
    Set_Check::set_enter_leave(this,Leave);
};

Employee add_employee(){
    string name;
    print("Enter Name: ","");
    getline(cin,name);
    print("Enter Salary [5000]: ");
    int salary=0;
    cin >> salary;
    if (!salary){
        salary = 5000;
    }
    print(salary);
    Employee emp(name,salary);
    return emp;

}


int menu(){
    print("\n\n\t\t1-Add Employee");
    print("\t\t2-Employee Enter");
    print("\t\t3-Employee Leave");
    print("\t\t4-Print This Month List");
    print("\n\nEnter Your Choice: ","");
    string m;
    getline(cin,m);
    while (true){
        int m;
        cin >> m;
        cin.ignore(); //numeric_limits<streamsize>::max(),'\n'
        switch (m){
            case 1:
            case 2:
            case 3:
            case 4:
                return m;
            default:
                cin.clear();
                cout << flush;
                system("CLS");
                print("INVALID INPUT");
        }
    }

};












int main(){

    
    add_employee();

    // Employee e1("Ali",20);
    // e1.enter();
    



}