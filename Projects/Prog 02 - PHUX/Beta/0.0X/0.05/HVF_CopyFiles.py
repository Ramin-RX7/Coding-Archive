import os
import shutil
import socket
Device_Name= socket.gethostname()

import HVF_AddDevice


print('please do not try to copy files with HIGH sizes.')
WTC= input(r'Type ADDRESS of where you want to copy it\'s files:' + '\n')
if len(WTC) <=3:
    print('We could\'t copy this file(s).')

if os.path.exists(WTC) == True:
    import glob
    for filename in glob.glob(os.path.join(WTC, '*.*')):
        shutil.copy(filename, '.\\HVF\\' + Device_Name + '\\Copied Files')
    #We can use code below instead of code above to copy
    """src_files = os.listdir(WTC)
    for file_name in src_files:
        full_file_name = os.path.join(WTC, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, '.\\HVF\\' + Device_Name + '\\Copied Files')"""

if os.path.exists(WTC) == False:
    print('Sorry. We could\'nt find this directory.')

"""src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)"""