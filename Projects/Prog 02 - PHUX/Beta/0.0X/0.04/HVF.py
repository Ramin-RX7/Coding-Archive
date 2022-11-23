import os
import socket
Device_Name= socket.gethostname()

# This line is for adding device to files.
def ADD_DEVICE():
    if os.path.exists('.\\HVF\\' + Device_Name)== True:
        pass

    if os.path.exists('.\\HVF\\' + Device_Name)== False:
        print('Please wait a second, We\'re adding this device to our files.')
        if os.path.exists('.\\HVF') == True:
            os.mkdir('.\\HVF\\' + Device_Name)
        if os.path.exists('.\\HVF') == False:
            os.mkdir('.\\HVF')
            os.mkdir('.\\HVF\\' + Device_Name)
            print('Device has been successfully added.')
    return ""
print(ADD_DEVICE())



def ADD_ImpFold():
    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files')== True:
        pass
    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files')== False:
        os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')

    if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information')== True:
        pass
    if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information')== False:
        os.mkdir('.\\HVF\\' + Device_Name + '\\System Information')
    return ""
print(ADD_ImpFold())



print('OK. Start as fast as you can.')
print('Tell us what we\'re going to do?')
WTD= input('1- Print List of Files. \n0- EXIT \n\n')       #WTD means What To Do

if WTD== '0':
    print(quit())
    
if WTD == '1':
    import HVF_FileList

if WTD == '2':
    import HVF_SysINFO

""" if WTD == '3':
    import """
  
