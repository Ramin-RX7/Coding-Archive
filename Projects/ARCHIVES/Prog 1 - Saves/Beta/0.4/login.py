print('Here you can login to your account')
print('')
print('')

from info import *
CUser    = input('Type your USERNAME or EMAIL: ')
CPassword= input('Type your PASSWORD: ')
if CUser == BEmail and CPassword == BPassword  or  CUser == BUsername and CPassword == BPassword:
    print('Welcome to your Dashboard')
else:
    print('Invalid request. Please re-check your USERNAME & PASSWORD.')
    FG=input('Forgot your password? Type YES to sign in with your sequrity question.')
        if FG== 'YES'
        FGA= input('What is your eye color?')
                if FGA == BSQ:
                    print('Welcome to your Dashboard \n at first change your PASSWORD')
                else:
                    print('Oops! Even you forgot your eyes color!')
        else:
             print(quit())
