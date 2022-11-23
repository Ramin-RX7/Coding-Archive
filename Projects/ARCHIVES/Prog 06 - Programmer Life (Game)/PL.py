from rx7 import read,wait,write,cls
from pyautogui import typewrite
import subprocess,os,random,sys

while True:
    opl=open('lool',mode='r')
    oplr=opl.read()
    WL=len(oplr)
    
    def LP():
        alfabet='qwert yuiop asdf ghjkl zxcvb nmQW ERTYU IOPAS DFGH JKLZX CVBNM'
        write('.\\lool','continue',random.choice(alfabet))

    #subprocess.Popen('cmd')
    #os.system('cls')

    if WL==0:
        def inp1():
            RYN=input('If You Are Ready, Type READY: ')
            if RYN.lower()=='ready':
                LP()
                print("Great! Let's go!")
                def sn():
                    nm=input('Type Your Name Then Press Enter:  ')
                    if len(nm)<3 or len(nm)>16:
                        print('Name Length should have between 3 to 16 characters.')
                        sn()
                    else:
                        print('Great.')
                        write(file='Name',text=nm)
                        wait(2)
                sn()
            else:
                inp1()
        cls()
        '''for char in LC:
            typewrite(char)
            wait(0.01)'''
        print(read('.\\Lools\\loq'))
        wait(10)
        inp1()

    if WL==1:
        print('\tLEVEL 1\n')
        def inp2():
            x=input('Try to encrypt it:  ')
            if x.lower()== '23z':
                print("Good Jub! You passed 1st level.")
                wait(2)
                LP()
            else:
                print('Not Good. Try again.')
                inp2()
        cls()
        print('''This is first level.
In some levels you most Ecnrypt or Decrypt a word or phrase that we gave you.
(Note: Memorising them will help you in next levels.)
                ''')
        print(read('.\\Lools\\dek'))
        wait(1.5)
        inp2()

    if WL==2:
        print('\tLEVEL 2\n')
        cls()
        print(read('.\\Lools\\no'))
        def inp3():
            x=input('Type the decrypted:  ')
            if x=='AtlasArmy':
                print("Very Good. Don't forget it.")
                wait(3)
                LP()
            else:
                print('Incorrect Input.')
        wait(2.5)
        inp3()

    if WL==3:
        print('\tSTORY SECTION\n')
        cls()
        print(read('.\\Lools\\HtrtNstn'))
        wait(0.12)
        print(read('.\\Lools\\HtrtNstn2'))        
        def inpStartStory():
            x=input('1-Yes \n2-No\n\nWhat do you choose?')
            if x=='1':
                ZZ= 'True'
                ChechGoNot(ZZ)
            elif x=='2':
                ZZ= 'False'
                ChechGoNot(ZZ)
            else:
                print('Type Number Only')
                inpStartStory()
        def ChechGoNot(XX):
            if XX=='True':
                print(read('.\\Lools\\HtrtT'))
                def KBN():
                    XX= input('What to do? \n1- Go for more relation \n2- Tell her for more \n3- Stop\n')
                    NVS= '''YOU START TOUCHING HER BACK.\nSHE WHINED.
YOU HELD YOUR HAND DOWN HER PANTS AND THEN YOU TOUCHED HER ASS...
                            '''
                    if XX=='1':
                        print(NVS)
                    if XX=='2':
                        print('-CAN WE GO FOR MORE?\n+YEAH.')
                        print(NVS)
                    if XX=='3':
                        print('''YOU STOPPED AND WENT BACKWARD BUT HER FACE SEEMS SHE WANTS SOMETHING.
YOU ASK: WHAT?\nSHE SAID: NOTHING\nBUT YOU UNDERSTOOD.\nYOU WENT CLOSER AGAIN.''')
                        print('AND'+NVS)
                        wait(0.15)
                    print('''\n\nYou both stopped.\nYou didn't finish it.It was first time and you weren't in good place.
Others were downstair and each momment they could came.\nIt was a big risk.
But you've done it for the first time in your life. 
''')
                KBN()
                wait(2)
                mm=input('''***Enter anything if you've finnished reading''')
                write('.\\Lools\\XmoN',text='x',mode='continue')
            elif XX=='False':
                print('You intercept that lust that night.')
                MM=input('''***Enter anything if you've finnished reading''')
            print('Good!')
            LP()
        inpStartStory()
        
    if WL==4:
        cls()
        print('MONTHLY REPORT\n')
        print('''30 June\nYour Income:    
1000  + (4*125) - 75  - 25  +  10  +  20 = 1430
U Had + Working - net - vpn + LVL1 + LVL2= Total
                 ''')
        write('.\\Lools\\ymon',text='1400')
        print('PC Storage:   300GB free from 512GB\nCPU: Core i3\nRam: 4GB ddr3')
        dsa=open('.\\Lools\\XmoN',mode='r')
        dwa=dsa.read()
        print('Number of Sex: {}'.format(len(dwa)))
        if len(dwa)!=0:
            print('(Finnaly you did what you were waiting for.)')        
        print('Skills:\n\tHacking Phones (from before)\n\tHacking PC (from before)\n\t+Hacking Simple web-site\n')
        MM=input('''***Press Enter if you've finnished reading''')
        LP()

    if WL==5:
        cls()
        print('Today you are going to play Coin flip with one of your friends.')
        def cf():
            bet=input('''***Type how much do you want to bet of your 1400 money:  ''')
            try:
                Bet=int(bet)
                if Bet>700:
                    print('''It shouldn't be more than 50% of your money''')
                    cf()
                elif Bet<100:
                    print('You need at least 100')
                    cf()
                else:
                    wol=random.choice(['w','l'])
                    if wol=='w':
                        print('You won.')
                        write('.\\Lools\\ymon',text=str(1500+Bet))
                    else:
                        print('You lost.')
                        write('.\\Lools\\ymon',text=str(1500-Bet))
                    wait(3)
                    LP()
            except ValueError:
                print('Only type numbers')
                cf()
        cf()

    if WL==6:
        print('\tSTORY SECTION\n')
        global HHP
        HHP=False
        cls()
        '''xn=open('.\\Lools\\XnoM', mode='r')
        xrd=xn.read()
        xln= len(xrd)'''
        print(read('.\\Lools\\hhp'))
        wait(17.5)
        if os.path.exists('.\\Lools\\XnoM')==True:
            print(read('.\\Lools\\hhpt'))
            wait(30)
        else:
            print(read('.\\Lools\\hhpf'))
            wait(5)
        print('''She look at the clock then she goes to bathroom.\nher phone is not locked!
it's one of the realy rare opportunities for you.\nso you decide to hack her phone.''')
        wait(7)
        def nvhk():
            def khkhp():
                for i in range(1,6):
                    def sssa(lstwrd,rang):
                        for i in range(rang):
                            wrdslctd=random.choice(lstwrd)
                            print(wrdslctd)
                            lstwrd.remove(wrdslctd)
                            wait(0.15)
                            print('Done.') 

                    if i==1:
                        print('Getting Permissions...')
                        wait(1.5)
                        wrdlst2=['Cameras Permission...','Contacts Permission...','Location Permission...']
                        sssa(wrdlst2,3)
                    if i==2:
                        print('Accessing to Files...')
                        wrdlst2=['Andriod Folder...','DCIM Folder...','Documents Folder...','Downloads Folder...',
                                'WhatsApp Folder...','Pictures Folder...','Telegram Folder...']
                        sssa(wrdlst2,7)
                    if i==3:
                        print('Changing Sequrity Settings...')
                        wrdlst2=['Google Securities...','Device Care Securities...']
                        sssa(wrdlst2,2)
                    if i==4:
                        print('Detecting Passwords...')
                        wait(4)
                        print('Done.')
                    if i==5:
                        print('Reaching Accounts...')
                        wrdlst2=['Google Accounts...','WhatsApp Account...','Telegram Accounts...']
                        sssa(wrdlst2,3)    
                    print('')
                    wait(1)
                global HHP
                HHP=True
                def progressbar(it, prefix="", size=50, file=sys.stdout):
                    count = len(it)
                    def show(j):
                        x = int(size*j/count)
                        file.write("%s[%s%s] %i/%i\r" % (prefix, "█"*x, " "*(size-x), j, count))
                        file.flush()        
                    show(0)
                    for i, item in enumerate(it):
                        yield item
                        show(i+1)
                    file.write("\n")
                    file.flush()

                for i in progressbar(range(100)):
                    time.sleep(0.05)
            
            def inphhp():
                write('.\\Lools\\hhptrmon','continue','c')
                ll=open('.\\Lools\\hhptrmon',mode='r')
                llr=ll.read()
                trynom=len(llr)
                print('\n')                
                if trynom<=5:
                        if trynom==5:
                            print("You are hearing that she is washing her hands.\nMaybe you won't have this opportunity again.\ntry once more.".upper())
                        HYN=input('Type CONFIRM an then press Enter to start hacking.')
                        if HYN=='CONFIRM':
                            khkhp()
                        else:
                            print('Type CONFIRM with UPPER CASE Letters.')
                            print("Come'on you don't have time.")
                            inphhp()
                else:
                    print('She is comming back.\nYou lost this opportunity.')
                    wait(2)
                    print('...')
                    wait(2)
            inphhp()
            print('She Returns from bathroom.\nYou are working with your phone seems nothing happend.')
            MM=input('''***Enter anything if you've finnished reading''')
        nvhk()
        LP()
        wait(2.5)

    if WL==7:
        cls()
        print('\tLEVEL 3\n')
        print('You found this sequence as a password of a simple host.')
        print('Try to solve it:')
        def in6():
            inp6= input('72 , 48 , 24 , 3*32 , ? , 88 , 8 , 32 , 56 , 16 , 40*2 , 8*8')
            if inp6=='40':
                print('Solved!')
                LP()
                wait(3)
            else:
                print('Wrong. Try Again.\n')
                in6()
    
    if WL==8:
        cls()
        print('\tSTORY SECTION\n')
        print('In to the deep of a suspicious website code, you found this.')
        print('URL: Atmy.onion\nUsername:zach2000\nPassword: Mr4che0r')
        print('You Start Tor Browser and then login to that account.')
        print('''As well as you thought it was not a good web-site.\nIt was the source of hackers.
Suddenly your screen gets dark and these word appear on your screen...
                 ''')
        wait(2)
        #wait(30)
        import pyautogui
        cls()
        pyautogui.press('f11')
        print(read('.\\Lools\\nrkreg'))
        wait(2)
        #wait(30)
        for i in range(9):
            pyautogui.press('f11')
        def inp8():
            def DWreg():
                import re
                def USER():
                    import re
                    global Username
                    Username= input('Type your Username: ')
                    if len(Username)>13 or len(Username)<5:
                        print('Username Length should be betweeen 5 and 13.\n')
                        USER()
                    else:
                        unch= re.search(r'\s',Username)
                        symchu=re.search(r'\w+',Username)
                        if unch!=None:
                            print('Username can contain LETTERS,NUMBERS and UNDERLINES, Not Space(s).\n')
                            USER()
                        else:
                            if len(symchu.group())!=len(Username):
                                print('Do not use special characters in your username.')
                                USER()
                            else:
                                return Username
                def PASS():
                    import re
                    global Password
                    Password= input('Type your password: ')
                    if len(Password)>15 or len(Password)<8:
                        print('Password Length Should Be Between 8 and 15.\n')
                        PASS()
                    else:
                        RePassword= input('Re-type your password: ')
                        if Password!=RePassword:
                            print('Passwords are not same.\n')
                            PASS()
                        else:
                            return Password
                USER()
                PASS()
                write('.\\Lools\\nu',text=Username)
                write('.\\Lools\\wp',text=Password)

            in8= input('1- Join them\n2- Leave The page\n\n')
            if in8=='1' or in8=='2':
                if in8=='1':
                    print('You stay in the page and a form appears.\nFeel it.(remember that it\'s DarkWeb and you shouldn\'t enter real information.)')
                    wait(2)
                    #wait(10)
                    cls()
                    DWreg()
                elif inp8=='2':
                    print('You leave the page and turn off the computer.')
                    wait(2)
            else:
                print('Invalid input.\n')
                inp8()
            print('\t1 HOUR LATER')
            print('''Somebody knocks the door.\nYou open the door. A young boy is there.
He says: Hello. I'm JACK from DarkWeb.\nWe think it's better for both of us to know each other more.''')
            if os.path.exists('.\\Lools\\wp')==True:
                print('You..\'re..welcome\nCome in.')
            else:
                print('- What? No man. I don\' like to join you.\nAnd you close the door.')
                print('Again he knocks the door.\n- What Do you want?\n+ I\'m sure you won\'t be regretful if you accept me.')
                print('- puhhh. OK. Come in.')
            wait(20)
            print(read('.\\Lools\\noadw'))
            wait(60)
            print('\n')
            MM=input('''***Enter anything if you've finnished reading''')
            LP()
        inp8()

    if WL==9:
            print('yesss')
            wait(10)




import time
time.sleep(7)
