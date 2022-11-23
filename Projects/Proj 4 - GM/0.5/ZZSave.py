def RDT():
    global now
    global DnT
    import datetime
    now = datetime.datetime.now()
    DnT= now.strftime("%Y-%m-%d %H:%M:%S")

from Ac_Info import Credit


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
    op_log.write(rdrd_log + str(DnT) + '\tRtX\t' + 'Win'   + '\tBet:' + str(Bet) + '\tGain: +' + str(Gain) + '\tCrdt:'+str(Credit) + '\tRt:' + str(OrgRatio) +'\n')
    op_log.close()

def SRtXLoose():
    from ZZRtXcach import Result
    from ZZRtXcach import Bet
    from ZZRtXcach import Gain
    from ZZRtXcach import OrgRatio
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRtX\t' + 'Loose' + '\tBet:' + str(Bet) + '\tGain: ' + str(Gain) + '\tCrdt:'+str(Credit) +  '\tRt:' + str(OrgRatio) +'\n')
    op_log.close()


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
    op_log.write(rdrd_log + str(DnT) + '\tRPS\t' + 'Win' + '\t\t\t+' + str(Bet) + '\tCrdt:'+str(Credit) +  '\tUsrChc:' + str(UsrChoice) + '  BtChc:' + BotChoice +'\n')
    op_log.close()
    
def SRPSLoose():
    from ZZRPScach import Result
    from ZZRPScach import Bet
    from ZZRPScach import UsrChoice
    from ZZRPScach import BotChoice
    RDT()
    rd_log= op_log= open('.\\GMsLOG\\C@cdn0',mode='r')
    rdrd_log= rd_log.read()
    op_log= open('.\\GMsLOG\\C@cdn0',mode='w')
    op_log.write(rdrd_log + str(DnT) + '\tRPS\t' + 'Loose' + '\t\t\t-' + str(Bet) + '\tCrdt:'+str(Credit) +  '\tUsrChc:' + str(UsrChoice) + '  BtChc:' + BotChoice +'\n')
    op_log.close()