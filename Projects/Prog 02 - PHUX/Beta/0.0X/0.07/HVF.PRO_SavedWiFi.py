import subprocess

subprocess.Popen('HVF.PRO_SavedWiFi.bat')
Wifi_Name= input('OK, Now type Wi-Fi name:  ')

OpWifi= open('HVF.PRO_ExtPass.bat', mode='w')
OpWifi.write('from \n@echo off \n>WiFiINFO.txt (\n  netsh wlan show profiles ' + Wifi_Name + ' key=clear\n)')
OpWifi.close()

subprocess.Popen('HVF.PRO_ExtPass.bat')