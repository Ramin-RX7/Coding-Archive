#from rx import *


"""
import sys,time

def progressbar(it, prefix="", size=50, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "-"*x, " "*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

for i in progressbar(range(100)):
    time.sleep(0.05)
"""


































#decor text or func
"""
def decoorr(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

@decoorr
def print_text():
  print("Hello world!")

print_text()
"""




"""class main:
    def __init__(self,name,age,password):
        self.name= name
        self.age= age
        self.password= password
        Credit= 20000
yname= input('Type your name: ')
yage= int(input('Type your age: '))
ypass= input('Type your password: ')

USER= main(yname,yage,ypass)
print('hello {0}'.format(USER.name))
"""
"""
Password=None
di= {'1':'@','2':'#','3':'$','4':'%','5':'^','6':'&','7':'*','8':'(','9':')','0':'!'}
def dec(ex):
    global Password
    Password= Password.replace(ex,di[ex])



Password= input('Type your password: ')
for char in Password:
    dec(char)
#print(Password)
a=open('Games.py',mode='w')
a.write('Password= \''+str(Password)+'\'')
a.close()
print('Password increapted.')
"""



#Reverse Dictionary
"""
a= {'a': '!H', 'b': 'Fd', 'c': '#Sd'}
l= a.items()
def tst():
    global a
    a={}
    for item in l:
        a[item[1]]=item[0]
tst()
print(a)
"""

#Get WeekDay
"""
#Number (Monday = 0)
import datetime
datetime.datetime.today()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
print(datetime.datetime.today().weekday())

#Str
from datetime import date
import calendar
my_date = date.today()
print(calendar.day_name[my_date.weekday()])
"""


#calculate %
"""a= 2
b= 4
def percentt():
    global a,b
    c= a+b
    d= 100/c
    a= int(round(a*d,0))
    b= int(round(b*d,0))
percentt()
print(a)
print(b)
"""


#Reverse string
"""a= input('Type sth: ')
b=[]
for let in a:
    b.insert(0,let)
c= ''.join(b)
print('This is reverese of it:',c)
"""
"""
a= input('Type sth: ')
a= a[::-1]
print(a)"""



#Increapt password
"""def tab(let):
    di= {'a':'!H','b':'Fd','c':'#Sd','d':'#Nd','e':'#HdE','f':'$Ht','g':'Pd','h':'^H]','i':'*HdI','j':'&[d','k':'*:d','l':'(Hg','m':'&Hl','n':'^Hk',
        'o':'(HO',')p':'pd','q':'!;d,','r':'$Hv','s':'@Hs','t':'Jd','u':'&D,','v':'$,d','w':'@Nfgd,','x':'@Hd;s','y':'^,hd','z':'!Cn',
        'A':'1XH','B':'5XFd','C':'3XSd','D':'3XNd','E':'3XHdE','F':'4XHt','G':'5XPd','H':'6XH]','I':'8XHdI','J':'7X[d','K':'8X:d','L':'9XHg','M':'7XHl',
        'N':'6XHk','O':'9XHO','P':'0Xpd','Q':'1X;d,','R':'4XHv','S':'2XHs','T':'5XJd','U':'7XD,','V':'4X,d','W':'2XNfgd,','X':'2XHd;s','Y':'6X,hd','Z':'1XCn',
        '1':'!@','2':'@#','3':'#$','4':'$%','5':'%^','6':'^&','7':'&*','8':'*(','9':'()','0':')!',
        '!':'12','@':'23','#':'34','$':'45','%':'56','^':'67','&':'78','*':'89','(':'90',')':'01',
        '-':'=','_':'+','=':'-','+':'-',    ',':'<','.':'>','/':'?','<':',','>':'.','?':'/',
        ';':':',"'":'"',':':';','"':"'",    '[':'{',']':'}','{':'[','}':']','\\':'|','|':'\\',
        }
    global b
    b=b.replace(let,di[let])
b=input('type your password: ')
for leter in b:
    tab(leter)
c=open('info.py',mode='w')
c.write('passw= \''+ str(b)+ '\'')
c.close()
print('now close the app')
import time
time.sleep(3)

#another file
def tab(let):
    di= {'a':'!H','b':'Fd','c':'#Sd','d':'#Nd','e':'#HdE','f':'$Ht','g':'Pd','h':'^H]','i':'*HdI','j':'&[d','k':'*:d','l':'(Hg','m':'&Hl','n':'^Hk',
        'o':'(HO',')p':'pd','q':'!;d,','r':'$Hv','s':'@Hs','t':'Jd','u':'&D,','v':'$,d','w':'@Nfgd,','x':'@Hd;s','y':'^,hd','z':'!Cn',
        'A':'1XH','B':'5XFd','C':'3XSd','D':'3XNd','E':'3XHdE','F':'4XHt','G':'5XPd','H':'6XH]','I':'8XHdI','J':'7X[d','K':'8X:d','L':'9XHg','M':'7XHl',
        'N':'6XHk','O':'9XHO','P':'0Xpd','Q':'1X;d,','R':'4XHv','S':'2XHs','T':'5XJd','U':'7XD,','V':'4X,d','W':'2XNfgd,','X':'2XHd;s','Y':'6X,hd','Z':'1XCn',
        '1':'!@','2':'@#','3':'#$','4':'$%','5':'%^','6':'^&','7':'&*','8':'*(','9':'()','0':')!',
        '!':'12','@':'23','#':'34','$':'45','%':'56','^':'67','&':'78','*':'89','(':'90',')':'01',
        '-':'=','_':'+','=':'-','+':'-',    ',':'<','.':'>','/':'?','<':',','>':'.','?':'/',
        ';':':',"'":'"',':':';','"':"'",    '[':'{',']':'}','{':'[','}':']','\\':'|','|':'\\',
        }
    global a
    a=a.replace(let,di[let])
a= input('Type your password: ')
for leter in a:
    tab(leter)
#print(a)
from info import passw
if a == passw:
    print('Login success!')
else:
    print('Invalid password.')
import time
time.sleep(5)"""



#random mouse move
"""import time
import random
import pyautogui
def move_mouse(how_long_in_seconds):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    xsize, ysize = pyautogui.size() 
    while time_elapsed < how_long_in_seconds:
        x, y = random.randrange(xsize), random.randrange(ysize)
        pyautogui.moveTo(x, y, duration=0.05)
        time_elapsed = time.time() - start_time
move_mouse(10)"""

#C:\\Users\\DELL\\Desktop\\tst.txt




#Chart
"""import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')
x_values = []
y_values = []
index = count()
def ali():
    print('hello')
def animate(i):
    global x_values
    global y_values
    x_values.append(next(index))
    y_values.append(i+1)
    plt.cla()
    plt.plot(x_values, y_values)
ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()
"""


#Card Number
"""from luhn.luhn import aLuhn
cardNumber = '6273811121423303263464'
trueOrFalse = aLuhn.doLuhn(cardNumber)
print(trueOrFalse)
"""

#Get removable drives
"""from __future__ import print_function
from os.path import exists

def drives():
    # Limit of 'N' chosen arbitrarily.
    # For letters in the first half of the alphabet:
    for drive in range(ord('F'), ord('L')):
        print('Drive', chr(drive), 'exists:', exists(chr(drive) + ':'))
drives()

def drives2():
    drive_list = []
    for drive in range(ord('F'), ord('L')):
        if exists(chr(drive) + ':'):
            drive_list.append(chr(drive))
    return drive_list

print("The following drives exist:", drives2())"""


#system information
"""import platform
d=platform.uname()
print(d)"""



#Create .zip file
"""zipObj = ZipFile('sample.zip', 'w')
 
# Add multiple files to the zip
zipObj.write('sample_file.csv')
zipObj.write('test_1.log')
zipObj.write('test_2.log')
# close the Zip File
zipObj.close()"""


#Extract .ZIP file
"""with ZipFile(file.zip, 'r') as zip:  
    zip.printdir() 
    zip.extractall() 
    print('Done!') """


#Download file
"""import urllib.request
print('Beginning file download with urllib2...')
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
urllib.request.urlretrieve(url, '/Users/scott/Downloads/cat.jpg')"""


#Password tester
"""import time
import string
paswd = input("Insert Password to Crack: \n")
def Brute(paswd):
   print("[+][+] Starting BruteForce...")
   charset = list(string.ascii_letters + string.digits + string.punctuation)
   result = ""
   x = 0
   while x <= len(paswd)-1:
      for char in charset:
         pchar = paswd[x]
         if char == pchar:
           print("[+] Trying...", char)
           print("[+][+]Matched (",char, ")")
           result += char
           print("[+][+]Current:",result)
           x += 1
           break
         else:
           print("[+] Trying...",char)     
   print("[+][+] Matching Done - Password Found:", result)
Brute(paswd)
"""


#Progressbar
"""
import PySimpleGUI as sg
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]
window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']
for i in range(1000):
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        break
    progress_bar.UpdateBar(i + 1)
window.close()"""


#get IP of Web Site
"""
import socket
socket.gethostbyname('www..ir')
"""
