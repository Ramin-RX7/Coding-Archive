import random
import time

NoC=0
Cards= ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']



Y=0
B=0
S=0
C=0
P=0
BY=0
BD=0
BS=0
BC=0
BP=0

def Give_To_Bot():
    def Calculate():
        JoC= Y+D+S+C+P
        #Bot_JoC= BY+BD+BS+BC+BP
        if JoC != Bot_JoC:
            if JoC < 21 and Bot_JoC < 21:
                if JoC > Bot_JoC:
                    print('You won!')
                if JoC < Bot_JoC:
                    print('You lost!')
                if JoC == Bot_JoC:
                    print('You won!')

            if JoC > 21 and Bot_JoC > 21:
                if JoC > Bot_JoC:
                    print('You lost!')
                if JoC < Bot_JoC:
                    print('You won!')            

            if JoC > 21 and Bot_JoC < 21:
                print('You lost!')
            if JoC < 21 and Bot_JoC > 21:
                print('You won!')
            if JoC == 21:
                print('You won!')
        if JoC == Bot_JoC:
            print('You won!')
        print('Your total is: ' + str(JoC))
        print('Bot total is: '  + str(Bot_JoC))
        import time
        time.sleep(15)
        quit()
    BY=0
    BD=0
    BS=0
    BC=0
    BP=0
    global Bot_JoC
    Bot_JoC= 0
    Bot_Given_Card= random.choice(Cards)
    if Bot_Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Bot_Given_Card= 10
        Bot_JoC = Bot_Given_Card
    elif Bot_Given_Card == 'A':
        Bot_Given_Card= 11
        Bot_JoC = Bot_Given_Card
    elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
        BY= Bot_Given_Card
        Bot_JoC = Bot_Given_Card
    print('1st card is: '+ str(BY))
    if BY <= 15:
        Bot_Given_Card= random.choice(Cards)
        #BD=0
        if Bot_Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
            Bot_Given_Card= 10
            BD = Bot_Given_Card
            Bot_JoC += BD
        elif Bot_Given_Card == 'A':
            Bot_Given_Card= 11
            BD = Bot_Given_Card
            Bot_JoC += BD
        elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
            BD = Bot_Given_Card
            Bot_JoC += BD    
        print('2nd card is: ' + str(BD))
        if BY+BD <=15:
            Bot_Given_Card= random.choice(Cards)
            #BS=0
            if Bot_Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
                Bot_Given_Card= 10
                BS = Bot_Given_Card
                Bot_JoC += BS
            elif Bot_Given_Card == 'A':
                Bot_Given_Card= 11
                BS = Bot_Given_Card
                Bot_JoC += BS
            elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                BS = Bot_Given_Card
                Bot_JoC += BS

            print('3rd card is ' + str(BS))
            if BY+BD+BS <=15:
                Bot_Given_Card= random.choice(Cards)
                #BC=0
                if Bot_Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
                    Bot_Given_Card= 10
                    BC = Bot_Given_Card
                    Bot_JoC += BC
                elif Bot_Given_Card == 'A':
                    Bot_Given_Card= 11
                    BC = Bot_Given_Card
                    Bot_JoC += BC
                elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                    BC = Bot_Given_Card
                    Bot_JoC += BC
                print('4th card is '+str(BC))
                if BY+BD+BS+BC <=15:
                    Bot_Given_Card= random.choice(Cards)
                    #BP=0
                    if Bot_Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
                        Bot_Given_Card= 10
                        BP = Bot_Given_Card
                        Bot_JoC += BP
                    elif Bot_Given_Card == 'A':
                        Bot_Given_Card= 11
                        BP = Bot_Given_Card
                        Bot_JoC += BP
                    elif Bot_Given_Card == 1 or Bot_Given_Card == 2 or Bot_Given_Card == 3 or Bot_Given_Card == 4 or Bot_Given_Card == 5 or Bot_Given_Card == 6 or Bot_Given_Card == 7 or Bot_Given_Card == 8 or Bot_Given_Card == 9 or Bot_Given_Card == 10:
                        BP = Bot_Given_Card
                        Bot_JoC += BD
                    print('5th card is '+str(BP))
                    #Bot_JoC= BY+BD+BS+BC+BP
                    Calculate()
                if BY+BD+BS+BC>15:
                    Bot_JoC= BY+BD+BS+BC
                    Calculate()

            if BY+BD+BS>15:
                Bot_JoC= BY+BD+BS
                Calculate()

        if BY+BD>15:
            Bot_JoC= BY+BD
            Calculate()
            
    if BY>15:
        Bot_JoC= BY+BD
        Calculate()

    



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



JoC= 0
Given_Card= random.choice(Cards)
print('Here it is; Your first card  ' + str(Given_Card))
#NoC= NoC+1
if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
    Given_Card_Nom = 10
    Y= Given_Card_Nom
    print('Your card is:  ' + str(Given_Card))
    print('Total is: ' + str(Y))
    
elif Given_Card == 'A':
    Given_Card_Nom = 11
    Y= Given_Card_Nom
    print('Your card is:  ' + str(Given_Card))
    print('Total is: ' + str(Y))
else:
    Y= Given_Card
    print('Your card is:  ' + str(Given_Card))
    print('Total is: ' + str(Y))




GCardYN= input('Do you need more? (Y/N)')
if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
    #NoC= NoC+1
    Given_Card= random.choice(Cards)
    D=0
    if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Given_Card_Nom = 10
        D= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D))
        
    elif Given_Card == 'A':
        Given_Card_Nom = 11
        D= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D))
    else:
        D= Given_Card
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D))


else:
    Give_To_Bot()





GCardYN= input('Do you need more? (Y/N)')
if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
    #NoC= NoC+1
    Given_Card= random.choice(Cards)
    S=0
    if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Given_Card_Nom = 10
        S= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S))
        
    elif Given_Card == 'A':
        Given_Card_Nom = 11
        S= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S))
    else:
        S= Given_Card
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S))


else:
    Give_To_Bot()




GCardYN= input('Do you need more? (Y/N)')
if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
    #NoC= NoC+1
    Given_Card= random.choice(Cards)
    C=0
    if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Given_Card_Nom = 10
        C= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C))
        
    elif Given_Card == 'A':
        Given_Card_Nom = 11
        C= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C))
    else:
        C= Given_Card
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C))


else:
    Give_To_Bot()




GCardYN= input('Do you need more? (Y/N)')
if GCardYN.lower() == 'y' or GCardYN.lower() == 'yes':
    #NoC= NoC+1
    Given_Card= random.choice(Cards)
    P=0
    if Given_Card == 'K' or Given_Card == 'Q' or Given_Card == 'J':
        Given_Card_Nom = 10
        P= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C+P))
        
    elif Given_Card == 'A':
        Given_Card_Nom = 11
        P= Given_Card_Nom
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C+P))
    else:
        P= Given_Card
        print('Your card is:  ' + str(Given_Card))
        print('Total is: ' + str(Y+D+S+C+P))
        print('You reached the maximum number of cards.')
        print('Waiting for dealer turn...')
        time.sleep(2)

else:
    Give_To_Bot()
