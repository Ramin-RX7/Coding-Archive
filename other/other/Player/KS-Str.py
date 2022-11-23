from pprint import pprint,pformat
import re
import rx7 as rx
print = rx.style.print

from win10toast import ToastNotifier
import simpleaudio as sa
sound2 = sa.WaveObject.from_wave_file('Notify2.wav')
sound3 = sa.WaveObject.from_wave_file('Notify3.wav')
toaster = ToastNotifier()
def Notify(title):
    toaster.show_toast(title,
                       " ",
                       icon_path=None,
                       duration=7,
                       threaded=True)
def Notify2():
    sound2.play()
def Notify3():
    sound3.play()




rx.cls()
import json,re
with open('Table.json') as f:
    Dic = json.load(f)["KS::Str"]

print("Choose Chapter:")
print("""
    1) Start
    2) Repeat
    3) Holiday
    4) 
    5) Toy Gift
    6) 
    7) 
    8) 
""")
Video = Dic[rx.io.selective_input("Chapter? ",[i for i in Dic.keys()])]

File = rf"E:\XXXX\other\ZzzzzzZ\Sorted\Unwatched\Kristina Sweet\Kristina Sweet ({Video['ID']}) (str{Video['Number']}).ts"
#rx.terminal.getoutput(f'"C:\\Program Files\\KMPlayer 64X\\KMPlayer64.exe" "{File}"')

print(f'"{Video["Name"]}"')
print()
if Video["Notes"]:
    print("Notes:")
    for note in Video['Notes']:
        print('    ',end='')
        print(note)
Orgasms = []
for t in Video["Orgasms"]:
    search = re.search(r"(\d\d)\.(\d\d)",t)
    minute = int(search.group(1))
    second = int(search.group(2))
    Orgasms.append(minute*60 + second)
Breaks = Video["Breaks"]
Break_times = []
for t in Breaks.keys():
    search = re.search(r"(\d\d)\.(\d\d)",t)
    minute = int(search.group(1))
    second = int(search.group(2))
    Break_times.append(minute*60 + second)
Notification_times =  Orgasms+Breaks

Timestamps = Video["Timestamps"]
total_time = 0
for nom,Chapter in enumerate(Timestamps):
    Notify(list(Chapter.values())[0])
    start = list(Timestamps[nom].keys())[0]
    try: end = list(Timestamps[nom+1].keys())[0]
    except IndexError: end = Video["Time"]
    time_str = re.search(r"(\d\d)\.(\d\d)",start)
    time_end = re.search(r"(\d\d)\.(\d\d)",end)
    minute = int(time_end.group(1))-int(time_str.group(1))
    second = int(time_end.group(2))-int(time_str.group(2))
    if second < 0:
        minute = minute-1
        second = 60+second
    print(list(Chapter.values())[0])
    time = minute*60 + second

    for i in range(time):
        rx.sleep(1)
        total_time+=1
        if total_time in Notification_times:
            if total_time in Orgasms:
                Notify2()
                Notify("Orgasm")
            elif total_time in Break_times:
                Notify3()
                for i,t in enumerate(Break_times):
                    if total_time==t:
                        print(Breaks[Breaks.keys()[i]])
                        break
print("END")
Notify("END")












