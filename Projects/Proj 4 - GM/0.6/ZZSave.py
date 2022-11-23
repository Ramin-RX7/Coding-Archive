def RDT():
    global now
    global DnT
    import datetime
    now = datetime.datetime.now()
    DnT= now.strftime("%Y-%m-%d %H:%M:%S")

from Ac_Info import Credit
import os
import time

########## Functions ##########

###BlackJack
def SBJWin():
    from ZZBJcach import Result
    from ZZBJcach import Bet
    from ZZBJcach import JoC
    from ZZBJcach import Bot_JoC
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tBJ\t' + 'Win\t\t\t+' + str(Bet) + '\tCrdt:'+str(Credit) + '\t\tUsr: ' + str(JoC) + '\t\tBt: ' + str(Bot_JoC) + '\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZBJcach.py')

def SBJLoose():
    from ZZBJcach import Result
    from ZZBJcach import Bet
    from ZZBJcach import JoC
    from ZZBJcach import Bot_JoC
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tBJ\t' + 'Loose\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit) + '\t\tUsr: '+str(JoC) + '\t\tBt: '+str(Bot_JoC) + '\n')
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
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCrsh\t' + 'Win' + '\tBet:' + str(Bet) + '\tGain: +' + str(Gain) + '\tCrdt:'+str(Credit) + '\tUsrRt: ' + str(UsrRatio) + '\tOrgRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZCrshcach.py')

def SCrshLoose():
    from ZZCrshcach import Result
    from ZZCrshcach import Bet
    from ZZCrshcach import Gain
    from ZZCrshcach import OrgRatio
    from ZZCrshcach import UsrRatio
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tCrsh\t' + 'Loose' + '\tBet:' + str(Bet) + '\tGain: -' + str(Bet) + '\tCrdt:'+str(Credit) + '\tUsrRt: ' + str(UsrRatio) + '\tOrgRt:' + str(OrgRatio) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZCrshcach.py')

###RatioX
def SRtXWin():
    from ZZRtXcach import Result
    from ZZRtXcach import Bet
    from ZZRtXcach import Gain
    from ZZRtXcach import OrgRatio
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
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tDR\t' + 'Loose' + '\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit-Bet) +  '\tUsrRll:' + str(UsrRoll) + '  BtRll:' + str(BotRoll) +'\n')
    op_log.close()
    time.sleep(2)
    os.remove('ZZDRcach.py')