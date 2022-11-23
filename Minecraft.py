import rx7 as rx
import pyautogui
import re
from selenium.webdriver import Chrome

print = rx.style.print

MODS_BASE_URL = "https://www.curseforge.com/minecraft/mc-mods"
DEFAULT_CF_CODE_PREFIX = "2020709689%3A"
VERSION_CF_CODE = {
    "1.18"  :   "8830",
    "1.18.1":   "8857",
    "1.18.2":   "9008",
    "1.19"  :   "9186",
    "1.19.1":   "9259",
    "1.19.2":   "9366"
}
LATEST = "1.19.2"



def download_mods(mod_names,version=LATEST):
    if type(mod_names) == list:
        mod_names = map(lambda x:x.lower(),mod_names)
    else:
        mod_names = [mod_names.lower()]

    version_code = VERSION_CF_CODE[version]
    
    browser = Chrome(r"C:\Users\Iranian\Downloads\Programs\chromedriver.exe")
    browser.maximize_window()
    dl_links = []
    skip = []
    for mod_name in mod_names:
        if mod_name in skip: continue
        print(f'[*] Checking "{mod_name}"','blue')
        url = f"{MODS_BASE_URL}/{mod_name}/files/all?filter-game-version={DEFAULT_CF_CODE_PREFIX}{version_code}"
        browser.get(url)
        source = browser.page_source
        source = source.split('\n')
        for line in source:
            if '<a data-action="file-link' in line:
                # print(line)
                code = re.match(r'.+files/(?P<FILE_CODE>.+)">',line).group('FILE_CODE')
                print(f'[+] Code has been found: "{code}"','green')
                dl_url = f"{MODS_BASE_URL}/{mod_name}/download/{code}/file"
                dl_links.append(dl_url)
                # print(f"    {dl_url}")
                # print('[+] File is being downloaded','green')
                break
        else:
            print("Error",'red')
            # rx.write("./tst.html","\n".join(source))
        print()
    for link in dl_links:
        browser.get(link)
        print("downloading..")
        pyautogui.moveTo(622,990)
        while True:
            if rx.pixel_color() == (110, 112, 115):
                pyautogui.click(500,1000)
                break
        rx.sleep(1)

    rx.sleep(30)
    browser.quit()

rx.cls()
Mods = {
    "Performance": ["sodium","lithium","phosphor"],
    "Building":  ["worldedit","litematica"],
    "Necessary": ["fabric-api","modmenu",'malilib'],
    "Visuals" :  ["lambdynamiclights"],
    "Tweaks"  :  ["minihud","tweakeroo"],
}
Main_Mods = {
    "Performance": ["dynamic-fps","fps-reducer","dashloader","bobby"],
    "Building" : ["kleeslabs-fabric"],
    "Tweak" : ["mouse-tweaks","tweakermore","fabric-bedrock-miner","item-scroller","mouse-wheelie",
               "betterf3","zoomify","easiervillagertrading"],
    "Communication": ["simple-voice-chat","dont-clear-chat-history","multiplayer-server-pause-fabric"],
    "Visuals": ["clear-despawn-fabric"],
    "Developing": ["spark"]
}

To_Download = []
for modlist in Main_Mods.values():  To_Download.extend(modlist)
download_mods(To_Download,"1.18.2")

Other_Mods = {
    "gilded-netherite",   # 1.18.2
    "gildedarmor"     ,   # 1.18.2 | 1.19
    "compress-em"     ,   # 1.18.2 | 1.19
    "golden-hoppers"  ,   # 1.18.2
    "speedy-hoppers"  ,   # 1.18.2
    "uppers"          ,   # 1.18.2 | 1.19
    "chisels-bits-for-fabric", # 1.18.2
    "indium",
    "ambientsounds",
    "vein-mining-fabric", # 1.18.x
    "immersive-portals-mod",
    "enchanting-infuser-forge",
    "pick-up-notifier",
    "tiny-skeletons-forge",
    "visual-workbench",
    "easy-magic",
    "universal-enchants-forge",
    "physics-mod",
    "presence-footsteps"
    "clumps"
}












































# Minecraft AFK
"""
import pyautogui
from pydirectinput import keyDown,keyUp,click,press,moveRel
rx.sleep(3)
t = rx.record()
while True:
    n = rx.random.integer(10,15)
    press('w',interval=0,presses=n)
    pyautogui.moveRel(170,0,duration=2)
    m = rx.random.integer(3,10)
    print(f"Waiting for {m} seconds")
    rx.sleep(m)
    if t.lap(False) > 30:
        exit()
"""
#Video Settings AFK
"""
Size= 1920,1080
Options: 750,625
    Video Settings: 625,475
        Graphics:        625,175
        Smooth Lighting: 625,250
        FPS: 1004,350
        Entity Shadow: 1275,425
        Dynamic Light: 625,575
        Details: 625,750
        Animations: 625,850
            Off: 800,925
            On:  475,925
"""
"""
import pyautogui
from pydirectinput import keyDown,keyUp,click,press,moveRel
Positions = {
    "Options":(39,58),
        "Video Settings":(32.5,44),
        "Graphics":(32.5,16),
        "Smooth Lighting": (32.5,23),
        "Entity Shadow": (66.5,40),
        "Dynamic Lights": (32.5,53),
        "Details": (32.5,70),
        "Animations": (32.5,79),
        "Animations::On":  (24.5,85.5),
        "Animations::Off": (41.5,85.5)
}
Bars = {
    "Max FPS": (52.3,30)
}
width,height = pyautogui.size()

def get_percent(rn,full):
    return (rn/full)*100
def calculate_pos(key):
    return (int((width/100)*Positions[key][0]),int((height/100)*Positions[key][1]))
def click_section(key,clicks=1):
    rx.sleep(0.5)
    pyautogui.moveTo(calculate_pos(key))
    rx.sleep(0.5)
    pyautogui.click(clicks=clicks)
#print(get_percent(475,width))
#print(calculate_pos("Entity Shadow"))
#print(pyautogui.position())
#pyautogui.moveTo(1004,325)

rx.sleep(3)
#"""
#press("esc")
#click_section('Options')
#click_section('Video Settings')
#click_section('Graphics',clicks=2)
#"""
#586415103














































"""
3:

    Home:   1371 71 -426 (NP: 190 -55)
    Fortress:  520 71 -315
    Fortress:  -55 37 -410
    End Portal: 544 70 -1977
    
    End Gateways:
        -951  47 -281
        -1845 62 -1075
        241   62 2330

    Farms:
        Slime:  7660 -1200    (NP: 975 -145)
        Gold:   0 -400
        Raid:   2200 -700

    Enchantments:
        Unbreaking 3
        Mending
        P4
        E5
        Infinity
        Looting 3
        Feather Falling 4
        Silk Touch
	Channeling


    House Designs:
        Kloof Road Masterpiece
        h3 / 314
        dupli casa    

"""



"""
Always around but I hide 'cause I'm better off
====================
We're all flames in the fire that keeps burning
We're inviting... the night in
Welcome, oh my heart's so full
I'm devoting myself to the night
There's no motive
We're just listening
We're existing
====================
Even though it hurts I can't slow down
Walls are closing in and I hit the ground
With there's no tomorrow echo in my mind
Just one last time
====================
چرا نمیمیری؟
یه روز کینه ها جلوی مردم کوه میشن
فرهاد رو دیدن داشت جای کوه گور میکند
فرهاد گورکن
بالاخره یه تونل پیدا میشه همه توش میرن
خوشحال شدن تهش نور دیدن
خوشحال شدن تهش نور دیدن ولی چراغ قطاری بود که داشت با سرعت عبور میگرد 
چرا نمیمیری؟
====================
This vicious cycle spins and spins
It picks back up where it begins
====================
بگو کجایی دادا؟ ما هنوز همینجاییم
زیر همین زمین هاییم به این خاک دچاریم دادا 
بد مالیدی دادا دیدی باد و طوفانه
گفتی ما میریم بابا د بگو کجایی دادا
====================
We bend until we break
Stand by and watch us all go up in flames
====================
Beyond the lights of society
That were killing me, quietly
Now I found myself, I found myself a home
====================
All this you give
Is why you suppose to live first
Stuck in a phase
(Is guided/misguided) by mistakes
====================
You're a wanderer just like me
Yeah you better know where you're going
====================



"""





"""
https://vanillatweaks.net/share/#Y0vaSp
Sur2:
    Home Loc       :    -295 68 -51
    Village1,Spawn :    -208 79 -150
    Village2       :    -1057 65 -398
    Cave1          :    -295 78 -143
        Station1:  -275 66 -140
    Cave2:              -415  0   -363
    Cave BL     :       -150 3700
    Spawner1(Zombie):   -300 -20 -70
    Spawner2(Zombie):   -204  -2 -185
    Spawner3(Skeleton): -177 -38 -219 
    Spawner4(Spider):   -117 -37 -204
    Spawner5(Spider):   -137 -42 -152
    Spawner6(Spider):   -75  -32 -176
    Spawner7(CSpider):  -486 -44  239
    Spawner8(Cspider):  -73  -2   -33
    Spawner9(Spider) :  -420 -14  -165
    Spawner10(Zombie):  -631 -15  -525
    Spawner11(Spider):  -131  14  3665
    Mineshaft1     :    -423 63 556
    Mineshaft2     :    -67  -9  -172
    Pillager Outpost:   1550  63  197

    NETHER:
      Nether Portal  :      /  -44  51 8
      Nether Wastes  :    -145  60  -60
      Soul sand valley:   -135  59  -259
      Bastion Remnant :   -380  86  90

    END:
      Gateways: 970  60 287
                1865 59 375
                2112 61 1474
                70 -1900
      Cities:
      	  3900 63 1000 (4)
      	  1650 65 950
      End Portal:: {ow= -1580,37,515 / nether=/-198,42,71
      End Gateway:: {main->others=  / others->main=695,69,941}
      860,59,738

"""


"""
Resource Pack:
    Aesthetic:
        Black Nether Bricks
    Terrain:
        Bushy Leaves
        Wavy Leaves
        Wavy Water
        Brighter Nether
    Variation:
        Variated Bookshelves
    Peace And Quiet:
        Piston
    Utility:
        Sticky Piston
        Directional Hopper
        Directional Dispencer Dropper
        Brewing Guide
    3D:
        Bookshelves

Data Packs:
    Mobs:
        More Mob Heads
    Utility:
        Item Average
"""

"""
Nether Portal Coords
Workstation Highlights
Items:
  Redstone totaion Wrench
  Player Head Drop
  Terracota Rotation Wrench
Mobs:
  Villager Death Mesasage
  More Mob Heads
RP:
Endless Endrods
Variation:
  Bookshelf
Peace:
  Piston
  Dispenser
Utility:
  Diminishing Tools
  Hunger Preview
  Sticky Piston Sides
  Dispenser
  Observer
  Groovy Levers
  Redstone Power Levels
Unobstructive:
  Lower Shield
  No Fog
  Translucent SpyGlass
3D:
  Bookshelf
  Ladder
  Rails
  Doors
  StoneCutter
  TrapDoors
GUI:
  Dark UI
Fun:
  What

"""
"""
Tweakeroo:
  Chestplate/Elytra Switcher
  Fast Right Click (and Blacklist)
  Fast Block Placement
  Auto Switch Mining
  Free Camera
  Death Coordinates
  Block Randomizer
  Hand Restock
  Shulker Inventory
  Elytra Camera (W/ GeneralKey)
  Breaking Restriction
  Fake Sneak
  After Clicker
  Breaking Grid
  Periodic Attack
  Fake Sneak Placement
  Swap Broken Tools
  Flexible Block Rotation (Half)
  Flexible Block Placement Offset
  Disable Offhand Rendering
  Zoom
  Disable Fog
  Item Unstacking Protection
  Hold Use Key (Interval & Duration)
  Portal Inventory Close
  Placement Grid
  Disable Particles
  Fly Speed
  Map Preview
  Persistant Chat
  Disable Wall Unsprint

Item Scroller:
  Move All Same Blocks: Alt+Click
  Move All Blocks: Alt+Shift+Click
  Drop All Same: Ctrl+Shift+Q
  Craft: <>

Minihud:
 H+C
  Light Level
  Shape Render
  Slime Chunk
  Beacon Overlay
  Structure Bounding Box
"""

"""
Minihud:
  RCtrl + :
    IRL Time  :  T
    MCDateTime:  Y
    Coord     :
    Facing    :
    Ratio     :  R
    Biome     :  I
    Speed     :  S
    FPS       :  F
    LightLevel:  L
    Ping      :  P
    MemoryUse :  M

Tweakeroo:
  Persistant Chat
  Chat Timestamp
  Map Preview
  PlayerInventoryPeak
  ShulkerDisplay
  Fake Sneak Placement:  Ctrl+F+A
  Elytra Camera   :  Z
  Zoom            :  C
  Permanent Sneak :  Ctrl+R_Shift
  Fake Sneak      :  Ctrl+F+S
  Fast Block Placement:  Ctrl+F+V
  Fast Right Click:  Ctrl+Alt+RClick
  Fast Left  Click:  Ctrl+Alt+LClick
  Free Camera     :  Ctrl+X
  Lava Visibility :  Ctrl+K+V
  Periodic Attack :  Ctrl+O+A
  Periodic Use    :  Ctrl+O+U
  Hold Attack     :  F3+O+A
  Hold Use        :  F3+O+U
  PrintDeath Coord:  Ctrl+D+C
  Auto Tool Swtich:  Y+S
  Inventory Peek  :  R
  Swap Elytra/Vent:  G

  
"""
