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
        // static int current_available_id;
        string fname,lname,ID;

    public:
        Person(string first_name,string last_name,string id)
        :fname(first_name),lname(last_name),ID(id){
        }
        string get_name(){
            return fname+string(" ")+lname;
        }
        
        explicit operator bool(){
            if (stoi(ID)){return true;}
            return false;
        }
        Person *next;


};


static vector<Person> people_list;
int current_available_id = 1;
Person* P = NULL;


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

Person* load_database(Person **p){
    vector<string> db;
    string s;
    ifstream f("./su_db.txt");
    while (getline(f,s)){
      	// cout << s;
      	db.push_back(s);
    }
    f.close();
    //print(db.size());
    Person *head = *p;
    for (int i=0;i<db.size();i+=1){
        // print(i);
        vector<string> v = split(db[i]);

        Person *last = *p;
        Person* newone = new Person(v[0],v[1],v[2]);
        if (*p == NULL){
            *p = newone;
        }
        else {
            print("asdf");
            while (last->next != NULL){
                last = last->next;
            }
            print("fdas");
            last->next = newone;
        }
        current_available_id++;
    }


    return *p;
}

void save_db(Person *p){
    string s;

    int i = 0;
    while (p != NULL){
        s +=  p->get_name()+" "+to_string(i+1)+"\n";
        p = p->next;
        i++;
    }
    ofstream f("./su_db.txt");
    f << s;
    f.close();
}


void add_person(Person** p){
    string fname;print("\nEnter First Name: ","");cin >> fname;cin.ignore();
    string lname;print("Enter Last Name: ","");cin >> lname;cin.ignore();
    Person* newone = new Person(fname,lname,to_string(current_available_id));
    newone->next = NULL;
    if (*p == NULL){
        *p = newone;
    }
    else {
        Person *last = *p;
        while (last->next != NULL){
            last = last->next;
        }
        last->next = newone;
    }
    save_db(*p);
    print(string("\nAdded \"")+fname+string(" ")+lname+string("\" With id ")+to_string(current_available_id));
    current_available_id++;
    pause();
};

int print_people_list(Person *p,bool print_detail=true){
    if (print_detail){
    print("\nID  NAME");
    print("--------------------");
    }
    int i = 0;
    while (p != NULL){
        print(to_string(i+1)+string("   ")+p->get_name());
        p = p->next;
        i++;
    }
    return i;
}

void del_person(Person **p){
    print("\n\n0-EXIT");
    int i = 0;
    i = print_people_list(*p,false);
    print("\nEnter Your Choice: ","");
    while (true){
        int m;
        cin >> m;
        cin.ignore();

        if (m==0){break;}
        else if (m>0 & m<=i){
            m = m-1;
            Person* p2= *p;
            if (m==0){
                *p = p2->next;
                string name = p2->get_name();
                delete p2;
                print(string("\"")+name+string("\" is removed"));
                save_db(*p);
                pause();
                return;
            }
            for (int i=0;p2!=NULL && i<m-1;i++){
                p2 = p2->next;
            }

            Person *next = (p2->next)->next;
            string name = p2->next->get_name();
            delete p2->next;
            p2->next = next;

            print(string("\"")+name+string("\" is removed"));
            save_db(p2);
            pause();
            break;
        }
        else {
            pause();
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
    




    return 0;
}




int main(){

    





    //P = load_database(&P);
    //add_person(&P);
    //add_person(&P);
    //add_person(&P);
    

    while (true){
        int choice = menu();
        switch (choice)
        {
        case 1:
            add_person(&P);
            break;
        case 2:
            del_person(&P);
            break;
        case 3:
            print_people_list(P);
            pause();
            break;
        case 4:
            return 0;
        }
        cout << flush;
        system("CLS");
    }

    return 0;
}
