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


"""
import PySimpleGUI as sg
from PySimpleGUI import *
PopupAnimated('.\\GMsLOG\\Imgs\\Crash',
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





Crsh='''
CCCCCCC  RRRRRRR     A     SSSSSSS  HH   HH\t\t\t\t\t\t\t{0}
CC       RR   RR   AA AA   SS       HH   HH\t\t\t\t\t\t\tCredit: {1}
CC       RRRRRRR  AA   AA  SS       HH   HH
CC       RRR      AAAAAAA  SSSSSSS  HHHHHHH
CC       RR RR    AA   AA       SS  HH   HH
CCCCCCC  RR   RR  AA   AA  SSSSSSS  HH   HH
'''.format(Nickname, Credit)
print(Crsh)
print('Your credit is:' + str(Credit))




Prtcpt= 'T'
def Game():
    ###
    Wt()
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
        op_cch.write('Result= \''  + str(res) + '\''  +
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
        global Rnd_Incm
        Gain= int(Bet*Zrib - Bet)
        Rnd_Incm= int(Bet*Zrib)
        
        if i > MZrib:
            print('\n\n Game has been finished at:' + str(MZrib) + 'x')
            if Zrib <= MZrib:
                #print('')
                #print('Game has finished at ' + str(MZrib) + 'x')
                if Prtcpt != 'F':
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
                if Prtcpt != 'F':
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
"""
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
"""

#####
## value= sg.PopupOKCancel('PopupOKCancel')
#####
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

def Wt():
    import os
    a=6.0
    #for nom in a:
    while a>=0.1:
        a-=0.1
        a= round(a,2)
        print(a)
        os.system('cls')
        print(Crsh)
    print('Match is started')


def BetC():
    import PySimpleGUI as sg
    global Bet,Zrib
    Zrib=0
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
                      [sg.Text('COEFFICENT:\t'), sg.Input(size=(20,10)),sg.Text(' :ضریب')],
                      [sg.Button('PLAY\t\t\t\t\t شروع',button_color=('white','green'),size=(39,2))]
                      #[sg.Button('PLAY'),sg.Text('\t\t\t\t'),sg.Button('شروع')]  # sg.Button('Exit')
                    ]
            window = sg.Window('BETTING PANEL', layout, no_titlebar='True',keep_on_top=True)
            event, values = window.read()
            """
            if Bet==0 and Zrib==0:
                #Zrib=0
                #Bet=0
                window.close()
                Game()
            else:
            #print(Bet)
            #print(Zrib)
            """
            try:
                Bet= int(values[0])
                print('')
                
            except ValueError:
                #print('PLEASE TYPE NUMBERS ONLY.')
                sg.popup('.لطفا تنها از اعداد استفاده نمایید\nPLEASE TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5,icon='.\\GMsLOG\\Imgs\\PWR.ico')
                BetC()
            print('')
            try:
                Zrib= float(values[1])
                Zrib= round(float(Zrib),2)
                if Zrib < 1.01:
                    print('AT LEAST YOU HAVE TO CHOOSE 1.01.')
                    BetC()
                if Zrib > 99.99:
                    print('99.99 IS THE MOST COEFFICENT.\n')
                    BetC()
                if 99.99 >= Zrib >= 1.01:
                    if Bet==0:
                        global Prtcpt
                        Prtcpt= 'F'
                        print('You did\'t participate in this this round.')
                    else:    
                        print('BET:\t\t {0}'.format(Bet))
                        print('COEFIICENT:\t\t {0}'.format(Zrib))
            except ValueError:
                #print('INVALID INPUT.\nYOU HAVE TO TYPE NUMBERS ONLY.\n')
                sg.popup('ضریب فقط میتواند عدد باشد.\nYOU HAVE TO TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=4,icon='.\\GMsLOG\\Imgs\\PWR.ico')
                BetC()
            window.close()
        mn()

        if Bet>Credit:
            print('NOT ENOUGH CREDIT')
            time.sleep(2)
            BetC()
        else:
            #print('game is going on..')
            print('\n\n')
            Game()
    
BetC()
