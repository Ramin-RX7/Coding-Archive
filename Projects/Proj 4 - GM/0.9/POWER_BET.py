import subprocess
import time
from Ac_Info import *
from Card_Info import *

import PySimpleGUI as sg
#sg.change_look_and_feel('')

from PySimpleGUI import *
PopupAnimated('.\\GMsLOG\\Imgs\\PWR2.png',
            message='   $ POWER BET $',
            background_color='Black',
            text_color='Gold',
            font=None,
            no_titlebar=True,
            grab_anywhere=True,
            keep_on_top=True,
            location=(None, None),
            alpha_channel=None,
            time_between_frames=0,
            transparent_color=None,
            )
import time
time.sleep(2)
PopupAnimated(image_source=None)


print('Welcome ' + Nickname)
def MainMenu():
    global MainNpt
    #from Ac_Info import Credit       #Chera Tasirnadaare?!
    import PySimpleGUI as sg
    layout=[
             [sg.Listbox(values=['GAMES','CHARGE ACCOUNT','CASHOUT','ACCOUNT INFO','HELP','ABOUT US'], size=(50, 10),auto_size_text=True,no_scrollbar=True)],
             [sg.Button('CHOOSE\t\tانتخاب',button_color=('White','Green'),size=('40','3'),)]
            ]
    window = sg.Window('MENU', layout,size=(360,250),keep_on_top=True, )
    event, values = window.read()
    window.close()
    
    if values[0] == None or values[0] == []:
        MainMenu()
    else:
        MainNpt=values[0][0]
        print(MainNpt)
    pass


    if MainNpt == 'GAMES':
        def WGF():
            import PySimpleGUI as sg
            layout2=[
                     [sg.Text('Which game do you want to play?\t\t.بازی مورد نظر را انتخاب کنید')],
                     [sg.Listbox(values=['Football','Crash','RatioX','🂡 Black Jack','FaXtor','Monti','RockPaperScissors', 'Dice Race'], size=(40, 10),auto_size_text=True)],
                     [sg.Button('SELECT\t\t\tانتخاب',button_color=('White','Green'),size=('40','6'),)]
                    ]
            window = sg.Window('GAMES', layout2,size=(360,275),no_titlebar=True,keep_on_top=True, )
            event2, values2 = window.read()
            window.close()

            if values2[0] == None or values2[0] == []:
                MainMenu()
            values2[0]=values2[0][0]
            if values2[0]=='Black Jack':
                subprocess.Popen('.\\GMsLOG\\GM--BJ.bat')
            if values2[0]=='Crash':
                subprocess.Popen('.\\GMsLOG\\GM--Crash.bat')
            if values2[0]=='RockPaperScissors':
                subprocess.Popen('.\\GMsLOG\\GM--RPS.bat')
            if values2[0]=='RatioX':
                subprocess.Popen('.\\GMsLOG\\GM--RtX.bat')
            if values2[0]=='Dice Race':
                subprocess.Popen('.\\GMsLOG\\GM--DiceRace.bat')            
            if values2[0]=='Football':
                subprocess.Popen('.\\GMsLOG\\GM--FootBall.bat')   
            if values2[0]=='FaXtor':
                subprocess.Popen('.\\GMsLOG\\GM--FXtr.bat')  
            if values2[0]=='Monti':
                subprocess.Popen('.\\GMsLOG\\GM--Monti.bat')    


        WGF()
    

    elif MainNpt == 'CHARGE ACCOUNT':
        subprocess.Popen('.\\GMsLOG\\Chrg.bat')
        MainMenu()


    elif MainNpt == 'CASHOUT':
        subprocess.Popen('.\\GMsLOG\\Cshot.bat')
        MainMenu()


    elif MainNpt == 'ACCOUNT INFO':
        print('Nickname:                ' + Nickname)
        print('Credit:                  ' + str(Credit))
        print('Email:                   ' + Email)
        print('Real Name:               ' + CardName)
        print('Default Card Number:     ' + str(CardNom))
        print('Real Name:               ' + CardName)
        print('Card IBAN Number:        ' + str(CardIBAN))
        print('')
        MainMenu()
    

    elif MainNpt == 'HELP':
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


    elif MainNpt == 'ABOUT US':
        print('Power Bet is simple Bet application developed with python.')
        print('Version: 1.0.0')
        print('Coder: RX')
        print('Emails:')
        print('         PowerBet.official@gmail.com')
        print('         PowerBet.official@protonmail.com')
        print('         PowerBet.official@pm.me')
        print('Thanks to everyone who\'ve helped for creating & expanding this project.')
        print('There Will be also POWER BET in web-browsers.')
        print('You can check Beta version of POWER BET in GitHub page.')
        MainMenu()





MainMenu()
