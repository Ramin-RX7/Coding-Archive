import os
import shutil
import subprocess
import time


def ProgressBar(Module_Nom):
    def Progressbar8000():
        import PySimpleGUI as sg
        sg.ChangeLookAndFeel('Black')
        layout = [[sg.Text('Downloading Module ...    '+ Module_Nom)],
                    [sg.ProgressBar(8000, orientation='h', size=(20, 20), key='progbar')]]
        window = sg.Window('Creating Account (in progress)', layout, no_titlebar=True, keep_on_top=True)
        for i in range(8000):
            event, values = window.Read(timeout=0)
            window.Element('progbar').UpdateBar(i + 1)
        window.Close()
    Progressbar8000()

    def Progressbar4000():
        import PySimpleGUI as sg
        sg.ChangeLookAndFeel('Black')
        layout = [[sg.Text('Installing Module...    '+ Module_Nom)],
                    [sg.ProgressBar(4000, orientation='h', size=(20, 20), key='progbar')]]
        window = sg.Window('Creating Account (in progress)', layout, no_titlebar=True, keep_on_top=True)
        for i in range(4000):
            event, values = window.Read(timeout=0)
            window.Element('progbar').UpdateBar(i + 1)
        window.Close()
    Progressbar4000()

    def Progressbar2500():
        import PySimpleGUI as sg
        sg.ChangeLookAndFeel('Black')
        layout = [[sg.Text('Loading Module...    '+ Module_Nom)],
                    [sg.ProgressBar(2500, orientation='h', size=(20, 20), key='progbar')]]
        window = sg.Window('Creating Account (in progress)', layout, no_titlebar=True, keep_on_top=True)
        for i in range(2500):
            event, values = window.Read(timeout=0)
            window.Element('progbar').UpdateBar(i + 1)
        window.Close()
    Progressbar2500()

#########################

def Main_Ins():
    os.mkdir('.\\Date_Time')
    os.mkdir('.\\Date_Time\\Live')
    os.mkdir('.\\Date_Time\\Passed')
    os.mkdir('.\\Downloads')
    os.mkdir('.\\Downloads\\Programs')
    os.mkdir('.\\IP')
    os.mkdir('.\\IP\\Live')
    os.mkdir('.\\IP\\Validator')
    os.mkdir('.\\MacAddress')
    os.mkdir('.\\Data')
    shutil.move('Prog_DL_List.txt'  , '.\\Downloads\\Programs\\' )
    #install module: PyAutoGUI
    subprocess.Popen('PyAutoGUI_Installer.bat')
    print('Please wait a moment... \nRequesting access to download')
    #
    import PySimpleGUI as sg
    sg.ChangeLookAndFeel('Black')
    layout = [[sg.Text('Download Access Request is Accepting...')],
                [sg.ProgressBar(2500, orientation='h', size=(20, 20), key='progbar')]]
    window = sg.Window('Creating Account (in progress)', layout, no_titlebar=True, keep_on_top=True)
    for i in range(2500):
        event, values = window.Read(timeout=0)
        window.Element('progbar').UpdateBar(i + 1)
    window.Close()
    #
    print('Download Access Accepted.')
    time.sleep(30)
    ProgressBar('1/2')
    os.remove('PyAutoGUI_Installer.bat')
    #install module: PySimpleGUI
    subprocess.Popen('PySimpleGUI_Installer.bat')
    print('Please wait a moment... \nWe\'re working on installation...\n')
    time.sleep(30)
    ProgressBar('2/2')
    os.remove('PySimpleGUI_Installer.bat')
    #
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
    OpInsDt= open('.\\Data\\Install.txt', mode='w')
    OpInsDt.write('InsDt= ' + '\'' + str(dt_string) + '\'')
    OpInsDt.close()
    pass


""" ========================== """
    ##########################
""" ========================== """


TypeCh= input('Type which version you want to install? \n1- One Device  \n2- More than 1 Device \n\n')
if TypeCh == '1':
    Main_Ins()
    NNOp = open("IS_Info.py", mode= 'w')
    NNOp.write(''' PL= []
Prog_Lst= PL''')
    NNOp.close()
    os.remove('IS - nX.py')


if TypeCh == '2':
    NN= input('Type your Nickname: ')
    if len(NN) > 0:
        Main_Ins()
        NNOp = open("IS_Info.py", mode= 'w')
        NNOp.write("NN= '" + NN + '''
PL= []
Prog_Lst= PL''')
        NNOp.close() 
        os.remove('IS - 1X.py')
    else:
        print('You didn\'t give us your Nickname.')
