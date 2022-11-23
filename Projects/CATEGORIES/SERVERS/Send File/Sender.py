
"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse
import rx7
while True:
    SoR= input('1) Recieve   2) Send')
    if SoR=='1':
        # device's IP address
        SERVER_HOST = socket.gethostbyname(socket.gethostname())
        #SERVER_HOST = "192.168.1.101"
        SERVER_PORT = 5001
        # receive 4096 bytes each time
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"
        # create the server socket
        # TCP socket
        s = socket.socket()
        # bind the socket to our local address
        s.bind((SERVER_HOST, SERVER_PORT))
        # enabling our server to accept connections
        # 5 here is the number of unaccepted connections that
        # the system will allow before refusing new connections
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        # accept connection if there is any
        client_socket, address = s.accept() 
        # if below code is executed, that means the sender is connected
        print(f"[+] {address} is connected.")
        # receive the file infos
        # receive using client socket, not server socket
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        # remove absolute path if there is
        filename = os.path.basename(filename)
        # convert to integer
        filesize = int(filesize)
        # start receiving the file from the socket
        # and writing to the file stream
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for _ in progress:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        # close the client socket
        client_socket.close()
        # close the server socket
        s.close()
    if SoR=='2':
        SEPARATOR = "<SEPARATOR>"
        BUFFER_SIZE = 1024 * 4 #4KB
        def send_file(filename, host, port=5001):
            # get the file size
            filesize = os.path.getsize(filename)
            # create the client socket
            s = socket.socket()
            print(f"[+] Connecting to {host}:{port}")
            s.connect((host, port))
            print("[+] Connected.")
            # send the filename and filesize
            s.send(f"{filename}{SEPARATOR}{filesize}".encode())
            # start sending the file
            progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "rb") as f:
                for _ in progress:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    s.sendall(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))
            # close the socket
            s.close()


        import rx7
        Reciever_IP= input('Type Reciever IP: ')
        File=input('Enter File Address: ')
        if rx7.File(File).path:
            send_file(File, Reciever_IP) #, port
        else:
            print('File Does Not Exists.')
    
