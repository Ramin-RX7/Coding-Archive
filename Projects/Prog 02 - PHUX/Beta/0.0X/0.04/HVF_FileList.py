import os
import socket
Device_Name= socket.gethostname()

from HVF import ADD_DEVICE
from HVF import ADD_ImpFold

print('Remember that you have to ADD this DEVICE to our files with just opening HVF file.')
WTL= input(r'Type ADDRESS of where you want to list it files:' + '\n')  #WTL means Where To List it files
if len(WTL) == 1:
    WTL = WTL.upper() + ':\\'

if os.path.exists(WTL) == True:
    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files\\List of Files (2).txt') == True: 
        with open(".\\HVF\\" + Device_Name + "\\List of Files\\List Of Files (3).txt", "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTL):
                for file in f:
                    filewrite.write(f"{r + file}\n")

    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files\\List of Files.txt') == True: 
        with open(".\\HVF\\" + Device_Name + "\\List of Files\\List Of Files (2).txt", "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTL):
                for file in f:
                    filewrite.write(f"{r + file}\n")


    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files\\List of Files.txt') == False:
        with open(".\\HVF\\" + Device_Name + "List of Files\\List of Files.txt", "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTL):
                for file in f:
                    filewrite.write(f"{r + file}\n")


    """if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files') == False: 
        os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')
                
        with open(".\\HVF\\" + Device_Name + '\\List of Files\\List of Files.txt', "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTL):
                for file in f:
                    filewrite.write(f"{r + file}\n")"""



    #=========================
    #We have to add a tool to count number of files.
    #=========================
    
    #count= 0
    #for line in open(r'E:\Coding\Prog 4 - Hack Via USB\0.1\List of Files\RaminRX\List of Files.txt').readlines(): count += 1
    #print(count)
    
else:
    ('Sorry. We could\'nt find this directory.')
