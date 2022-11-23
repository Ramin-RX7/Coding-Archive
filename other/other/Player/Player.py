import json
from pprint import pprint,pformat
import os

import rx7 as rx
import PySimpleGUI as sg
import addict


rx.cls()

Main_Dir = r"E:\\XXX\\ZzzzzzZ\\Sorted"
print = rx.style.print


with open('Table.json') as f:
    Dict = json.load(f)
table = addict.Addict(Dict)
#print(table['Elsa Jean'].Movies)

sg.theme('darkblue')




while True:
    Main_Layout:list = []

    i = 0
    row = 0
    Main_Layout.append([])
    for folder in rx.files.MEMBERS.dirs_all(Main_Dir):
        if rx.files.MEMBERS.files_exactdir(folder)  and  not folder.endswith('New Folder'):
            #print(folder)
            Main_Layout[row].append(sg.Button(folder[folder.rindex('\\')+1:],size=(15,2)))
            i+=1
        if i == 3:
            i   =  0
            row += 1
            Main_Layout.append([])
    Main_Win = sg.Window('XXX',Main_Layout,resizable=True) #,size=(500,500)
    ARTIST,VALUE = Main_Win.read()
    print(f"'{ARTIST}' was selected")
    if ARTIST in ('None',None,'Exit'):
        exit()

    Videos = rx.files.MEMBERS.files_exactdir(Main_Dir+'/'+ARTIST)

    Movies:list = []
    Porns :list = []
    Anals :list = []
    Others:list = []

    for file_ in Videos:
        Basename = os.path.basename(file_).split('.')[0]
        if Basename.startswith('Movie'):
            Movies.append([sg.Button(len(Movies)+1, size=(6,1),key=f'Movie ({len(Movies)+1})')])
        elif Basename.startswith('Porn'):
            Porns.append([sg.Button(len(Porns)+1  , size=(6,1),key=f'Porn ({len(Porns)+1})')])
        elif Basename.startswith('Anal'):
            Anals.append([sg.Button(len(Anals)+1  , size=(6,1),key=f'Anal ({len(Anals)+1})')])
        else:
            Others.append([sg.Button(len(Others)+1, size=(6,1),key=f'Other({len(Others)+1})')])
    Highest = max(len(Movies),len(Porns),len(Anals),len(Others))
    for List in [Movies,Porns,Anals,Others]:
        for extra in range(Highest-len(List)):
            List.append([sg.Button(len(Movies)+1 , size=(6,1),disabled=True,button_color=('black','grey'))])

    Main_Win.Disable()

    Art_Win = True
    while Art_Win:
        Artist_Layout:list = [ 
            [sg.T('Movies',font=(1,15)),sg.T(' Porns ',font=(1,15)),sg.T(' Anals ',font=(1,15)),sg.T(' Other',font=(1,15)),],
            [sg.Col(Movies),sg.Col(Porns),sg.Col(Anals),sg.Col(Others)]
        ]

        Artist_Win = sg.Window(ARTIST,Artist_Layout)#,size=(1000,500))
        Video,Artist_Values = Artist_Win.read()
        print(Video)
        if not Video:
            Art_Win = False
        else:
            FILE = rx.files.search_file(Video+'.*',f"{Main_Dir}/{ARTIST}")[0]
            print(FILE)
            Main_Win.disappear()
            Artist_Win.disappear()
            print([Video[:Video.index('(')-1]])

            Vid_Win = True
            while Vid_Win:
                Video_Layout = []
                try:
                    #print(table.Videos[ARTIST][Video[:Video.index('(')-1]][Video[Video.index('(')+1:-1]],'red')
                    for scene in table.Videos[ARTIST][Video[:Video.index('(')-1]][Video[Video.index('(')+1:-1]]:
                        Video_Layout.append([sg.Button(scene[0],size=(15,2),key=scene[1])])
                        #print(scene,'red')
                except:
                    #raise
                    print('No Queue Found in DB')
                    Video_Layout.append([sg.T('No Queue is Provided for this video')])
                Video_Win = sg.Window(ARTIST+' - '+Video,list(Video_Layout))
                Scene,Scene_V = Video_Win.read()
                print(Scene,'green')
                print(Scene_V,'green')
                if not Scene:
                    Vid_Win=False
                else:
                    Min,Sec = str(Scene).split('.')
                    Min = Min if len(Min)==2 else '0'+Min
                    Sec = Sec if len(Sec)==2 else Sec+'0'
                    #print(Min,'green')
                    #print(Sec,'green')
                    def mv(Min,Sec,FILE):
                        rx.terminal.getoutput(f'"C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe" /startpos 00:{Min}:{Sec} "{FILE}"')
                    import threading
                    t = threading.Thread(target=mv,args=(Min,Sec,FILE))
                    t.start()
                Video_Win.close()
                del Video_Win, Video_Layout
        Artist_Win.reappear()
        Artist_Win.close()
        del Artist_Layout,Artist_Win


    Main_Win.close()
    print('End')














"""
ALl_Anals = {
    'Elsa Jean'     : {f"Elsa Jean ({str(i)})"     : False   for i in range(2,5)},
    'Emily Willis'  : {f"Emily Willis ({str(i)})"  : False   for i in range(1,6)},
    'Haley Reed'    : {f"Haley Reed ({str(i)})"    : False   for i in range(1,9)},
    'Jada Stevens'  : {f"Jada Stevens ({str(i)})"  : False   for i in range(1,6)},
    'Lana Rhoads'   : {f"Lana Rhoads ({str(i)})"   : False   for i in range(1,17)},
    'Nicole Aniston': {f"Nicole Aniston ({str(i)})": False   for i in range(1,2)},
    'Kyler Quinn'   : {f"Kyler Quinn ({str(i)})"   : False   for i in range(1,4)},
    'Mia Malkova'   : {f"Mia Malkova ({str(i)})"   : False   for i in range(1,6)},
    
    'Customs'       : {f"Custom ({str(i)})":False                          for i in range(1,10)},
    'X'             : {f"X ({str(i)})":False                          for i in range(1,4)},
}
with open('Anals.json','w') as f:
    json.dump(ALl_Anals,f,indent=4)
List_All_Anals = []
for Artist_Videos in ALl_Anals.values():
    for video in Artist_Videos.keys():
        List_All_Anals.append(video)
pprint(List_All_Anals)
"""


#"C:\Program Files\KMPlayer 64X\KMPlayer64.exe" /startpos 00:05:00 "C:\Users\Iranian\Downloads\Video\Friends S8\Friends.S08E01.1080p.PMV.mkv"
