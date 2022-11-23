import os
import socket
Device_Name= socket.gethostname()


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


# This line is for important folders to files.
def ADD_ImpFold():
    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files')== True:
        pass
    if os.path.exists('.\\HVF\\' + Device_Name + '\\List of Files')== False:
        os.mkdir('.\\HVF\\' + Device_Name + '\\List of Files')

    if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information')== True:
        pass
    if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information')== False:
        os.mkdir('.\\HVF\\' + Device_Name + '\\System Information')

    if os.path.exists('.\\HVF\\' + Device_Name + '\\Copied Files')== True:
        pass
    if os.path.exists('.\\HVF\\' + Device_Name + '\\Copied Files')== False:
        os.mkdir('.\\HVF\\' + Device_Name + '\\Copied Files')

    return ""
print(ADD_ImpFold())