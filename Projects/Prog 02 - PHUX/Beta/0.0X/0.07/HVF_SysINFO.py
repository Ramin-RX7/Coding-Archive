import os
import platform
SysINFO=platform.uname()
import socket
Device_Name= socket.gethostname()

import HVF_AddDevice


SysINFO_Fol= '.\\HVF\\' + Device_Name + '\\System Information\\'
OpSysINFO= open(SysINFO_Fol + 'System INFO.txt', mode= 'w', encoding='utf-8')
OpSysINFO.write(str(SysINFO))
OpSysINFO.close()
