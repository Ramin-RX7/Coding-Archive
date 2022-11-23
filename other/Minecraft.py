#rx.sleep(1.5)
import pyautogui
from pydirectinput import keyDown,keyUp,click,press,moveRel
import rx7 as rx



def jump():
    press('space')
    keyDown('w')
    rx.sleep(0.2)
    keyUp('w')
#jump()


def turn_around():
    pyautogui.moveRel(332,0,duration=1)
#turn_around()


def build_backward(item_nom=0,number=1,levels=1,adjust=True,min=False):
    built = 0
    #] Go to block
    if adjust:
        keyDown('shift')
        keyDown('w')
        rx.sleep(1)
        keyUp('w')    
        pyautogui.moveRel(0,200,duration=1)
        pyautogui.moveRel(0,-130,duration=1)
    #] Building
    press(str(item_nom))
    keyDown('s')
    for i in range(0,number if levels==1  else number-1):
        if built == 64:
            built = 0
        rx.sleep(0.8)
        click()
        built += 1
    keyUp('s')
    keyUp('shift')

    if levels>1:
        if min == 0:
            min = 1
        elif min == 1:
            min = 0
        keyDown('shift')
        keyDown('w')
        rx.sleep(2)
        keyUp('w')    
        press(str(item_nom))
        jump()
        turn_around()
        keyDown('shift')
        keyDown('s')
        rx.sleep(0.2)
        keyUp('s')
        keyUp('shift')
        pyautogui.moveRel(0,200,duration=1)
        pyautogui.moveRel(0,-30,duration=1)
        click()
        rx.sleep(0.1)
        click()
        build_backward(item_nom,number-1,levels-1,adjust,min)
#rx.sleep(5)
#build_backward(0,10,6)


def goto(blocks_nom):
    keyDown('shift')
    keyDown('w')
    rx.sleep(0.75*blocks_nom)
    keyUp('w')
    keyUp('shift')
#goto()

def afk():
    last_move = ''
    while True:
        direction = rx.random.choose(list({'w','d','s','a'}-set(last_move)))
        direction = 'w'
        last_move = str(direction)
        sleep = rx.random.choose(range(1,8))*15
        print(sleep)
        rx.sleep(sleep)
        keyDown('shift')
        keyDown(direction)
        rx.sleep(2)
        keyUp(direction)
        keyDown('s')
        rx.sleep(0.5)
        keyUp('s')
        keyUp('shift')
        turn_around()
rx.sleep(3)
#afk()


def rapid_click(times):
    for i in range(times):
        click(button=pyautogui.RIGHT)
        rx.sleep(0.2)
#rx.sleep(2)
#rapid_click(200)
#build_backward(0,6,6)




"""blueprint = '''
 #
 1 1 1 1 1 1 1 1 .
 1 . . . . . . 1 1
 1 . . . . . . . 1
 1 . . . . . . . 1
 1 . . . . . . . 1
 1 . . . . . . . 1
 1 1 1 1 . . . . 1
 . . . 1 1 . . . 1
 . . . . 1 1 1 1 1
 #
 '''
 i=0
 x=0
 line_list = ['' for line in blueprint.split('\n')[2:-2]]
 
 blueprint = '''
 #
 1 1
 1 0
 1 1
 #
 '''
 def adjust():
     keyDown('shift')
     keyDown('w')
     rx.sleep(1)
     keyUp('w')    
     pyautogui.moveRel(0,200,duration=1)
     pyautogui.moveRel(0,-90,duration=1)
 adjust()
 for _ in len(blueprint.split('\n')[0]):
     for nom,line in enumerate(blueprint.split('\n')[2:-2]):
         print(nom,line)
         keyDown('shift')
         keyDown('s')
         rx.sleep(0.75)
         keyUp('s')
         keyUp('shift')
         if line[i] == "1":
             click()
     i+=2
     keyDown('shift')
     keyDown('d')
     rx.sleep(0.75)
     keyUp('d')
     keyUp('shift')
     goto(len(blueprint.split('\n')[2:-2]))
 
"""