from GM_Info import Nickname
from GM_Info import Credit
from GM_Info import Crash_Wins
from GM_Info import Crash_Loses
from GM_Info import BJ_Wins
from GM_Info import BJ_Loses
from GM_Info import RPS_Wins
from GM_Info import RPS_Loses

#Main
def UserChoiceF():

    def BotChoiceF():
        def AdWin():
            op_inf= open('.\\GM_Info.py',mode='w')
            op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                         'Credit= '         + str(Credit + Bet) +
                         '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                         '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                         '\nRPS_Wins= '      + str(RPS_Wins+1)        + '\nRPS_Loses= '    + str(RPS_Loses) #+ 
                         )
            op_inf.close()
        def AdLose():
            op_inf= open('.\\GM_Info.py',mode='w')
            op_inf.write('Nickname= \''    + Nickname + '\'\n'   +
                         'Credit= '         + str(Credit - Bet) +
                         '\nCrash_Wins= '   + str(Crash_Wins)   + '\nCrash_Loses= ' + str(Crash_Loses) +
                         '\nBJ_Wins= '      + str(BJ_Wins)        + '\nBJ_Loses= '    + str(BJ_Loses)    +
                         '\nRPS_Wins= '      + str(RPS_Wins)        + '\nRPS_Loses= '    + str(RPS_Loses+1) #+ 
                         )
            op_inf.close()


        SampleSpace= ['r','p','s']
        import random
        BotChoice= random.choice(SampleSpace)
        
        #Calculation
        if UserChoice == BotChoice:
            print('Draw!')
        else:
            if UserChoice == 'r' and BotChoice == 'p':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'r' and BotChoice == 's':    
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 'p' and BotChoice == 's':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 'p' and BotChoice == 'r':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            if UserChoice == 's' and BotChoice == 'r':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You lost!')
                #Result= 'Lost'
                AdLose()

            if UserChoice == 's' and BotChoice == 'p':
                print('Your Choice is '+UserChoice  +  '\nBot Choice is '+BotChoice)
                print('You Won!')
                #Result= 'Win'
                AdWin()

            print('Please wait a momment...')
            import time
            time.sleep(2)

    UserChoice= input('Rock, Paper or Scissor? (R/P/S)   ')
    if UserChoice.lower() == 'r' or UserChoice.lower() == 'p' or UserChoice.lower() == 's':
        BotChoiceF()
    else:
        print('Wrong choice.')
        UserChoiceF()



Bet=0
#Choose bet value
def BetC():
    global Bet
    print('Your credit is:' + str(Credit))
    Bet= input('Type your bet: ')
    try:
        Bet= int(Bet)
        #Start the game
        UserChoiceF()
    except ValueError:
        print('Invalid Nimber')
        BetC()
    
BetC()




