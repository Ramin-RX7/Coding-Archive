print('Here you can login to your account')
print('')
print('')



from XFInfo import *
CUser    = input('Type your USERNAME or EMAIL: ')
CPassword= input('Type your PASSWORD: ')
if CUser == BEmail and CPassword == BPassword  or  CUser == BUsername and CPassword == BPassword:
    print('Welcome to your dashboard')
    from XFHidden import *
else:
    print('Invalid request. Please re-check your USERNAME & PASSWORD.')
    FG=input('Forgot your password? Type YES to sign in with your sequrity question.')    
    if FG== 'YES':      #FG means FORGOT YOUR PASSWORD?
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
        print(quit())
