using System;

namespace Tutor
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            
            // Console.;
        }
    }
}


/*
print:
    Console.WriteLine()  //Console comes from System
Console.
        beep
        clear
        equals
        ReadLine()
check for overflow:
    checked {
        byte num = 255;
        num =  num +1
    }
    // if there'll be a overflow, exception will be raised
with null:
    int? num1 = null;
property:
    private string color;
    public string Color {
        get { return color; }
        set { color = value; }
    }
    // or:
    public string Color {
        get {
            return color.ToUpper(); 
        }
        set { 
            if(value == "Red")
                color = value; 
            else
                Console.WriteLine("This car can only be red!");
        }
    }
Inheritance:
    public class Dog : Animal {
        // code
    }
    // use "base.attr" to access parent class attributes 
    // add "virtual" kw to be able to overriden
Interfaces
    similar to Abstract Classes But:
        No Instances are created.
        NO METHODS ARE ALLOWED AT ALL
    All Interfaces are Public
    There are NO access modifiers (public, private, protected etc.), 
        (because they are not allowed.)
foreach:
    foreach (int j in n ) {
        int i = j-100;
        Console.WriteLine("{0}", j);
    }
Lists:
    array to list:
        List<string> mylist = new List<string>(myarr);
    add collection to a list:
        mycollection.AddRange(animals);
    using System.Collections.Generic;
        .insert(index, item)
        .add(item)
        .InsertRange(index, collection)
        .Remove(item)
        .RemoveAt(index)
        .RemoveRange(index, n)
        .clear()
        .LastIndexOf("item")
        .Reverse()
Dictionaries:
    Dictionary<string, int> users = new Dictionary<string, int>();
    // or
    Dictionary<string, int> users = new Dictionary<string, int>()
    {
    { "John Doe", 42 },
    { "Jane Doe", 38 },
    { "Joe Doe", 12 },
    { "Jenna Doe", 12 }
    }; 

    if(users.ContainsKey(key))
    foreach (KeyValuePair<string, int> user in users)

Strings:
    .Clone()
    .Contains(item)
    .EndsWith() StartsWith()
    .Equals
    .IndexOf(item)
    .ToLower() .ToUpper()
    .Insert(index, item)
    .Split(item)
    .Remove(item)
    .Replace(item,new_item)
    .Substring(ind_f, ind_l)
    .Trim()

Structs

Enums:
    enum Days { Sun, Mon, tue, Wed, thu, Fri, Sat };
    int WeekdayEnd = (int)Days.Fri;

Files:
    read:
    using (var sr = File.OpenText(path)) {
            string s;
            while ((s = sr.ReadLine()) != null) {
                Console.WriteLine(s);
            }
        }
    write:
    var path = @"C:\Users\escap\Source\Repos\ConsoleApp1\ConsoleApp1\Main.cs";
    if (!File.Exists(path))
        using (var sw = File.CreateText(path))
        {
            sw.WriteLine("for (int i = 0; i<length; i++)");
        }








*/

