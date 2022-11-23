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
from Ac_Info import DR_Wins
from Ac_Info import DR_Loses
#from ZZSave import VluOfPlyd
from Ac_Info import RmnnVluCshot


print('This Game Will Be Added In Next Version.')
time.sleep(7)
quit()


print('WITH THIS GAME YOU WILL NEVER LOSE ALL OF YOUR MONEY!')
#print('Your credit is:' + str(Credit))
"""####
Bet= input('Type your bet: ')
Bet= int(Bet)"""


def Game():
    ###
    #Mese Ghadre Motlaghesh konam behtare. (93<frabtzrb<=97)
    ###
    frabtzrb = random.randint(0,100)
    if 98 < frabtzrb:
        MZrib= random.uniform(5, 50)
        MZrib= round(MZrib,2)

    elif 95 < frabtzrb <= 98 :
        MZrib= random.uniform(2.01, 14.99)
        MZrib= round(MZrib,2)

    elif 76 < frabtzrb <= 95 :
        MZrib= random.uniform(1.01, 2)
        MZrib= round(MZrib,2)

    elif 54 < frabtzrb <= 76 :
        MZrib= random.uniform(0.51, 1)
        MZrib= round(MZrib,2)

    elif 37 < frabtzrb <= 54 :
        MZrib= random.uniform(1, 1.5)
        MZrib= round(MZrib,2)

    elif frabtzrb <= 37 :
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
            file.write("%s[%s%s] %i/%i\r" % (prefix, "$"*x, "."*(size-x), j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()


    for i in progressbar(range(100), "Computing: ", 50):
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
                            '\nRatioX_Wins= '  + str(RatioX_Wins+1)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                            '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                            )
                op_inf.close()
                #from ZZSave import VluOfPlyd
                #VluOfPlyd(Bet)
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
                            '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses+1) +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                            '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                            )
                op_inf.close()
                #from ZZSave import VluOfPlyd
                #VluOfPlyd(Bet)
                cache('Loose')
                time.sleep(1)
                ZZSave.SRtXLoose() 
                print('Total credits of account: ' + str(Credit + Gain))
            if 1 == MZrib:
                print('What a luck! \nRound has been finished with 1x ratio!')
            PlyAgn()
            #time.sleep(5)
            #break


def BetC():
    if Credit == 0:
        print('You don\'t have enough credit for playing (0$). \nPlease Charge your account.')
        time.sleep(6)
        quit()
    else:
        global Bet
        Bet=0
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
        subprocess.Popen('.\\GMsLOG\\GM--RtX.bat')
        quit()


BetC()



######################################
#Generating Ratio
#MZrib= round(random.uniform(0.01, 1),2)
