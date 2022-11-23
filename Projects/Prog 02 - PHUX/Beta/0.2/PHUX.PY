from rx7 import *
import os,socket,subprocess,pyautogui

import AD


Device_Name= socket.gethostname()+' - '+system.accname()

def SysINFO():
    import platform,uuid,re
    WIFIS=set(x[2:] for x in re.findall(r': .*', subprocess.getoutput('netsh wlan show profiles')))
    write('.\\F\\{}\\SystemInfo'.format(Device_Name),mode='replace',text='SI:\n{0}\n{1}\n\nMac: {2}\n\nWIFI:\n{3}'.format(platform.uname(),subprocess.getoutput('systeminfo'),hex(uuid.getnode()),WIFIS))
SysINFO()

#subprocess.Popen('explorer ".\\V"')







'''
def devmgmt():
    import pyautogui
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('devmgmt.msc')
    pyautogui.press('enter')
    wait(5.0)
    pyautogui.hotkey('win', 'up')
'''
'''
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
