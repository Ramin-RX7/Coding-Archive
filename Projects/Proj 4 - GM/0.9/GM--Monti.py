import random
ORGNOM= random.randint(1,100)
#print(ORGNOM)
import PySimpleGUI as sg

def setnom():
    global values, Nom
    from Ac_Info import Credit
    layout= [ [sg.Text('    '),sg.Text('CREDIT:   {0}'.format(Credit)),sg.Text('    \t\t\t    :اعتبار')],
            [sg.Text('    '),sg.Text('BET:     ')  , sg.Input(size=(30,10),focus=True),sg.Text('  :مقدار')],
            [sg.Text('    '),
            sg.Radio('Upper than  X  بیشتر از      ', "RADIO1",),
            sg.Radio('Lower than  X  کمتر از', "RADIO1")],
            [sg.Text('X= '),sg.Slider(range=(2, 99), orientation='h', size=(30, 20), default_value=50, tick_interval=97,),],
            [sg.Text('     '),
            sg.Button('START\t\t\tشروع',button_color=('White','Green'),size=(36,2),font=(15))]           
            ]
    window = sg.Window('BETTING PANEL', layout, no_titlebar='True',keep_on_top=True)
    event, values = window.read()
    window.close()
    if values[0]==None or values[0]=='':
        setnom()
    else:    
        Bet= int(values[0])
        if Bet==0:
            print('It\'s not enough for playing.')
            setnom()
        if Bet>Credit:
            print('You don\'t have enough credit.')
            print('You need {0} more credits for this.'.format(Bet-Credit))
    Nom= values[3]
    if values[1]==False and values[2]==False:

        layout=[ [sg.Text('Please choose Lower or Upper.        .لطفا کمتر یا بیشتر را انتخاب نمایید',font=(35))],
                 [sg.Text('\t\t\t   '),sg.Button('OK',size=(8,2),button_color=('White','Green'),)]
                ]
        window = sg.Window('Error', layout, no_titlebar='True',keep_on_top=True, auto_close=True, auto_close_duration=5)
        window.read()
        window.close()
        setnom()
setnom()



layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(100, orientation='h', size=(50, 30), key='progressbar',bar_color=('Green','Silver'))],
          [sg.Text('\t\t\t\t'), sg.Text(0,key='CxC',auto_size_text=True,size=(50,50),font=(30,30),text_color='Black',)],
          #[sg.Cancel()]]
          ]
window = sg.Window('Custom Progress Meter', layout,size=(500,150),no_titlebar=True,keep_on_top=True,)
progress_bar = window['progressbar']

for i in range(1,100):
    event, valuess = window.read(timeout=850)
    window.FindElement('CxC').update(i)
    if event == 'Cancel'  or event is None:
        break
    progress_bar.UpdateBar(i + 1)

    if i >= ORGNOM:
        import time
        time.sleep(3)
        window.close()
        print('Round Has Been Finished')
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
        break







import time
time.sleep(5)
