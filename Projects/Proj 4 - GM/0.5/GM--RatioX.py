import random
import os
import subprocess
import time
import sys
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


print('WITH THIS GAME YOU WILL NEVER LOSE ALL OF YOUR MONEY!')
print('Your credit is:' + str(Credit))
"""####
Bet= input('Type your bet: ')
Bet= int(Bet)"""


def Game():
    ###
    #Mese Ghadre Motlaghesh konam behtare. (93<frabtzrb<=97)
    ###
    frabtzrb = random.randint(0,100)
    if frabtzrb > 98:
        MZrib= random.uniform(30, 99.99)
        MZrib= round(MZrib,2)

    elif frabtzrb <= 98 and frabtzrb > 94:
        MZrib= random.uniform(2.01, 30)
        MZrib= round(MZrib,2)
        
    elif frabtzrb <=  94 and frabtzrb > 67:
        MZrib= random.uniform(1, 2)
        MZrib= round(MZrib,2)

    elif frabtzrb >=45 and frabtzrb <= 67:
        MZrib= random.uniform(0.51, 1)
        MZrib= round(MZrib,2)

    elif frabtzrb < 45:
        MZrib= random.uniform(0.01, 0.50)
        MZrib= round(MZrib,2)

    #######################################
    def cache(res):
        op_cch= open('.\\ZZRtXcach.py',mode='w')
        op_cch.write('Result= \''  + str(res) + '\'' +
                     '\nBet= '     + str(Bet)  + 
                     '\nGain= '   + str(Gain)  +
                     '\nOrgRatio= ' + str(MZrib)    
                     )
        op_cch.close()
    ###################


    def progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()


    for i in progressbar(range(100), "Computing: ", 40):
        time.sleep(0.05) # any calculation you need
        Gain= round(Bet*MZrib - Bet)
        Rnd_Incm= round(Bet*MZrib)
        if i > MZrib:
            print('\n\n Round has been finished at:' + str(MZrib) + 'x')
            if 1 < MZrib:
                #print('')
                #print('Game has finished at ' + str(MZrib) + 'x')
                print('You Won!')
                print('You gained ' + str(Gain))
                print('Total income of this round: ' + str(Rnd_Incm))
                op_inf= open('.\\Ac_Info.py',mode='w')
                op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                            'Credit= '         + str(Credit + Gain)  +
                            '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                            '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                            '\nRPS_Wins= '     + str(RPS_Wins)       + '\nRPS_Loses= '   + str(RPS_Loses)   +
                            '\nRatioX_Wins= '  + str(RatioX_Wins+1)    + '\nRatioX_Loses= '+ str(RatioX_Loses)
                            )
                op_inf.close()
                cache('Win')
                time.sleep(1)
                ZZSave.SRtXWin()                
                print('Total credits of account: ' + str(Credit + Gain))


            if 1 >  MZrib:
                if MZrib == 0:
                    print('The worst possible chance of the world!')
                else:
                    pass
                #print('')
                #print('Game has finished at ' + str(MZrib) + 'x')
                print('You Lost!')
                print('You lost ' + str(Gain))
                op_inf= open('.\\Ac_Info.py',mode='w')
                op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                            'Credit= '         + str(Credit + Gain)+
                            '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                            '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                            '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                            '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses+1)
                            )
                op_inf.close()
                cache('Loose')
                time.sleep(1)
                ZZSave.SRtXLoose() 
                print('Total credits of account: ' + str(Credit + Gain))
            if 1 == MZrib:
                print('What a luck! \nRound has been finished with 1x ratio!')


            time.sleep(5)
            break



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
            if Bet == 0:
                print('It\'s not enough for playing.')
                BetC()
            else:
                Game()

    except ValueError:
        print('Invalid Number')
        BetC()
    
BetC()

######################################
#Generating Ratio
#MZrib= round(random.uniform(0.01, 1),2)
