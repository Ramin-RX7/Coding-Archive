from XFInfo import *

WC= input('Type what you want to change? (PASSWORD - EMAIL - EyeColor)')    #WC means What to Change?

if WC== 'PASSWORD':
    print('Please enter a PASSWORD with at least 8 CHARACTERS.')
    print('Note that CAPITAL LETTERS Are important.')
    NP =  input('Type  your  NEW  PASSWORD: ')  #NP  means New Password
    CNP=  input('Re-Type your NEW PASSWORD: ')  #CNP means Check New Password
    if NP == CNP and len(NP) >= 8:
        print('PASSWORD has been changed Successfully.')
        ope= open('XFInfo.py', mode='w')
        ope.write('BUsername= ' + '\'' + BUsername + '\'' + '\n'
                  'BPassword= ' + '\'' + NP        + '\'' + '\n'
                  'BEmail= '    + '\'' + BEmail    + '\'' + '\n'
                  'BSQ= '       + '\'' + BSQ       + '\'' + '\n')
        ope.close()
    elif NP != CNP and len(NP) < 8:
        print('PASSWORD & RE-ENTER are not same. \nPASSWORD must be at least 8 CHARACTERS.')
    elif NP != CNP:
        print('PASSWORD & RE-ENTER are not same.')
    elif len(NP) < 8:
        print('PASSWORD must be at least 8 CHARACTERS.')



elif WC== 'EMAIL':
    NE =  input('Please enter your NEW EMAIL: ')
    CNE=  input('Re-type your NEW EMAIL:      ')
    import re
    NECon=re.search(r'[\w.]+@+[\w.]+', NE)
    
    if NE==CNE and NECon!=None:
        print('EMAIL has been changed Successfully.')
        ope= open('XFInfo.py', mode='w')
        ope.write('BUsername= ' + '\'' + BUsername  + '\'' + '\n'
                  'BPassword= ' + '\'' + BPassword  + '\'' + '\n'
                  'BEmail= '    + '\'' + NE.lower() + '\'' + '\n'
                  'BSQ= '       + '\'' + BSQ        + '\'' + '\n')        
        ope.close()
    elif NE != CNE and NECon == None:
        print('EMAIL is invalid. \n Email & RE-ENTER are not same.')
    elif NE != CNE:
        print('EMAIL & RE-ENTER are not same.')
    elif NECon == None:
        print('EMAIL is invalid.')



elif WC== 'EyeColor':
    print('Note that CAPITAL LETTERS Are important.')
    NSQ =  input('Please enter your NEW SEQURITY ANSWER: ')
    CNSQ=  input('Re-type your NEW SEQURITY ANSWER:      ')
   
    if NSQ==CNSQ and len(NSQ)<=12 and len(NSQ)>=3 :
        print('Your SEQURITY ANSWER has been changed Successfully.')
        ope= open('XFInfo.py', mode='w')
        ope.write('BUsername= ' + '\'' + BUsername  + '\'' + '\n'
                  'BPassword= ' + '\'' + BPassword  + '\'' + '\n'
                  'BEmail= '    + '\'' + BEmail     + '\'' + '\n'
                  'BSQ= '       + '\'' + NSQ        + '\'' + '\n') 
        ope.close()
    elif NSQ != CNSQ or len(NSQ)>12 or len(NSQ) < 3:
        print('Color is invalid. \n SEQURITY ANSWER & RE-ENTER are not same.')
    elif NSQ != CNSQ:
        print('SEQURITY ANSWER & RE-ENTER are not same.')
    elif len(NSQ)>12 or len(NSQ)<3:
        print('Color is invalid.')    

else:
    print('Invalid request.')




        






