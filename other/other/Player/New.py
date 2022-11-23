from pprint import pprint,pformat
import re
import rx7 as rx
print = rx.style.print

import json,re


with open('Table.json') as f:
    Dic = json.load(f)

LIST = [
"KS::Str",
"KS::OutOfStr",
"KS::NoStr",
"Emma Hix",
"Others"
]

Types = [LIST[0]]
Tryst = True
VIDEO_LENGTH = "Normal"  

Data = {Type:Dic[Types] for Type in Types} if Types  else {lname:Dic[lname] for lname in LIST}
LENGTH = 0
for Type in Data:
    LENGTH += len(list(Data[Type].keys()))
required_timestamps = [""]

def choose():
    SELECTION = rx.random.integer(1,LENGTH)
    # print(f"{SELECTION} is selected")
    i = 0
    for Type in Data:
        for vid in Data[Type]:
            i+=1
            if i == SELECTION:
                try:
                    if Tryst and  not Data[Type][vid]["Tryst"]:
                        choose()
                        break
                    timestamps = Data[Type][vid]["Timestamps"]
                    for section in required_timestamps:
                        
                    print(f"{SELECTION} is approved")
                    print(vid)
                    pprint(Data[Type][vid])
                    break
                except KeyError:
                    choose()
                    break

choose()







"""
KS::Str       =  10
KS::OutOfStr  =  6
KS::NoStr     =  30
Emma Hix      =  13
Others        =  31
"""



