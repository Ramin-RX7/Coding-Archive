from rx import *
from subprocess import Popen
import time,os

#Shutdown
#Restart
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
        if Pass == SQ__:
            p('\nWelcome RX!\n\n')
            op= open('.\\RX\\Access.py', mode='w')
            #op.write('TF= True')
            op.close()
            Main()
        else:
            p('Invalid Password.\n')
            Login()
    else:
        p('There is no Account with this username.\n')
        Login()


syms=['@', '$', '%','>>>','>>> $']
sym= rand.choice(syms)
nick=['','','','sur','boss','RX','now']
cent=['What to do','How can I help you',]
def Main():
    Inp= input('\n{0} {1}?  \n{2} '.format(rand.choice(cent),rand.choice(nick),sym))
    # IP & Mac Address
    if Inp[:2]=='IP':
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
        p('Informatted way  is :',MacIF)
        print("In formatted way is : ", end="") 
        MacF= ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
        for ele in range(0,8*6,8)][::-1])
        p(MacF) 
        
    # Logout & Quit
    elif Inp=='Logout':
        import os
        os.remove('.\\Access.py')
    elif Inp.lower()=='exit' or Inp.lower()=='quit':
        import os
        if os.path.exists('.\\Access.py')==True:
            os.remove('.\\Access.py')
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


    # System and in-app
    elif Inp=='mini':
        pass#################################Minimize
    elif Inp=='WIFI':
        Popen('.\\RX\\CMD.bat')




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


    # Open Folders
    elif Inp=='CH folder':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin"')
    elif Inp=='CH Super':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super"')
    elif Inp=='CH Photo':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super\\2017-08-08 16.32.06 1576837726031578273_3007194494.jpg"')
        wait(5)
        #import pyautogui
        #pyautogui.click(1000,400)
        keyboard('f5')
    elif Inp=='X Porn':
        Popen('explorer "E:\\X List\\ZzzzzzZ\\Sorted"')      
    elif Inp=='Hack Folder':
        Popen('explorer "D:\\Program Files\\XXX\\Hack"') 
    elif Inp=='Photo Collection':
        Popen('explorer "D:\\Program Files\\XXX\\Collected"')
        
                     




    else:
        p('Sorry. I didn\'t get that.')
        p('ERROR:  command "{}" not found.'.format(Inp).upper())
    Main()


if os.path.exists('.\\RX\\Access.py')==True:
    p('Welcome Back RX')
    Main()
else:
    Login()
