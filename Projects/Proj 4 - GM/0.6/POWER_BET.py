import subprocess
from Ac_Info import *
from Card_Info import *

print('Welcome ' + Nickname)
def MainMenu():
    #from Ac_Info import Credit       #Chera Tasirnadaare?!
    print('Credit: ' + str(Credit))
    print('Type where you want to go?')
    print('1-Games / 2-Charge Account / 3-Cashout / 4-Account INFO / 5-Help / 6-About Us')
    MainNpt= input('')
    if MainNpt == '1':
        def WGF():
            print('Which game do you want to play?')
            print('1-Black Jack / 2-Crash / 3-RockPaperScissors / 4-RatioX / 5-Dice Race   / 99-Back to Main Menu')
            WG= input('')
            if WG == '1':
                subprocess.Popen('.\\GMsLOG\\GM--BJ.bat')
            elif WG == '2':
                subprocess.Popen('.\\GMsLOG\\GM--Crash.bat')
            elif WG == '3':
                subprocess.Popen('.\\GMsLOG\\GM--RPS.bat')
            elif WG == '4':
                subprocess.Popen('.\\GMsLOG\\GM--RtX.bat')
            elif WG == '5':
                subprocess.Popen('.\\GMsLOG\\GM--DiceRace.bat')
            elif WG == '99':
                MainMenu()
            else:
                print('Invalid Input.')
            WGF()
        WGF()
    
    elif MainNpt == '2':
        subprocess.Popen('.\\GMsLOG\\Chrg.bat')
        MainMenu()

    elif MainNpt == '3':
        subprocess.Popen('.\\GMsLOG\\Cshot.bat')
        MainMenu()

    elif MainNpt == '4':
        print('Nickname:                ' + Nickname)
        print('Credit:                  ' + str(Credit))
        print('Email:                   ' + Email)
        print('Real Name:               ' + CardName)
        print('Default Card Number:     ' + str(CardNom))
        print('Real Name:               ' + CardName)
        print('Card IBAN Number:        ' + str(CardIBAN))
        print('')
        MainMenu()
    
    elif MainNpt == '5':
        #######
        #######
        #######
        #MainMenu()
        pass

    elif MainNpt == '6':
        print('Power Bet is simple Bet application developed with python.')
        print('Version: 1.0.0')
        print('Coder: RX')
        print('Emails:')
        print('         PowerBet.official@gmail.com')
        print('         PowerBet.official@protonmail.com')
        print('         PowerBet.official@pm.me')
        print('')
        MainMenu()





MainMenu()
