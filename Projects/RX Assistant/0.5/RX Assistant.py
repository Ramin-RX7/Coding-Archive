
"""
# TODO:
    > App Library
    > Colorize
    > Use while loop instead of main func (but in a func)
    > Singleton Launch (With File)
    > Icon
    > Notification
    > Open:
        > CH Photo (Random)
"""

import rx7 as rx
from subprocess import Popen
import time,os,re
import hashlib


print = rx.style.print
ALL_CHARS = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@$%^&*()-=_+[]{};'\:"|,./<>?`~#"""

class Affine:
    """
    - Case Sensetive
    - Supports Numbers and Symbols
    - Both keys should be integer 
    - key1 should be relatively prime to len(alphabet)
    - key1 will be converted to  range(1,len(alphabet))
    - key2 will be converted to  range(0,len(alphabet))
    """

    class Tools:
        @staticmethod
        def getInverse(key1, alphabet):
            for i in range(1, len(alphabet)):
                if ((int(key1)*int(i)) % int(len(alphabet))) == 1:
                    return i
            return 0

        @staticmethod
        def _EncDec(text, keys, alphabet, Enc):
            key1 = keys[0]
            key2 = keys[1]
            ans = ""
            for char in text:
                try:
                    if Enc:
                        alphI = (alphabet.index(char) * key1 + key2) % len(alphabet)
                    else:
                        aInverse = Affine.Tools.getInverse(key1, alphabet)
                        alphI = (aInverse * (alphabet.index(char) - key2)) % len(alphabet)
                    enc = alphabet[alphI]
                except ValueError:
                    enc = char
                    #raise
                    #raise Exception("Can't find char '" + char + "' of text in alphabet!")
                ans += enc
            return ans

    @staticmethod
    def encrypt(text, keys, alphabet=ALL_CHARS):
        '''
        text:  String to encrypt with Affine Cipher\n
        keys:  List of keys to use.
         (See Affine help to understand keys of this cipher)\n
        alphabet: a subscriptable iterable which contains all characters  
        you want to use for Affine Cipher (default= lowers+uppers+digits+symbols)
        '''
        return Affine.Tools._EncDec(text, keys, alphabet, True)

    @staticmethod
    def decrypt(text, keys, alphabet=ALL_CHARS):
        '''
        text:  String to decrypt with Affine Cipher\n
        keys:  List of keys to use. ([key1, key2])
         (See Affine help to understand keys of this cipher)\n
        alphabet: a subscriptable iterable which contains all characters  
        you want to use for Affine Cipher (default= lowers+uppers+digits+space+symbols)
        '''
        return Affine.Tools._EncDec(text, keys, alphabet, False)
class RailFence:
    '''
    -> Transposition
    Case Sensetive.
    Support Numbers and Symbols.
    Key Must be an Integer Lower Than Word Length and Higher than 1.
    '''
    @staticmethod
    def encrypt(text, key, **kwargs):  
        rail = [ ['\n' for _2 in range(len(text))] for _ in range(key)]
        dir_down = False
        row, col = 0, 0
        
        for i in range(len(text)):
            if (row == 0) or (row == key - 1): 
                dir_down = not dir_down
            rail[row][col] = text[i] 
            col += 1
            if dir_down: 
                row += 1
            else: 
                row -= 1

        result = [] 
        for i in range(key): 
            for j in range(len(text)): 
                if rail[i][j] != '\n': 
                    result.append(rail[i][j]) 

        return "".join(result)

    @staticmethod
    def decrypt(text, key, **kwargs): 
        rail = [['\n' for i in range(len(text))]  
                    for j in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(text)): 
            if row == 0: 
                dir_down = True
            if row == key - 1: 
                dir_down = False 
            rail[row][col] = '*'
            col += 1 
            if dir_down: 
                row += 1
            else: 
                row -= 1

        index = 0
        for i in range(key): 
            for j in range(len(text)): 
                if ((rail[i][j] == '*') and
                (index < len(text))): 
                    rail[i][j] = text[index] 
                    index += 1

        result = [] 
        row, col = 0, 0
        for i in range(len(text)): 
            if row == 0: 
                dir_down = True
            if row == key-1: 
                dir_down = False
            if (rail[row][col] != '*'): 
                result.append(rail[row][col]) 
                col += 1
            if dir_down: 
                row += 1
            else: 
                row -= 1

        return "".join(result)



def Login(Usernames,Password):
    Username = rx.io.selective_input('Type Your Username: ',Usernames,
                          invalid='There is no Account with this username.',ignore_case=True)
    import getpass
    while True:
        Pass= getpass.getpass(prompt='Type Your Password: ') 
        if hashlib.md5(bytes(Pass,'utf-8')).hexdigest() == Password:
            print('\nWelcome RX!','green')
            #rx.write('.\\RX\\Access.py')
            
            break
        else:
            print('Invalid Password','red')
    return Username

syms=['$','>>>','>>> $']
sym= rx.random.choose(syms)
nick=['RX','now']
cent=['What to do','How can I help you']
Wrong= 0
def Main():
    global Wrong
    if Wrong>=5:
        rx.files.remove('.\\RX\\Access.py')
        print('%sDue to security things you have to login again %sRX%s.\nThank you.%s'% 
              (rx.fg('red'),rx.fg('green'),rx.fg('red'),rx.attr(0)))
        rx.wait(4)
        rx.cls()
        Wrong=2
        Login()

    try:
        print(f'\n{rx.random.choose(cent)} {rx.random.choose(nick)}?')
        #Inp= rx.io.wait_for_input(f'{sym} ')
        Inp = input(f'\r{sym} ')
    except KeyboardInterrupt:
        exit()

    Striped = Inp.strip()

    if not Inp:pass
    elif Inp.strip().lower() in ('cls','clear'):
        rx.cls()
    # IP & Mac Address
    elif Regex:=re.match(r'''ip (?P<Website>.+)''',Inp,re.IGNORECASE
                ):
        print(rx.system.ip_website(Regex.group('Website')))
    elif Inp.lower() == 'my ip':
        print(f"Local  IP:  '{rx.system.ip_local() }'")
        try:
            ip_global =  rx.system.ip_global()
        except ConnectionError:
            ip_global = 'UNDEFINED'
        print(f"Global IP:  '{ip_global}'")
    elif Regex:=re.match(r'''Valid(ate)? IP (?P<IP>[0-9\.]+)''',Inp,re.IGNORECASE):
        ip_regex= r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
        IP = Regex.group('IP')
        if re.search(ip_regex,IP):  
            print("Valid IP Address")
        else:  
            print("Invalid IP Address")
    elif Regex:=re.match(r'Mac( Address)?',Inp,re.IGNORECASE):  # '$' at the end or not?
        print(f'Informatted :  {rx.system.mac_address()}')
        print(f"formatted   :  {rx.system.mac_address(True)}") 

    # Logout & Quit
    elif Striped.lower() in ('logout','exit','quit'):
        import os
        os.remove('.\\RX\\Access.py')

        # VPN
        """elif Inp=='Windscribe':
            pass#################################Popen('.\\')
         elif Inp=='Proton VPN':
            pass#################################Popen('.\\')
         # Applications
         elif Inp=='Record Screen':
            pass###########
         elif Inp=='Github':
            Popen('.\\RX\\App\\Windscribe.aa')
         elif Inp=='My Password List':
         elif Inp=='WIFI':
        """

    elif Striped.lower() in ('date time','datetime','now'):
        from datetime import datetime
        print("Date and Time: "+ datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    elif Regex:= re.match(r'Time Passed from (?P<F_Date>.+)',Striped,re.IGNORECASE):
        F_Date = [int(i) for i in Regex.group('F_Date').split('/')] 
        from datetime import datetime
        import rx7.Date_Time as dt
        Now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(F_Date,'red')
        print(str(dt.date_time.passed_date(F_Date,return_time='day'))    + '  Days')
        print(str(dt.date_time.passed_date(F_Date,return_time='hour'))   + '  Hours')
        print(str(dt.date_time.passed_date(F_Date,return_time='minute')) + '  Minutes')    
        print(str(dt.date_time.passed_date(F_Date,return_time='second')) + '  Seconds')

        print(f"Are passed from  '{F_Date[0]}/{F_Date[1]}/{F_Date[2]} 00:00:00'  Until  '{Now}'")


    # System and in-app
    elif Inp.lower() in ('mini','minimize'):
        import ctypes
        ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    elif Inp=='About':
        print('''
        This is an assistant which works in terminal.
        It supports usefull widgets those everyone needs.
        'NOTE THAT THIS ASSISTANT CAN NOT CHAT WITH YOU'

        NAME:           ASIX
        Created on:     2-1-2020
        STATUS:         Releasing new updates
        CREATOR:        RX
        ''')


    # Open Folders
    elif Inp=='CH folder':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin"')
    elif Inp=='CH Super':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super"')
    elif Inp=='CH Photo':
        Popen('explorer "D:\\Program Files\\XXX\\Collected\\CELEBRITY\\Courtney Hadwin\\Super\\2017-08-08 16.32.06 1576837726031578273_3007194494.jpg"')
        rx.wait(5)
        import pyautogui
        #pyautogui.click(1000,400)
        pyautogui.press('f5')
    elif Inp=='X Porn':
        Popen('explorer "E:\\X List\\ZzzzzzZ\\Sorted"')      
    elif Inp=='Hack Folder':
        Popen('explorer "D:\\Program Files\\XXX\\Hack"') 
    elif Inp=='Photo Collection':
        Popen('explorer "D:\\Program Files\\XXX\\Collected"')
        

    #ping site --> ip site ro mide


    elif Inp=='Commands':
        print('here is list of all commands:\n')
        Commands='''
            Data:
                IP
                My IP
                Mac Address
                ### Tracert

            Logout & Quit:
                Logout
                exit/quit

            Date & Time:
                Date Time
                Time Passed from

            System & In-App:
                ### Mini
                WIFI
                Commands

            ONLY RX PC:
                CH:
                    CH folder
                    CH Super
                    CH Photo

                Folders:
                    X Porn
                    HackFolder
                    Photo Collection
        '''
        Commands=Commands.split('\n')
        for letter in Commands:
            print(letter)
            rx.wait(0.05)

    else:
        print('Sorry. I didn\'t get that.')
        print('ERROR:  command "{}" not found.'.format(Inp).upper())

    Main()




if __name__ == "__main__":

    enc_aff = Affine.encrypt(rx.read('./RX/Dec.db').replace('\n','#'),keys=[21,23])
    dec_aff = Affine.decrypt(rx.read('./RX/Data.db'),keys=[21,23]).replace('#','\n')
    #print(enc_aff)
    #print(dec_aff)
    exec(dec_aff)
    #exit()
    print('\n')

    #Login(Usernames,Password)
    Main()
