import subprocess
import time
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
        print('''\n
HH   HH  EEEEEE  LL      PPPPPPP
HH   HH  EE      LL      PP   PP
HH   HH  EE      LL      PP   PP
HHHHHHH  EEEEEE  LL      PPPPPPP
HH   HH  EE      LL      PP
HH   HH  EEEEEE  LLLLLL  PP     \n\n\n''')
        print('Games: There are 5 games in Version 1.0.0 .')
        print('1)Black Jack  2)Crash  3)Dice Race  4)RatioX  5)RPS\n')
        print('''1- BLACK JACK:
    Black Jack or 21 is first game. Computer is dealer so you can choose value of the bet.
    When game is draw, dealer wins.
    When you are BLACKJACK it\'s not important what cards computer has, you win.
    Maximum number of cards is 5. After that it\'s bot turn. 
    Ace is always 11. Photos are all 10.\n''')
        print('''2- CRASH:
    This game is an idea of MONTIEGO. It\'s one of the most popular games in Persian Online Casinos,
    After choosing bet, you have to choose a coefficient, for example 2.25. Then press ENTER.
    Then game will start and the chart goes on. If it passes your coefficient, you win the game.
    If it doesn\'t pass your coefficient, you lose.
    Also there is something good for you. If Your coefficient is same of Game coefficient you win!
    Coefficient is between 0 and 99.99 and you have to choose at least 1.01 to play the game.\n''')
        print('''3- Dice Race:
    This game is simple. There are 4 dices. 2 for you and 2 for bot.
    Then they roll. If total of your dices are more, you win. If Bot total is more, bot win.
    When they are same there are two ways:
        A)If no one have Double, game is draw.  B: If someone has Double We add 1 to it\'s total.
        example:
            Your Roll: 4-4     Bot Roll: 5-4
            In fact Bot should win. But First of all we add 1 to your total. So you will be 9 same as bot.
            Because you have Double You win the game.
    If somebody has Double 1, we add 3 to his/her total.''')
        time.sleep(4)
        MainMenu()
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
