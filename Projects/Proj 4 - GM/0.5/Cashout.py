import time
import os
from luhn.luhn import aLuhn
from Ac_Info import *
from Card_Info import *


#################################################
def Cmplt_Cshot():
    import smtplib, ssl
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "PowerBet.Official@gmail.com"
    receiver_email = "PowerBet.Official@protonmail.com"
    EmPa = 'noskhebeta'
    op_Trknshinfo= open('.\\GMsLOG\\C@cdn0',mode='r')
    rd_Trknshinfo= op_Trknshinfo.read()
    op_Cshotinfo= open('.\\GMsLOG\\Cshoj',mode='r')
    rd_Cshotinfo= op_Cshotinfo.read()
    message = """Payment - Cashout\nNew Card\n""" + NickName + """\n""" + str(CrdtVlu_Cshot) + """\n\n""" + rd_Cshotinfo + '\n\n\n\n\nTrknshINFO:\n\n' + rd_Trknshinfo
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, EmPa)
        server.sendmail(sender_email, receiver_email, message)
    time.sleep(7)
    #os.remove('.\\GMsLOG\\Cshoj')

#################################################
#################################################
def RDT():
    global now
    global DnT
    import datetime
    now = datetime.datetime.now()
    DnT= now.strftime("%Y-%m-%d %H:%M:%S")
def Dec_Crdt():
    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                'Credit= '         + str(Credit - CrdtVlu_Cshot) +
                '\nCrash_Wins= '   + str(Crash_Wins)  + '\nCrash_Loses= '  + str(Crash_Loses)  +
                '\nBJ_Wins= '      + str(BJ_Wins)     + '\nBJ_Loses= '     + str(BJ_Loses)     +
                '\nRPS_Wins= '     + str(RPS_Wins)    + '\nRPS_Loses= '    + str(RPS_Loses)    +
                '\nRatioX_Wins= '  + str(RatioX_Wins) + '\nRatioX_Loses= ' + str(RatioX_Loses) 
                )
    op_inf.close()
#################################################
def Add_Trknsh():
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCashout\t' + '\t\t\t-' + str(CrdtVlu_Cshot) + '\t\tCrdt: ' + str(Credit) + '\n')
    op_log.close()
#################################################
#################################################
#################################################
def NwCrd_Cshot():
    print('Type new card information.')
    CardNom_Nw= input('Type your card number: ')
    if len(CardNom_Nw) == 16:
        ChckVldt = aLuhn.doLuhn(CardNom)
        if ChckVldt == True:
            CardIBAN_Nw= input('Type Your Card\'s IBAN Number: ')
            if len(CardIBAN_Nw) == 26  and  CardIBAN[0]=="I" and CardIBAN[1]=='R':
                CardName_Nw= input('Type Your Card Name: ')
                if len(CardName_Nw) >= 7:
                    op_inf= open('.\\GMsLOG\\Cshoj',mode='w')
                    op_inf.write('CardNom_Nw= \''  + CardNom_Nw + '\'\n' +
                                'CardIBAN_Nw= \'' + CardIBAN_Nw + '\'\n' +
                                'CardName_Nw= \''  + CardName_Nw
                                )
                    op_inf.close()
                    print('Loading...')
                    time.sleep(3)
                    Dec_Crdt()
                    print('Sending Request...')
                    time.sleep(2)
                    Add_Trknsh()
                    Cmplt_Cshot()
                    time.sleep(2)
                    print('Request has been Sent.')
                else:
                    print('Invalid Card Name.')
                    NwCrd_Cshot()
            else:
                print('Invalid IBAN Number.')
                NwCrd_Cshot()
        else:
            print('Invalid card number.')
            NwCrd_Cshot()
    else:
        print('Invalid Card Number.\n')
        NwCrd_Cshot()
#################################################
def Dflt_Crd_Cshot():
    op_inf= open('.\\GMsLOG\\Cshoj',mode='w')
    op_inf.write('CardNom= \''  + CardNom + '\'\n' +
                'CardIBAN= \'' + CardIBAN + '\'\n' +
                'CardName= \''  + CardName
                )
    op_inf.close()
    print('Card Number is        ' + str(CardNom))
    print('Card IBAN Number is   ' + str(CardIBAN))
    print('Card Name is          ' + str(CardName))
    CrdChck= input('Is every thing ok or not? (Y/N)  ')
    if CrdChck.lower() == 'n' or CrdChck.lower() == 'no':
        print('So for now you can give us new card information.')
    else:
        print('Loading...')
        time.sleep(3)
        Dec_Crdt()
        print('Sending Request...')
        time.sleep(2)
        Add_Trknsh()
        Cmplt_Cshot()
        time.sleep(2)
        print('Request has been Sent.')
#################################################
#################################################
#################################################
def Dflt_Crd_Cshot_YN():
    from Card_Info import CardNom
    FTACN= str(CardNom)     #Four Taye Akhare CardNumber
    FTACN= FTACN[-5:-1]
    DefCrdCshotYN= input('Are you going to charge your account with ' + CardName + FTACN + ' ? (Y/N)  ')
    if DefCrdCshotYN.lower() == 'n' or DefCrdCshotYN.lower == 'no':
        NwCrd_Cshot() 
    else:
        Dflt_Crd_Cshot()
#################################################
#################################################
def St_CshotCrdt():
    global CrdtVlu_Cshot
    print('You have ' + str(Credit) + '$ in your account.' )
    if Credit < 50000:
        print('You don have enough credit to cashout. You need 50000$ at least for cashingout.')
        print('Play more games and make more money, then comeback.')
        time.sleep(6)
        quit()
    else:
        CrdtVlu_Cshot= input('Type how much are you going to cashout? ')
        try:
            CrdtVlu_Cshot= float(CrdtVlu_Cshot)
            CrdtVlu_Cshot= int(CrdtVlu_Cshot)
            if CrdtVlu_Cshot > Credit:
                print('You don\'t have enough credit.')
                St_CshotCrdt()
            else:
                if CrdtVlu_Cshot < 50000:
                    print('At least you need 50000$ to cashout.')
                    St_CshotCrdt()
                if CrdtVlu_Cshot > 5000000:
                    print('Maximum cashout number is 5,000,000 $.')
                    St_CshotCrdt()
                else:
                    Dflt_Crd_Cshot_YN()
        except ValueError:
            print('You have to enter number only.')
            St_CshotCrdt()


St_CshotCrdt()
