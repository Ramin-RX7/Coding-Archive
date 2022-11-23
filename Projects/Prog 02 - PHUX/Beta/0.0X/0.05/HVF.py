import HVF_AddDevice


# This line is for main menu
def Main_Menu():
    print('OK. Start as fast as you can.')
    print('Tell us what we\'re going to do?')
    print('1- Print List of Files. \n2- Get System INFO \n3- Copy Files of a Folder   \n0- EXIT ')       #WTD means What To Do
    while True:    
        WTD= input('\n')

        if WTD== '0':
            print(quit())
            
        if WTD == '1':
            import HVF_FileList

        if WTD == '2':
            import HVF_SysINFO

        if WTD == '3':
            import HVF_CopyFiles
        return WTD
print(Main_Menu())
