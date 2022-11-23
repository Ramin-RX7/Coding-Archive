import socket
Device_Name= socket.gethostname()

OpWifi= open('.\\HVF\\' + Device_Name + '\\F\\System Info', mode='w')
OpWifi.write('@echo off \n>SystemINFO(PRO).txt (\n  systeminfo\n)')
OpWifi.close()
#import time
#time.sleep(2)
import subprocess
subprocess.Popen('.\\HVF\\' + Device_Name + '\\PRO\\System INFO\\System Info (PRO).bat')
