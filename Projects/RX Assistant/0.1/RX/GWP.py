import random
import time
import os

Ready=False
def WF_Lst():
    time.sleep(1)
    os.system('netsh wlan show profiles')
    print('\n\n')
    time.sleep(1.5)

def Show_Info():
    global Rtr
    Rtr= input('Type Router Name: ')
    os.system('netsh wlan show profiles {0}'.format(Rtr))

def Get_Secure_INFO(RtrNm):
    YN= input('\nPlease Type "CONFIRM" To Start Hacking {0}:  '.format(RtrNm))
    if YN == 'CONFIRM':
        InfoWP('')
        time.sleep(1.5)
        print('Sending Request...')
        time.sleep(2)
        print('Getting Information...')
        time.sleep(2)
        print('PASSWORD FOUND')
        time.sleep(1.2)
        print('READY')
        global Ready
        Ready= True
        print('\n\n')
    else:
        print('Operation Has Been Cancelled.')

def InfoWP(Alaki):
    i=0
    lst= ['Starting...','Downloading Files...','Downloading...','Waiting for permission...','Collecting information',
    'Loading...','Waiting...','Checking','Pinging...','READY','Alright','Permission allowed','Action in progress...',
    'Access','Getting IP...','Getting MacAddresss...','Intializing...','Loging in...','Tracerting...',
    'Starting...','Downloading Files...','Downloading...','Waiting for permission...','Collecting information',
    'Loading...','Waiting...','Checking','Pinging...','READY','Alright','Permission allowed','Action in progress...',
    'Access','Getting IP...','Getting MacAddresss...','Intializing...','Loging in...','Tracerting...']
    while i < 500:
        chc= random.choice(lst)
        print(chc)
        #lst.remove(chc)
        i+=1
        time.sleep(0.025)
    if i >= 120:
        print('Every thing is checked.')
        print('\n\n')
        time.sleep(3)

def Show_Password(RtrNm):
    if Ready==True:
        os.system('netsh wlan show profiles {0} key=clear'.format(RtrNm))
    else:
        print('I couldn\'t get password.\nPlease check for getting secure info first, then trying to get password.')



def WF_Main():
    
    WF_Inp=input('WIFI> ')
    if WF_Inp=='WF_Lst()':
        WF_Lst()
    elif WF_Inp=='Show_Info()':
        Show_Info()
    elif WF_Inp[:16]=='Get_Secure_INFO(':
        Get_Secure_INFO(WF_Inp[16:-1])
    elif WF_Inp[:14]=='Show_Password(':
        Show_Password(WF_Inp[14:-1])
    elif WF_Inp=='leave':
        quit()
    else:
        print('Sorry, I didn\'t get that.\nERROR:  WRONG COMMAND.')
    WF_Main()

if os.path.exists('Access.py')==True:
    print('WIFI: ')
    WF_Main()
else:
    WF_Main()
