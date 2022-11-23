'''
This Module is one to make your code shorter.
Collection of most usefull function and methods from popular modules of python.

FEATURES:
 - print   ==>                           p
 - re(Function_Name,Times) :             "repeat a function for certain times"
 - a[::-1] ==>                           rev(a)       (you can also use integers: 158 ==> 851)
 - read(file_path) :                     return content of the file
 - write(file_path) :                    write things you want in file you want. (Read Help)
 - time.sleep(seconds) ==>               wait(sec)
 - cls() :                               function to clear the console and terminal.
 - progressbar() :                       function for creating in-app progressbar. (Read Help)
 - string(First_Letter,Last_Letter) :    return a string from first argumant until second argumant (Only integer or letter). 
 - exists(path) :                        return True if file exists. else False.
 - CLASS rand:                           1- item(population) :        "random item from population."
                                         2- integer(First,Last) :     "random integer between First and Last"
                                         3- O1(decimal_number=17) :   "random float between 0 and 1. Default rounding is 17"
                                         4- number(First,Last):       "random number(integer or float) between First and Last"
 - CLASS Math:                                         
                                         1- sqrt(number):             "return square root of number."


Written By RX
Last Update: 1-30-2020
'''

def p(ex,rep=None):
    '''
    p is print!
    But because we use it a lot, we\'ve decided to make it one letter.
    Example:
        p('Hello World')
        ==>Hello World
    Example:
        p('Hello <>. How are you?','World')
        ==>Hello World. How are you?
    '''
    Ex=ex
    if rep!=None:
        Ex= ex.replace('<>',rep)
    print(Ex)


def re(Function_name,Times):
    '''
    re is for repeating a function.
    for more info see the example below.
    Example:
        re(Func_Name, 3)
        ==> "function Func_Name will launch 3 times."
    '''
    i=1
    while i <= Times:
        i+=1
        Function_name() 


def rev(ex):
    '''
    This function is for reversing Strings, Lists, Tuples And also Integers.
    Example:
        b= rev('Football')
        print(b)
        ==> llabtooF
    '''
    if type(ex)==int:
        ex= str(ex)
        ex= ex[::-1]
        ex= int(ex)
    else:
        #global ex
        ex= ex[::-1]
        #print(ex)
    return ex


def read(file):
    '''
    This can help you to read your file faster.
    Example:
        read_file('C:\\users\\Jack\\test.txt')
        ==> "Content of 'test.txt' will be shown."
    '''
    op= open(file,mode='r')
    FileR= op.read()
    op.close()
    return FileR
    #print(FileR)
    


def write(file,mode='replace',text=None):
    if mode=='replace':
        op= open(file,mode='w')
        if text==None:
            text= input('Type what you want.\n\n')
        op.write(text)
        print('File has been created/changed.')
        op.close()
    elif mode=='continue':
        opr= open(file,mode='r')
        FileR= opr.read()
        op= open(file,mode='w')
        if text==None:
            text= input('Type what you want to add in the end of the file.\n\n')
        op.write(FileR+'\n'+text)
        print('File has been created/changed.')
        op.close() 
    else:   
        print('Error\nmode can only be: 1-replace(default)  2-continue\nNot "{0}"'.format(mode)) 


def wait(seconds):
    '''
    Use this if you want your program wait for a certain time.
    Example:
        wait(3)
        ==> "Nothing happen and there will be no calculation for 3 seconds"
    '''
    import time
    time.sleep(seconds)

SQ__= 'powernrxbetfromporto'
def cls():
    '''
    You can use this function if you want to clear the environment.
    '''
    import os
    os.system('cls')


def progressbar(Total=100,Dashes_Nom=100,Time=1,Dashes_Shape='-',Complete_Shape='#',Pre_Text='Loading: '):
    '''
    Use this function to make a custom in-app progress bar.
    Example:
        progressbar(Total=100,Dashes_Nom=100,Time=1,Dashes_Shape='-',Complete_Shape='#', Pre_Text='Loading')
        ==>   Loading: [####------] 40/100
    '''
    import sys
    def Progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write("%s[%s%s] %i/%i\r" % (prefix, Complete_Shape*x, Dashes_Shape*(size-x), j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()
    import time
    for i in Progressbar(range(Total), Pre_Text, Dashes_Nom):
        time.sleep(Time)


def string(First_Letter='a',Last_Letter='z'):
    if type(First_Letter)==type(Last_Letter):
        if type(First_Letter)==str:
            Alfa='abcdefghijklmnopqrstuvwxyz'
            for i in range(26):
                if Alfa[i] == First_Letter:
                    fi= i
                if Alfa[i] == Last_Letter:
                    li= i+1
            strin= Alfa[fi:li]
            return strin
        elif type(First_Letter)==int:
            strin=''
            i=First_Letter
            for i in range(First_Letter,Last_Letter+1):
                strin= strin+str(i)
            return strin
        elif type(First_Letter)!=int and type(First_Letter)!=str:
            print('Invalid input for argumant(s).\n{0}&{1} are {2}.\nBut Valid input should have "str" or "int" type.'.format(First_Letter,Last_Letter,type(First_Letter)))
    else:
        print('Invalid input.\nFirst argumant is {0} And Second argumant is {1} \nArgumants should have the same type.'.format(type(First_Letter),type(Last_Letter)))


def exists(file_path):
    '''
    Search for the file And Returns a boolean.
    if file exists: True
    else: False
    '''
    import os
    return os.path.exists(file_path)


def keyboard(button):
    import pyautogui
    pyautogui.press(button)





class rand:
    def choice(item):
        import random
        return random.choice(item)
    def integer(first_number,last_number):
        import random
        return random.randint(first_number,last_number)
    def O1(decimal_number=17):
        import random
        return round(random.random(),decimal_number)
    def number(first_number,last_number):
        import random
        return random.uniform(first_number,last_number)        



class Math:
    def sqrt(number):
        import math
        return math.sqrt(number)
