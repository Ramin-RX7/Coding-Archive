from pprint import pprint,pformat
import re
import rx7 as rx
print = rx.style.print


import json,re
with open('Table.json') as f:
    Dic = json.load(f)["Flatirons"]



ND_Dic = []
Time_Dic = {
    "Very Short":  [],
    "Short"     :  [],
    "Normal"    :  [],
    "Long"      :  [],
    "Very Long" :  [],
}
for star in Dic:
    #Star = star+": " if star != "Others" else ""
    Star = star+"::"
    for movie in Dic[star]:
        if not movie.startswith("-"):
            #print(f"{star}: {movie}")
            Name = f"{Star}{movie}"
            ND_Dic.append(Name)
            time = float(re.search(r'::(?P<time>\d+\.\d+)',movie).group('time'))
            if   time<1: Time_Dic['Very Short'].append(Name)
            elif time<2: Time_Dic['Short'].append(Name)
            elif time<3: Time_Dic['Normal'].append(Name)
            elif time<4: Time_Dic['Long'].append(Name)
            else:        Time_Dic['Very Long'].append(Name)

"""
print(f"Total      ::  {len(ND_Dic)}")
print(f'Very Shorts::  {len(Time_Dic["Very Short"])}')
print(f'Shorts     ::  {len(Time_Dic["Short"])}')
print(f'Normal     ::  {len(Time_Dic["Normal"])}')
print(f'Long       ::  {len(Time_Dic["Long"])}')
print(f'Very Long  ::  {len(Time_Dic["Very Long"])}')
#"""
#exit()



Types= ['Any','Anal','Oil','Half','Done','Long','Short']
Type= Types[0]
for nom,movie in enumerate(ND_Dic[:-1]):
    if Type == 'Anal'  and  'Anal' not in movie:
        ND_Dic[nom] = ""
    elif Type == 'Oil'   and  'Oil' not in movie:
        ND_Dic[nom] = ""
    elif Type == 'Long':
        try: length = re.search(r'.*::.*::(?P<LENGTH>\d+\.\d+)',movie).group('LENGTH')
        except: print(movie);print('ERROR');raise
        if float(length) < 2.00:
            ND_Dic[nom] = ""
    elif Type == 'Short':
        try: length = re.search(r'.*::(?P<LENGTH>\d+\.\d+)',movie).group('LENGTH')
        except: print(movie);print('ERROR');raise
        if float(length) >= 2.00:
            ND_Dic[nom] = ""
ND_Dic = [movie for movie in ND_Dic if movie]

#print(ND_Dic)
print(rx.random.choose(ND_Dic))











"""
Dict = []

Positions = {
    'h': 'Hashti',
    'c': 'Cowgirl',
    'r': 'Reverse-Cowgirl',
    'd': 'Doggy-Style',
    's': 'Suck',
    'x': 'X',
    'm': 'Missionary',
    'f': 'Fingering',
    'sh': 'Show',
    'al':'Ass-Licking',
    'sp':'Spoon',
    'cs':'Cumshot',
    'cp':'Creampie',
    'mv':'Movie'
}
import json
with open('Table.json') as f:
    Dic = json.load(f)

for pornstar in list(Dic['Flatirons'].keys())[4:]:
    new_vid_list = []
    for video in Dic['Flatirons'][pornstar]:
        txt = f'{pornstar}::{video}'
        lngth = input(f"{txt}{' '*(30-len(txt))}:  ")
        new_val = video+'::'+lngth#.replace('.',':')
        #Dic['Flatirons'][pornstar].remove(video)
        new_vid_list.append(new_val)
    Dic['Flatirons'][pornstar] = list(new_vid_list)
    print(Dic['Flatirons'][pornstar])
    #break

with open('Flatirons.json','w') as f:
    json.dump(Dic,f,indent=4)
"""




'''
while True:
    name = input('NAME:  ')
    time = input('TIME:  ')
    if not time or not name:
        print(Dict)
    else:
        Dict.append((Positions[name],float(time)))
    print()
'''
"""
Khaabide : Flatiron - Snake
7 : G-Whiz - Seashell - Valedictorian
"""




