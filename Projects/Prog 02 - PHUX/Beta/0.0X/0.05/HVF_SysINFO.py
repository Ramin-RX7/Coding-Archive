import os
import platform
SysINFO=platform.uname()
import socket
Device_Name= socket.gethostname()

import HVF_AddDevice


OpSysINFO= open(".\\HVF\\" + Device_Name+ "\\System Information\\System INFO.txt", mode= "w", encoding="utf-8")
OpSysINFO.write(SysINFO)
OpSysINFO.close()
