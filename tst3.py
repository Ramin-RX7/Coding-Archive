import rx7 as rx






























"""
cis.tehvp.xyz:800
nl.tehvp.xyz:555
nl2.tehvp.xyz:555
nl3.tehvp.xyz:555
fn.tehvp.xyz:555
fn2.tehvp.xyz:800
fn3.tehvp.xyz:800
fr.tehvp.xyz:555
ca.tehvp.xyz:800
"""




"""
وکیل - بهجت آباد - 500 - 09124076986

یاسین - ولیعصر - 1000 - 02166468003
    تهران چهارراه ولیعصر خ برادران مظفر جنوبی کوچه خواجه نصیر پلاک ۴ خوابگاه یاسین

اردشیر - انقلاب - 600 - 02166177840

رادمان - فاطمی - 1200 - 02188990851
    خیابان دکتر فاطمی، نرسیده به وزآرت کشور، خیابان علیزآده(5)، پلاک 12

دمساز - انقلاب - 800 - 02166700499

الوند - دروازه دولت - 660 - 02177517207 - 09187976091

مجلل - میدان جهاد - 800 - 02188557922

سبحان - ستارخان کاشانیپور - 320 - 02144207420

برج شیشه ای - قائم مقام - 900 - 09124371173


#famir0912 526 8513


آرتام - 850
صادقیه - - 800 - 
آریا - 800

آریانا - امیریه - 420*2 - 02166953411

قائم2 - هفت تیر - 650*2 - 02188306532
    ميدان هفت تير خيابان ايرانشهر خيابان اذرشهر پلاك ١٦

ویلا - میدون فردوسی - 2*500 - 02188913420
"""

"""
پاییزان - ولیعصر
ویلا - انقلاب
قائم 2 - هفت تیر
توحید - توحید
ایزد - نواب
ارغوان - شهرک غرب
محمودیه - محمودیه
آریانا - ولیعصر
آریاک - ولیعصر
دمساز - ولیعصر
صدرا - هفت تیر
دکتر فاطمی - انقلاب
"""
































































# Sort Dict by value
'''
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])
'''

# Different ways to test multiple flags at once in Python
'''
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')
# These only test for truthiness:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')
'''

# Merge 2 Dicts
'''
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
'''

#.format()
"""
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
>>> '{:,}'.format(1234567890)
'1,234,567,890'
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
"""


#Youbit
'''
"""
from youbit import Encoder
with Encoder('C:/Users/Iranian/Desktop/tst.py') as encoder:
    path = encoder.encode('C:\\Users\\Iranian\\Desktop')  # Saves output in 'C:/mydirectory'. Defaults to current working directory.
    print(path)
"""
"""
from youbit import Encoder
with Encoder('C:/Users/Iranian/Desktop/json.hpp') as encoder:
    encoder.encode()
    print("encoded")
    url = encoder.upload(browser='chrome')  # Extract cookies from Opera browser
    print("uploaded")
    print(url)
"""

#import youbit.util
#print(youbit.util.b64_to_dict("gASVhgAAAAAAAAB9lCiMDG9yaWdpbmFsX01ENZSMIGEyMmYzNTZiODBjMGI0MjBkODdjZjllYmJhMmE1NWE1lIwIZmlsZW5hbWWUjAZ0c3QucHmUjApyZXNvbHV0aW9ulE2AB004BIaUjANicHCUSwGMCnplcm9fZnJhbWWUiYwLZWNjX3N5bWJvbHOUSyB1Lg=="))
#exit()

"""from youbit import Decoder
with Decoder('C:/Users/Iranian/Desktop/YOUBIT-tst.py/video.mp4') as decoder:
    path = decoder.decode(
        'C:/Users/Iranian/Desktop/YOUBIT-tst.py/',  # Save output in 'C:/mydirectory'. Defaults to current working directory.
        ecc = 32,  # The 'ecc' value that was used during encoding.
        bpp = 1,  # The 'bpp' value that was used during encoding.
        zero_frame = False  # Whether or not 'zero frames' were used during encoding.
    )
    print(path)
"""
"""
from youbit import Decoder
with Decoder('https://youtu.be/tk6SmFWrPME') as decoder:
    decoder.download()
    print("Downloaded")
    path = decoder.decode('C:/Users/Iranian/Desktop/')  # Save output in 'C:/mydirectory'. Defaults to current working directory.
    print("decoded")
    print(path)
"""
'''


# Google Drive
"""
from Google import Create_Service

CLIENT_SECRET_FILE = "XXX"
API_NAME =  "drive"
API_VERSION = "v3"
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

'''
# Create Dir
dir_names = ['tst1',"tst2"]
for dir_name in dir_names:
    file_metadata = {
        'name':dir_name,
        'mimeType':"application/vnd.google-apps.folder",
    }
    service.files().create(body=file_metadata).execute()
#'''

'''
# Upload File
from googleapiclient.http import MediaFileUpload
folder_id = ""
file_names = []
mime_types = []
for f_name,f_type in zip(file_names,mime_types):
    file_metadata = {
        'name':f_name,
        'parent':[folder_id],
    }
    media = MediaFileUpload(f_name,mimetype=f_type)
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
#'''
"""


# Spotdl Music Download Dir
"""
Dic= rx.read('music.txt').split('\n')
for line in Dic:
    if not line: continue
    artist,album,url = line.split('::')
    rx.files.mkdir(f'./{artist}/{album}')
    print('ok')
    rx.terminal.run(f'spotdl -o "./{artist}/{album}" {url}')
"""


# Tiktok DL
"""
import pyautogui
#print(pyautogui.position())
rx.wait(0.25)
Date = input('Enter Date:  ')
pyautogui.hotkey('win','down')
pyautogui.click(x=907,y=491)
pyautogui.typewrite(f'Downloads\\Video\\2020-{Date}.mp4')
pyautogui.press('enter')
rx.wait(1)
while True:
    if rx.pixel_color(646, 636) == (24, 26, 27):
        break
rx.wait(0.5)
pyautogui.click(970, 470)
pyautogui.press('right',3)
pyautogui.press('enter')
"""


#List of Apps/Repositories
"""
#] APPS:
 #> Metasploit
 #> Nmap
 #> Git
 #> Sherlock
 #> SET
 #> Hashcat
 #> John

#] Repo:
 #> design-patterns-for-humans
 #> pure-bash-bible
 #> LaZagne (Credentials recovery project)
 #> Clone-Wars
 #> Ciphey (Automatically decrypt encryptions without knowing the key or cipher)
"""


