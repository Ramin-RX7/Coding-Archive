import rx7 as rx
import zipfile,os
import PySimpleGUI as sg
sg.theme('Black')
layout=[
        [sg.T('Type Archive Name: '),sg.In(background_color='LightGrey',text_color='Black',size=(37,1),key='FILENAME')],
        [sg.Button('Choose Files' ,button_type=sg.BUTTON_TYPE_BROWSE_FILES, size=(10,1)),
         sg.Button('Choose Folder',button_type=sg.BUTTON_TYPE_BROWSE_FOLDER,size=(11,1),key='FOLDER1'),
         sg.Button('Choose Folder',button_type=sg.BUTTON_TYPE_BROWSE_FOLDER,size=(11,1),key='FOLDER2'),
         sg.Button('Choose Folder',button_type=sg.BUTTON_TYPE_BROWSE_FOLDER,size=(11,1),key='FOLDER3'),],
        [sg.Button('Start',pad=((175,0),(0,0)))],    
        ]
window= sg.Window('Archive',layout)
x=True
while x:
    e,v= window.read(timeout=1000)
    if v['FOLDER1']!='':
        window['FOLDER1'].update(os.path.basename(v['FOLDER1']))
    if v['FOLDER2']!='':
        window['FOLDER2'].update(os.path.basename(v['FOLDER2']))
    if v['FOLDER3']!='':
        window['FOLDER3'].update(os.path.basename(v['FOLDER3']))
    #print(e,v)
    if e=='Start':
        if v['FOLDER1'] or v['FOLDER1'] or v['FOLDER1'] or v['Choose Files']:
            if v["FILENAME"]:
                x=False
            else:
                sg.popup('Enter Filename.')    
        else:
            sg.popup('Nothing to Add to Archive.')
window.close()



FILES= v['Choose Files'].split(';')
if v['FOLDER1']:
    FILES.append(v['FOLDER1'])
if v['FOLDER2']:
    FILES.append(v['FOLDER2'])
if v['FOLDER3']:
    FILES.append(v['FOLDER3'])
print(FILES)


if rx.file.exists(f'{v["FILENAME"]}.rx'):
    mod='a'
    rx.file.rename(v['FILENAME']+'.rx',v['FILENAME']+'.zip')
else:
    mod= 'w'

zipobj= zipfile.ZipFile(f'{v["FILENAME"]}.zip', mod)
for FILE in FILES:
    zipobj.write(FILE,os.path.basename(FILE))
#zipobj.setpassword(b'1234')
zipobj.close()
rx.file.rename(v['FILENAME']+'.zip',v['FILENAME']+'.rx')