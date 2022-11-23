import os
import socket
Device_Name= socket.gethostname()


WTC= input(r'Type ADDRESS of where you want to list it files:' + '\n')  #WTC means where to copy
if len(WTC) == 1:
    WTC = WTC.upper() + ':\\'

if os.path.exists(WTC) == True:

    if os.path.exists('.\\HVF') == True:
        if os.path.exists('.\\HVF\\' + Device_Name)== True:
            if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files' == True:  
                if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files\\List Of Files.txt') == True:
                
                    with open(".\\HVF\\" + Device_Name + "\\List of Files\\List Of Files (2).txt", "w", encoding="utf-8") as filewrite:
                        for r, d, f in os.walk(WTC):
                            for file in f:
                                filewrite.write(f"{r + file}\n")


                if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files\\List of Files.txt') == False:

                    with open(".\\HVF\\" + Device_Name + "List of Files\\List of Files.txt", "w", encoding="utf-8") as filewrite:
                        for r, d, f in os.walk(WTC):
                            for file in f:
                                filewrite.write(f"{r + file}\n")


            if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files' == False: 
                os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')
            
                with open(".\\HVF\\" + Device_Name + '\\List of Files\\List of Files.txt', "w", encoding="utf-8") as filewrite:
                    for r, d, f in os.walk(WTC):
                        for file in f:
                            filewrite.write(f"{r + file}\n")


        if os.path.exists('.\\HVF\\' + Device_Name)== False:
            os.mkdir('.\\HVF\\' + Device_Name)
            os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')

            with open(".\\HVF\\" + Device_Name + '\\List of Files\\List of Files.txt', "w", encoding="utf-8") as filewrite:
                for r, d, f in os.walk(WTC):
                    for file in f:
                        filewrite.write(f"{r + file}\n")


    if os.path.exists('.\\HVF') == False:
        os.mkdir('.\\HVF\\')
        os.mkdir('.\\HVF\\' + Device_Name)
        os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')

        with open(".\\HVF\\List of Files" + Device_Name + "\\List of Files.txt", "w", encoding="utf-8") as filewrite:
            for r, d, f in os.walk(WTC):
                for file in f:
                    filewrite.write(f"{r + file}\n")

    #=========================
    #We have to add a tool to count number of files.
    #=========================
    
    #count= 0
    #for line in open(r'E:\Coding\Prog 4 - Hack Via USB\0.1\List of Files\RaminRX\List of Files.txt').readlines(): count += 1
    #print(count)
    
else:
    ('Sorry. We could\'nt find this directory.')
