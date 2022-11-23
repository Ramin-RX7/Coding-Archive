import socket
import time

def Start():
    import subprocess
    subprocess.Popen('.\\GMsLOG\\install1.bat')
    import time
    time.sleep(1)
    import os

def internet(host="8.8.8.8", port=53, timeout=3):

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

        print('Connecting...')
        Start()
    except socket.error as ex:
        print('You are not connected to internet!')
        time.sleep(3)
internet()






