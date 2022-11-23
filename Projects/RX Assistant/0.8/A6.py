from ast import Pass
import rx7 as rx
import json

from websockets import Data

with open("db.json") as f:
    Database = json.load(f)

class WIFI:
    def connected_devices():
        Password = rx.io.wait_for_input('Enter "A6::WIFI" Password:  ')
        nex = Password.split("-")
        for nickname in nex:
            if nickname not in {**(Database["Phones"]),**(Database["Groups"])}:
                print(f"{nickname} not found in db")
                return False
        print("Yessss")
    #WIFI.connected_devices()

class Terminal:
    @staticmethod
    def pulse(seconds:int=0):
        bat = "./A6/LJ/start.bat"
        rx.write(bat,f"ping 127.0.0.1 -n {seconds+1} > nul\nexit")
        rx.terminal.run(f"start {bat}")
        # subprocess.call('python x.py', creationflags=subprocess.CREATE_NEW_CONSOLE)

