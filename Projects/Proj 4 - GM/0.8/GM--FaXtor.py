import random
import time
import os


Bet= int(input('Type your bet: '))
os.system('cls')
NOMS=[]
for i in range(0,10):
    nom= round(random.uniform(1.01,99.99),2)
    NOMS.append(nom)
#print(NOMS)

Lst=['-.--', '-.--', '-.--', '-.--', '-.--', '-.--', '-.--', '-.--', '-.--', '-.--', ]
x=0

def Cont():
    print('You won ' + str(Bet*NOMS[-1]))

def MN():
    global x
    for nom in NOMS:
        Lst.remove(Lst[x])
        for zz in range(1,30):
            a= round(random.uniform(1.01,99.99),2)
            Lst.insert(x,a)
            print('''BET: {0}
PLAYING: '''.format(Bet) + str(Lst))
            time.sleep(0.05)
            Lst.remove(Lst[x])
            os.system('cls')

        Lst.insert(x,nom)
        print('''BET: {0}
PLAYING: '''.format(Bet) + str(Lst))
        time.sleep(0.6)
        x+=1
        if nom != NOMS[9]:
            os.system('cls')
        #elif x==9:
        #    Cont()            
        #else:
        #    MN()
        #if x==10:
            
    Cont()
MN()    






time.sleep(5)
