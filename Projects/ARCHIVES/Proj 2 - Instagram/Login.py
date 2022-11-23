import random
import string
import pyautogui
import time

#import webbrowser
#Insta_Login= 'https://www.instagram.com/accounts/login/?source=auth_switcher/'
#webbrowser.open_new_tab(Insta_Login)
pyautogui.click(315,741)
time.sleep(7)
pyautogui.typewrite('https://www.instagram.com/accounts/login/?source=auth_switcher/')
pyautogui.click(345,81)
time.sleep(10)

from users import userss

#usename
pyautogui.click(700,221)
pyautogui.typewrite(userss[3])
time.sleep(1)

#pass
pyautogui.click(700,265)
pyautogui.typewrite('falofakeekhale')
time.sleep(1)

#login button
pyautogui.click(700,307)
time.sleep(6)


#######
#######
#######

# No notify
pyautogui.click(677,532)

#Follow suggest with 0 following
pyautogui.click(320,50)
pyautogui.typewrite('https://www.instagram.com/explore/people/suggested/')
pyautogui.click(345,81)
def faloba0():
    time.sleep(5)
    pyautogui.click(925,268)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.move(0,63)
    pyautogui.click()
    time.sleep(1)
    pyautogui.scroll(-260)
    time.sleep(2)
faloba0()
faloba0()
faloba0()
faloba0()


#####


#Follow other Fakes

def faloF():
    pyautogui.click(683,110)
    pyautogui.typewrite(userss[0])
    pyautogui.move(0,50)
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.click(760,215)

    pyautogui.click(683,110)
    pyautogui.typewrite(userss[1])
    pyautogui.move(0,50)
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.click(760,215)

    pyautogui.click(683,110)
    pyautogui.typewrite(userss[3])
    pyautogui.move(0,50)
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.click(760,215)
faloF()


#####


# Follow X Person
def faloX():
    pyautogui.click(683,110)
    pyautogui.typewrite('arghavan.co')
    pyautogui.move(0,50)
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.click(735,215)
    time.sleep(3)
faloX()

#exit chrome
pyautogui.click(1342,5)

