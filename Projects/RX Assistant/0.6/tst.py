import rx7 as rx
rx.clear()

'''
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
spot_client = Client(base_url="https://testnet.binance.vision")
#print(spot_client.avg_price("XRPUSDT"))
#print(spot_client.ticker_price("XRPUSDT"))
'''

#db9e2f07dfbd47bd2b1cc7db0496903168521d2174d758c050857202ff16c7a5

"""
import pyttsx3
engine = pyttsx3.init()
engine.say("btc is 19100")
engine.runAndWait()
"""

"""
#GENIUS_ACCESS_TOKEN
#73bgnCCuLsZPdjuE5vF4PRwvJr69Kw3lPiizgSQ-HOxOWYX7kVRBhYKwtDuZM57y
import lyricsgenius
genius = lyricsgenius.Genius("73bgnCCuLsZPdjuE5vF4PRwvJr69Kw3lPiizgSQ-HOxOWYX7kVRBhYKwtDuZM57y")
genius.verbose = False
song = genius.search_song("ads;fjasf;jsaklf;afj",)
print(song.lyrics)
#song.save_lyrics('lyrics.json',overwrite=True)
"""

def check_if_on_pc():
    import pyautogui,keyboard
    afk = 0
    ms = pyautogui.position()
    while True:
        keyboard.start_recording()
        if pyautogui.position() == ms:
            #print("No mouse move")
            afk +=1
        else:
            #print("mouse moved")
            ms = pyautogui.position()
            afk = 0
        rx.sleep(1)
        if keyboard.stop_recording():
            #print("keyborad moved")
            afk = 0
        else:
            #print("no keyboard move")
            afk +=1
        if afk >= 5:
            print("Not doing anything for 5s")
            exit()
#check_if_on_pc()
def count_10():
    while True:
        x,y = rx.random.choose(range(1,10),2)
        print(x*y)
        rx.sleep(1)




import threading
c10 = threading.Thread(target=count_10)
ciopc = threading.Thread(target=check_if_on_pc)

c10.start()
ciopc.start()


