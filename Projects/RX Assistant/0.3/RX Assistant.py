from rx import *
from subprocess import Popen
import time,os,re


#Icon
#Notification
#Open  CH Photo (Random)
#Open  
#

def Login():
    global Username,Pass
    Username= input('Type Your Username: ')
    if Username == 'RX':
        import getpass
        Pass= getpass.getpass(prompt='Type Your Password: ') 
        from rx import __SQ_
        if Pass == __SQ_:
            style.text('\nWelcome RX!','green')
            write('.\\RX\\Access.py')
            Main()
        else:
            p('Invalid Password.\n')
            Login()
    else:
        p('There is no Account with this username.\n')
        Login()


syms=['$','>>>','>>> $']
sym= rand.choice(syms)
nick=['','','','sur','boss','RX','now']
cent=['What to do','How can I help you',]
Wrong= 0
def Main():
    global Wrong
    if Wrong>=5:
        file.delete('.\\RX\\Access.py')
        from colored import fg,attr
        print('%sDue to security things you have to login again %sRX%s.\nThank you.%s'% (fg('red'),fg('green'),fg('red'),attr(0)))
        wait(4)
        cls()
        Wrong=2
        Login()
    Inp= input('\n{0} {1}?  \n{2} '.format(rand.choice(cent),rand.choice(nick),sym))
    # IP & Mac Address
    if Inp[:2]=='IP' or Inp[:2]=='ip' or Inp[:2]=='Ip':
        import socket
        p(socket.gethostbyname(Inp[3:]))
    elif Inp=='My IP':
        import socket
        p(socket.gethostbyname(socket.gethostname()))
    elif Inp[:8]=='Valid IP':
        import re
        regex= '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
        IP=Inp[9:]
        if(re.search(regex, IP)):  
            p("Valid IP Address")
        else:  
            p("Invalid IP Address")
    elif Inp=='Mac Address':
        import uuid
        MacIF= hex(uuid.getnode()) 
        p(MacIF)
        p('Informatted way  is : {}'.format(MacIF))
        print("In formatted way is : ", end="") 
        MacF= ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
        for ele in range(0,8*6,8)][::-1])
        p(MacF) 
        
    # Logout & Quit
    elif Inp=='Logout':
        import os
        os.remove('.\\RX\\Access.py')
    elif Inp.lower()=='exit' or Inp.lower()=='quit':
        import os
        if file.exists('.\\RX\\Access.py')==True:
            os.remove('.\\RX\\Access.py')
        quit()

        # VPN
        """elif Inp=='Windscribe':
            pass#################################Popen('.\\')
        elif Inp=='Proton VPN':
            pass#################################Popen('.\\')
        # Applications
        elif Inp=='Record Screen':
            pass###########
        elif Inp=='Github':
            Popen('.\\RX\\App\\Windscribe.aa')
        """
    elif Inp=='My Password List':
        import os
        if os.path.exists('D:\\Program Files\\XXX\\Passwords\\KeePass-2.42.1')==True:
            Popen('D:\\Program Files\\XXX\\Passwords\\KeePass-2.42.1\\KeePass.exe')
            p('Openning...')
        else:
            p('Sorry, I Couldn\'t Find Them.')



    elif Inp=='Date Time':
        from datetime import datetime
        print("Date and Time: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    elif Inp[:16]=='Time Passed from':
        from datetime import date
        import datetime
        def Passed(FDate,LDate='Now'):
            
            F_date = date(int(FDate[:4]), int(FDate[5:7]), int(FDate[8:10]))
            if LDate=='Now':
                now = datetime.datetime.now()
                L_date = date(int(now.strftime('%Y')),int(now.strftime('%m')), int(now.strftime('%d')))
            else:
                L_date= date(int(LDate[:4]),int(LDate[5:7]),int(LDate[8:10]))
            delta = L_date - F_date
            #print('\n\n')
            p(str(delta.days        ) + '  Days')
            p(str(delta.days * 24   ) + '  Hours')
            p(str(delta.days * 1440 ) + '  Minutes')    
            p(str(delta.days * 86400) + '  Seconds')
            p('Are passed from  '+ str(F_date) + '  Until  ' + str(L_date))
        if len(Inp)==27:
            Passed(Inp[17:])
        else:
            Passed(Inp[17:27],Inp[34:])



    # System and in-app
    elif Inp=='Mini':
        import ctypes
        ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    elif Inp=='WIFI':
        Popen('.\\RX\\CMD.bat')
    elif Inp=='About':
        print('''
This is an assistant which works in terminal.
It supports usefull widgets those everyone needs.
'NOTE THAT THIS ASSISTANT CAN NOT CHAT WITH YOU'

NAME:           HAXIN
Created on:     2-1-2020
STATUS:         Releasing new updates
CREATOR:        RX
        ''')


    # Open Folders
    elif Inp=='CH folder':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin"')
    elif Inp=='CH Super':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super"')
    elif Inp=='CH Photo':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super\\2017-08-08 16.32.06 1576837726031578273_3007194494.jpg"')
        wait(5)
        import pyautogui
        #pyautogui.click(1000,400)
        pyautogui.press('f5')
    elif Inp=='X Porn':
        Popen('explorer "E:\\X List\\ZzzzzzZ\\Sorted"')      
    elif Inp=='Hack Folder':
        Popen('explorer "D:\\Program Files\\XXX\\Hack"') 
    elif Inp=='Photo Collection':
        Popen('explorer "D:\\Program Files\\XXX\\Collected"')
        

    #ping site --> ip site ro mide
    







    elif Inp=='Commands':
        p('here is list of all commands:\n')
        Commands='''
Data:
    IP
    My IP
    Mac Address
    ### Tracert

Logout & Quit:
    Logout
    exit/quit

Date & Time:
    Date Time
    Time Passed from

System & In-App:
    ### Mini
    WIFI
    Commands

ONLY RX PC:
    CH:
        CH folder
        CH Super
        CH Photo

    Folders:
        X Porn
        HackFolder
        Photo Collection'''
        Commands=Commands.split('\n')
        for letter in Commands:
            print(letter)
            wait(0.05)






    else:
        p('Sorry. I didn\'t get that.')
        p('ERROR:  command "{}" not found.'.format(Inp).upper())
    Main()


if file.exists('.\\RX\\Access.py')==True:
    p('Welcome Back RX')
    Main()
else:
    Login()
