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

    LoF_Fol= '.\\HVF\\' + Device_Name + '\\List of Files\\'
    if os.path.exists(LoF_Fol)== True:
        pass
    if os.path.exists(LoF_Fol)== False:
        os.mkdir(LoF_Fol)

    SysINFO_Fol= '.\\HVF\\' + Device_Name + '\\System Information'
    if os.path.exists(SysINFO_Fol)== True:
        pass
    if os.path.exists(SysINFO_Fol)== False:
        os.mkdir(SysINFO_Fol)

    CopFil_Fol= '.\\HVF\\' + Device_Name + '\\Copied Files'    
    if os.path.exists(CopFil_Fol)== True:
        pass
    if os.path.exists(CopFil_Fol)== False:
        os.mkdir(CopFil_Fol)
    return ""
print(ADD_ImpFold())

def ADD_PRO():
    PRO_Fol= '.\\HVF\\' + Device_Name + '\\PRO'
    if os.path.exists(PRO_Fol)== True:
        pass
    if os.path.exists(PRO_Fol)== False:
        os.mkdir(PRO_Fol)

    PROWifi_Fol= '.\\HVF\\' + Device_Name + '\\PRO\\Wifi'
    if os.path.exists(PROWifi_Fol)== True:
        pass
    if os.path.exists(PROWifi_Fol)== False:
        os.mkdir(PROWifi_Fol)
    
    PROSysINFO_Fol= '.\\HVF\\' + Device_Name + '\\PRO\\System INFO\\'
    if os.path.exists(PROSysINFO_Fol)== True:
        pass
    if os.path.exists(PROSysINFO_Fol)== False:
        os.mkdir(PROSysINFO_Fol)
    return ""
print(ADD_PRO())

