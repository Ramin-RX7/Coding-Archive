import random
import os
import subprocess
import time
from GM_Info import Nickname
from GM_Info import Credit
from GM_Info import Crash_Wins
from GM_Info import Crash_Loses
from GM_Info import BJ_Wins
from GM_Info import BJ_Loses

#Bat_Chart= "E:\\Coding\\Proj 3 - GM\\0.2\\test.bat"

"""MDic= {'1':'r', '2':'a'}
print(a.get('1'))
print(a['2'])"""

print('Your credit is:' + str(Credit))
####
Bet= input('Type your bet: ')
Bet= int(Bet)


Zrib= input('Type your cash out coefficient: ')
Zrib= float(Zrib)



######################################
#Generating ORG Zarib
frabtzrb = random.randint(0,100)
if frabtzrb >= 85:
    MZrib= random.uniform(20, 99.99)
    MZrib= round(MZrib,2)

elif frabtzrb < 85 and frabtzrb >= 65:
    MZrib= random.uniform(5, 40)
    MZrib= round(MZrib,2)
    
elif frabtzrb <  65 and frabtzrb >=30:
    MZrib= random.uniform(1, 10)
    MZrib= round(MZrib,2)

elif frabtzrb <  30 and frabtzrb >=10:
    MZrib= random.uniform(1, 2)
    MZrib= round(MZrib,2)

elif frabtzrb < 10:
    nmne = [0,1]
    MZrib= random.choice(nmne)
#######################################







####
#tm= MZrib
#subprocess.Popen(Bat_Chart)
#time.sleep(tm)
#os.system("TASKKILL /F /IM chrome.exe")


##################################################
import sys

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


import time

for i in progressbar(range(100), "Computing: ", 40):
    time.sleep(0.5) # any calculation you need
    Gain= Bet*Zrib
    Rnd_Incm= Bet*Zrib
    
    if i > MZrib:
        print('\n\n Game has been finished at:' + str(MZrib) + 'x')
        if Zrib <= MZrib:
            #print('')
            #print('Game has finished at ' + str(MZrib) + 'x')
            print('You Won!')
            print('You gained ' + str(Gain))
            #print('Total income of this round: ' + str(Rnd_Incm))
            op_inf= open('.\\GM_Info.py',mode='w')
            op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                        'Credit= '         + str(Credit + Rnd_Incm) +
                        '\nCrash_Wins= '   + str(Crash_Wins+1)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                        '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses))
            op_inf.close()
            print('Total credits of account: ' + str(Credit + Rnd_Incm))
        if Zrib >  MZrib:
            #print('')
            #print('Game has finished at ' + str(MZrib) + 'x')
            print('You Lost!')
            print('You lost ' + str(Bet))
            op_inf= open('.\\GM_Info.py',mode='w')
            op_inf.write('Nickname= \'' + Nickname + '\'\n'  +
                        'Credit= ' + str(Credit - Bet) +
                        '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                        '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses))
            op_inf.close()
            print('Total credits of account: ' + str(Credit - Bet))
        time.sleep(10)
        break
##################################################








"""
if Zrib <= MZrib:
    #print('')
    #print('Game has finished at ' + str(MZrib) + 'x')
    print('You Won!')
    print('You gained ' + str(Gain))
    print('Total income of this round: ' + str(Totl_Incm))

    op_inf= open('.\\GM_Info.py',mode='w')
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

    op_inf= open('.\\GM_Info.py',mode='w')
    op_inf.write('Nickname= \'' + Nickname + '\'\n'  +
                'Credit= ' + str(Credit + Totl_Incm) +
                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses))
    op_inf.close()
"""
