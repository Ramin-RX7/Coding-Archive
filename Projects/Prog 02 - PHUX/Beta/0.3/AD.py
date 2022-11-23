import socket,os,rx7

Device_Name= socket.gethostname()+' - '+rx7.system.accname()
def ADD_DEVICE():
    if not os.path.exists('.\\F\\' + Device_Name):
        print('Please Wait a Second \nAdding This Device to our Files...')
        if not os.path.exists('.\\F'):
            os.mkdir('.\\F')
        os.mkdir('.\\F\\' + Device_Name)
        print('Device Has Been Successfully Added.\n')
ADD_DEVICE()

'''
def ADD_ImpFold():
    LoF_Fol= '.\\F\\' + Device_Name + '\\List of Files\\'
    if not os.path.exists(LoF_Fol):
        os.mkdir(LoF_Fol)

    CopFil_Fol= '.\\F\\' + Device_Name + '\\Copied Files'    
    if not os.path.exists(CopFil_Fol):
        os.mkdir(CopFil_Fol)
ADD_ImpFold()
'''