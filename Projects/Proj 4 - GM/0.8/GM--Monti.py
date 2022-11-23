import random

ORGNOM= random.randint(1,100)




import PySimpleGUI as sg



layout= [ 
          [sg.Text('    '),
           sg.Radio('Upper than  X  بیشتر از      ', "RADIO1",),
           sg.Radio('Lower than  X  کمتر از', "RADIO1")],
          [sg.Text('     '),
           sg.Text('X= '),sg.Slider(range=(2, 99), orientation='h', size=(30, 20), default_value=50, tick_interval=97,),],
          [sg.Button('START\t\t\tشروع',button_color=('White','Green'),size=(36,2),font=(15))]           
         ]
window = sg.Window('BETTING PANEL', layout, no_titlebar='True',keep_on_top=True)
event, values = window.read()
window.close()

Nom= values[2]


if values[0]==False and values[1]==False:
    print('(You didn\'t participate in this round)')

print('Number is {}'.format(str(ORGNOM)))
if values[0]==True:
    if Nom<ORGNOM:
        print('You won.')
    if Nom==ORGNOM:
        print('Draw, No Bet.')
    if Nom>ORGNOM:
        print('You Lost.')

if values[1]==True:
    if Nom>ORGNOM:
        print('You won.')
    if Nom==ORGNOM:
        print('Draw, No Bet.')
    if Nom<ORGNOM:
        print('You Lost.')




import time
time.sleep(5)