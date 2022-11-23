import socket,os,rx

Device_Name= socket.gethostname()+' - '+rx.system.accname()
def ADD_DEVICE():
    if os.path.exists('.\\F\\' + Device_Name)== True:
        pass

    if os.path.exists('.\\F\\' + Device_Name)== False:
        print('Please wait a second \nAdding this device to our files...')
        if os.path.exists('.\\F') == True:
            os.mkdir('.\\F\\' + Device_Name)
        if os.path.exists('.\\F') == False:
            os.mkdir('.\\F')
            os.mkdir('.\\F\\' + Device_Name)
            print('Device has been successfully added.\n')
ADD_DEVICE()

def ADD_ImpFold():

    LoF_Fol= '.\\F\\' + Device_Name + '\\List of Files\\'
    if os.path.exists(LoF_Fol)== True:
        pass
    if os.path.exists(LoF_Fol)== False:
        os.mkdir(LoF_Fol)

    CopFil_Fol= '.\\F\\' + Device_Name + '\\Copied Files'    
    if os.path.exists(CopFil_Fol)== True:
        pass
    if os.path.exists(CopFil_Fol)== False:
        os.mkdir(CopFil_Fol)

    Wifi_Fol= '.\\F\\' + Device_Name + '\\Wifi'
    if os.path.exists(Wifi_Fol)== True:
        pass
    if os.path.exists(Wifi_Fol)== False:
        os.mkdir(Wifi_Fol)
ADD_ImpFold()
