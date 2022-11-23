import os
import shutil


if os.path.exists('C:\\RIP\\Programs\\Saves\\') == True:
    pass

elif os.path.exists('C:\\RIP\\Programs\\') == True:
    os.mkdir('C:\\RIP\\Programs\\Saves\\')


elif os.path.exists('C:\\RIP\\') == True:
    os.mkdir('C:\\RIP\\Programs\\')
    os.mkdir('C:\\RIP\\Programs\\Saves\\')


elif os.path.exists('C:\\RIP\\') == False:
    os.mkdir('C:\\RIP\\')
    os.mkdir('C:\\RIP\\Programs\\')
    os.mkdir('C:\\RIP\\Programs\\Saves\\')





shutil.copy('XFLogin.py'  , 'C:\\RIP\\Programs\\Saves\\')
shutil.copy('XFForm.py'   , 'C:\\RIP\\Programs\\Saves\\')
shutil.copy('XFChange.py' , 'C:\\RIP\\Programs\\Saves\\')

shutil.move('XFHidden.py', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\')
shutil.move('XFSVTXT.py', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\')
shutil.move('XFSVNOM.py', 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\')




#os.remove('setup.py')
