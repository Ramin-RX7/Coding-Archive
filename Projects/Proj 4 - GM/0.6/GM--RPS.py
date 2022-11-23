import time
import ZZSave
from Ac_Info import Nickname
from Ac_Info import Credit
from Ac_Info import Crash_Wins
from Ac_Info import Crash_Loses
from Ac_Info import BJ_Wins
from Ac_Info import BJ_Loses
from Ac_Info import RPS_Wins
from Ac_Info import RPS_Loses
from Ac_Info import RatioX_Wins
from Ac_Info import RatioX_Loses
from Ac_Info import DR_Wins
from Ac_Info import DR_Loses



#Main
def Game():

    def cache(res):
        op_cch= open('.\\ZZRPScach.py',mode='w')
        op_cch.write('Result= \''  + str(res) + '\'' +
                     '\nBet= '     + str(Bet)  + 
                     '\nUsrChoice=  \''   + str(UserChoice) + '\''
                     '\nBotChoice=  \'' + str(BotChoice) + '\''
                     )
        op_cch.close()

    def BotChoiceF():
        def AdWin():
            op_inf= open('.\\Ac_Info.py',mode='w')
            op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                         'Credit= '         + str(Credit + Bet) +
                         '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                         '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                         '\nRPS_Wins= '      + str(RPS_Wins+1)        + '\nRPS_Loses= '    + str(RPS_Loses) +
                         '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses)
                         )
            op_inf.close()
            import time
            cache('Win')
            time.sleep(1)
            ZZSave.SRPSWin()
        def AdLose():
            op_inf= open('.\\Ac_Info.py',mode='w')
            op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                         'Credit= '         + str(Credit - Bet) +
                         '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                         '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                         '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses+1) +
                         '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) 
                         )
            op_inf.close()
            import time
            cache('Loose')
            time.sleep(1)
            ZZSave.SRPSLoose()

        SampleSpace= ['r','p','s']
        import random
        global BotChoice
        BotChoice= random.choice(SampleSpace)
        
        #Calculation
        if UserChoice == BotChoice:
            print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
            print('Draw!')
        else:
            if UserChoice == 'r' and BotChoice == 'p':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'r' and BotChoice == 's':    
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 'p' and BotChoice == 's':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'p' and BotChoice == 'r':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 's' and BotChoice == 'r':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 's' and BotChoice == 'p':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            #print('Please wait a momment...')
        time.sleep(2)
        PlyAgn()

    UserChoice= input('Rock, Paper or Scissor? (R/P/S)   ')
    if UserChoice.lower() == 'r' or UserChoice.lower() == 'p' or UserChoice.lower() == 's':
        BotChoiceF()
    else:
        print('Wrong choice.')
        Game()



def PlyAgn():
    PAYN= input('Do you want to play again? (Y/N)  ')
    if PAYN.lower() == 'n' or PAYN.lower() == 'no':
        print('OK, Closing the app...')
        time.sleep(1)
        quit()
    else:
        #import os
        #os.system('cls')
        import subprocess
        subprocess.Popen('.\\GMsLOG\\GM--RPS.bat')
        quit()



Bet=0
#Choose bet value
def BetC():
    global Bet
    print('Your credit is:' + str(Credit))
    Bet= input('Type your bet: ')
    try:
        Bet= int(Bet)
        if Bet > Credit:
            print('You don\'t have enough credit.')
            BetC()
        else:
            #Start the game
            Game()
    except ValueError:
        print('Invalid Nimber')
        BetC()
    
BetC()




