import os
import socket
Device_Name= socket.gethostname()


WTC= input(r'Type ADDRESS of where you want to list it files:' + '\n')  #WTC means where to copy
if len(WTC) == 1:
    WTC = WTC.upper() + ':\\'

if os.path.exists(WTC) == True:  

    if os.path.exists('.\\List of Files')== True:
        if os.path.exists('.\\List of Files\\' + Device_Name) == True:
        
            with open(".\\List of Files\\" + Device_Name + "\\List Of Files (2).txt", "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(WTC):
                    for file in f:
                        filewrite.write(f"{r + file}\n")
        elif os.path.exists('.\\List of Files\\' + Device_Name) == False:
            os.mkdir('.\\List of Files\\'+Device_Name)
            
            with open(".\\List of Files\\" + Device_Name + "\\List Of Files.txt", "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(WTC):
                    for file in f:
                        filewrite.write(f"{r + file}\n")  
    else:
        os.mkdir('.\\List of Files')
        os.mkdir('.\\List of Files\\'+Device_Name) 
            
        with open(".\\List of Files\\" + Device_Name + "\\List Of Files.txt", "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTC):
                for file in f:
                    filewrite.write(f"{r + file}\n")

    #count= 0
    #for line in open(r'E:\Coding\Prog 4 - Hack Via USB\0.1\List of Files\RaminRX\List of Files.txt').readlines(): count += 1
    #print(count)
    
else:
    ('Sorry. We could\'nt find this directory.')


