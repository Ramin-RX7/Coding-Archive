import re



PyLib= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\'


print('This is our Web-Site registration form. \n')
print('For logging in you need USERNAME or EMAIL and PASSWORD.')
print('If you forgot your PASSWORD you can use your Email to RECOVER or CHANGE your PASSWORD.')
print('Don\'t share your EMAIL! There\'s a way to login to your account with just USERNAME & PASSWORD')
print('Answer of SECURE QUESTION is another way to login.')
print('\n')


Username= input('Username: ')
Email=    input('Email: ')
ECon=     re.search(r'[\w.]+@+[\w.]+', Email)       #ECon is for Checking that Email is real or not.
Password= input('password: ')
RePass=   input('Re-enter your Password: ')         #RePass is re entering Password for checking correct.
Email= Email.lower()
Username= Username.lower()

TFA= input('Do you want to have 2 factor authentication? \n1-Yes \n2-No \n\n')
if TFA == '1':
    SQ= input('What is your eye color?')
    if len(Username)>=5 and Password == RePass and len(Password)>=8 and ECon != None and len(SQ) >=3:
        print('Great, now you\'ve your own account.')
        print('Your username is: ' + Username)
        print('Your password is: ' + Password)
        print('Your Email is: '    + Email)
        print('Your eye color is: '+ SQ)

    crinfo = open(PyLib + 'XFInfo.py', mode= 'w')
    crinfo.write('BUsername= ' + '\'' + Username + '\'' +'\n'+
                 'BPassword= ' + '\'' + Password + '\'' +'\n'+
                 'BEmail= '    + '\'' + Email    + '\'' +'\n'+
                 'BSQ= '       + '\'' + SQ       + '\'' )
    crinfo.close()

if TFA == '2':
    if len(Username)>=5 and Password == RePass and len(Password)>=8 and ECon != None:
        print('Great, now you\'ve your own account.')
        print('Your username is: ' + Username)
        print('Your password is: ' + Password)
        print('Your Email is: '    + Email)

    crinfo = open(PyLib + 'XFInfo.py', mode= 'w')
    crinfo.write('BUsername= ' + '\'' + Username + '\'' +'\n'+
                 'BPassword= ' + '\'' + Password + '\'' +'\n'+
                 'BEmail= '    + '\'' + Email    + '\'' +'\n'+
                 'BSQ= '       + 'None' )
    crinfo.close()


if ECon == None:
    print('Error: Email is invalid.')

if len(Username)<5:
    print('Error: Username must be at least 5 characters.')

if len(Password) < 8:
    print('Error: Password must be at least 8 characters.')

if Password!=RePass:
    print('Error: Password & confirmation of it do not match.')



    
'''
crinfo.close()
crrinfo= open('info.py', mode= 'r')
print(crrinfo.read())
''' #we can use this part instead of first 'IF' (Largest 'IF').
print(quit())
