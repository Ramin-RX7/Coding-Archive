print('Here you can login to your account')
print('')
print('')


from XFInfo import *
from XFRIPSCRT import *


MW=input('1- Login \n2- Forgot Password?')
if MW == '1':
        CUser    = input('Type your USERNAME or EMAIL: ')
        CPassword= input('Type your PASSWORD:          ')
        if  CUser.lower() == BEmail and CPassword == BPassword  or  CUser.lower() == BUsername and CPassword == BPassword:
            print('Welcome to your dashboard')
            from XFHidden import *

        else:
            print('Invalid request. Please re-check your USERNAME & PASSWORD.')
        
        
        
elif MW == '2':
        RFP= input('Do you relay forgot your password? \n1-Yes \n2-No \n \n')
        if RFP == '1':
            import smtplib, ssl
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "RIPSavesProg@gmail.com"
            from XFInfo import BEmail
            from XFInfo import BPassword
            receiver_email = BEmail
            EmPa = RIPSavesEmailPass
            message = """\Photossubject: this is sbj 
            It seems you forgot your password. \nYour password is:  
            """ + BPassword + """\n\n\nPlease open CHANGE file and change your password to a phrace you can remember."""
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, EmPa)
                server.sendmail(sender_email, receiver_email, message)
                
                if BSQ != None:
                    MW=input('1- Login \n2- Forgot Password?')
                if MW == '1':
                    CPassword = input('Type your USERNAME or EMAIL: ')
                    CSQ =       input('Type your PASSWORD:          ')
                    if CSQ == BSQ and CPassword == BPassword:
                        print('Welcome to your dashboard')
                        from XFHidden import *        
                    else:
                        print('Invalid Information.')
                
                if BSQ == None:
                                    MW=input('1- Login \n2- Forgot Password?')
                if MW == '1':
                    CPassword = input('Type your USERNAME or EMAIL: ')
                    if CPassword == BPassword:
                        print('Welcome to your dashboard')
                        from XFHidden import *        
                    else:
                        print('Invalid Information.')
                
                
