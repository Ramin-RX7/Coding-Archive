import random
import os
import subprocess
import time

Bat_Chart= "E:\\Coding\\Proj 3 - GM\\test.bat"

"""MDic= {'1':'r', '2':'a'}
print(a.get('1'))
print(a['2'])"""

print('TEST')
####
Bet= input('Type your bet: ')
Bet= int(Bet)

Zrib= input('Type your cash out coefficient: ')
Zrib= float(Zrib)


MZrib= random.uniform(1, 99.99)
MZrib= round(MZrib,2)

Gain= Bet*MZrib - Bet
Totl_Incm= Bet*MZrib

tm= MZrib+10
####
subprocess.Popen(Bat_Chart)
time.sleep(tm)
os.system("TASKKILL /F /IM chrome.exe")

if Bet < MZrib:
    print('')
    print('Game has finished at ' + str(MZrib) + 'x')
    print('You Won!')
    print('You gained ' + str(Gain))
    print('Total income of this round: ' + str(Totl_Incm))



