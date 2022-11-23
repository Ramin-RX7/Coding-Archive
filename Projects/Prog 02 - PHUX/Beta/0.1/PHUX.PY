from rx import *
import os,socket,subprocess,pyautogui

import AD


Device_Name= socket.gethostname()+' - '+system.accname()

def SysINFO():
    import platform
    PlatSys= platform.uname()
    CMDSys=  subprocess.getoutput('systeminfo')
    import uuid
    Mac= hex(uuid.getnode())
    write('.\\F\\{}\\SystemInfo'.format(Device_Name),mode='replace',text='{0}\n\n{1}\nMac: {2}'.format(PlatSys,CMDSys,Mac))
#SysINFO()
 

#subprocess.Popen('explorer ".\\V"')

def devmgmt():
    import pyautogui
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('devmgmt.msc')
    pyautogui.press('enter')
    wait(5.0)
    pyautogui.hotkey('win', 'up')


def unin():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('control')
    pyautogui.press('enter')
    wait(1)
    pyautogui.hotkey('win','up')
    sx,sy=pyautogui.size()
    pyautogui.click(sx/20.2,sy/1.05)
    pyautogui.typewrite('unin')
    wait(0.25)
    pyautogui.click(sx/7.8,sy/7.83)

'''
cmd = subprocess.Popen('cmd.exe /K cd /')
pyautogui.typewrite('netsh wlan show profiles')
pyautogui.press('enter')
pyautogui.typewrite('netsh wlan show profiles  key=clear')
pyautogui.press('left',presses=10)
'''


