print('This is our Web-Site registration form. \n')
Username= input('Username:')
Password= input('password:')
RePass=   input('Re-enter your Password:')
if len(Username)>=5 and Password == RePass and len(Password)>=8:
    print('Great, now you\'ve your own account.')
    print('Your username is: ' + Username + '\n' + 'Your password is:' + Password)
if len(Username)<5:
    print('Error: Username must be at least 5 characters.')
if len(Password) < 8:
    print('Error: Password must be at least 8 characters.')
if Password!=RePass:
    print('Error: Password & confirmation of it do not match.')
