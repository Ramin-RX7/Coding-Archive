#include <iostream>
// #include <cstdlib> //
#include <algorithm> 


using namespace std;

int kabise[]={
    1210,1214,1218,1222,1226,1230,1234,1238,1243,1247,1251,1255,1259,1263,1267,1271,1276,
    1280,1284,1288,1292,1296,1300,1304,1309,1313,1317,1321,1325,1329,1333,1337,1342,1346,
    1350,1354,1358,1362,1366,1370,1375,1379,1383,1387,1391,1395,1399,1403,1408,1412,1416,
    1420,1424,1428,1432,1436,1441,1445,1449,1453,1457,1461,1465,1469,1474,1478,1482,1486,
    1490,1494,1498
};
// INP%4=0 and x%100!=0 ()

int mil_months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int sham_months[12] = {31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29};

int sham_b_year=1207,sham_b_month=1,sham_b_day=1;
int mil_b_year =1828,mil_b_month=3 ,mil_b_say=21;



void mil_to_sham(int year,int month,int day){
    if (year < mil_b_year) throw;  if (month > 12) throw;  if (day > 31)  throw;

    //> days passed in milady 
    //] Days of all years but the last year
    int nom_of_days = 0;//-81 //not calculating first 3 month
    int nom_of_kabises = 0;
    for (int i=mil_b_year; i<year ;i++){
        nom_of_days+=365;
        if (i%4==0 && i%100!=0)  nom_of_days+=1;
    }
    // cout << "✓Nom of days1  : " << nom_of_days << endl;
    //] Days of last year
    for (int i=0; i<month-1 ;i++){
        nom_of_days += mil_months[i];
    }
    // cout << "✓Nom of days2  : " << nom_of_days << endl;
    nom_of_days += day-1;
    cout << "?<2-3> Nom of days1  : " << nom_of_days << endl;

    //> add days to shamsi beggining date
    int sham_year = sham_b_year;
    nom_of_kabises = 0;
    int* kabise_end = end(kabise);
    for (int i=sham_b_year; i<sham_b_year+(year-mil_b_year) ;i++){
        nom_of_days-=365;
        if (find(kabise,kabise_end,i) != kabise_end)  {nom_of_days-=1;};
        sham_year++;
    }
    cout << "Nom of rem days1: " << nom_of_days << endl;
    cout << "sham year       : " << sham_year << endl;
    






    int sham_month = 1;
    for (int i=1;i<=12;i++){
        // if (i<=3){
        //     if (i>=1){nom_of_days+=mil_months[i];}
        //     if (i>=2){nom_of_days+=mil_months[i];}
        //     if (i==3){nom_of_days+=21;}
        // }
         if (i>=month){
            break;
        }
        else {
            sham_month++;
        }
        nom_of_days -= sham_months[i];
    }
    cout << "sham month      : " << sham_month << endl;

    cout << "Nom of rem days2: " << nom_of_days << endl;






};










int main(){


    mil_to_sham(2010,5,10);



    return 0;
};
