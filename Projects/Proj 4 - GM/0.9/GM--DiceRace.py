import time
from random import randrange
from Ac_Info import *
import ZZSave
#from ZZSave import VluOfPlyd

print('Your Credit is: {}'.format(Credit))
############################################################################
############################################################################
############################################################################
def cache(res):
    op_cch= open('.\\ZZDRcach.py',mode='w')
    op_cch.write('Result= \''  + str(res) + '\'' +
                 '\nBet= '     + str(Bet)  + 
                 '\nUsrRoll= '   + str(player_scope)  +
                 '\nBotRoll= ' + str(comp_scope)    
                 )
    op_cch.close()
############################################################################
def WinF():
    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                 'Credit= '         + str(Credit+Bet) +
                 '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                 '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                 '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses)  +
                 '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                 '\nDR_Wins= '  + str(DR_Wins+1)    + '\nDR_Loses= '+ str(DR_Loses) +
                 '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                 )
    op_inf.close()
    #VluOfPlyd(Bet)
    cache('Win')
    time.sleep(1)
    ZZSave.SDRWin()

def LooseF():
    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                 'Credit= '         + str(Credit-Bet) +
                 '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                 '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                 '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses)  +
                 '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses) +
                 '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses+1) +
                 '\nRmnnVluCshot= '  + str(RmnnVluCshot - Bet)
                 )
    op_inf.close()
    #VluOfPlyd(Bet)
    cache('Loose')
    time.sleep(1)
    ZZSave.SDRLoose()
############################################################################
############################################################################
############################################################################
def Game():
    global player_scope
    global comp_scope
    #----------Function print_dice----------------------------
    def print_dice(dice_one, dice_two):
        #---------Lists for the formation of the dice----------
        d1 = ['422222224',
            '300000003',
            '300010003',
            '300000003',
            '422222224']

        d2 = ['422222224',
            '301000003',
            '300000003',
            '300000103',
            '422222224']
        
        d3 = ['422222224',
            '300000103',
            '300010003',
            '301000003',
            '422222224']
            
        d4 = ['422222224',
            '301000103',
            '300000003',
            '301000103',
            '422222224']
            
        d5 = ['422222224',
            '301000103',
            '300010003',
            '301000103',
            '422222224']      
        
        d6 = ['422222224',
            '301000103',
            '301000103',
            '301000103',
            '422222224']
            
        dice = [d1, d2, d3, d4, d5, d6]
        #--END----Lists for the formation of the dice------
        
        
        d1 = dice[dice_one-1]
        d2 = dice[dice_two-1]
        res_dice = []
        
        #-----------combine dice--------
        for i in range(0,5):
            res_dice.append(d1[i]+d2[i])
            i += 1
        #---END-----combine dice-------    
        
        #----------Print two dice------
        i = 0      
        res = ''      
        for ls in res_dice:
            for t in ls:
                if i == len(ls)/2: res += '   '
                if t =='2':
                    res += '-'
                elif t == '3':
                    res += '|'
                elif t == '4':
                    res += '+'
                elif t == '1':
                    res += 'O'
                else:
                    res += ' '
                i += 1    
            print(res)
            res = ''
            i = 0
        #---END----Print two dice------
    #--END-----Function print_dice------------------

    #------Your roll two dice, and their sum--------
    player_dice_one = randrange(1,6)               
    player_dice_two = randrange(1,6)
    if player_dice_one ==player_dice_two:
        player_scope = player_dice_one + player_dice_two + 1
    else:
        player_scope = player_dice_one + player_dice_two

    #------Your roll two dice, and their sum--------
    comp_dice_one = randrange(1,6)
    comp_dice_two = randrange(1,6)
    if comp_dice_one == comp_dice_two:
        comp_scope = comp_dice_one + comp_dice_two + 1
    else:
        comp_scope = comp_dice_one + comp_dice_two
    #---------Print result--------------------------
    print('\n.....Your   Roll......')    
    time.sleep(1)
    print_dice(player_dice_one, player_dice_two)
    time.sleep(3)
    print('\n......Bot   Roll......')
    time.sleep(1)
    print_dice(comp_dice_one, comp_dice_two)
    #---------Determine the winner------------------
    time.sleep(2)
    print('')
    if player_scope > comp_scope:
        print('-------You Win-------')
        print(u'\u0020'*7+str(player_scope)+' Vs '+str(comp_scope))
        print('\nYou won ' + str(Bet))
        WinF()
    elif player_scope < comp_scope:
        print('------You Lose-------')
        print(u'\u0020'*7+str(player_scope)+' Vs '+str(comp_scope))
        print('\nYou Lose ' + str(Bet))
        LooseF()
    else:
        print('--------Draw---------')
        print(u'\u0020'*7+str(player_scope)+' Vs '+str(comp_scope))
    time.sleep(1)
    PlyAgn()
    #---END---Determine the winner------------------

############################################################
############################################################
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
        subprocess.Popen('.\\GMsLOG\\GM--DiceRace.bat')
        quit()



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
            
            layout =[ [sg.Text('CREDIT: \t\t   {0}'.format(Credit)),sg.Text('\t\t:اعتبار')],
                    [sg.Text('BET:   \t\t')  , sg.Input(size=(20,10),focus=True),sg.Text('   :مبلغ')],
                    [sg.Button('PLAY\t\t\t\t\t شروع',button_color=('white','green'),size=(39,1))]
                    ]
            window = sg.Window('BETTING PANEL', layout, no_titlebar='True',keep_on_top=True)
            event, values = window.read()
            window.close()
            print('')
            try:
                Bet= int(values[0])
                print('')
                
            except ValueError:
                #print('PLEASE TYPE NUMBERS ONLY.')
                sg.popup('.لطفا تنها از اعداد استفاده نمایید\nPLEASE TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5,icon='.\\GMsLOG\\Imgs\\Dice.ico')
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
            #print('\n\n')
            print('Bet: {}'.format(Bet))
            Game()  




BetC()
