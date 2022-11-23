import random
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


"""
import PySimpleGUI as sg
from PySimpleGUI import *
PopupAnimated('.\\GMsLOG\\Imgs\\BlackJack',
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
"""







print('''
BBBBBB   LL          A     CCCCCCC  KK   KK           JJJJJ    A     CCCCCCC  KK   KK 
BB   BB  LL        AA AA   CC       KK  KK             JJ    AA AA   CC       KK  KK  
BBBBBBB  LL       AA   AA  CC       KKKK               JJ   AA   AA  CC       KKKK    
BB   BB  LL       AAAAAAA  CC       KKKK               JJ   AAAAAAA  CC       KKKK    
BB   BB  LL       AA   AA  CC       KK  KK         JJ  JJ   AA   AA  CC       KK  KK  
BBBBBB   LLLLLLL  AA   AA  CCCCCCC  KK   KK        JJJJJJ   AA   AA  CCCCCCC  KK   KK 
''')
NoC=0
Cards= ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
Smbls= ['♠', '♣', '♥ ', '♦']
JoC=0
Y=0
D=0
S=0
C=0
P=0
"""BY=0
BD=0
BS=0
BC=0
BP=0"""


def Game():

    def cache(res):
        op_cch= open('.\\ZZBJcach.py',mode='w')
        op_cch.write('Result= \''  + str(res) + '\'' +
                     '\nBet= '     + str(Bet)  + 
                     '\nJoC= '   + str(JoC)  +
                     '\nBot_JoC= ' + str(Bot_JoC)    
                     )
        op_cch.close()


    def WinF():
        print('You Won!')
        op_inf= open('.\\Ac_Info.py',mode='w')
        op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                     'Credit= '         + str(Credit+Bet) +
                     '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                     '\nBJ_Wins= '      + str(BJ_Wins+1)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                     '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses)  +
                     '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                     '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                     '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                     )
        op_inf.close()
        #ZZSave.VluOfPlyd(Bet)
        cache('Win')
        time.sleep(1)
        ZZSave.SBJWin()

    def LoseF():
        print('You Lost!')
        op_inf= open('.\\Ac_Info.py',mode='w')
        op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                     'Credit= '         + str(Credit-Bet) +
                     '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                     '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses+1)    +
                     '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses)  +
                     '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                     '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                     '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                     )
        op_inf.close()
        #ZZSave.VluOfPlyd(Bet)
        cache('Loose')
        time.sleep(1)
        ZZSave.SBJLoose()


    def Calculate():
        #JoC= Y+D+S+C+P
        #Bot_JoC= BY+BD+BS+BC+BP
        if JoC != Bot_JoC:
            if JoC < 21 and Bot_JoC < 21:
                if JoC > Bot_JoC:
                    WinF()
                if JoC < Bot_JoC:
                    LoseF()

            if JoC > 21 and Bot_JoC > 21:
                if JoC > Bot_JoC:
                    LoseF()
                if JoC < Bot_JoC:
                    WinF()            

            if JoC > 21 and Bot_JoC < 21:
                LoseF()
            if JoC < 21 and Bot_JoC > 21:
                WinF()
            if JoC == 21:
                print('BlackJack!')
                WinF()
            if Bot_JoC == 21 and JoC != 21:
                print('Bot is BlackJack!')
                LoseF()
        if JoC == Bot_JoC:
            print('Draw. No Bet.')
        print('Your total is: ' + str(JoC))
        print('Bot total is: '  + str(Bot_JoC))
        PlyAgn()
        #time.sleep(12)
        #quit()
    #BY=0
#    BD=0
 #   BS=0
  #  BC=0
   # BP=0
    def GtB():
        global Bot_JoC
        Bot_JoC= 0
        Bot_Given_Card= random.choice(Cards)
        if Bot_Given_Card == 'K' or Bot_Given_Card == 'Q' or Bot_Given_Card == 'J':
            print('Bot 1st card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
            Bot_Given_Card= 10
            Bot_JoC = Bot_Given_Card
        elif Bot_Given_Card == 'A':
            print('Bot 1st card is: '+ str(Bot_Given_Card))
            Bot_Given_Card= 11
            Bot_JoC = Bot_Given_Card
        elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
            Bot_JoC = Bot_Given_Card
            print('Bot 1st card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
        print('')
        if Bot_JoC <= 15:
            Bot_Given_Card= random.choice(Cards)
            #BD=0
            if Bot_Given_Card == 'K' or Bot_Given_Card == 'Q' or Bot_Given_Card == 'J':
                print('Bot 2nd card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                Bot_Given_Card= 10
                Bot_JoC += Bot_Given_Card
            elif Bot_Given_Card == 'A':
                print('Bot 2nd card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                Bot_Given_Card= 11
                Bot_JoC += Bot_Given_Card
            elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                Bot_JoC += Bot_Given_Card    
                print('Bot 2nd card is: ' + str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
            print('')
            if Bot_JoC <=15:
                Bot_Given_Card= random.choice(Cards)
                #BS=0
                if Bot_Given_Card == 'K' or Bot_Given_Card == 'Q' or Bot_Given_Card == 'J':
                    print('Bot 3rd card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                    Bot_Given_Card= 10
                    Bot_JoC += Bot_Given_Card
                elif Bot_Given_Card == 'A':
                    print('Bot 3rd card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                    Bot_Given_Card= 11
                    Bot_JoC += Bot_Given_Card
                elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                    Bot_JoC += Bot_Given_Card
                    print('Bot 3rd card is ' + str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                print('')
                if Bot_JoC <=15:
                    Bot_Given_Card= random.choice(Cards)
                    #BC=0
                    if Bot_Given_Card == 'K' or Bot_Given_Card == 'Q' or Bot_Given_Card == 'J':
                        print('Bot 4th card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                        Bot_Given_Card= 10
                        Bot_JoC += Bot_Given_Card
                    elif Bot_Given_Card == 'A':
                        print('Bot 4th card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                        Bot_Given_Card= 11
                        Bot_JoC += Bot_Given_Card
                    elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                        Bot_JoC += Bot_Given_Card
                        print('Bot 4th card is '+str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                    print('')
                    if Bot_JoC <=15:
                        Bot_Given_Card= random.choice(Cards)
                        #BP=0
                        if Bot_Given_Card == 'K' or Bot_Given_Card == 'Q' or Bot_Given_Card == 'J':
                            print('Bot 5th card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                            Bot_Given_Card= 10
                            Bot_JoC += Bot_Given_Card
                        elif Bot_Given_Card == 'A':
                            print('Bot 5th card is: '+ str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                            Bot_Given_Card= 11
                            Bot_JoC += Bot_Given_Card
                        elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                            Bot_JoC += Bot_Given_Card
                            print('Bot 5th card is '+str(Bot_Given_Card)+' '+str(random.choice(Smbls)))
                        print('')
                        #Bot_JoC= BY+BD+BS+BC+BP
                        Calculate()
                    if Bot_JoC>15:
                        Calculate()

                if Bot_JoC>15:
                    Calculate()

            if Bot_JoC>15:
                Calculate()
                
        if Bot_JoC>15:
            Calculate()


    def GtU():
        global JoC
        Given_Card= random.choice(Cards)
        if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
            print('Your card is:  ' + str(Given_Card)+' '+str(random.choice(Smbls)))
            Given_Card_Nom = 10 
            JoC += Given_Card_Nom           
            print('Total is: ' + str(JoC))

        elif Given_Card == 'A':
            print('Your card is:  ' + str(Given_Card)+' '+str(random.choice(Smbls)))
            Given_Card_Nom = 11 
            JoC += Given_Card_Nom           
            print('Total is: ' + str(JoC))
        else:
            print('Your card is:  ' + str(Given_Card)+' '+str(random.choice(Smbls)))
            JoC += Given_Card
            print('Total is: ' + str(JoC))
        import time
        time.sleep(0.2)
        GCardYN= input('Do you need more? (Y/N)')
        if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
            GtU()
        else:
            GtB()


    
    #Choose bet value
    def BetC():
        import PySimpleGUI as sg
        global Bet,Zrib
        Bet=0
        if Credit == 0:
            print('You don\'t have enough credit for playing (0$). \nPlease Charge your account.')
            time.sleep(6)
            quit()
        else:
            Bet=0
            def mn():
                global Bet,Zrib
                
                layout =[ [sg.Text('CREDIT: \t\t {0}'.format(Credit)),sg.Text('\t\t:اعتبار')],
                        [sg.Text('BET:   \t\t')  , sg.Input(size=(20,10),focus=True),sg.Text(' :مقدار')],
                        [sg.Button('PLAY\t\t\t\t\t شروع',button_color=('white','green'),size=(39,1))]
                        ]
                window = sg.Window('BETTING PANEL', layout, no_titlebar='True',keep_on_top=True)
                event, values = window.read()
                print('')
                try:
                    Bet= int(values[0])
                    print('')
                    
                except ValueError:
                    #print('PLEASE TYPE NUMBERS ONLY.')
                    sg.popup('.لطفا تنها از اعداد استفاده نمایید\nPLEASE TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5,icon='.\\GMsLOG\\Imgs\\PWR.ico')
                    BetC()
                print('')
                window.close()
            mn()

            if Bet>Credit:
                print('NOT ENOUGH CREDIT')
                time.sleep(2)
                BetC()
            else:
                #print('game is going on..')
                print('\n\n')
                GtU()        
        """if Credit == 0:
            print('You don\'t have enough credit for playing (0$). \nPlease Charge your account.')
            time.sleep(4)
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
                        GtU() 
            except ValueError:
                print('Invalid Number')
                BetC()"""


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
            subprocess.Popen('.\\GMsLOG\\GM--BJ.bat')
            quit()



    BetC()



    ################################
    """global JoC
    Given_Card= random.choice(Cards)
    print('Here it is; Your first card  ' + str(Given_Card))
    #NoC= NoC+1
    if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Given_Card_Nom = 10
        Y= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y))
        GtU()
    elif Given_Card == 'A':
        Given_Card_Nom = 11
        Y= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y))
        GtU()
    else:
        Y= Given_Card
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y))
        GtU()"""


"""def NeedMore():
    GCardYN= input('Do you need more? (Y/N)')
    if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
        #NoC= NoC+1
        Given_Card= random.choice(Cards)
        if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
            Given_Card_Nom = 10
            JoC= JoC + Given_Card_Nom
            print('Your card is:  ' + str(Given_Card))
            print('Total is: ' + str(JoC))
            
        elif Given_Card == 'A':
            Given_Card_Nom = 11
            JoC= JoC + Given_Card_Nom
            print('Your card is:  ' + str(Given_Card))
            print('Total is: ' + str(JoC))

        else:
            JoC= JoC + Given_Card
            print('Your card is:  ' + str(Given_Card))
            print('Total is: ' + str(JoC))
    
        NeedMore()
    
    else:
        Give_To_Bot()"""
    ###################################




Game()
