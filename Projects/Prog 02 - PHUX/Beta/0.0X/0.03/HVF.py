print('OK. Start as fast as you can.')
print('Tell us what we\'re going to do?')
WTD= input('1- Print List of Files. \n0- EXIT \n\n')       #WTD means What To Do

if WTD== '0':
    print(quit())
    
if WTD == '1':
    from HVF_FileList import *

if WTD == '2':
    from HVF_SysINFO import *