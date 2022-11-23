import time
import random
from Ac_Info import *
#global variables
#spanish teams
barcelona = ['Barcelona','LUIS SUAREZ','MESSI','DEMBELE','RAKITIC','SERGIO.B','A. INIESTA','SEMEDO','PIQUE','ALBA','MASCHERANO','TER STEGEN']
madrid = ['Real Madrid','RONALDO', 'BALE','BENZEMA','KROOS','MODRIC','ISCO','CARVAJAL','SERGIO RAMOS','MARCELO','CASEMIRO','KEYLOR NAVAS']
valencia = ['Valencia','GEOFFREY KONDOGBIA','RAFAEL','FERRAN TORRES','NEMANJA','PAREJO','ANDRREAS PERERIA','JOSE LUIS','MARTIN','EZEQUEIL GARAY','JAVIER JIMENEZ','GABRIEL PAULISTA']
atmadrid = ['Atletico Madrid','FERNANDO TORRES','KEVIN GAMEIRO','ANTOINE GRIEZMAN','SAUL','KOKE','GABI','JUANFRAN','STEFAN SAVIC','DIEGO GODIN','FILIPE LUIS','JAN OBLAK']
sevilla = ['Sevilla','STEVAN JOVETIC','POZO','LUCIANO VIETTO','SAMIR NASRI','PABLO SARABIA','FRANCO VASQUEZ','GABRIEL MERCADO','NICOLAS PAREJA','ADIL RAMI','BENOIT TREMOULINAS','SERGIO RICO']
#english teams
manc = ['Manchester City','KUN AGUERO','GABRIEL JESUS','RAHEEM STERLING','DAVID SILVA','KEVIN DE BRUYNE','FERNANDINHO','BENJAMIN MENDY','NICOLAS OTAMENDI','JOHN STONES','KYLE WALKER','CLAUDIO BRAVO']
manu = ['Manchester United','ZLATAN IBRAHIMOVIC','ROMELU LUKAKU','ANTHONY MARTIAL','MATA','NEMANJA MATIC','PAUL POGBA','ERIC BAILLY','CHRIS SMALLING','ANTINIO VALENCIA','ASHLEY YOUNG','DE GEA']
chelsea = ['Chelsea','EDEN HAZARD','MORATA','WILLIAN','CESC FABREGAS',"N'GOLO KANTE",'MARCOS ALONSO','AZPILICUETA','DAVID LUIZ','ANTONIO RUDIGER','DAVIDE ZAPPACOSTA','THIBAUT COURTOIS']
tottenham = ['Tottenham','HARRY KANE','HEUNG-MIN SON','DELE ALLI','MOUSA DEMBELE','ERIC DIER','CHRISTIAN ERIKSON','TOBY ALDERWEIRALD','DANNY ROSE','KIERAN TRIPPIER','KYLE WALKER','HUGO LLORIS']
liverpool = ['Liverpool','SADIO MANE','ROBERTO FIRMINO','DANIEL STURRIDGE','COUTINHO','MOHAMED SALAH','GEORGINIO WIJNALDUM','ALBERTO MORENO','NATHANIEL CLYNE','JOEL MATIP','JAMES MILNER','SIMON MIGNOLET']
arsenal= ['Arsenal','LACAZZETE','AUBAMEYANG','PEPE','TORIERRA','OZIL','XHAKA','BELLERIN','LUIS','KOLASINAC','MUSTAFI','LENO']
#italian teams
napoli = ['Napoli','LORENZO INSIGNE','JOSE CALLEJON','LEONARDO PAVOLETTI','ALLAN','MAREK HAMSIK','JORGINHO','VLAD CHIRICHES','KALIDOU KOULIBALY','CHRISTIAN MAGGIO','RAUL ALBIOL','PEPE REINA']
juventus = ['Juventus','PAULO DYBALA','GONZALO HIGUAIN','MARIO  MANDZUKIC','KWADWO ASAMOAH','JUAN CAUDRADO','SAMI KHEDIRA','MEDHI BENATIA','LEONARDO BONUCCI','GIORGIO CHIELLINI','DANI ALVES','GIANlUIGI BUFFON']
inter = ['Inter Milan','MOHAMED BAKAYOKO','EDER','GABRIEL BARBOSA','MARCELO BROZOVIC','ANTONIO CANDREVA','GARY MEDEL','MARCO ANDREOLLI','CRISTIAN ANSALDI',"DANILO D'AMBROSIA",'MIRANDA','SAMIR HANDANOVIC']
roma = ['AS Roma','EDIN DZEKO','STEPHAN EL SHAARAWAY','FRANCESCO TOTTI','DANIELE DE ROSSI','ALESSANDRO FLORENZI','LORENZO GROSSI','BRUNO PERES','EROS DE SANTIS','EMERSON','FEDERICO FAZIO','WOJCIECH SZCZESNY']
lazio = ['Lazio','FELIPE CAICEDO','CIRO IMMOBILE','NAANI','DAVIDE DI GENNARO','FELIPE ANDERSON','NICOLO ARMINI','DUSAN BASTA','BASTOS','JORDAN LUKAKU','MAURICIO','THOMAS STRAKOSHA']
####
####
TeamPowers= {'Liverpool':         99, 
             'Barcelona':         96, 
             'Real Madrid':       96, 
             'Juventus':          92, 
             'Manchester City':   86, 
             'Atletico Madrid':   84, 
             'Inter Milan':       82, 
             'Chelsea':           79, 
             'Arsenal':           79, 
             'AS Roma':           79, 
             'Manchester United': 79, 
             'Tottenham':         79, 
             'Sevilla':           74, 
             'Napoli':            74, 
             'Valencia':          69, 
             'Lazio':             75, 
            }
Cards_Get= 0
ResultGm= 0
team1 = chelsea
team2 = manu
goals = 0
scorers = []
yellow = []
red = []
#randoms
def select_team():
    global team1, team2, checker, checker2
    checker2 = True
    checker = None

    teams = {'BARCELONA':barcelona,'REAL MADRID':madrid,'VALENCIA':valencia,'ATLETICO MADRID':atmadrid,'SEVILLA':sevilla,'MANCHESTER CITY':manc,'MANCHESTER UNITED':manu,'CHELSEA':chelsea,'TOTTENHAM':tottenham,'LIVERPOOL':liverpool,'ARSENAL':arsenal,'NAPOLI':napoli,'JUVENTUS':juventus,'INTER MILAN':inter,'AS ROMA':roma,'LAZIO':lazio}
    teamL= ['Liverpool','Manchester City','Arsenal','Arsenal','Chelsea','Manchester United','Tottenham',
            'Real Madrid','Barcelona','Atletico Madrid','Valencia','Sevilla','Juventus','Inter Milan','AS Roma','Lazio',]
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

select_team()
def find_team(player):
    if player in team1:
        return team1
    else:
        return team2


def WinBetC(TeamNom,Bet):
    Income= Bet*TeamNom
    print('You Won ' + str(Bet*TeamNom))
    op_inf= open('.\\Ac_Info.py',mode='w')
    op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                'Credit= '         + str(Credit - Bet + Income)+
                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                '\nRmnnVluCshot= '  + str(RmnnVluCshot)
                )
    op_inf.close()    
def LooseBetC(Bet):
    print('You Lost ' + str(Bet))
def BetResF():
    global team1Zrb
    global team2Zrb
    TeamPowers= {'Liverpool':     99, 
             'Barcelona':         96, 
             'Real Madrid':       96, 
             'Juventus':          92, 
             'Manchester City':   86, 
             'Atletico Madrid':   83, 
             'Inter Milan':       82, 
             'Chelsea':           76, 
             'Arsenal':           76, 
             'AS Roma':           76, 
             'Manchester United': 76, 
             'Tottenham':         76, 
             'Sevilla':           70, 
             'Napoli':            70, 
             'Valencia':          66, 
             'Lazio':             66, 
            }
    if TeamPowers[team1[0]] > TeamPowers[team2[0]]:
        if TeamPowers[team1[0]] - TeamPowers[team2[0]] > 29:
            team1Zrb= 1.20
            DrawZrb=  1.95
            team2Zrb= 2.25    
        if 29 >= TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 21:
            team1Zrb= 1.25
            DrawZrb=  1.85
            team2Zrb= 2.05
        if 21 > TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 15:
            team1Zrb= 1.35
            DrawZrb=  1.80
            team2Zrb= 1.95
        if 15 > TeamPowers[team1[0]] - TeamPowers[team2[0]] >= 10:
            team1Zrb= 1.65
            DrawZrb=  1.60
            team2Zrb= 1.90
        if 10 > TeamPowers[team1[0]] - TeamPowers[team2[0]] > 5:
            team1Zrb= 1.80
            DrawZrb=  1.55
            team2Zrb= 1.95
        if 5 >= TeamPowers[team1[0]] - TeamPowers[team2[0]]:
            team1Zrb= 1.95
            DrawZrb=  1.45
            team2Zrb= 1.95        

    elif TeamPowers[team1[0]] < TeamPowers[team2[0]]:
        if TeamPowers[team2[0]] - TeamPowers[team2[0]] > 29:
            team1Zrb= 2.25
            DrawZrb=  1.95
            team2Zrb= 1.20    
        if 29 >= TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 21:
            team1Zrb= 2.05
            DrawZrb=  1.85
            team2Zrb= 1.25
        if 21 > TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 15:
            team1Zrb= 1.95
            DrawZrb=  1.70
            team2Zrb= 1.35
        if 15 > TeamPowers[team2[0]] - TeamPowers[team1[0]] >= 10:
            team1Zrb= 1.90
            DrawZrb=  1.60
            team2Zrb= 1.65
        if 10 > TeamPowers[team2[0]] - TeamPowers[team1[0]] > 5:
            team1Zrb= 1.95
            DrawZrb=  1.50
            team2Zrb= 1.80
        if 5 >= TeamPowers[team2[0]] - TeamPowers[team1[0]]:
            team1Zrb= 1.95
            DrawZrb=  1.45
            team2Zrb= 1.95  

    elif TeamPowers[team1[0]] == TeamPowers[team2[0]]:
        team1Zrb= 1.75
        DrawZrb=  1.35
        team2Zrb= 1.75
    print(team1[0]+':\t\t\t\t'+str(team1Zrb))
    print('Draw:\t\t\t\t\t'+str(DrawZrb))
    print(team2[0]+':\t\t\t\t'+str(team2Zrb))


    from Ac_Info import Credit
    global ResultGm
    ResultGm= input('Result:   1-'+team1[0]+'  2-Draw  3-'+team2[0]+'           ')
    global BetRes 
    BetRes=0
    if ResultGm == '1' or ResultGm == '2' or ResultGm == '3':
        print('Your credit is:' + str(Credit))
        BetRes= input('Type your bet: ')
        try:
            BetRes = int(BetRes)
            if BetRes > Credit:
                print('You don\'t have enough credit.')
                BetResF()
            else:
                #Start the game
                if BetRes == 0:
                    print('It\'s not enough for playing.')
                    BetResF()
                else:
                    op_inf= open('.\\Ac_Info.py',mode='w')
                    op_inf.write('Nickname= \''    + Nickname + '\'\n'+
                                'Credit= '         + str(Credit - BetRes)+
                                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses+1) +
                                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                                '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                                '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                                '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                                '\nRmnnVluCshot= '  + str(RmnnVluCshot - BetRes)
                                )
                    op_inf.close()
        except ValueError:
            print('Invalid Number')
            BetResF()
    else:
        BetCardsF()

def BetCardsF():
    global Cards_Get
    print('Your credit is:' + str(Credit-BetRes))
    Cards_Get= input('Number of Cards:    1-More than 2.5      2-Less than 2.5          ')
    if Cards_Get == '1' or Cards_Get == '2': 
        global BetCards   
        BetCards= input('Type your bet: ')
        try:
            BetCards = int(BetCards)
            if BetCards > Credit-BetRes:
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
                                'Credit= '         + str(Credit - BetRes - BetCards)+
                                '\nCrash_Wins= '   + str(Crash_Wins) + '\nCrash_Loses= ' + str(Crash_Loses) +
                                '\nBJ_Wins= '      + str(BJ_Wins)    + '\nBJ_Loses= '    + str(BJ_Loses)      +
                                '\nRPS_Wins= '     + str(RPS_Wins)   + '\nRPS_Loses= '   + str(RPS_Loses)     +
                                '\nRatioX_Wins= '  + str(RatioX_Wins)    + '\nRatioX_Loses= '+ str(RatioX_Loses)  +
                                '\nDR_Wins= '  + str(DR_Wins)    + '\nDR_Loses= '+ str(DR_Loses) +
                                '\nRmnnVluCshot= '  + str(RmnnVluCshot - BetRes - BetCards)
                                )
                    op_inf.close()
        except ValueError:
            print('Invalid Number')
            BetCardsF()


def randomness():
    global team, w, teams,strikers, midfielders, re, rea
    w = random.randint(1,2)
    teams = (team1, team2)

    PwrT= TeamPowers[team1[0]] + TeamPowers[team2[0]]
    LmtTm= random.randint(0,PwrT)
    if LmtTm <= TeamPowers[team1[0]]:
        team= team1
    else:
        team= team2
    
    #team = random.choice(teams)
    strikers = random.choice(team[1:3])
    midfielders =random.choice(team[4:6])
    re = [strikers, midfielders]
    rea = random.choice(re)


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

def beautifulgoal():
    global scorers
    global goals
    goals += 1
    print('{0} gets the ball takes it past 1!'.format(rea))
    print('2 PLAYERS!')
    print('3 WHOLE PLAYERS!!')
    if w == 1:
        print('And {0} scores a beautiful goal!'.format(rea))
        entry = (rea,j)
        scorers.append(entry)
    else:
        print('He misses upon all his hardwork')
    time.sleep(3.5)

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
        print("{0} \t '{1}'".format(i,str(minutes[c])))
        c += 1

    print('')
    print('CARDS: ')
    try:
        global yellow
        print('YELLOW Cards: ')
        for item in yellow:
            print(item)
    except NameError:
        print('NO YELLOW CARDS.')
    print('')
    try:
        global red
        print('Red Cards: ')
        for item in red:
            print(item)
    except NameError:
        print('NO RED CARDS.')


    global ResultGm
    global team1Zrb
    global team2Zrb
    print('\n\n\n')
    print('BET:\n\n')
    if ResultGm == '1' or ResultGm == '2' or ResultGm == '3':
        print('GAME RESULT: ')
        if ResultGm == '1':
            if goalcount1>goalcount2:
                print('YOU WON!')
                WinBetC(team1Zrb,BetRes)
            else:
                print('YOU LOST!')
                LooseBetC(BetRes)
        if ResultGm == '2':
            if goalcount1==goalcount2:
                print('YOU WON!')
                WinBetC(team1Zrb,BetRes)
            else:
                print('YOU LOST!')
                LooseBetC(BetRes)
        if ResultGm == '3':
            if goalcount1<goalcount2:
                print('YOU WON!')
                WinBetC(team1Zrb,BetRes)
            else:
                print('YOU LOST!')
                LooseBetC(BetRes)
        print('\n')
    else:
        pass
    ####
    #global yellow
    #global red
    print('')
    if Cards_Get == '1' or Cards_Get == '2':
        print('NUMBER OF CARDS: ' + str(len(yellow)+len(red)))
        if Cards_Get == '1':
            if len(yellow)+len(red) > 2:
                print('YOU WON!')
                WinBetC(2,BetCards)
            else:
                print('YOU LOST!')
                LooseBetC(BetCards)
        if Cards_Get == '2':
            if len(yellow)+len(red) <= 2:
                print('YOU WON!')
                WinBetC(2,BetCards)
            else:
                print('YOU LOST!')    
                LooseBetC(BetCards)
    else:
        pass

def penalty():
    global scorers
    global rea
    organize(rea)
    print('{0} dashes into the penalty box'.format(rea))
    print('But is roughly tackled by {0}'.format(defenders))
    r = random.randint(1,2)
    if r == 1:
        f= random.randint(1,4)
        PS=['Oh, The referee says it\'s penalty','The referee point to the spot']
        print(random.choice(PS))
        if f <= 3:
            PG= ['AND {0} SMASHES IT INTO THE NET'.format(rea), 'IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.']
            print(random.choice(PG))
            entry = (rea,j)
            scorers.append(entry)
        else:
            print('The keeper saves it!')
    else:
        print('The refree waves it off!!')
    time.sleep(3.5)



def freekick():
    global scorers
    i = random.randint(1,3)
    #print('{0} is tackled very close to the box'.format(rea))
    print('It\'s a free kick!')
    if i >= 2:
        FL= ['The ball is out and it\'s a goal kick', '{0} Misses!'.format(rea)]
        print(random.choice(FL))
    else:
        FG= ['AND {0} SMASHES IT INTO THE NET'.format(rea), 'IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.', 'GOAL!!!']
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
        HL= ['But it sails over the post!', 'It hits the bar!', 'The keeper saves it.', 'It was not enough for goal.']
        print(random.choice(HL))
    else:
        HG= ['AND {0} SMASHES IT INTO THE NET'.format(rea), 'IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.', 'GOAL!!!']
        print(random.choice(HG))          
        entry = (rea,j)
        scorers.append(entry)
    time.sleep(3.5)

def longshot():
    global scorers
    rn = random.randint(1,4)
    rea = random.choice(team[1:6])
    print('{0} fancies his luck from far!!!'.format(rea))
    if rn == 1:
        LG= ['WHAT A HIT, {0}'.format(rea), 'HE HAS DONE IT.', 'WHAT A SHOT!!!']
        print(random.choice(LG))
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
    card = random.randint(1,6)
    if 4 <= card <= 5:
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
            freekick()

    if card == 6 and player not in yellow:
        print('OH, IT\'S STRAIGHT RED!!!')
        red.append(player)
        t = find_team(player)
        t.remove(player)
    if card == 6 and player in yellow:
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
    g = random.randint(1,3)
    if rn == 1:
        print('{0} tries a shot, but the ball gets deflected!!!'.format(rea))
        print('{0} volleys it back into the box with a thump!!!'.format(midfielder))
        if g == 1:
            print('FLIES INTO THE NET!!!')
            VG= ['IT\'S A GOAL, {0}'.format(rea), 'HE HAS DONE IT.', 'GOAL!!!']
            print(random.choice(VG))
            entry = (rea,j)
            scorers.append(entry)
        else:
            print('OFF TARGET!!!')
    if rn == 2:
        print('{0} dribbles with the ball at the side of the box!!!'.format(rea))
        print('Goes for a curling effort!!!')
        if g == 1:
            VG= ['WHAT AN AMAZING GOAL!!!!!','THAT\'S FANTASTIC','AND THAT IS SPECIAL, {0}']
            print(random.choice(VG))            
            entry = (rea,j)
            scorers.append(entry)
        else:
            VL= ['No, It\'s out.','What a horrible shot!!','The ball is out and it\'s a goal kick']
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
        print('WONDERFUL GOAL!!!')
        entry = (rea,j)
        scorers.append(entry)
    else:
        print('Wasted Effort!!!')
    time.sleep(3.5)
    

    
 

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
            j += 1
        if j == 45:
            print(j,'MINUTES\nHALF TIME!!!\n')
            time.sleep(7)
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
        elif e in range(45,47):
            display(min(j), freekick())
            j += 1
        elif e in range(20,23):
            display(min(j), booking())
            j += 1
        elif e in range(80,83):
            display(min(j), longshot())
            j += 1
        elif e in range(75,78):
            display(min(j), volley_curler())
            j += 1
        elif e == 38:
            display(min(j), counter_attack())
            j += 1
            
        else:
            j += 1
        randomness()
def main():
    if checker == True and checker2 == True:
        ####
        BetResF()
        
        ####
        lineup()      
        versus()
        randomness()
        events()
        scoresheet()
    if checker == False:
        print("""
PLEASE PICK FROM THE AVAILABLE TEAMS WHICH ARE:
BARCELONA
MADRID
SEVILLA
ATLETICO MADRID
VALENCIA
MANCHESTER CITY
MANCHESTER UNITED
CHELSEA
TOTTENHAM
LIVERPOOL
"""  )
    if checker2 == False:
       print('Can Not Play A Team Against Itself!!!')
main()
time.sleep(10)
