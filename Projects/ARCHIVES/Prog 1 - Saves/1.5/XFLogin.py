print('Here you can login to your account')
print('')
print('')


from XFInfo import *

while True:
    MW=input('1- Login \n2- Forgot Password?')
    if MW == '1':
        CUser    = input('Type your USERNAME or EMAIL: ')
        CPassword= input('Type your PASSWORD:          ')
        if CUser.lower() == BEmail and CPassword == BPassword  or  CUser.lower() == BUsername and CPassword == BPassword:
            print('Welcome to your dashboard')
            from XFHidden import *

        else:
            print('Invalid request. Please re-check your USERNAME & PASSWORD.')
        
        
        
    elif MW == '2':
        print('Now you can use your sequrity question to login.')
        ASQ= input('What is your eye color?')   #ASQ is ANSWER of Sequrity question.
        if ASQ == BSQ:
            print('Welcome to your Dashboard \n at first change your PASSWORD')
            from XFHidden import *
        else:
            print('Oops! Even you forgot your eyes color!')
            print('Well this is your last chance to login')
            print('Now you most know both of your USERNAME and EMAIL')
            FU= input('Type your username: ')       #FU means USERNAME when user forgot Password
            EU= input('Type your EMAIL: ')          #EU means EMAIL    when user forgot Password
            if FU==BUsername  and  EU==BEmail:
                print('Welcome to your Dashboard.')
                print('Remember that you login WITHOUT PASSWORD. Change your PASSWORD now.')
                from XFHidden import *
            else:
                print('We\'re sorry. You can\'t login to your account. :|') 
                print('Best way is trying agsin later and if even you couldn\'t remember then, you can delete your account and data from CHANGE.py file.')