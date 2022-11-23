import os
import platform
SysINFO=platform.uname()
import socket
Device_Name= socket.gethostname()


if os.path.exists('.\\HVF') == True:
    if os.path.exists('.\\HVF\\' + Device_Name)== True:
        if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information') == True:

            OpSysINFO= open(".\\HVF\\" + Device_Name+ "\\System Information\\System INFO.txt", mode= "w", encoding="utf-8")
            OpSysINFO.write(SysINFO)
            OpSysINFO.close()

        if os.path.exists('.\\HVF\\' + Device_Name + '\\System Information') == False:
            os.mkdir('.\\HVF\\' + Device_Name + '\\System Information')

            OpSysINFO= open(".\\HVF\\" + Device_Name+ "\\System Information\\System INFO.txt", mode= "w", encoding="utf-8")
            OpSysINFO.write(SysINFO)
            OpSysINFO.close()


    if os.path.exists('.\\HVF\\' + Device_Name)== False:
        os.mkdir('.\\HVF\\' + Device_Name)
        os.mkdir('.\\HVF\\' + Device_Name + '\\System Information')

        OpSysINFO= open(".\\HVF\\" + Device_Name+ "\\System Information\\System INFO.txt", mode= "w", encoding="utf-8")
        OpSysINFO.write(SysINFO)
        OpSysINFO.close()

if os.path.exists('.\\HVF') == False:
    os.mkdir('.\\HVF\\')
    os.mkdir('.\\HVF\\' + Device_Name)
    os.mkdir('.\\HVF\\' + Device_Name + '\\System Information')

    OpSysINFO= open(".\\HVF\\" + Device_Name+ "\\System Information\\System INFO.txt", mode= "w", encoding="utf-8")
    OpSysINFO.write(str(SysINFO))
    OpSysINFO.close()