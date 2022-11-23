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

print('''
CCCCCCC  RRRRRRR     A     SSSSSSS  HH   HH
CC       RR   RR   AA AA   SS       HH   HH
CC       RRRRRRR  AA   AA  SS       HH   HH
CC       RRR      AAAAAAA  SSSSSSS  HHHHHHH
CC       RR RR    AA   AA       SS  HH   HH
CCCCCCC  RR   RR  AA   AA  SSSSSSS  HH   HH
''')
print('Your credit is:' + str(Credit))





def Game():
    ###
    #Mese Ghadre Motlaghesh konam behtare. (93<frabtzrb<=97)
    ###
    #Generating ORG Zarib
    frabtzrb = random.randint(0,100)
    if frabtzrb > 97:
        MZrib= random.uniform(1, 99.99)
        MZrib= round(MZrib,2)

    elif 93 < frabtzrb <= 97:
        MZrib= random.uniform(1, 25)
        MZrib= round(MZrib,2)
        
    elif 77 < frabtzrb <= 93:
        MZrib= random.uniform(1, 15)
        MZrib= round(MZrib,2)

    elif 63 < frabtzrb <= 77:
        MZrib= random.uniform(1.5, 2)
        MZrib= round(MZrib,2)        

    elif 43 < frabtzrb <= 63:
        MZrib= random.uniform(1, 1.5)
        MZrib= round(MZrib,2)

    elif 9 < frabtzrb <= 43:
        MZrib= random.uniform(1.01, 2)
        MZrib= round(MZrib,2)        

    elif frabtzrb <= 9:
        nmne = [0,1]
        MZrib= random.choice(nmne)
    ##################################################
    ####
    #tm= MZrib
    #subprocess.Popen(Bat_Chart)
    #time.sleep(tm)
    #os.system("TASKKILL /F /IM chrome.exe")
    ####
    ##################################################
    def cache(res):
        op_cch= open('.\\ZZCrshcach.py',mode='w')
        op_cch.write('Result= \''  + str(res) + '\'' +
                     '\nBet= '     + str(Bet)  + 
                     '\nGain= '     + str(Gain)  + 
                     '\nUsrRatio= '   + str(Zrib)  +
                     '\nOrgRatio= ' + str(MZrib)    
                     )
        op_cch.close()




    def progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write("%s[%s%s] %i/%i\r" % (prefix, "$"*x, "_"*(size-x), j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()



    for i in progressbar(range(100), "Playing: ", 50):
        time.sleep(0.5) # any calculation you need
        Gain= Bet*Zrib - Bet
        Rnd_Incm= Bet*Zrib
        
        if i > MZrib:
            print('\n\n Game has been finished at:' + str(MZrib) + 'x')
            if Zrib <= MZrib:
                #print('')
                #print('Game has finished at ' + str(MZrib) + 'x')
                print('You Won!')
                print('You gained ' + str(Gain))
                print('Total income of this round: ' + str(Rnd_Incm))
                op_inf= open('.\\Ac_Info.py',mode='w')
                op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                            'Credit= '         + str(Credit + Gain)  +
                            '\nCrash_Wins= '   + str(Crash_Wins+1)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                            '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                            '\nRPS_Wins= '     + str(RPS_Wins)       + '\nRPS_Loses= '   + str(RPS_Loses)   + 
                            '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                            '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                            )
                op_inf.close()
                #VluOfPlyd(Bet)
                cache('Win')
                time.sleep(1)
                ZZSave.SCrshWin()
                print('Total credits of account: ' + str(Credit + Gain))
            if Zrib >  MZrib:
                #print('')
                #print('Game has finished at ' + str(MZrib) + 'x')
                print('You Lost!')
                print('You lost ' + str(Bet))
                op_inf= open('.\\Ac_Info.py',mode='w')
                op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                            'Credit= '         + str(Credit - Bet)+
                            '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                            '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                            '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                            '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                            '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                            '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                            )
                op_inf.close()
                #VluOfPlyd(Bet)
                cache('Loose')
                time.sleep(1)
                ZZSave.SCrshLoose()
                print('Total credits of account: ' + str(Credit - Bet))
            time.sleep(1)
            PlyAgn()
            #time.sleep(5)
            #break




##################################################
def CoefficientF():
    global Zrib
    Zrib= input('Type your cash out coefficient: ')
    try:
        Zrib= round(float(Zrib),2)
        if Zrib < 1.01:
            print('At least you have to choose 1.01.')
            CoefficientF()
        if Zrib > 99.99:
            print('99.99 is the most coefficient.')
            CoefficientF()
        if 99.99 >= Zrib >= 1.01:
            Game()

    except ValueError:
        print('Invalid Coefficient.')
        CoefficientF()



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
        subprocess.Popen('.\\GMsLOG\\GM--Crash.bat')
        quit()



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
                    CoefficientF() 
        except ValueError:
            print('Invalid Number')
            BetC()
    
BetC()









##################################################
"""
if Zrib <= MZrib:
    #print('')
    #print('Game has finished at ' + str(MZrib) + 'x')
    print('You Won!')
    print('You gained ' + str(Gain))
    print('Total income of this round: ' + str(Totl_Incm))

    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                'Credit= '         + str(Credit + Totl_Incm) +
                '\nCrash_Wins= '   + str(Crash_Wins+1)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses))
    op_inf.close()
    print('Total credits of account: ' + str(Credit))


if Zrib >  MZrib:
    #print('')
    #print('Game has finished at ' + str(MZrib) + 'x')
    print('You Lost!')
    print('You lost ' + str(Bet))
    print('Total credits: ' + str(Credit))

    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \'' + Nickname + '\'\n'  +
                'Credit= ' + str(Credit + Totl_Incm) +
                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses))
    op_inf.close()
"""
