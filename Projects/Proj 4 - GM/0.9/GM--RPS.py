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
from Ac_Info import RmnnVluCshot





import PySimpleGUI as sg
from PySimpleGUI import popup_animated as PopupAnimated
PopupAnimated('.\\GMsLOG\\Imgs\\PWR2.png',
            message='   $ POWER BET $',
            background_color='Black',
            text_color='Gold',
            font=None,
            no_titlebar=True,
            grab_anywhere=True,
            keep_on_top=True,
            location=(1250, 592),
            alpha_channel=0.1,
            time_between_frames=0,
            transparent_color=None,
            )
import time
time.sleep(0.5)
PopupAnimated(image_source=None)
###
PopupAnimated('.\\GMsLOG\\Imgs\\RPS',
            message=None,
            background_color=None,
            text_color=None,
            font=None,
            no_titlebar=True,
            grab_anywhere=True,
            keep_on_top=True,
            location=(None, None),
            alpha_channel=None,
            time_between_frames=0,
            transparent_color=None
            )
import time
time.sleep(2)
PopupAnimated(image_source=None)







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
                         '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                         '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                         )
            op_inf.close()
            #VluOfPlyd(Bet)
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
                         '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses)  +
                         '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                         )
            op_inf.close()
            #VluOfPlyd(Bet)
            cache('Loose')
            time.sleep(1)
            ZZSave.SRPSLoose()

        SampleSpace= ['Rock','Paper','Scissors']
        import random
        global BotChoice
        BotChoice= random.choice(SampleSpace)
        
        #Calculation
        if UserChoice == BotChoice:
            if UserChoice == 'Rock' and BotChoice == 'Rock':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\RR',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
            if UserChoice == 'Paper' and BotChoice == 'Paper':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\PP',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
            if UserChoice == 'Scissors' and BotChoice == 'Scissors':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\SS',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)

            print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
            print('Draw!')
        else:
            if UserChoice == 'Rock' and BotChoice == 'Paper':

                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\RP',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            #location=(1250, 592),
                            #alpha_channel=1,
                            #time_between_frames=0,
                            #transparent_color=None,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)



                print('Your Choice is ROCK\nBot Choice is PAPER')
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'Rock' and BotChoice == 'Scissors': 
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\RS',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)

                print('Your Choice is ROCK\nBot Choice is SCISSORS')
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 'Paper' and BotChoice == 'Scissors':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\PS',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
                                
                print('Your Choice is PAPER\nBot Choice is SCISSORS')
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'Paper' and BotChoice == 'Rock':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\PR',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
                                
                print('Your Choice is PAPER\nBot Choice is ROCK')
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 'Scissors' and BotChoice == 'Rock':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\SR',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
                                
                print('Your Choice is SCISSORS\nBot Choice is ROCK')
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'Scissors' and BotChoice == 'Paper':
                PopupAnimated('.\\GMsLOG\\Imgs\\RPS_Deck\\SP',
                            #message='   $ POWER BET $',
                            background_color='Black',
                            text_color='Gold',
                            font=None,
                            no_titlebar=True,
                            grab_anywhere=True,
                            keep_on_top=True,
                            )
                import time
                time.sleep(4)
                PopupAnimated(image_source=None)
                                
                print('Your Choice is SCISSORS\nBot Choice is PAPER')
                print('You Won!')
                #Result= 'Win'
                AdWin()

            #print('Please wait a momment...')
        import time
        time.sleep(2)
        PlyAgn()





    import PySimpleGUI as s
    #sg.ChangeLookAndFeel('Black')
    layout= [ [sg.Text('CREDIT: \t\t {0}'.format(Credit)),sg.Text('\t\t:اعتبار')],
              [sg.Text('BET:   \t\t')  , sg.Input(size=(20,10),focus=True),sg.Text(' :مقدار')],
              [sg.Text('Choose your weapon.\t\t.انتخاب کنید')],
              [sg.Listbox(values=['Rock\t\t\t\t\tسنگ', 'Paper\t\t\t\t\tکاغذ', 'Scissors\t\t\t\tقیچی'],no_scrollbar=True, size=(40, 5),auto_size_text=True)],
              [sg.Button('SET BET\t\t\tانتخاب شرط',button_color=('White','Green'),size=('37','6'),tooltip='You will turn to betting page.\n.با کلیک کردن به صفحه انتخاب مبلغ هدایت میشوید')]
             ]
    window = sg.Window('Please Choose\tانتخاب کنید', layout,size=(330,230), no_titlebar=True)
    event, values = window.read()
    window.close()

    if values[0]==[] or values[0]=='' or values[0]==None:
        Game()
    else:
        pass
    try:
        values[1]=values[1][0]
    except IndexError:
        Game()
    pass
    if values[1]=='Rock\t\t\t\t\tسنگ':
        UserChoice= 'Rock'
    if values[1]=='Paper\t\t\t\t\tکاغذ':
        UserChoice= 'Paper'
    if values[1]=='Scissors\t\t\t\tقیچی':
        UserChoice= 'Scissors'
    pass
    try:
        Bet= int(values[0])
        print('')
        
    except ValueError:
        #print('PLEASE TYPE NUMBERS ONLY.')
        sg.popup('.لطفا تنها از اعداد استفاده نمایید\nPLEASE TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5,icon='.\\GMsLOG\\Imgs\\PWR.ico')
        Game()
    print('')
    if Bet>Credit:
        print('NOT ENOUGH CREDIT')
        time.sleep(2)
        Game()
    else:
        #print('game is going on..')
        print('\n\n')
    BotChoiceF()

    """UserChoice= input('Rock, Paper or Scissors? (R/P/S)   ')
    if UserChoice.lower() == 'r' or UserChoice.lower() == 'p' or UserChoice.lower() == 's':
        BotChoiceF()
    else:
        print('Wrong choice.')
        Game()"""



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
if Credit==0:
    print('You don\'t have enough credit for playing (0$). \nPlease Charge your account.')
else:
    Game()




