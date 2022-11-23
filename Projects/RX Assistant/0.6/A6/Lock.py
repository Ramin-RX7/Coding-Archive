import hashlib
import rx7 as rx
fp_module = rx.import_module('./A6/Lib/FP/fingerprint.py')

def Login():
    while True:
        try:
            rx.cls()
            myFP = fp_module.FingerPrint()
            myFP.open()
            # myFP.identify()
            print("[?] Please Touch the Fingerprint Sensor")
            if myFP.verify():
                print("True")
                rx.files.remove("./A6/Lock.ini","file")
                break
            else:
                print("[-] Wrong Finger Input",'red')
                rx.wait(0.51)
        except KeyboardInterrupt:
            break
        except OSError as e:
            print(e)
            input("press enter")
            print("[*] Couldn't Detect Finger; Please Try Again",'dodger_blue_1')
            rx.wait(0.52)
        except Exception as E:
            print(E)
            input("press enter")
        finally:
            myFP.close()
    
    return True

Login()
