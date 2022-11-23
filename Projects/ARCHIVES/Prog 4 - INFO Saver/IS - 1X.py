import os
import subprocess
import socket
hostname = socket.gethostname()
import pyautogui

print('Welcome ' + hostname + '!')
LoginRd = open(".\\Data\\Login.txt", mode= 'r')
LoginRdd= LoginRd.read()
LoginOp = open(".\\Data\\Login.txt", mode= 'w')
LoginOp.write(LoginRdd + 'X')
LoginOp.close()
LoginNom= len(LoginRdd) + 1

clear = lambda: os.system('cls')  #Only on Windows System

while True:
    print('Choose where are you going to?')
    MC= input('''10- Launch Programs \n11- Program Download(Pack) \n21- IP (Pack) \n22- Mac Address finder \n31-Date & Time (Pack)
90- Clear Data \n91- Data\n\n''')
    #21 - 22 - 31 - 11 - 10 - 90 - 91
    if MC=='21':
        IP_Pack = input('1-Live IP \n2-IP Validator \n\n')

        if IP_Pack == '1':
            IPAddr = socket.gethostbyname(hostname)   
            print("Your Computer IP Address is:" + IPAddr)

            IpLvRd = open(".\\IP\\Live\\IP.txt", mode= 'r')
            IpLvRdd= IpLvRd.read()
            from datetime import datetime
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y - %H:%M:%S :  ")
            IpLvOp = open(".\\IP\\Live\\IP.txt", mode= 'w')
            IpLvOp.write(IpLvRdd + '\n' + dt_string + IPAddr)
            IpLvOp.close() 

        if IP_Pack == '2':
            import re
            regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

            def check(Ip):
                if(re.search(regex, Ip)):  
                    print("Valid Ip address")  
                    IpVldtRd = open(".\\IP\\Validator\\IP.txt", mode= 'r')
                    IpVldtRdd= IpVldtRd.read()
                    IpVldtOp = open(".\\IP\\Validator\\IP.txt", mode= 'w')
                    IpVldtOp.write(IpVldtRdd + '\n' + Ip + ': VALID \n')
                    IpVldtOp.close()                    
                else:  
                    print("Invalid Ip address") 
                    IpVldtRd = open(".\\IP\\Validator\\IP.txt", mode= 'r')
                    IpVldtRdd= IpVldtRd.read()
                    IpVldtOp = open(".\\IP\\Validator\\IP.txt", mode= 'w')
                    IpVldtOp.write(IpVldtRdd + '\n' + Ip + ': INVALID \n')
                    IpVldtOp.close()  
            # 
            if __name__ == '__main__' :
                IP = input('Type IP Address: ')
                check(IP)

        
    elif MC == '22':
        import uuid
        MacIF= hex(uuid.getnode()) 
        print (MacIF)

        import uuid 
        print ("In formatted way is : ", end="") 
        MacF= ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
        for ele in range(0,8*6,8)][::-1])
        print (MacF)    
        """MacAdrsRd = open(".\\MacAddress\\Address.txt", mode= 'r')
        MacAdrsRdd= IpVldtRd.read()"""
        #import socket
        #Device_Name= socket.gethostname()
        MacAdrsOp = open(".\\MacAddress\\Address.txt", mode= 'w')
        MacAdrsOp.write(MacIF + '  -  ' + MacF)
        MacAdrsOp.close()         
        """import re, uuid  
        print ("The MAC address in formatted and less complex way is : ", end="") 
        print (':'.join(re.findall('..', '%012x' % uuid.getnode())))"""


    elif MC == '31':
        DnT= input('1- Live Date & Time \n2-Days passed from a date \n\n')
        if DnT== '1':
            from datetime import datetime
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Date and Time: ", dt_string)

            LvTmRd = open(".\\Date_Time\\Live\\Live.txt", mode= 'r')
            LvTmRdd= LvTmRd.read()
            LvTmOp = open(".\\Date_Time\\Live\\Live.txt", mode= 'w')
            LvTmOp.write(LvTmRdd + '\n' + dt_string)
            LvTmOp.close()
        
        elif DnT == '2':
            from datetime import date
            print('Type date of first date below.')
            D=int(input('Type Day:   '))
            M=int(input('Type Month: '))
            Y=int(input('Type Year:  '))
            f_date = date(Y, M, D)

            LTCh= input('1- Custome Date \n2- Live Date \n\n')
            if LTCh == '1':
                LD=int(input('Type Day:   '))
                LM=int(input('Type Month: '))
                LY=int(input('Type Year:  '))
                l_date = date(LY, LM, LD)
                delta = l_date - f_date
                print(delta.days)
                print(delta)

            elif LTCh == '2':
                from datetime import datetime
                now = datetime.now()
                LD= int(now.strftime('%d'))
                LM= int(now.strftime('%m'))
                LY= int(now.strftime('%Y'))
                f_date = date(Y, M, D)
                l_date = date(LY, LM, LD)
                delta = l_date - f_date
                print('\n\n')
                print(str(delta.days        ) + '  Days')
                print(str(delta.days * 24   ) + '  Hours')
                print(str(delta.days * 1440 ) + '  Minutes')    
                print(str(delta.days * 86400) + '  Seconds')
                print('\nAre passed from  '+ str(f_date) + '  Until  ' + str(l_date))

            else:
                print('Invalid Choice.')
        else:
            print('There is no choice with this number')


    elif MC == '11':
        def AddProg_Dl2Lst(Prog_Name, Category):
            from datetime import datetime
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            AdProg2LstRd = open(".\\Downloads\\Programs\\Prog_DL_List.txt", mode= 'r')
            AdProg2LstRdd= AdProg2LstRd.read()
            AdProg2LstOp = open(".\\Downloads\\Programs\\Prog_DL_List.txt", mode= 'w')
            AdProg2LstOp.write(AdProg2LstRdd+'In '+dt_string+' -  '+Category+':        '+Prog_Name+'  Was downloaded.\n')
            AdProg2LstOp.close()
            pass

        def AddProg_Name2Lst(ProgName):
            AdProgName2LstRd = open(".\\IS_Info.py", mode= 'r')
            AdProgName2LstRdd= AdProgName2LstRd.read()
            AdProgName2LstOp = open(".\\IS_Info.py", mode= 'w')
            AdProgName2LstOp.write(AdProgName2LstRdd + "+ ['" + ProgName + "']")
            AdProgName2LstOp.close()
            pass

        def AddProg_2Lnch(ProgName):
            print('We\'re waiting for you to install the app...')
            FlLct= input('Please give us ' + ProgName + 'file location.')
            if os.path.exists(FlLct) == True:
                OpProgBat= open('.\\Downloads\\Programs\\' + ProgName + '_St.bat', mode='w')
                OpProgBat.write('''start "" "'''+ FlLct + '\\' + ProgName +'''.exe"''')
                OpProgBat.close()
            else:
                print('Wrong location.')
                AddProg_2Lnch(ProgName)

        print('There are some categories here. Choose which you want?')
        ProgCh= input('1- VPN \n\n')
        if ProgCh == '1':
            WhVPN= input('What VPN you want to download? \n1- Proton VPN \n2- Windscribe \n3- Psiphon \n4- X VPN \n\n')

            if WhVPN == '1':
                Proton_VPN= 'http://download1322.mediafire.com/ycn8vdtv6rhg/65oz2w4zwq008py/ProtonVPN_win_v1.10.1.exe'
                import webbrowser
                webbrowser.open_new_tab(Proton_VPN)
                AddProg_Dl2Lst('Proton_VPN','VPN')
                AddProg_Name2Lst('Proton_VPN')
                print('Browser is opening... \n')
                print('PROTON VPN  is going to download...\n')
                AddProg_2Lnch('ProtonVPN')
            if WhVPN == '2':
                Windscribe= 'http://download1235.mediafire.com/h78e96aqn01g/vhj0i83xbezaqjr/Wi.ndscr.ibe.exe'
                import webbrowser
                webbrowser.open_new_tab(Windscribe)
                AddProg_Dl2Lst('Windscribe','VPN')
                AddProg_Name2Lst('Windscribe')
                print('Browser is opening... \n')
                print('WINDSCRIBE  is going to download...\n')
                AddProg_2Lnch('Windscribe')
            if WhVPN == '3':
                Psiphon= 'http://download2262.mediafire.com/0t67g11szoig/0ufj0a6jpw3rbqu/psiphon3.exe'
                import webbrowser
                webbrowser.open_new_tab(Psiphon)
                AddProg_Dl2Lst('Psiphon','VPN')
                AddProg_Name2Lst('Psiphon')
                print('Browser is opening... \n')
                print('PSIPHON  is going to download...\n')
                print('Psiphon does not need to install.')
                AddProg_2Lnch('Psiphon')
            if WhVPN == '4':
                X_VPN= 'http://download1492.mediafire.com/8u4n1ml8bl9g/2wcupmgj21n73kg/X-VPN_Installer41.0_322.exe'
                import webbrowser
                webbrowser.open_new_tab(X_VPN)
                AddProg_Dl2Lst('X_VPN','VPN')
                AddProg_Name2Lst('X_VPN')
                print('Browser is opening... \n')
                print('X VPN  is going to download...\n')                     
                AddProg_2Lnch('X_VPN')


    elif MC == '10':
        print('Ok. Which Program are going to launch? \n')
        W2Open= input('1- Proton VPN \n2- Windscribe \n3-Psiphon \n4- X VPN')
        if W2Open == '1':
            if os.path.exists('.\\Downloads\\Programs\\ProtonVPN_St.bat') == True:
                subprocess.Popen('.\\Downloads\\Programs\\ProtonVPN_St.bat')
                
                Screen_Size= pyautogui.size()
                Sc_Width= Screen_Size[0]
                Sc_Height= Screen_Size[1]
                pyautogui.moveTo(Sc_Width/6.09,Sc_Height/2.65)
                import time
                time.sleep(1)
                #Start
                pyautogui.click()
                #Minimize
                pyautogui.moveTo(Sc_Width/1.43,Sc_Height/12)
                pyautogui.click()
                print('Proton VPN is connecting...')
            else:
                print('Something is wrong. \nMaybe you didn\'t give us program location or location is wrong or even you didn\'t download it!')
        elif W2Open == '2':
            if os.path.exists('.\\Downloads\\Programs\\Windscribe_St.bat') == True:
                subprocess.Popen('.\\Downloads\\Programs\\Windscribe_St.bat')
                import pyautogui
                Screen_Size= pyautogui.size()
                Sc_Width= Screen_Size[0]
                Sc_Height= Screen_Size[1]
                pyautogui.moveTo(Sc_Width/1.72,Sc_Height/2.38)
                import time
                time.sleep(5)
                #Start
                pyautogui.click()
                time.sleep(1)
                #Minimize
                pyautogui.moveTo(Sc_Width/1.776,Sc_Height/1.71)
                pyautogui.click()
                print('Windscribe is connecting...')
            else:
                print('Something is wrong. \nMaybe you didn\'t give us program location or location is wrong or even you didn\'t download it!')
        elif W2Open == '3':
            if os.path.exists('.\\Downloads\\Programs\\Psiphon_St.bat') == True:
                subprocess.Popen('.\\Downloads\\Programs\\PsiphonVPN_St.bat')
            else:
                print('Something is wrong. \nMaybe you didn\'t give us program location or location is wrong or even you didn\'t download it!')
        elif W2Open == '4':
            if os.path.exists('.\\Downloads\\Programs\\X_VPN_St.bat') == True:
                subprocess.Popen('.\\Downloads\\Programs\\X_VPN_St.bat')
            else:
                print('Something is wrong. \nMaybe you didn\'t give us program location or location is wrong or even you didn\'t download it!')
        else:
            print('Wrong choice.')


    elif MC == '90':
        print('You\'re here to clear your data.')
        ClCh= input('1- Live IP \n2-Valid IP \n3- Mac Address \n4-Live Date and Time \n5-Passed Days \n6- Programs Download List \nX- All\n\n')

        if ClCh == '1':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\IP\\Live\\IP.txt", mode= 'w')
                IpLvOp.write('')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        elif ClCh == '2':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\IP\\Validator\\IP.txt", mode= 'w')
                IpLvOp.write('')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        elif ClCh == '3':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\MacAddress\\Address.txt", mode= 'w')
                IpLvOp.write('')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        elif ClCh == '4':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\Date_Time\\Live\\Live.txt", mode= 'w')
                IpLvOp.write('')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        elif ClCh == '5':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\Date_Time\\Passed\\Passed.txt", mode= 'w')
                IpLvOp.write('')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        if ClCh == '6':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                IpLvOp = open(".\\Downloads\\Programs\\Prog_DL_List.txt", mode= 'w')
                IpLvOp.write('Date		       -  Category    Name\n\n')
                IpLvOp.close()
                print('Data has been deleted just now!')
            else:
                pass

        if ClCh.lower() == 'x':
            YN= input('Are you sure about deleting your data? Yes/No    ')
            if YN.lower == 'yes':
                YNLst= input('This can\'t be recovered. Yes/No     ')
                if YNLst.lower() == 'yes':
                    IpLvOp = open(".\\IP\\Live\\IP.txt", mode= 'w')
                    IpLvOp.write('')
                    IpLvOp.close()
                    IpLvOp = open(".\\IP\\Validator\\IP.txt", mode= 'w')
                    IpLvOp.write('')
                    IpLvOp.close()  
                    IpLvOp = open(".\\MacAddress\\Address.txt", mode= 'w')
                    IpLvOp.write('')
                    IpLvOp.close()
                    IpLvOp = open(".\\Date_Time\\Live\\Live.txt", mode= 'w')
                    IpLvOp.write('')
                    IpLvOp.close()
                    IpLvOp = open(".\\Date_Time\\Passed\\Passed.txt", mode= 'w')
                    IpLvOp.write('')
                    IpLvOp.close()
                    IpLvOp = open(".\\Downloads\\Programs\\Prog_DL_List.txt", mode= 'w')
                    IpLvOp.write('Date		       -  Category    Name\n\n')
                    IpLvOp.close()
                    print('Data has been deleted just now!')
                else:
                    pass
            else:
                pass


    elif MC == '91':
        print('Device Name: ' + hostname)
        print('Login times: ' + LoginNom)
        pass


    else:
        print('There is no panel with this choice. (This message is error because of you or wrong codes!)\n\n')
