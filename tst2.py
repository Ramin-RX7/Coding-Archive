import rx7 as rx
#__import__('os').system('cls')

# TODO:
#   argparse

###
# time.clock() -- time.process_time()
# os.scandir() -- os.DirEntry 
































#win32api.SetFileAttributes('x.txt',win32con.FILE_ATTRIBUTE_HIDDEN)
#win32api.Beep(3000,300)
#win32clipboard.OpenClipboard()
#v= win32clipboard.GetClipboardData()
#{!!!}win32clipboard.SetClipboardText(b'heeeee')
#v = win32api.GetCommandLine()
#v = win32api.GetCurrentThreadId()
#v=win32api.GetConsoleTitle()
#v=win32api.SetConsoleTitle('sss')
#win32api.SetEnvironmentVariable(name,value)
#v= win32profile.GetAllUsersProfileDirectory()
#v= win32profile.GetProfilesDirectory()











# PolybiusSquare
# Caesar

# Polyalphabetic:	Alberti Enigma Trithemius Vigenère
# Polybius square:  ADFGVX Bifid Nihilist Tap-code Trifid VIC
# Square:           Playfair Two-square Four-square
# Substitution:     Affine Atbash Autokey Beaufort Caesar Chaocipher Great Hill Pigpen ROT13 Running-key
# Transposition:    ColumnarDoubleMyszkowskiRail fenceRoute




































































'''
def check_parentheses(s):
    """ Return True if the parentheses in string s match, otherwise False. """
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0

def find_parentheses(s):
    """ Find and return the location of the matching parentheses pairs in s.

    Given a string, s, return a dictionary of start: end pairs giving the
    indexes of the matching parentheses in s. Suitable exceptions are
    raised if s contains unbalanced parentheses.

    """

    # The indexes of the open parentheses are stored in a stack, implemented
    # as a list

    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs

test_strings = [
    'as (adjks) sdj(ds(dfsf)) fdd(dsd(dsdss(1))dsds)ddsd',
    'as (adjks) sdj(ds(dfsf) fdd(dsd(dsdss(1))dsds)ddsd',
    'as (adjks) sdj(ds(dfsf) fdddsd(dsdss(1)))dsdsddsd',
]

for Line_Nom, Text in enumerate(SOURCE, 1):
    print('\ntest string {}:\n{}'.format(Line_Nom, Text))
    print('Parentheses match?', check_parentheses(Text))
    try:
        parentheses_locs = find_parentheses(Text)
        print('Parentheses locations:\n{}'.format(str(
                    sorted([(k,v) for k, v in parentheses_locs.items()])
           )))
    except IndexError as e:
        print(str(e))
'''


































































































# IterFunc_tools
'''
from functools import reduce, partial, singledispatch

li = [5, 8, 10] 
sum = reduce((lambda x, y: x - y), li) 
#print (sum) 

def power(a, b):
    return a**b
pow2 = partial(power, b = 2)
pow4 = partial(power, b = 4)
power_of_5 = partial(power, 5)

@singledispatch
def fun(s): 
    print(str(s))
@fun.register(str)
def fun_str(s): 
    print('its str:  '  +  s * 2) 

fun('Hello') 
fun(10) 
fun(False)
#x1 = list(product('abcdefghijklmnopqrstuvwxyz', repeat = 5)) 
'''

# rename my movies
'''
import os
import rx7.lite as rx

i = 1
Dir  =  'D:/Movie/HYMIM S2'
Name =  'How I Met Your Mother'
Info =  ''
S    =  2#Dir[-1]
Ext  =  '.mkv'

for File in rx.files.MEMBERS.files_exactdir(Dir):
    
    #rx.files.rename(Dir+'/'+File, Dir+'/'+File.replace('(Official Video)',''))
    
    #Info = File.replace('.',' ')[14:-34]
    
    N = '0'+str(i) if i < 10 else str(i)

    rx.files.rename(
        Dir+'/'+File, f'{Dir}/{Name} S0{S}E{N}{" - "+Info if Info else ""}{Ext}'
        )
    
    i += 1
    
# HIMYM
'''

# Add folder to sys.path for imports
'''
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
#import HellusioX
'''

'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)         
'''



# default browser (windows)
r'''
def get_default_browser():
    from winreg import HKEY_CURRENT_USER, OpenKey, QueryValue
    with OpenKey(HKEY_CURRENT_USER,
                 r"Software\Classes\http\shell\open\command") as key:
        return QueryValue(key, None)
'''

# PEP8or
'''
from yapf.yapflib.yapf_api import FormatFile
FormatFile("rx.py", in_place=True)
import autopep8
rx.write('Hash.py',autopep8.fix_file('Hash.py'))
'''

# One upper (like msfconsole intro)


# Work for files
'''
import urllib,shutil
with urllib.request.urlopen('http://download.thinkbroadband.com/10MB.zip') as response, open("10MB.zip", 'wb') as f:
    shutil.copyfileobj(response, f)
'''

# 2 3 5 7 11 13
'''
 import sys
 def find_prime(num):
     # 2 3 5 7 11 13
     res_list = []
     for i in range(2, num + 1):
         if res_list != [] and any(i % l == 0 for l in res_list):
             continue
         res_list.append(i)
     return res_list
'''

# Folder Size
'''
 import os
 directory= 'ramin'
 dir_size = 0  # Set the size to 0
 fsizedicr = {'Bytes': 1,
              'Kilobytes': float(1) / 1024,
              'Megabytes': float(1) / (1024 * 1024),
              'Gigabytes': float(1) / (1024 * 1024 * 1024)}
 for (path, dirs, files) in os.walk(
         directory):  # Walk through all the directories. For each iteration, os.walk returns the folders, subfolders and files in the dir.
     for file in files:  # Get all the files
         filename = os.path.join(path, file)
         dir_size += os.path.getsize(filename)  # Add the size of each file in the root dir to get the total size.
 
 fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]  # List of units
 
 if dir_size == 0:
     print("File Empty")  # Sanity check to eliminate corner-case of empty file.
 else:
     for units in sorted(fsizeList)[::-1]:  # Reverse sort list of units so smallest magnitude units print first.
         print("Folder Size: " + units)
'''

'''
 from tqdm import tqdm,tqdm_gui
 for i in tqdm_gui(range(1000),'Loading'): do_step()
 ''''''
 def do_step():
     i=5;i*= i**10;i*= i**20;i*= i**20;i*= i**10
 from alive_progress import alive_bar
 items = range(1000)                  # retrieve your set of items
 with alive_bar(len(items),spinner='pulce') as bar:   # declare your expected total
     for item in items:               # iterate as usual
         # process each item
         do_step()
'''

'''
 names = [
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'LIGHT_GRAY',
    'DARK_GRAY',
    'LIGHT_RED',
    'LIGHT_GREEN',
    'LIGHT_YELLOW',
    'LIGHT_BLUE',
    'LIGHT_MAGENTA',
    'LIGHT_CYAN',
    'WHITE',
    'GREY_0',
    'NAVY_BLUE',
    'DARK_BLUE',
    'BLUE_3A',
    'BLUE_3B',
    'BLUE_1',
    'DARK_GREEN',
    'DEEP_SKY_BLUE_4A',
    'DEEP_SKY_BLUE_4B',
    'DEEP_SKY_BLUE_4C',
    'DODGER_BLUE_3',
    'DODGER_BLUE_2',
    'GREEN_4',
    'SPRING_GREEN_4',
    'TURQUOISE_4',
    'DEEP_SKY_BLUE_3A',
    'DEEP_SKY_BLUE_3B',
    'DODGER_BLUE_1',
    'GREEN_3A',
    'SPRING_GREEN_3A',
    'DARK_CYAN',
    'LIGHT_SEA_GREEN',
    'DEEP_SKY_BLUE_2',
    'DEEP_SKY_BLUE_1',
    'GREEN_3B',
    'SPRING_GREEN_3B',
    'SPRING_GREEN_2A',
    'CYAN_3',
    'DARK_TURQUOISE',
    'TURQUOISE_2',
    'GREEN_1',
    'SPRING_GREEN_2B',
    'SPRING_GREEN_1',
    'MEDIUM_SPRING_GREEN',
    'CYAN_2',
    'CYAN_1',
    'DARK_RED_1',
    'DEEP_PINK_4A',
    'PURPLE_4A',
    'PURPLE_4B',
    'PURPLE_3',
    'BLUE_VIOLET',
    'ORANGE_4A',
    'GREY_37',
    'MEDIUM_PURPLE_4',
    'SLATE_BLUE_3A',
    'SLATE_BLUE_3B',
    'ROYAL_BLUE_1',
    'CHARTREUSE_4',
    'DARK_SEA_GREEN_4A',
    'PALE_TURQUOISE_4',
    'STEEL_BLUE',
    'STEEL_BLUE_3',
    'CORNFLOWER_BLUE',
    'CHARTREUSE_3A',
    'DARK_SEA_GREEN_4B',
    'CADET_BLUE_2',
    'CADET_BLUE_1',
    'SKY_BLUE_3',
    'STEEL_BLUE_1A',
    'CHARTREUSE_3B',
    'PALE_GREEN_3A',
    'SEA_GREEN_3',
    'AQUAMARINE_3',
    'MEDIUM_TURQUOISE',
    'STEEL_BLUE_1B',
    'CHARTREUSE_2A',
    'SEA_GREEN_2',
    'SEA_GREEN_1A',
    'SEA_GREEN_1B',
    'AQUAMARINE_1A',
    'DARK_SLATE_GRAY_2',
    'DARK_RED_2',
    'DEEP_PINK_4B',
    'DARK_MAGENTA_1',
    'DARK_MAGENTA_2',
    'DARK_VIOLET_1A',
    'PURPLE_1A',
    'ORANGE_4B',
    'LIGHT_PINK_4',
    'PLUM_4',
    'MEDIUM_PURPLE_3A',
    'MEDIUM_PURPLE_3B',
    'SLATE_BLUE_1',
    'YELLOW_4A',
    'WHEAT_4',
    'GREY_53',
    'LIGHT_SLATE_GREY',
    'MEDIUM_PURPLE',
    'LIGHT_SLATE_BLUE',
    'YELLOW_4B',
    'DARK_OLIVE_GREEN_3A',
    'DARK_GREEN_SEA',
    'LIGHT_SKY_BLUE_3A',
    'LIGHT_SKY_BLUE_3B',
    'SKY_BLUE_2',
    'CHARTREUSE_2B',
    'DARK_OLIVE_GREEN_3B',
    'PALE_GREEN_3B',
    'DARK_SEA_GREEN_3A',
    'DARK_SLATE_GRAY_3',
    'SKY_BLUE_1',
    'CHARTREUSE_1',
    'LIGHT_GREEN_2',
    'LIGHT_GREEN_3',
    'PALE_GREEN_1A',
    'AQUAMARINE_1B',
    'DARK_SLATE_GRAY_1',
    'RED_3A',
    'DEEP_PINK_4C',
    'MEDIUM_VIOLET_RED',
    'MAGENTA_3A',
    'DARK_VIOLET_1B',
    'PURPLE_1B',
    'DARK_ORANGE_3A',
    'INDIAN_RED_1A',
    'HOT_PINK_3A',
    'MEDIUM_ORCHID_3',
    'MEDIUM_ORCHID',
    'MEDIUM_PURPLE_2A',
    'DARK_GOLDENROD',
    'LIGHT_SALMON_3A',
    'ROSY_BROWN',
    'GREY_63',
    'MEDIUM_PURPLE_2B',
    'MEDIUM_PURPLE_1',
    'GOLD_3A',
    'DARK_KHAKI',
    'NAVAJO_WHITE_3',
    'GREY_69',
    'LIGHT_STEEL_BLUE_3',
    'LIGHT_STEEL_BLUE',
    'YELLOW_3A',
    'DARK_OLIVE_GREEN_3',
    'DARK_SEA_GREEN_3B',
    'DARK_SEA_GREEN_2',
    'LIGHT_CYAN_3',
    'LIGHT_SKY_BLUE_1',
    'GREEN_YELLOW',
    'DARK_OLIVE_GREEN_2',
    'PALE_GREEN_1B',
    'DARK_SEA_GREEN_5B',
    'DARK_SEA_GREEN_5A',
    'PALE_TURQUOISE_1',
    'RED_3B',
    'DEEP_PINK_3A',
    'DEEP_PINK_3B',
    'MAGENTA_3B',
    'MAGENTA_3C',
    'MAGENTA_2A',
    'DARK_ORANGE_3B',
    'INDIAN_RED_1B',
    'HOT_PINK_3B',
    'HOT_PINK_2',
    'ORCHID',
    'MEDIUM_ORCHID_1A',
    'ORANGE_3',
    'LIGHT_SALMON_3B',
    'LIGHT_PINK_3',
    'PINK_3',
    'PLUM_3',
    'VIOLET',
    'GOLD_3B',
    'LIGHT_GOLDENROD_3',
    'TAN',
    'MISTY_ROSE_3',
    'THISTLE_3',
    'PLUM_2',
    'YELLOW_3B',
    'KHAKI_3',
    'LIGHT_GOLDENROD_2A',
    'LIGHT_YELLOW_3',
    'GREY_84',
    'LIGHT_STEEL_BLUE_1',
    'YELLOW_2',
    'DARK_OLIVE_GREEN_1A',
    'DARK_OLIVE_GREEN_1B',
    'DARK_SEA_GREEN_1',
    'HONEYDEW_2',
    'LIGHT_CYAN_1',
    'RED_1',
    'DEEP_PINK_2',
    'DEEP_PINK_1A',
    'DEEP_PINK_1B',
    'MAGENTA_2B',
    'MAGENTA_1',
    'ORANGE_RED_1',
    'INDIAN_RED_1C',
    'INDIAN_RED_1D',
    'HOT_PINK_1A',
    'HOT_PINK_1B',
    'MEDIUM_ORCHID_1B',
    'DARK_ORANGE',
    'SALMON_1',
    'LIGHT_CORAL',
    'PALE_VIOLET_RED_1',
    'ORCHID_2',
    'ORCHID_1',
    'ORANGE_1',
    'SANDY_BROWN',
    'LIGHT_SALMON_1',
    'LIGHT_PINK_1',
    'PINK_1',
    'PLUM_1',
    'GOLD_1',
    'LIGHT_GOLDENROD_2B',
    'LIGHT_GOLDENROD_2C',
    'NAVAJO_WHITE_1',
    'MISTY_ROSE1',
    'THISTLE_1',
    'YELLOW_1',
    'LIGHT_GOLDENROD_1',
    'KHAKI_1',
    'WHEAT_1',
    'CORNSILK_1',
    'GREY_100',
    'GREY_3',
    'GREY_7',
    'GREY_11',
    'GREY_15',
    'GREY_19',
    'GREY_23',
    'GREY_27',
    'GREY_30',
    'GREY_35',
    'GREY_39',
    'GREY_42',
    'GREY_46',
    'GREY_50',
    'GREY_54',
    'GREY_58',
    'GREY_62',
    'GREY_66',
    'GREY_70',
    'GREY_74',
    'GREY_78',
    'GREY_82',
    'GREY_85',
    'GREY_89',
    'GREY_93'
    ]
 for color in names: rx.style.print('Test 123:  '+color,BG=color.lower())
 rx.style.print('Test 123:  ','gold_1')
 rx.style.print('Test 123:  ','gold_3b')
 input()
'''

# https://host2.rj-mw1.com/media/mp3/Gdaal-Mese-Tehran-(Ft-Imanemun).mp3
# https://host2.media-rj.app/media/music_video/hq/erfan-gdaal-tanbih.mp4

'''
class Singleton():
    def __new__(cls):
        if not hasattr(cls,'__instance'):
            cls.__instance= super().__new__(cls)
        return cls.__instance
'''

# Func Logger
'''
def dec(func):
    def inside(*args, **kwargs):
        x= func(*args,**kwargs)
        Line= cf.f_lineno
        func_info= rx.read(__file__).splitlines()[Line-1]
        rx.write('log.txt',f'{func_info} --> {x} || (Line: {Line})\n',mode='continue')
        return x
    return inside

@dec
def double(nom):
    return nom*2 
@dec
def summ(nom1,nom2):
    return nom1*nom2
summ(nom1=3,nom2=4)
'''

# Get Line number
'''
from inspect import currentframe, getframeinfo
cf = currentframe()
#filename = getframeinfo(cf).filename
print ("This is line  ", cf.f_lineno)
'''


# Set registery string
r'''
import winreg
access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
access_key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,r"SOFTWARE\Microsoft\Command Processor",0,winreg.KEY_WRITE)
winreg.SetValueEx(access_key,'Autorun',0,winreg.REG_SZ,'prompt $t')

'''

# DICT CREATOR
'''
def CREATE(SS,LENGTH):
    complete_list = []
    for current in range(LENGTH):
        a = [i for i in SS]
        for y in range(current):
            a = [x+i for i in SS for x in a  if x!=i]
        complete_list = complete_list+a
    return complete_list
    #print('Number of Generated Words:  '+str(len(complete_list)))
#CREATE(['ramin','1383','xxx'],2,'tst')
for i in CREATE(['ramin','1383','xxx'],2):
    print(i)
'''

# RJ DL
'''import requests
import json
import re
from subprocess import call

def get_download_link(link):
    media_type = re.split(r'/', link)[3]
    file_name = re.split(r'/', link)[5]
    session = requests.Session()
    if media_type == "podcasts":
        response = session.get("https://www.radiojavan.com/podcasts/podcast_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/podcast/mp3-256/" + file_name + ".mp3"
    elif media_type == "mp3s":
        response = session.get("https://www.radiojavan.com/mp3s/mp3_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/mp3/" + file_name + ".mp3"
    elif media_type == "videos":
        response = session.get("https://www.radiojavan.com/videos/video_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/music_video/hq/" + file_name + ".mp4"
    else:
        return None
    return url

if __name__ == "__main__":
    link = input("Enter link: ")
    download_link = get_download_link(link)
    if download_link:
        import urllib,shutil
        with urllib.request.urlopen(download_link) as response, open(file_name, 'wb') as f:
            shutil.copyfileobj(response, f)        
    else:
        print('Sorry, unsupported link!')
'''



# MP3 Tags
'''
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
mp3 = MP3File('Bemoghash.mp3')
mp3.song = 'RX'
mp3.save()
print(mp3.get_tags())
'''
"""
Allowed tags:
    - artist;
    - album;
    - song;
    - track;
    - comment;
    - year;
    - genre;
    - band (version 2.x);
    - composer (version 2.x);
    - copyright (version 2.x);
    - url (version 2.x);
    - publisher (version 2.x).
"""
'''
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os
DIR= 'mg'
for FILE in os.listdir(DIR):
    NAME= FILE[:-4]
    mp3 = MP3File(DIR+'\\'+FILE)
    mp3.copyright = 'RX7'
    mp3.artist= 'Martin Garrix'
    
    #if '(' in NAME: mp3.song= f"{NAME[:NAME.index('(')-1]}"
    #else: mp3.song= NAME
    mp3.song= NAME

    mp3.album=''
    mp3.save()
    print(NAME)
'''


# Connected Wifi Name:
'''
import re
search= re.search(r'Profile.*', subprocess.getoutput('netsh wlan show interfaces')).group()[25:]
'''

# WF_PS (Not Mine)
'''
a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
dic={}
for i in a:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try: dic[i]=results[0]   
    except IndexError: dic[i]=''
'''

# Flush
"""import time, sys
while True:
    sys.stdout.write("\r" + str(time.time()))
    #sys.stdout.flush()"""


# Keyboard Module
'''
# Keyboard module in Python 
import keyboard 
#keyboard.add_hotkey('a', lambda: keyboard.write('Geek'))  #if a is clicked geek is typed
#keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey'))  
#keyboard.wait('esc') 
#keyboard.call_later(x,delay=3)'''

# PySimpleGUI Progressbar
'''
import PySimpleGUI as sg
sg.theme('LightGrey')
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar',bar_color=('Green','LightGrey'))],
          [sg.Cancel()]]
window = sg.Window('Custom Progress Meter', layout,no_titlebar=True,keep_on_top=True,grab_anywhere=True,resizable=True)
progress_bar = window['progressbar']
for i in range(1000):
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        break
    progress_bar.UpdateBar(i + 1)
window.close()
'''

#PySimpleGUI Mouse n Keyboard Capture
'''
import PySimpleGUI as sg
# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"
text_elem = sg.Text(size=(18, 1))
layout = [[sg.Text("Press a key or scroll mouse")],
          [text_elem],
          [sg.Button("OK")]]
window = sg.Window("Keyboard Test", layout,  return_keyboard_events=True, use_default_focus=False)
# ---===--- Loop taking in user input --- #
while True:
    event, value = window.read()
    if event == "OK" or event is None:
        print(event, "exiting")
        break
    text_elem.update(event)
'''

# Make KM in range()
r'''
import re
def Make_KM(input):
    if not re.search(r'^\d{10}$', input):
        return False

    check = int(input[9])
    s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)
noms=set()
for i in range (369999999,375000001):
    print(i)
    if Make_KM('0'+str(i)):
        noms.add(i)
write('nom',str(noms))
'''

# Win10Notifi
'''
"""
from infi.systray import SysTrayIcon
def say_hello(systray): print ("Hello, World!")
def simon(): print('hello simon')
def x(): print('x')
menu_options = (("Say Hello", None, say_hello),
                ('A sub-menu', "submenu.ico", (('Say Hello to Simon', "simon.ico", simon),
                                               ('Do nothing', None, x)))
)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()
"""
#####################
def system_tray(menu, icon, hover_text):
    from infi.systray import SysTrayIcon
    systray= SysTrayIcon(icon,hover_text,menu,)
    systray.start()
    return systray
def say_hello(systray): print ("Hello, World!")
def simon(): print('hello simon')
def x(): print('x')
menu_options = (("Say Hello", None, say_hello),
                ('A sub-menu', "submenu.ico", (('Say Hello to Simon', "simon.ico", simon),
                                               ('Do nothing', None, x)))
)
x= system_tray(menu_options,None,'myhover')
'''




