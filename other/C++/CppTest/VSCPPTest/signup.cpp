#include <iostream>
#include <memory>
#include <filesystem>
#include <vector>
#include <fstream>
using namespace std;





template <typename T>
void print(T inp,string end="\n"){
    cout << inp << end;
}
void pause(){
    cout << flush;
    system("pause");
}


class Person{
    private:
        //static int current_available_id;
        string fname,lname,ID;

    public:
        Person(string first_name,string last_name,string id)
            :fname(first_name),lname(last_name),ID(id){
        }
        string get_name(){
            return fname+string(" ")+lname;
        }
};

vector<Person> people_list;
int current_available_id = 1;


vector<string> split(string s,string del=" "){
    int start = 0;
    int end = s.find(del);
    vector<string> v;
    while (end != -1){
        //  print(s.substr(start,end-start));
        v.push_back(s.substr(start,end-start));
        start = end+del.size();
        end=s.find(del,start);
    }
    v.push_back(s.substr(start,end-start));
    return v;
}

vector<Person> load_database(){
    vector<string> db;
    string s;
    ifstream f("./signup_db.txt");
    while (getline(f,s)){
      	// cout << s;
      	db.push_back(s);
    }
    f.close();
    vector<Person> DB;
    //print(db.size());
    for (int i=0;i<db.size();i+=1){
        // print(i);
        vector<string> v = split(db[i]);
        DB.push_back(Person(v[0],v[1],v[2]));
        current_available_id++;
    }
    return DB;
}

void save_db(){
    string s;
    for (int i=0;i<people_list.size();i++){
        s += people_list[i].get_name() + " " + to_string(i+1) + "\n";
    }
    ofstream f("./signup_db.txt");
    f << s;
    f.close();
}


void add_person(){
    string fname;
    print("\nEnter First Name: ","");
    cin >> fname;
    cin.ignore();
    string lname;
    print("Enter Last Name: ","");
    cin >> lname;
    cin.ignore();
    Person newone(fname,lname,to_string(current_available_id));
    people_list.push_back(newone);
    save_db();
    print(string("\nAdded \"")+fname+string(" ")+lname+string("\" With id ")+to_string(current_available_id));
    current_available_id++;
    pause();
};

void print_people_list(){
    print("\nID  NAME");
    print("--------------------");
    for (int i=0;i<people_list.size();i++)
        print(to_string(i+1)+string("   ")+people_list[i].get_name());
    print("");
    pause();
}

void del_person(){
    print("0-EXIT");
    for (int i=0;i<people_list.size();i++)
        print(to_string(i+1)+string("-")+people_list[i].get_name());
    print("\nEnter Your Choice: ","");
    while (true){
        int m;
        cin >> m;
        cin.ignore();
        if (m==0){break;}
        else if (m>0 & m<=people_list.size()){
            string name = people_list[m-1].get_name();
            people_list.erase(people_list.begin()+m-1);
            print(string("\"")+name+string("\" is removed"));
            current_available_id--;
            save_db();
            pause();
            break;
        }
        else {
            cout << flush;
            system("CLS");
            print("INVALID INPUT");
            break;
        }
    }
}


int menu(){
    print("\n\n\t\t1-Add Person");
    print("\t\t2-Delete Person");
    print("\t\t3-List People");
    print("\t\t4-Exit");
    print("Enter your choice: ","");
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
    // return 0;
}




int main(){

    people_list = load_database();
    
    while (true){
        int choice = menu();
        switch (choice)
        {
        case 1:
            add_person();
            break;
        case 2:
            del_person();
            break;
        case 3:
            print_people_list();
            break;
        case 4:
            return 0;
        }
        cout << flush;
        system("CLS");
    }

    return 0;
}
