"""
# TODO:
    > Colorize
    ? Use while loop instead of main func (but in a func)
    > Singleton Launch (With File)
    > Notification
    > Password Savor
    > Alarm
    X Minimize to Tray
    > Change Terminal Title (in each section)
    < Crypto:
        > Save Last Table (with date and then print it before getting new data)
        > Add more detail to crypto::wallet
    > Add pause after printing output

"""

import re
import hashlib
import datetime
import math
import time
import sys
import pprint
import json
import argparse
import subprocess

import rx7 as rx
import addict
from tabulate import tabulate
import cryptocompare

abs_path = rx.files.abspath(__file__)
rx.system.chdir(abs_path[:abs_path.rindex('\\')])

from Functions import *
from A6.Lib.Tray import SysTrayIcon
fp_module = rx.import_module('./A6/Lib/FP/fingerprint.py')



print = rx.style.print

ALL_CHARS = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@$%^&*()-=_+[]{};'\:"|,./<>?`~#"""+"\n"

syms=['']
#₳Ī§$†εЄє₣Ǥ₽Ħ₸₩χψ
sym= rx.random.choose(syms)
nick=['RX','now']
cent=['What to do','How can I help you']
Wrong= 0

Today = datetime.datetime.now().strftime("%d/%m/%Y")
Icon_Path = "C:/Users/Iranian/Downloads/Documents/A6.ico"


class RailFence:
    '''
    Key:  1<"int"<len
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
class Transpose:
    '''
    len(word)>key>1
    '''
    @staticmethod
    def encrypt(text, key, **kwargs):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    @staticmethod
    def decrypt(text, key, **kwargs):
        numOfColumns = math.ceil(len(text) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)
def Encrypt_Data(data):
    return RailFence.encrypt(Transpose.encrypt(data,23),7)
def Decrypt_Data(data):
    return Transpose.decrypt(RailFence.decrypt(data,7),23)

def Login(Usernames,Password):
    #Username = rx.io.selective_input('Type Your Username: ',Usernames,
    #                invalid='There is no Account with this username.',ignore_case=True)
    wrong = 0
    while wrong != 5:
        try:
            rx.cls()
            myFP = fp_module.FingerPrint()
            myFP.open()
            # myFP.identify()
            print("[?] Please Touch the Fingerprint Sensor"+(" again"if wrong else ""))
            if myFP.verify():
                break
            else:
                print("[-] Wrong Finger Input",'red')
                rx.wait(1)
                wrong += 1
        except KeyboardInterrupt:
            break
        except OSError:
            print("[*] Couldn't Detect Finger; Please Try Again",'dodger_blue_1')
            rx.wait(2)
        finally:
            myFP.close()
    else:
        print('Many Wrong Fingerprints. Your Password is Required','red')
        rx.wait(3)
        while True:
            rx.cls()
            Pass= rx.io.getpass(prompt='[?] Enter Your Password: ') 
            if hashlib.md5(bytes(Pass,'utf-8')).hexdigest() == Password:
                break
                #rx.write('.\\RX\\Access.py')
            else:
                print('[-] Invalid Password','red')
                rx.wait(1)
    
    return True

def Save_DB(DB):
    rx.write('./A6/Database.db',Encrypt_Data(str(DB).replace("    ",'').replace('\n','')))






def Main():
  while True:
   try:
    rx.terminal.getoutput('title A6')
    rx.cls()
    print('\nWelcome RX!','green')

    print(f'\n{rx.random.choose(cent)} {rx.random.choose(nick)}?')


    Inp = input(f'A6> ').strip()
    Lower = Inp.lower()

    if not Inp:pass
    elif Inp.strip().lower() in ('cls','clear'):
        rx.cls()


    #] Logout & Quit
    elif Lower in ('logout','exit','quit'):
        rx.files.remove('.\\RX\\Access.py')


    #] Date & Time
    elif Lower in ('date time','datetime','now'):
        print("Date and Time: "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print()
        pause()
    elif Regex:= re.match(r'Time Passed from (?P<F_Date>.+)',Inp,re.IGNORECASE):
        F_Date = [int(i) for i in Regex.group('F_Date').split('/')]
        import rx7.Date_Time as dt
        Now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(F_Date,'red')
        print(str(dt.date_time.passed_date(F_Date,return_time='day'   )) + '  Days'    ,  'yellow')
        print(str(dt.date_time.passed_date(F_Date,return_time='hour'  )) + '  Hours'   ,  'yellow')
        print(str(dt.date_time.passed_date(F_Date,return_time='minute')) + '  Minutes' ,  'yellow')
        print(str(dt.date_time.passed_date(F_Date,return_time='second')) + '  Seconds' ,  'yellow')

        print(f"Are passed from  '{F_Date[0]}/{F_Date[1]}/{F_Date[2]} 00:00:00'  Until  '{Now}'", 'yellow')
        print()
        pause()


    #] IP & Mac & WiFi Address
    elif Regex:=re.match(r'''ip (?P<Website>.+)''',Inp,re.IGNORECASE):
        print(rx.system.ip_website(Regex.group('Website')), 'yellow')
        print()
        pause()
    elif Regex:=re.match(r'(get )?my ip',Inp,re.IGNORECASE):
        print(f"Local  IP:  '{rx.system.ip_local() }'", 'yellow')
        try:
            ip_global =  rx.system.ip_global()
        except ConnectionError:
            ip_global = 'UNDEFINED'
        print(f"Global IP:  '{ip_global}'", 'yellow')
        print()
        pause()
    elif Regex:=re.match(r'''Valid(ate)? IP (?P<IP>[0-9\.]+)''',Inp,re.IGNORECASE):
        ip_regex= r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
        IP = Regex.group('IP')
        if re.search(ip_regex,IP):  
            print("[+] Valid IP Address",'green')
        else:  
            print("[-] Invalid IP Address",'red')
        print()
        pause()
    elif Regex:=re.match(r'Mac ?(Address)?',Inp,re.IGNORECASE):  # '$' at the end or not?
        print(f'Informatted :  {rx.system.mac_address()}')
        print(f"formatted   :  {rx.system.mac_address(True)}") 
        print()
        pause()
    elif Regex:=re.match(r"(get )?wifi password(s)?",Inp,re.IGNORECASE):
        WIFIS=set(list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles'))))
        print('[*] Getting Wifi Passwords...','dodger_blue_1')
        try:
            dic={}
            for wifi in WIFIS:
                a=subprocess.getoutput(f'netsh wlan show profiles {wifi} key=clear')
                try:
                    new=re.search(r'Key Content.*',a)
                    new=new.group()
                    new= new[new.index(':')+2:]
                    dic[wifi]=new
                    print(f"\rDone.  ({len(dic)})",end='')
                except: dic[wifi]='None'
            print()
            if len(dic):
                pprint.pprint(dic)
                print('\n')
            else: print('Failed!\n')
        except: print('Failed!')
        print()
        pause()


    #] Cryptocurrency APP
    elif Regex:=re.match(r'crypto.*',Lower,re.IGNORECASE):
        Cryptocurrency(Lower)


    #] Encryption APP
    elif Regex:=re.match(r'(encrypt|hash) .*',Inp,re.IGNORECASE):
        pass#Encryption()

    #] Song Lyrics
    elif Regex:=re.match(r"get (?P<SONG>.*) lyrics",Inp,re.IGNORECASE):
        song_name = Regex.group('SONG')
        print(f'[*] Getting "{song_name}" Lyrics from "Genius"...','dodger_blue_1')
        from A6.Lib.Genius import Genius
        genius = Genius("73bgnCCuLsZPdjuE5vF4PRwvJr69Kw3lPiizgSQ-HOxOWYX7kVRBhYKwtDuZM57y")
        genius.verbose = False
        song = genius.search_song(song_name)
        if song:
            rx.cls()
            print(f"{song.artist} - {song.title_with_featured}",'yellow')
            print('\n')
            print(song.lyrics.replace('EmbedShare URLCopyEmbedCopy',''))
            print('\n')
            #song.save_lyrics('lyrics.json',overwrite=True,verbose=False)
        else:
            print("[-] No Song Found With This Credit",'red')
        print()
        pause()
        #song.save_lyrics('lyrics.json',overwrite=True)
        

    # System and in-app
    elif Lower in ('mini','minimize'):
        minimize()

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
        print()
        print('Sorry. I didn\'t get that.')
        print('[-] command "{}" not found.'.format(Inp).upper(), 'red')
        rx.sleep(2)
   
   except (KeyboardInterrupt,EOFError,OSError):
    Exit()
    #Main()



class Cryptocurrency:

    def Get_Dollar_Price():
        if DB["Cryptocurrency"]["Dollar_Price"][0] != Today:
            from selenium import webdriver
            print("[*] Getting Today's Dollar Price")
            browser = webdriver.Chrome(r"C:\Users\Iranian\Downloads\Compressed\chromedriver.exe")
            browser.minimize_window()
            browser.get("https://www.tgju.org/profile/price_dollar_rl")
            for element in list(browser.find_elements_by_xpath('.//span[@data-col = "info.last_trade.PDrCotVal"]')):
                if element.text:
                    Dollar_Price = int(element.text.replace(',','')[:-1])# + 600
                    browser.quit()
                    DB["Cryptocurrency"]["Dollar_Price"] = [Today,Dollar_Price]
                    Save_DB(DB)
                    #print("Dollar_Price Saved in DB for Today",'green')
                    break
        else:
            Dollar_Price = DB["Cryptocurrency"]["Dollar_Price"][1]

        return Dollar_Price

    class INFO:
        Sub_Apps = ["Wallet","Market"]
        class Tray:
            def Wallet(systray):
                Set_LastActive(DB)
                rx.terminal.run('start cmd /c "asix.py --Cryptocurrency:Wallet"')
            def Market(systray):
                Set_LastActive(DB)
                rx.terminal.run('start cmd /c "asix.py --Cryptocurrency:Market"')
            Menu = ('Crypto', None,
              (
                ("Wallet",None,Wallet),
                ("Market",None,Market), 
              )
            )
    
    def __init__(self,Entry,msg=None):
        rx.cls()
        if msg: print(msg)
        Regex = re.match(r'crypto ?(?P<Section>.*)',Entry,re.IGNORECASE)
        Section = Regex.group('Section')
        #print(Section)
        #exit()
        if not Regex.group('Section'):
            print('''
            1- Wallet
            2- Market
            ''')
            Section = rx.io.selective_input('A6::Crypto> ',
                                                ['1','2','Exit'],ignore_case=True)
            Section = {'1':'wallet','2':'market','exit':'exit'}[Section]
            rx.cls()
        if Section not in ('wallet','market','exit'):
            Cryptocurrency('Crypto',msg='Invalid Input')
    
        if Section == 'exit':
            return
    
        if Section == 'wallet':
            def Wallet_func():
                rx.cls()
                Data = dict(DB['Cryptocurrency'])
                print("Enter Section:")
                print("""
                1-Show Wallet
                2-Add  Transaction
                3-Edit Transaction
                4-Show Transactions
                5-Calculate Profit
                """)
                cc_wlt_inp = rx.io.selective_input(
                    "A6::Cryptocurrency> ",["1","2","3","4","exit",],ignore_case=True)
                if cc_wlt_inp.lower() == 'exit':
                    return
                elif cc_wlt_inp == '1':
                    Currencies = Data['Currencies']
                    Wallet = {}
                    Dollar_Price = Cryptocurrency.Get_Dollar_Price()
                    Tag_List = []
                    
                    for currency in Currencies:
                        Symbol = Currencies[currency]["Symbol"]
                        Tag_List.append(Symbol)
                        Wallet[currency] = [0.00,Symbol,]

                    for currency in Currencies:
                        for transaction in Currencies[currency]['Transactions']:
                            #print(f"{currency}::{transaction['Type']}")
                            if transaction['Type'] == 'Buy':
                                Wallet[currency][0] += transaction['Amount']
                            elif transaction['Type'] == 'Sell':
                                Wallet[currency][0] -= transaction['Amount']
                            else:
                                print(f'DB ERROR in "Cryptocurrency::Currencies::{currency}::transaction"','red')
                        Wallet[currency][0] = round(Wallet[currency][0],3)
                        print(Wallet[currency],'dodger_blue_1')
                        #print(Wallet[currency][2],'green')
                    print('\n[*] Getting Data...','dodger_blue_1')
                    Prices = cryptocompare.get_price(Tag_List, ['USD'])
                    for currency in Currencies:
                        Wallet[currency].append( round(Wallet[currency][0]*Prices[Wallet[currency][1]]["USD"],3))
                        Wallet[currency].append(int(Wallet[currency][2]*Dollar_Price))

                    rx.cls()
                    print()
                    #pprint.pprint(Wallet)
                    Table = []
                    for currency in Wallet:
                        Table.append(
                            [currency,Wallet[currency][0],Wallet[currency][2],Wallet[currency][3]]
                        )
                    print(tabulate(Table,tablefmt="fancy_grid",
                                   headers=["Currency","Amount","USD Amount","Rial Amount"],
                                   stralign='left',numalign='left'
                    ))
                    print()
                    pause()
                    Wallet_func()

                elif cc_wlt_inp == '2':
                    Name = rx.io.wait_for_input('Currency Name     :   ').title()
                    if Name not in Data['Currencies']:
                        Symbol = rx.io.wait_for_input('Currency Symbol   :  ').upper()
                        Data['Currencies'][Name] = {"Name":Name,"Symbol":Symbol,"Transaction":[]}
    
                    Type =  rx.io.selective_input("Type [Buy/Sell]   :   ",['B','S'],ignore_case=True)
                    if Type=='b': Type="Buy"
                    else: Type="Sell"
                    Amount =  float(rx.io.wait_for_input ('Amount            :   '))
                    Date = input('Date              :  ') or datetime.datetime.now().strftime("%d/%m/%Y")
                    USD_Price = float(rx.io.wait_for_input('Currency USD Price:  '))
                    USD_Amount  =  float(input('USD Amount        :   '))
                    Rial_Price  =  float(input('Rial Price        :   '))
                    Rial_Amount =  float(input('Rial Amount       :   '))
                    USDT = int(input('USDT Price        :   '))
    
                    Data['Currencies'][Name]["Transactions"] .append({
                        "Type"        :  Type,
                        "Amount"      :  Amount,
                        "Date"        :  Date,
                        "USD Amount"  :  USD_Price,
                        "USD Price"   :  USD_Amount ,
                        "Rial Amount" :  Rial_Price ,
                        "Rial Price"  :  Rial_Amount,
                        "USDT"        :  USDT
                    })
                    Data['Transactions'].append([len(Data['Transactions'])+1,
                                                 Data['Currencies'][Name]["Symbol"],
                                                 Type,Date,Amount,Rial_Amount
                                                 ])
                    DB["Cryptocurrency"] = Data
                    Save_DB(DB)
                elif cc_wlt_inp == '3':
                    print(tabulate(Data['Transactions'],tablefmt="fancy_grid",
                                headers=["TAG","TYPE","DATE","AMOUNT","R_PRICE"],
                                stralign='left',numalign='left',
                    ))
                    transaction_id = rx.io.selective_input("Enter Transaction ID:  ",
                                            [str(i) for i in range(1,len(Data['Transactions'])+1)])
                    for currency in Data['Currencies']:
                        for transaction in Data['Currencies'][currency]["Transactions"]:
                            if transaction['ID'] == int(transaction_id):
                                break
                elif cc_wlt_inp == '4':
                    print(tabulate(Data['Transactions'],tablefmt="fancy_grid",
                            headers=["TAG","TYPE","DATE","AMOUNT","R_PRICE"],
                            stralign='left',numalign='left',
                    ))
                    pause()
                elif cc_wlt_inp == '5': pass
            Wallet_func()
    
        if Section == 'market':
            #print(cryptocompare.get_historical_price('XRP','USD'))
            #CRYPTOCOMPARE_API_KEY for Env_Var
            print('Getting Up-To-Date Data...')
            cryptocompare.cryptocompare._set_api_key_parameter('db9e2f07dfbd47bd2b1cc7db0496903168521d2174d758c050857202ff16c7a5')
            Currency_List = {"Bitcoin":'BTC', "Ethereum":'ETH',"XRP":'XRP',
                             "Tron":'TRX',"EOS":"EOS","Cardano":"ADA",
                             "Litecoin":"LTC", "Stellar":"XLM","DOGE":"DOGE"}
            Prices = cryptocompare.get_price(list(Currency_List.values()), ['USD'])
            #print(Prices)
            
            CL_Tag_Name = {v: k for k, v in Currency_List.items()}

            rx.cls()
            Table = []
            for currency_tag in CL_Tag_Name:
                Table.append([CL_Tag_Name[currency_tag],currency_tag,Prices[currency_tag]["USD"]])
            print('Current Market:')
            print(tabulate(Table,tablefmt="fancy_grid",
                           headers=["Currency","Tag","Price"],
                           stralign='left',numalign='left'
            ))
            print()
            
            Dollar_Price = Cryptocurrency.Get_Dollar_Price()

            for row in Table:
                row.append(readable_num(int(row[2]*Dollar_Price)))
            rx.cls()
            print(f"Dollar Price: {Dollar_Price}T")
            print(tabulate(Table,tablefmt="fancy_grid",
                           headers=["Currency","TAG","USD Price","Rial Price"],
                           stralign='left',numalign='left'
            ))
            print()
    
    
            pause()
    
        Cryptocurrency('Crypto')
    
    
    
        """
        Currencies = enumerate(Data.keys(),1)
        print("Available Currencies:")
        for currency in Currencies:
            print(f"  {currency[0]}-{currency[1]}")
        """
        """
        import yfinance as yf
        data = yf.download(tickers='XRP-USD', period = '3h', interval = '15m')
        print(data)
        """





#< APP Options >#
#] Tray
def say_hello(systray): print("Hello, World!")
def t_minimize(systray):
    minimize()
def t_Cryptocurrency(systray):
    DB["Account"]["last_active"] = time.time()
    Save_DB(DB)
    rx.terminal.run('start cmd /c "asix.py --cryptocurrency"')
    #Cryptocurrency('Crypto')

def on_quit(systray):
    print('Exiting... on quit','red')
    pid = rx.system.pid()
    rx.terminal.getoutput(f'taskkill /pid {pid} /F')
    #sys.exit(1)
menu_options = (
                ('Minimize', None, t_minimize),
                Cryptocurrency.INFO.Tray.Menu,

                #('on_quit', None, on_quit),
               )


def Set_LastActive(DB):
    DB["Account"]["last_active"] = time.time()
    Save_DB(DB)


def check_if_on_pc():
    import pyautogui,keyboard
    afk = 0
    ms = pyautogui.position()
    add = False
    while True:
        if not rx.files.exists("./A6/Lock.ini"):
            keyboard.start_recording()
            if pyautogui.position() == ms:
                #print("No mouse move")
                afk +=1
                add = True
            else:
                #print("mouse moved")
                ms = pyautogui.position()
                afk = 0
            rx.sleep(1)
            if keyboard.stop_recording():
                #print("keyborad moved")
                afk = 0
            else:
                #print("no keyboard move")
                if not add:
                    afk +=1
                    add = False
            if afk >= 300:
                print("Not doing anything for 300s")
                rx.terminal.run(f"start python ./A6/Lock.py {DB['Account']['Usernames']} {DB['Account']['Password']}")
                rx.write("./A6/Lock.ini","")
                afk = 0


def Exit():
    if Logged_In:
        Set_LastActive(DB)
        systray.shutdown()
        #print('Exiting...','red')
    print("\nPlease Quit from Traybar\n")
    pause()





if __name__ == "__main__":

    q = rx.read('./A6/Dec.json')

    #] Loading DB
    DB = rx.read('./A6/Database.db')
    DB = Decrypt_Data(DB)
    DB = eval(DB)
    #DB = addict.Dict(DB)
    #pprint.pprint(DB)
    
    #.replace("    ",'').replace('\n','')
    #rx.write('./A6/Database.db',Encrypt_Data(q.replace("    ",'').replace('\n','')))
    #with open('./A6/Dec.json','w') as f: json.dump(DB,f,indent=4)
    #exit()


    import threading


    rx.cls()
    set_title('A6')

    Logged_In = False
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '--Cryptocurrency':
                Cryptocurrency('Crypto')
        else:
            if time.time() - DB["Account"]["last_active"] > 10:
                Logged_In = True
                #Logged_In = Login(DB['Account']['Usernames'],DB['Account']['Password'])

            systray = SysTrayIcon(Icon_Path, "Example tray icon", menu_options,on_quit,1)
            systray.start()
            #Main()
            

            MainThread = threading.Thread(target=Main)
            MainThread.start()
            CtL = threading.Thread(target=check_if_on_pc)
            #CtL.start()



    except (KeyboardInterrupt,EOFError,OSError):
        if Logged_In:
            Set_LastActive(DB)
            systray.shutdown()
        #print('Exiting...','red')
        print("\nPlease Quit from Traybar")

    #rx.cls()
    #Cryptocurrency(DB['Cryptocurrency'])





