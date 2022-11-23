import os
import shutil
import subprocess

Src= 'C:\\RIP\\Programs\\Saves\\'
if os.path.exists(Src) == True:
    pass

elif os.path.exists('C:\\RIP\\Programs\\') == True:
    os.mkdir(Src)


elif os.path.exists('C:\\RIP\\') == True:
    os.mkdir('C:\\RIP\\Programs\\')
    os.mkdir(Src)


elif os.path.exists('C:\\RIP\\') == False:
    os.mkdir('C:\\RIP\\')
    os.mkdir('C:\\RIP\\Programs\\')
    os.mkdir(Src)



PyLibSv= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES'
if os.path.exists(PyLibSv) == True:
    pass

if os.path.exists(PyLibSv) == False:
    os.mkdir(PyLibSv)
    
 
PyLibSvPhts= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Photos'      
if os.path.exists(PyLibSvPhts) == True:
    pass

if os.path.exists(PyLibSvPhts) == False:
    os.mkdir(PyLibSvPhts)


PyLibSvVids= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Videos'
if os.path.exists(PyLibSvVids) == True:
    pass

if os.path.exists(PyLibSvVids) == False:
    os.mkdir(PyLibSvVids)
    


PyLibSvFls= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files'
if os.path.exists(PyLibSvFls) == True:
    pass

if os.path.exists(PyLibSvFls) == False:
    os.mkdir(PyLibSvFls)



shutil.copy('XFLogin.py'  , Src)
shutil.copy('XFForm.py'   , Src)
shutil.copy('XFChange.py' , Src)



PyLib= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\'
shutil.move('XFHidden.py', PyLib)
shutil.move('XFSVTXT.py' , PyLib)
shutil.move('XFSVNOM.py' , PyLib)
shutil.move('XFRIPSCRT.py' , PyLib)


subprocess.Popen('PySimpleGUI_install.bat')


#os.remove('PySimpleGUI_Install.bat')
#os.remove('setup.py')