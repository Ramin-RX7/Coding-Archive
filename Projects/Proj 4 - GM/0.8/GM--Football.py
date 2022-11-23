#
# 1- Nom of attempts (In targets)
# 2- Nom of fouls
# 3- Nom of cards
# 4- % of possession
#

from pyautogui import press
press('f11')
import time
import random
from Ac_Info import *
import ZZSave

import PySimpleGUI as sg


#global variables
#Spanish Teams
barcelona = ['Barcelona','LUIS SUAREZ','MESSI','ANTOINE GRIEZMAN','DEMBELE','RAKITIC','DE JONG','SERGIO.B','PIQUE','ALBA','UMTITI','TER STEGEN']  # ARTURO VIDAL - 
madrid = ['Real Madrid', 'BALE','BENZEMA','EDEN HAZARD','KROOS','MODRIC','MARCO ASENSIO','CASEMIRO','CARVAJAL','SERGIO RAMOS','MARCELO','THIBAUT COURTOIS'] # MARCO ASENSIO - ISCO
valencia = ['Valencia','RODRIGO','GOMES GONZALEZ','JOSE GAYA','PAREJO','DANIEL WASS','COQUELIN','GEOFFREY KONDOGBIA','EZEQUEIL GARAY','JAVIER JIMENEZ','GABRIEL PAULISTA','CILLESSEN']
atmadrid = ['Atletico Madrid','DIEGO COSTA','ALVARO MORATA','JOAO FELIX','SAUL','KOKE','GABI','JUANFRAN','GIMENEZ','DOS SANTOS','TRIPPIER','JAN OBLAK']
sevilla = ['Sevilla','EL HADDADI MUNIR','JAVIER HERNANDEZ','KOUNDLE','LUCAS OCAMPOS','JESUS NAVAS','OLIVER TORRES','BANEGA','JOAN JORDAN','SANTOS SILVA','RODRIGUES','vACLIK']
#English Teams
manc = ['Manchester City','KUN AGUERO','GABRIEL JESUS','RAHEEM STERLING','DAVID SILVA','KEVIN DE BRUYNE','GUNDOGAN','FERNANDINHO','NICOLAS OTAMENDI','LAPORTE','KYLE WALKER','EDERSON']  # BERNARDO SILVA - SANE - RODRI
manu = ['Manchester United','RASHFORD','ANTHONY MARTIAL','LINGARD','MATA','NEMANJA MATIC','PAUL POGBA','MAGUIRE','LINDELOF','WAN-BISSAKA','ASHLEY YOUNG','DE GEA']
chelsea = ['Chelsea','GIROUD','TAMMY ABRAHAM','WILLIAN','MATEO KOVACIC','JORGINHO',"N'GOLO KANTE",'MARCOS ALONSO','AZPILICUETA','ANTONIO RUDIGER','ZOUMA','KEPA']#Jorginio
tottenham = ['Tottenham','HARRY KANE','HEUNG-MIN SON','DELE ALLI','CHRISTIAN ERIKSON','LUCAS MOURA','ERIC DIER','TOBY ALDERWEIRALD','DANNY ROSE','JAN VERTONGHEN','KYLE WALKER','HUGO LLORIS'] #SISSOKO
liverpool = ['Liverpool','SADIO MANE','ROBERTO FIRMINO','MOHAMED SALAH','OXLADE-CHAMBERLAIN','JORDAN HENDERSON','GEORGINIO WIJNALDUM','ALEXANDER ARNOLD','ROBERTSON','VIRGIL VAN DIJK','FABINHO','ALISSON'] # JAMES MILNER - NABY KEITA - SHAQIRI
arsenal= ['Arsenal','AUBAMEYANG','LACAZZETE','PEPE','TORIERRA','OZIL','GRANIT XHAKA','HECTOR BELLERIN','DAVID LUIS','KOLASINAC','SOKRATIS','LENO'] # MUSTAFI - CEBALLOS - GUENDOUZI - 
#Italian Teams
napoli = ['Napoli','LORENZO INSIGNE','JOSE CALLEJON','LOZANO','ALLAN','RUIZ OENA','ZIELINSKI','MARIO RUI','KALIDOU KOULIBALY','DI LORENZO','MANOLAS','ALEX MERET']
juventus = ['Juventus','RONALDO','PAULO DYBALA','GONZALO HIGUAIN','DOUGLAS COSTA','JUAN CAUDRADO','DE LIGT','LEONARDO BONUCCI','GIORGIO CHIELLINI','DANI ALVES','GIANlUIGI BUFFON']  # MARIO  MANDZUKIC - MATUIDI - RABIOT - SAMI KHEDIRA
inter = ['Inter Milan','MROMELU LUKAKU','LAUTARO MARTINEZ','ALEXIS SANCHEZ','MARCELO BROZOVIC','ANTONIO CANDREVA','ASAMOAH','DIEGO GODIN','STEFAN DE VRIJ',"DANILO D'AMBROSIA",'SKRINIAR','SAMIR HANDANOVIC']#ROMELU LUKAKU - Alexis Sanchez
roma = ['AS Roma','EDIN DZEKO','KLUIVERT','PASTORE','MKHITARYAN','JORDAN VERETOUT','ZANIOLO','KOLAROV','SMALLING','MANCINI','FEDERICO FAZIO','PAU LOPEZ']
lazio = ['Lazio','FELIPE CAICEDO','CIRO IMMOBILE','SAVIC','FELIPE CAICEDO','LUIS ALBERTO','RADU','LAZZARI','ACERBI','RAMOS MARCHI','LUCAS LEIVA','THOMAS STRAKOSHA']
#Other Teams
psg= ['PSG','CAVANI','MBAPPE','NEYMAR','ICARDI','VERRATI','DI MARIA','DERAXLER','KIMPEMBE','MARQUINHOS','TIAGO SILVA','KEYLOR NAVAS']
byrn=['Bayern Munich','LEWANDOVSKI','MULLER','GNABRY','COUTINHO','PERISIC','KINGSLEY COMAN','THIAGO','KIMMICH','ALABA','PAVARD','NEUR']
bvb= ['Borussia Dortmund','REUS','PACO ALCASER','THORGAN HAZARD','JADON SANCHO','WITSEL','JULIAN WEIGL','LUCASZ PISZCZEK','MANUEL AKANJI','ACHRAF HAKIMI','HUMMELS','BURKI']

####
####
TeamPowers= {'Liverpool':         99, 
             'Barcelona':         94, 
             'Real Madrid':       94,
             'Bayern Munich':     90, 
             'Juventus':          90,
             'PSG':               87, 
             'Manchester City':   86, 
             'Atletico Madrid':   82, 
             'Borussia Dortmund': 82,
             'Inter Milan':       80, 
             'Chelsea':           76, 
             'Arsenal':           76, 
             'AS Roma':           76, 
             'Manchester United': 76, 
             'Tottenham':         76, 
             'Sevilla':           71, 
             'Napoli':            71, 
             'Valencia':          66, 
             'Lazio':             66, 
            }
Cards_Get= 0
ResultGm= 0
BetGoal= 0
Goal_Number_Bet= 0
team1 = chelsea
team2 = manu
goals = 0
scorers = []
yellow = []
red = []
Bet_Type= ''
Bet= ''
UsrChs=''
Income= ''


def tedad():
    from datetime import datetime
    #CrDt= datetime.today().strftime('Dt%m_%d')
    DT= datetime.today().strftime('%d')
    DT=str(DT)
    XX=0
    for nom in DT:
        XX+=int(nom)
    #print(DT)
    QT= datetime.today().strftime('%m%d')
    fll= QT+'.py'
    import os
    if os.path.exists('GMsLOG\\Prdct\\'+fll)==True:
        opgmr= open('GMsLOG\\Prdct\\'+fll,mode='r')
        opgmrr= opgmr.read()
        #print((len(opgmrr)-12)/2)
        if (len(opgmrr)-12)/2 < int(XX):
            opgmrr= opgmrr[0:-1]
            opgmw= open('GMsLOG\\Prdct\\'+fll,mode='w')
            opgmw.write(str(opgmrr) +'1,]')
            opgmw.close()
        else:
            print('YOU CAN NOT PLAY ANYMORE TODAY. \nPLAY FOOTBAL FORCAST TOMORROW')
            time.sleep(5)
            quit()
    else:
        a=open('GMsLOG\\Prdct\\'+fll, mode='w')
        a.write('PrdctNom= [1,]')
        a.close()
tedad()






layout= [
        [sg.Text('Credit:\t\t    {0}\t\t :موجودی'.format(Credit),font=(35))],
        [sg.Button('START\t\t\tشروع',button_color=('White','Green'),size=(40,2),font=(15))]
        ]
window = sg.Window('Match Result - {}'.format(Credit), layout,size=(400,100),no_titlebar=True,auto_close=True,auto_close_duration=5,keep_on_top=True,)
event, values = window.read()
window.close()
#print('YOUR CREDIT IS: '+str(Credit)+'\n')
#randoms
def select_team():
    global team1, team2, checker, checker2
    checker2 = True
    checker = None

    teams = {'PSG':psg,'BORUSSIA DORTMUND':bvb,'BAYERN MUNICH':byrn,'BARCELONA':barcelona,'REAL MADRID':madrid,'VALENCIA':valencia,'ATLETICO MADRID':atmadrid,'SEVILLA':sevilla,'MANCHESTER CITY':manc,'MANCHESTER UNITED':manu,'CHELSEA':chelsea,'TOTTENHAM':tottenham,'LIVERPOOL':liverpool,'ARSENAL':arsenal,'NAPOLI':napoli,'JUVENTUS':juventus,'INTER MILAN':inter,'AS ROMA':roma,'LAZIO':lazio}
    teamL= ['Liverpool','Manchester City','Arsenal','Chelsea','Manchester United','Tottenham',
            'Real Madrid','Barcelona','Atletico Madrid','Valencia','Sevilla',
            'Juventus','Inter Milan','AS Roma','Lazio',
            'Bayern Munich','Borussia Dortmund','PSG'
            ]
    import random
    team1 = random.choice(teamL)
    teamL.remove(team1)
    team1= team1.upper()
    #print(team1)
    if team1 in teams.keys():
        team1 = teams[team1]
        checker = True
    else:
        print(team1,'Does not exist or has not yet been added!!!')
        checker = False
    team2 = random.choice(teamL)
    teamL.remove(team2)
    team2= team2.upper()
    #print(team2)
    if team2 in teams.keys():
        team2 = teams[team2]
        if checker != False:
           checker = True
    else:
        print(team2,'Does not exist or has not yet been added')
        checker = False
    if team2 == team1:
        checker2 = False
    print(team1[0] + '  VS  ' + team2[0])

    layout=[
             [sg.Button('{0}   VS   {1}'.format(team1[0],team2[0]),button_color=('White','Black'),size=(250,50),font=(250,50))]
            ]
    window = sg.Window('Match Result - {}'.format(Credit), layout,size=(1000,180),no_titlebar=True,auto_close=True,auto_close_duration=5,keep_on_top=True, )
    event, values = window.read()
    window.close()



select_team()
def find_team(player):
    if player in team1:
        return team1
    else:
        return team2

def add2lst():
    global Income
    if Result == 'Win':
        pass
    else:
        Income= Bet - Bet*2
        print(Income)
    op_cch= open('.\\ZZFootballcach.py',mode='w')
    op_cch.write('Type= \''  + str(Bet_Type) + '\'' +
                 '\nBet= '     + str(Bet)  + 
                 '\nZrib= '     + str(Zrib)  + 
                 '\nUsrChs= '   + str(UsrChs)  +
                 '\nResult= \'' + str(Result) + '\'' +
                 '\nIncome= ' + str(Income)   
                 )
    op_cch.close()
    ZZSave.SFootball()


def WinBetC(TeamNom,Bet):
    global Result,Income
    Income= Bet*TeamNom
    Income= int(Income)
    print('You Won ' + str(Income))
    op_inf= open('.\\Ac_Info.py',mode='w')
    NCredit= Credit - Bet + Income
    NVluCshot= RmnnVluCshot-Bet
    Result= 'Win'
    op_inf.write('''Nickname= "{0}"
Credit= {1}
Crash_Wins= {2}  \nCrash_Loses= {3}
BJ_Wins= {4}     \nBJ_Loses= {5}
RPS_Wins= {6}    \nRPS_Loses= {7}
RatioX_Wins= {8} \nRatioX_Loses= {9}
DR_Wins= {10}   \nDR_Loses= {11}
RmnnVluCshot= {12}'''.format(Nickname,NCredit,Crash_Wins,Crash_Loses,BJ_Wins,BJ_Loses,RPS_Wins,RPS_Loses,RatioX_Wins,RatioX_Loses,DR_Wins,DR_Loses,NVluCshot)
                )
    op_inf.close()    
def LooseBetC(Bet):
    print('You Lost ' + str(Bet))
    global Result
    Result= 'Lose'
def BetResF():
    global team1Zrb
    global team2Zrb
    global DrawZrb

    if TeamPowers[team1[0]] > TeamPowers[team2[0]]:
        if TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 30:
            team1Zrb= 1.20
            DrawZrb=  2.15
            team2Zrb= 3.05    
        if 29 >= TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 21:
            team1Zrb= 1.25
            DrawZrb=  1.95
            team2Zrb= 2.45
        if 21 > TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 15:
            team1Zrb= 1.35
            DrawZrb=  1.85
            team2Zrb= 2.15
        if 15 > TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 10:
            team1Zrb= 1.55
            DrawZrb=  1.80
            team2Zrb= 2.05
        if 10 > TeamPowers[team1[0]] - TeamPowers[team2[0]] > 5:
            team1Zrb= 1.85
            DrawZrb=  1.70
            team2Zrb= 2.15
        if 5 >= TeamPowers[team1[0]] - TeamPowers[team2[0]]:
            team1Zrb= 2.15
            DrawZrb=  1.55
            team2Zrb= 2.25        

    elif TeamPowers[team1[0]] < TeamPowers[team2[0]]:
        if TeamPowers[team2[0]] - TeamPowers[team1[0]] > 29:
            team1Zrb= 3.05
            DrawZrb=  2.15
            team2Zrb= 1.20    
        if 29 >= TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 21:
            team1Zrb= 2.15
            DrawZrb=  1.85
            team2Zrb= 1.25
        if 21 > TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 15:
            team1Zrb= 1.95
            DrawZrb=  1.70
            team2Zrb= 1.35
        if 15 > TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 10:
            team1Zrb= 2.05
            DrawZrb=  1.80
            team2Zrb= 1.55
        if 10 > TeamPowers[team2[0]] - TeamPowers[team1[0]] > 5:
            team1Zrb= 2.15
            DrawZrb=  1.70
            team2Zrb= 1.85
        if 5 >= TeamPowers[team2[0]] - TeamPowers[team1[0]]:
            team1Zrb= 2.25
            DrawZrb=  1.55
            team2Zrb= 2.15  

    elif TeamPowers[team1[0]] == TeamPowers[team2[0]]:
        team1Zrb= 1.75
        DrawZrb=  1.35
        team2Zrb= 1.75
    print(team1[0]+':\t\t\t\t'+str(team1Zrb))
    print('Draw:\t\t\t\t\t'+str(DrawZrb))
    print(team2[0]+':\t\t\t\t'+str(team2Zrb))


    from Ac_Info import Credit
    global ResultGm
    #sg.ChangeLookAndFeel('Black')
    #ResultGm= input('Result:   1-'+team1[0]+'  2-Draw  3-'+team2[0]+'           ')
    layout= [
            [sg.Text('Who Will win the game?\t\t برنده بازی؟')],
            #[sg.Listbox(values=['{0}                                   {1}x'.format(team1[0],team1Zrb), 'Draw                                        {0}x'.format(DrawZrb), '{0}                                   {1}x'.format(team2[0],team2Zrb)], size=(40, 5),auto_size_text=True)],
            [sg.Listbox(values=['{0}'.format(team1[0]), 'Draw', '{0}'.format(team2[0])], size=(40, 5),auto_size_text=True)],
            [sg.Button('SET BET\t\t\tانتخاب شرط',button_color=('White','Green'),size=('40','6'),tooltip='You will turn to betting page.\n.با کلیک کردن به صفحه انتخاب مبلغ هدایت میشوید')]
            ]

    window = sg.Window('Match Result - {}'.format(Credit), layout,size=(350,180),icon='.\\GMsLOG\\Imgs\\Football.ico')
    event, values = window.read()
    window.close()
    if values[0] == None or values[0] == []:
        #ResultGM= ''
        BetCardsF()
    else:
        values[0]=values[0][0]
        if values[0]==team1[0]:
            ResultGm = '1'
        if values[0]=='Draw':
            ResultGm = '2'
        if values[0]==team2[0]:
            ResultGm = '3'
        print('MATCH RESULT BET:   {}'.format(values[0]))
        global BetRes 
        BetRes=0
        if ResultGm == '1' or ResultGm == '2' or ResultGm == '3':
            layoutMB=[
                    [sg.Text('Credit: \t\t{}\t\t:موجودی'.format(Credit))],
                    [sg.Text('BET:   \t')  , sg.Input(size=(20,10),focus=True),sg.Text(' :مقدار')],
                    [sg.Button('BET\t\t\tشرطبندی',button_color=('White','Green'),size=('40','6'),tooltip='BET\tثبت شرط')]
                    ]
            windowMB = sg.Window('Match Result - {}'.format(Credit), layoutMB,size=(350,100),icon='.\\GMsLOG\\Imgs\\Football.ico')
            event, values = windowMB.read()
            windowMB.close()
            BetRes= values[0]

            #print('Your credit is:' + str(Credit))
            try:
                BetRes = int(BetRes)
                if BetRes > Credit:
                    sg.popup('You don\'t have enough credit.\n.اعتبار شما برای این مبلغ کافی نیست',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5)
                    BetResF()
                else:
                    #Start the game
                    if BetRes == 0:
                        sg.popup('It\'s not enough for playing.\n.این مبلغ برای بازی کردن کافی نیست',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5)
                        BetResF()
                    else:
                        op_inf= open('.\\Ac_Info.py',mode='w')
                        op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                                    'Credit= '         + str(Credit - BetRes)                                   +
                                    '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                                    '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)    +
                                    '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)   +
                                    '\nRatioX_Wins= '  + str(RatioX_Wins)+ '\nRatioX_Loses= '+ str(RatioX_Loses)+
                                    '\nDR_Wins= '      + str(DR_Wins)    + '\nDR_Loses= '    + str(DR_Loses)    +
                                    '\nRmnnVluCshot= ' + str(RmnnVluCshot - BetRes)
                                    )
                        op_inf.close()
            except ValueError:
                sg.popup('.لطفا تنها از اعداد استفاده نمایید\nPLEASE TYPE NUMBERS ONLY.',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5)
                #print('Invalid Number')
                BetResF()
        
        elif ResultGm == '':
            BetCardsF()

        else:
            sg.popup('Invalid Input.\n.ورودی نامعتبر',title='Error',keep_on_top=True,auto_close=True,auto_close_duration=5)
            #print('Invalid Input.')
            BetResF()

def BetCardsF():
    global Cards_Get
    print('Your credit is:' + str(Credit))
    Cards_Get= input('Number of Cards:    \n1-More than 2.5 (1.30x)     2-Less than 2.5  (1.75x)\n3-More than 3.5 (2.05x)     4-Less than 3.5  (1.30x)        ')
    if Cards_Get == '1' or Cards_Get == '2' or Cards_Get == '3' or Cards_Get == '4': 
        global BetCards   
        BetCards= int(input('Type your bet: '))
        try:
            if BetCards > Credit:
                print('You don\'t have enough credit.')
                BetCardsF()
            else:
                #Start the game
                if BetCards == 0:
                    print('It\'s not enough for playing.')
                    BetCardsF()
                else:
                    op_inf= open('.\\Ac_Info.py',mode='w')
                    op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                                'Credit= '         + str(Credit - BetCards)+
                                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                                '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                                '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                                '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                                '\nRmnnVluCshot= '  + str(RmnnVluCshot - BetCards)
                                )
                    op_inf.close()
        except ValueError:
            print('Invalid Number')
            BetCardsF()

    elif Cards_Get == '':
        BetGoalsF()

    else:
        print('Invalid input. \n')
        BetCardsF()

def BetGoalsF():
    global Goal_Number_Bet
    print('Your credit is:' + str(Credit))
    Goal_Number_Bet= input('Number of Goals:     \n1-More than 2.5 (1.40x)       2-Less than 2.5 (2.05) \n3-More than 3.5 (1.75x)       4-Less than 3.5 (1.60) \n5-More than 4.5 (2.60x)       6-Less than 4.5 (1.25)\n')
    if Goal_Number_Bet == '1' or Goal_Number_Bet == '2' or Goal_Number_Bet == '3' or Goal_Number_Bet == '4' or Goal_Number_Bet == '5' or Goal_Number_Bet == '6': 
        global BetGoal   
        BetGoal= input('Type your bet: ')
        try:
            BetGoal = int(BetGoal)
            if BetGoal > Credit-BetRes:
                print('You don\'t have enough credit.')
                BetGoalsF()
            else:
                #Start the game
                if BetGoal == 0:
                    print('It\'s not enough for playing.')
                    BetGoalsF()
                else:
                    op_inf= open('.\\Ac_Info.py',mode='w')
                    op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                                'Credit= '         + str(Credit - BetGoal)+
                                '\nCrash_Wins= '   + str(Crash_Wins)  + '\nCrash_Loses= '  + str(Crash_Loses) +
                                '\nBJ_Wins= '      + str(BJ_Wins)     + '\nBJ_Loses= '     + str(BJ_Loses)      +
                                '\nRPS_Wins= '     + str(RPS_Wins)    + '\nRPS_Loses= '    + str(RPS_Loses)     +
                                '\nRatioX_Wins= '  + str(RatioX_Wins) + '\nRatioX_Loses= ' + str(RatioX_Loses)  +
                                '\nDR_Wins= '      + str(DR_Wins)     + '\nDR_Loses= '     + str(DR_Loses) +
                                '\nRmnnVluCshot= ' + str(RmnnVluCshot - BetGoal)
                                )
                    op_inf.close()
        except ValueError:
            print('Invalid Number')
            BetGoalsF()

    elif Goal_Number_Bet == '':
        pass

    else:
        print('INVALID INPUT. \n\n')
        BetGoalsF()    



def randomness():
    global team, w, teams,strikers, midfielders, re, rea, GK
    w = random.randint(1,2)
    teams = (team1, team2)

    PwrT= TeamPowers[team1[0]] + TeamPowers[team2[0]]
    LmtTm= random.randint(0,PwrT)
    if LmtTm <= TeamPowers[team1[0]]:
        team= team1
        teamO= team2
    else:
        team= team2
        teamO= team1
    
    #team = random.choice(teams)
    strikers = random.choice(team[1:3])
    midfielders =random.choice(team[4:6])
    re = [strikers, midfielders]
    rea = random.choice(re)
    GK= teamO[-1]

randomness()
defenders = None

def organize(rea):
    global defenders
    if rea in team1:
        defenders = random.choice(team2[7:-2])
    else:
        defenders = random.choice(team1[7:-2])

def versus():
    #print('{0}   VS   {1}'.format(team1[0], team2[0]))
    pass

def lineup():
    time.sleep(2)
    print('')
    print('The of lineup of {0} is:'.format(team1[0]))
    for i in team1[1::]:
        print(i)
        time.sleep(1)
    time.sleep(2.5)
    print('\n\nThe of lineup of {0} is:'.format(team2[0]))
    for i in team2[1::]:
        print(i)
        time.sleep(1)
    time.sleep(4)

def scoresheet():
    global scorers
    c = 0
    minutes = []
    goal_scorers = []
    goalcount1 = 0
    goalcount2 = 0
    for i in scorers:
     goal_scorers.append(scorers[c][0])
     c += 1
    c = 0
    for i in scorers:
        minutes.append(scorers[c][1])
        c += 1
    for i in goal_scorers:
        if i in team1:
            goalcount1 += 1
        else:
            goalcount2 += 1

    print(team1[0]+'  '+str(goalcount1)+' - '+str(goalcount2)+'  '+team2[0])
    print('\n')
    if goalcount1>goalcount2:
        print(team1[0] + ' Wins!')
        #if TeamPowers[team1[0]] - TeamPowers[team2[0]] == : 
    elif goalcount2>goalcount1:
        print(team2[0] + ' Wins!')
    elif goalcount1 == goalcount2:
        print('Its draw!')


    print('')
    print('SCORERS:')
    c = 0
    for i in goal_scorers:
        print("   {0} \t '{1}'".format(i,str(minutes[c])))
        c += 1
    print('')
    print('CARDS: ')
    try:
        global yellow
        print('YELLOW Cards: ')
        for item in yellow:
            print('   '+item)
    except NameError:
        print('NO YELLOW CARDS.')
    print('')
    try:
        global red
        print('Red Cards: ')
        for item in red:
            print('   '+item)
    except NameError:
        print('NO RED CARDS.')

    Offside_Nom1= random.randint(3,6)
    Offside_Nom2= random.randint(3,6)
    Corner_Nom1 = random.randint(3,7)
    Corner_Nom2 = random.randint(3,7)
    import PySimpleGUI as sg
    sg.Popup('{0}\t\tTEAMS\t\t{1}       \n{2}\t\t\tGoals\t\t\t{3}   \n{4}\t\t\tOffsides\t\t{5}     \n{6}\t\t\tCorners\t\t\t{7}'.format(team1[0],team2[0],str(goalcount1),str(goalcount2),str(Offside_Nom1),str(Offside_Nom2),str(Corner_Nom1),str(Corner_Nom2)),auto_close=True,auto_close_duration=15,keep_on_top=True,)
    #time.sleep(5)

    global ResultGm
    global team1Zrb
    global team2Zrb
    global DrawZrb
    print('\n')
    print('BET:\n')
    if ResultGm == '1' or ResultGm == '2' or ResultGm == '3':
        global Bet_Type,Bet,Zrib,UsrChs
        Bet= BetRes
        Bet_Type= 'Main'
        UsrChs= ResultGm
        print('GAME RESULT: ')
        if ResultGm == '1':
            Zrib= team1Zrb
            YP='YOUR PREDICTION:     HOME WINNING\t\t\tپیشبینی شما:    برد میزبان'
            if goalcount1>goalcount2:
                Rslt='RESULT:              \t\tHOME WON\t\t\t\tنتیجه:    برد میزبان'
                WL='YOU WON!'
                WinBetC(team1Zrb,BetRes)
            else:
                if goalcount1<goalcount2:
                    Rslt='RESULT:              \t\tAWAY WON\t\t\t\tنتیجه:    برد میهمان'
                if goalcount1==goalcount2:
                    Rslt='RESULT:              DRAW\t\t\t\t\tنتیجه:    تساوی'
                WL='YOU LOST!'
                LooseBetC(BetRes)
        if ResultGm == '2':
            Zrib= DrawZrb
            YP='YOUR PREDICTION:     DRAW\t\t\t\tپیشبینی شما:     مساوی'
            if goalcount1==goalcount2:
                Rslt='RESULT:              DRAW\t\t\t\tنتیجه:    تساوی'
                WL='YOU WON!'
                WinBetC(team1Zrb,BetRes)
            else:
                if goalcount1>goalcount2:
                    Rslt='RESULT:              \t\tHOME WON\t\t\tنتیجه:    برد میزبان'
                if goalcount1<goalcount2:
                    Rslt='RESULT:              \t\tAWAY WON\t\t\tنتیجه:    برد میهمان'
                WL='YOU LOST!'
                LooseBetC(BetRes)
        if ResultGm == '3':
            Zrib= team2Zrb
            YP='YOUR PREDICTION:     AWAY WINNING\t\t\tپیشبینی شما:    برد میهمان'
            if goalcount1<goalcount2:
                Rslt='RESULT:              \t\tAWAY WON\t\t\tنتیجه:    برد میهمان'
                WL='YOU WON!'
                WinBetC(team2Zrb,BetRes)
            else:
                if goalcount1>goalcount2:
                    Rslt='RESULT:              \t\tHOME WON\t\t\tنتیجه:    برد میزبان'
                if goalcount1==goalcount2:
                    Rslt='RESULT:              DRAW\t\t\t\tنتیجه:    تساوی'                   
                WL='YOU LOST!'
                LooseBetC(BetRes)

        import PySimpleGUI as sg
        sg.popup('{0}\n{1}\n{2}'.format(YP,Rslt,WL))
        #time.sleep(5)            
        print('\n')
    else:
        pass
    ####
    #global yellow
    #global red
    print('')
    if Cards_Get == '1' or Cards_Get == '2' or Cards_Get == '3' or Cards_Get == '4':
        #global Bet_Type,Bet,UsrChs
        UsrChs= Cards_Get
        Bet= BetCards
        Bet_Type= 'Card'
        print('NUMBER OF CARDS: ' + str(len(yellow)+len(red)))
        if Cards_Get == '1':
            Zrib= 1.3
            if len(yellow)+len(red) > 2:
                print('YOU WON!')
                WinBetC(1.3,BetCards)
            else:
                print('YOU LOST!')
                LooseBetC(BetCards)
        if Cards_Get == '2':
            Zrib= 1.75
            if len(yellow)+len(red) <= 2:
                print('YOU WON!')
                WinBetC(1.75,BetCards)
            else:
                print('YOU LOST!')    
                LooseBetC(BetCards)
        if Cards_Get == '3':
            Zrib= 2.05
            if len(yellow)+len(red) > 3:
                print('YOU WON!')
                WinBetC(2.05,BetCards)
            else:
                print('YOU LOST!')    
                LooseBetC(BetCards)
        if Cards_Get == '4':
            Zrib= 1.3
            if len(yellow)+len(red) <= 3:
                print('YOU WON!')
                WinBetC(1.3,BetCards)
            else:
                print('YOU LOST!')    
                LooseBetC(BetCards)
    else:
        pass
    ###
    print('')
    ###
    if Goal_Number_Bet == '1' or Goal_Number_Bet == '2' or Goal_Number_Bet == '3' or Goal_Number_Bet == '4' or Goal_Number_Bet == '5' or Goal_Number_Bet == '6': 
        #global Bet_Type, Bet,UsrChs
        UsrChs= Goal_Number_Bet       
        Bet_Type= 'Goals'
        Bet= BetGoal       
        MGs= goalcount1+goalcount2
        print('NUMBER OF GOALS: '+str(goalcount1+goalcount2))
        #WinBetC(team1Zrb,BetRes)
        #LooseBetC(BetGoal)
        if Goal_Number_Bet == '1':
            Zrib= 1.4
            if MGs >= 3:
                print('YOU WON!')
                WinBetC(1.40,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
        if Goal_Number_Bet == '2':
            Zrib= 2.05
            if MGs < 3:
                print('YOU WON!')
                WinBetC(2.05,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
        if Goal_Number_Bet == '3':
            Zrib= 1.75
            if MGs >= 4:
                print('YOU WON!')
                WinBetC(1.75,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
        if Goal_Number_Bet == '4':
            Zrib= 1.6
            if MGs < 4:
                print('YOU WON!')
                WinBetC(1.60,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
        if Goal_Number_Bet == '5':
            Zrib= 2.6
            if MGs >= 5:
                print('YOU WON!')
                WinBetC(2.60,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
        if Goal_Number_Bet == '6':
            Zrib= 1.25
            if MGs < 5:
                print('YOU WON!')
                WinBetC(1.25,BetGoal)
            else:
                print('YOU LOST!')
                LooseBetC(BetGoal)
    else:
        pass

    add2lst()

def beautifulgoal():
    global scorers
    global goals
    goals += 1
    print('{0} Gets the ball takes it past 1!'.format(rea))
    print('2 Players!')
    print('3 Whole players!!')
    w= random.randint(1,3)
    if w == 1:
        print('AND {0} SCORES A BEAUTIFUL GOAL!'.format(rea))
        entry = (rea,j)
        scorers.append(entry)
    else:
        print('He misses upon all his hardwork')
    time.sleep(3.5)

def penalty():
    global scorers
    global rea
    organize(rea)
    print('{0} dashes into the penalty box'.format(rea))
    print('But is roughly tackled by {0}'.format(defenders))
    r = random.randint(1,2)
    if r == 1:
        f= random.randint(1,5)
        PS=['Oh, The referee says it\'s penalty','The referee point to the spot']
        print(random.choice(PS))
        if f <= 3:
            PG= ['AND {0} SMASHES IT INTO THE NET'.format(rea), 'IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.']
            print(random.choice(PG))
            entry = (rea,j)
            scorers.append(entry)
        else:
            print('The keeper saves it! \nIt was briliant save from {0}'.format(GK))
    else:
        print('The refree waves it off!!')
    time.sleep(3.5)



def freekick():
    global scorers
    i = random.randint(1,7)
    #print('{0} is tackled very close to the box'.format(rea))
    print('It\'s a free kick!')
    if i >= 3:
        FL= ['The ball is out and it\'s a goal kick', '{0} Misses!'.format(rea)]
        print(random.choice(FL))
    else:
        FG= ['AND {0} SMASHES IT INTO THE NET'.format(rea), 'IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT. {0} MAKES THE GAME REALY GOOD.'.format(rea), 'GOAL!!! {0}'.format(rea)]
        print(random.choice(FG))       
        entry = (rea,j)
        scorers.append(entry)
    time.sleep(3.5)
    
    i = random.randint(1,2)
    #w = random.randint(1,2)

def header():
    global scorers
    global w
    rea = random.choice(team[1:3])
    print('{0} gets his head on a cross by {1}'.format(rea,midfielders))
    time.sleep(1.25)
    f= random.randint(1,3)
    if f >= 2:
        HL= ['But it sails over the post!', 'It hits the bar!', '{0} saves it.'.format(GK), 'It was not enough for goal.']
        print(random.choice(HL))
    else:
        HG= ['AND {0} SMASHES IT INTO THE NET', 'IT\'S A GOAL, {0}', 'HE HAS DONE IT. AND {0} MAKES THE GAME ON.', 'GOAL!!!, {0}']
        print(random.choice(HG).format(rea))          
        entry = (rea,j)
        scorers.append(entry)
    time.sleep(3.5)

def longshot():
    global scorers
    rn = random.randint(1,9)
    rea = random.choice(team[1:6])
    print('{0} fancies his luck from far!!!'.format(rea))
    if rn == 1 or rn == 2:
        LG= ['WHAT A HIT, {0}', 'HE HAS DONE IT. {0} FINISHED IT BEAUTIFULLY', 'WHAT A SHOT!!!  WHAT  A  SHOT  BY  {0}']
        print(random.choice(LG).format(rea))
        print('GOAL!!!') 
        entry = (rea,j)
        scorers.append(entry)
    else:
        LL= ['That was nowhere near the post!!!', 'What a horrible shot by {0}!!!'.format(rea), 'Great save, Real plus!', 'Ooooh so close but it hits the bar!!!']
        print(random.choice(LL))
        #print('What a horrible shot by {0}!!!'.format(rea))
        #print()
    time.sleep(3.5)
#referee events
def card(player):
    global yellow, red, defend, rea
    card = random.randint(1,7)
    if 4 <= card <= 6:
            print('The refree gives a hard talk to {0}'.format(player))
    if 1 <= card <= 3:
        if player in yellow:
            print('It\'s his second yellow card.')
            print('IT\'S A RED CARD FOR {0}'.format(player))
            print("He's Off!!!")
            red.append(player)
            t = find_team(player)
            t.remove(player)
        else:
            print('IT\'S A YELLOW CARD FOR {0}!!!'.format(player))
            yellow.append(player)
            if player == defend:
                freekick()
            else:
                pass

    if card == 7 and player not in yellow:
        print('OH, IT\'S STRAIGHT RED!!!')
        red.append(player)
        t = find_team(player)
        t.remove(player)
    if card == 7 and player in yellow:
        print('It\'s his second yellow card.')
        print('IT\'S A RED CARD FOR {0}'.format(player))
        print("He's Off!!!")
        red.append(player)
        t = find_team(player)
        t.remove(player)
    time.sleep(3.5)

def booking():
    global yellow, red, defend
    #yellow = []
    #red = []
    rea = random.choice(team[1:6])
    organize(rea)
    defend = defenders
    rn = random.randint(1,3)
    wound = random.randint(1,10)
    if rn == 1:
        print('{0} tries to get past {1} with a few cheeky skills!!!'.format(rea, defend))
        print('But {0} delivers a hard takle!!!'.format(defend))
        card(defend)
    if rn == 2:
        print('{0} and {1} are in a tight struggle for the ball!!!'.format(rea, defend))
        print('{0} ends up pushing {1} down!!!'.format(defend, rea))
        card(defend)   
    if rn == 3:
        print('{0} goes down easily from a challenge'.format(rea))
        print('The refree says its a dive!!!')
        card(rea)
    if wound == 7 and rn != 3:
        injury(rea)
    time.sleep(3.5)

def injury(player):
    rn = random.randint(1,2)
    if rn == 1:
       print('{0} has suffered a nasty injury!!!'.format(player)) 
       print('And has to be taken off!!!')
       print('The fans cheer as he walks of the pitch!!!')  
       t = find_team(player)
       t.remove(player)
    if rn == 2:
       print('{0} as reveived a slight injury!!!'.format(player))
       print('He has been taken off for treatment at the sidelines')
    time.sleep(3.5)

def volley_curler():
    global scorers
    rea = random.choice(team[1:3])
    midfielder = random.choice(team[4:6])
    rn = random.randint(1,2)
    g = random.randint(1,7)
    if rn == 1:
        print('{0} tries a shot, but the ball gets deflected!!!'.format(rea))
        print('{0} volleys it back into the box with a thump!!!'.format(midfielder))
        if g == 1 or g == 2:
            print('FLIES INTO THE NET!!!')
            VG= ['IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.', 'GOAL!!!']
            print(random.choice(VG))
            entry = (rea,j)
            scorers.append(entry)
        else:
            print('Off target!!!')
    if rn == 2:
        print('{0} dribbles with the ball at the side of the box!!!'.format(rea))
        print('Goes for a curling effort!!!')
        if g == 1 or g == 2:
            VG= ['WHAT AN AMAZING GOAL FROM {0} !!!','THAT\'S FANTASTIC, {0}','AND THAT IS SPECIAL, {0}']
            print(random.choice(VG).format(rea))            
            entry = (rea,j)
            scorers.append(entry)
        else:
            VL= ['No, It\'s out.','What a horrible shot!!','The ball is out and it\'s a goal kick','{0} Saves it'.format(GK)]
            print(random.choice(VL))
    time.sleep(3.5)

def opposite(player):
    if player in team1:
        return team2
    if player in team2:
        return team1
            
def counter_attack():
    global scorers
    g = random.randint(1,2)
    te = find_team(rea)
    te2 = opposite(rea)
    print('{0} failed attack has left {1} on the charge!!!'.format(te2[0],te[0]))
    print('{0} leads the charge!!!'.format(rea))
    print('{0} dribbles past the opposing defenders!!!'.format(rea))
    print('And he goes for goal!!!')
    if g == 1:
        print('WONDERFUL GOAL BY {0}!!!'.format(rea))
        entry = (rea,j)
        scorers.append(entry)
    else:
        print('Wasted Effort!!!')
    time.sleep(3.5)
    
def Corner():
    rea = random.choice(team[1:3])
    midfielder = random.choice(team[4:6])
    print('It\'s a corner')
    CCC= ['{0} delivers a curling cross','{0} delivers a beautiful cross', '{0} Crosses']
    print(random.choice(CCC).format(midfielder))
    print('{0} Shots'.format(rea))
    CG= random.randint(1,4)
    if CG == 1:
        GR= ['GOAL!!! {0}','IT\'S A GOAL! {0}','WHAT A HEADER BY {0}']
        print(random.choice(GR).format(rea))
        entry = (rea,j) 
        scorers.append(entry)            
    else:
        OR= ['The keeper saves it','And it\'s a goal kick','No, It\'s out', 'What a save from {0}'.format(GK)]
        print(random.choice(OR))
    #entry = (rea,j) 
    #scorers.append(entry)


j = 1
def min(j):
    print('{0} MINUTES'.format(j))
def display(func1, func2):
    print('')
def events():
    global j
    while j <= 90:
        e = random.randint(1,100)
        if j == 1:
            print('\n\n')
            print(j,'MINUTE\nKICK OFF!!!\n')
            time.sleep(1)
            j += 1
        if j == 45:
            print('\n',j,'MINUTES\nHALF TIME!!!\n\n')
            time.sleep(15)
            j += 1
           
        if j > 90:
            print(j,'MINUTES\nFULL TIME!!!\n\n\n')
            j += 1
        if e in range(1,2):
            display(min(j), header())
            j += 1
        elif e == 99:
            display(min(j), beautifulgoal())
            j += 1
        elif e == 94:
            display(min(j), penalty())
            j += 1
        elif e in range(80,83):
            display(min(j), longshot())
            j += 1
            j += 1
        elif e in range(75,78):
            display(min(j), volley_curler())
            j += 1
        elif e in range(45,46):
            display(min(j), freekick())
            j += 1
        elif e == 38:
            display(min(j), counter_attack())
            j += 1            
        elif e in range(29,31):
            display(min(j), Corner())
            j += 1         
        elif e in range(20,23):
            display(min(j), booking())
            j += 1   
        else:
            j += 1
        randomness()






def Main():
    if checker == True and checker2 == True:
        import os
        os.system('cls')
        print(str('{0}  VS  {1}'.format(team1[0],team2[0])).upper())
        BetResF()

        lineup()      
        versus()
        randomness()
        events()
        scoresheet()
    if checker == False:
        print('PLEASE PICK FROM THE AVAILABLE TEAMS')
    if checker2 == False:
       print('Can Not Play A Team Against Itself!')
Main()
time.sleep(10)
