import rx7 as rx
import PySimpleGUI as sg
import keyboard


settings= {}
settings['themes'] = sg.list_of_look_and_feel_values()

sg.theme('Black')

menu_layout= [
              ['File',['New','Open','Save','Save As','---','Exit']],
              ['Edit',['Undo','---','Cut','Copy','Paste','Delete','---','Find...','Replace...','---','Select All','Date/Time']],
              ['Format',['Theme', settings['themes'],'Font','Tab Size','Show Settings']],
              ['Run',['Run Module']],
              ['Help',['View Help','---','About Me']]
              ]

LAYOUT= [
         [sg.Menu(menu_layout)],
         [sg.Text('NewFile.txt',key='_FILE_',size=(100,1),font=('arial','11','bold'),text_color='gray25')],
         [sg.Multiline(default_text='', key='_BODY_', size=(110,30))],
         ]

WINDOW= sg.Window('Text Editor',LAYOUT,size=(800,400))





def open_file(window): # CTRL+O shortcut key
    ''' Open a local file in the editor '''
    try: # 'OUT OF INDEX' error in trinket if 'CANCEL' button is pressed
        filename = sg.popup_get_file('File Name:', title='Open', no_window=True)
    except:
        return
    if filename not in (None,''):
        file_text= rx.read(filename)
        window['_BODY_'].update(value=file_text)
        window['_FILE_'].update(value=filename.replace('/',' > '))
        settings.update(filename=filename, body=file_text, info=filename.replace('/',' > '))

def save_file_as(window, values):
    ''' Save the active file as another file, also called for new files '''
    try: # 'OUT OF INDEX' error in Trinket if 'CANCEL' button is clicked
        filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
    except:
        return
    if filename not in (None,''):
        with open(filename,'w') as f:
            f.write(values['_BODY_'])
        window['_INFO_'](value=filename.replace('/',' > '))
        settings.update(filename=filename, info=filename.replace('/',' > '))

def save_file(window, values): # CTRL+S shortcut key
    ''' Save active file. If new, then calls the `save_file_as` function '''
    filename = settings.get('filename')
    if filename not in (None,''):
        with open(filename,'w') as f:
            f.write(values['_BODY_'])
        window['_FILE_'](value=filename.replace('/',' > '))
        settings.update(filename=filename, info=filename.replace('/',' > '))
    else:
        save_file_as(window, values)









while True:
    e,v= WINDOW.read()

    
    keyboard.add_hotkey('ctrl + save', lambda: save_file, args=(WINDOW,v))


    if e in (None,'Exit'):
        break

    if e =='Open':
        open_file(WINDOW)

    if e=='Save':
        save_file(WINDOW, v)

    if e=='Save As':
        save_file_as(WINDOW, v)







