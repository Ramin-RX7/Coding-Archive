"""def create():
    from AcInfoGen import generatingName
    generatingName()"""
import pyautogui
import random
import string
import webbrowser
Insta= 'https://Instagram.com/'
webbrowser.open_new_tab(Insta)
import time
time.sleep(7)


# Generating Full Name
BName=['Ali','Ramin','Hasan','Hassan','Mehrdad','Saeed','Mehdi','Aliw','Ali','Ali','Ali','Mohammad','Mohamad','Mohammad','Mammad','Mohammad','Reza','Farzad','Farokh','Farhad','Mohamad','Kianoosh','Mahan','Hossein','Farshaad','Farshid','Toraj','Masoud','Mojtaba','Vahid','Amirhossein','Fereidon','Amirali','Keyvan','Kiarash','Abed','Sina','Sorosh','Shahb','Shahriar','Rasol','Shahyad','Kamran','Kamiyar','Khosro','Amin','Arash','Ehsan','Arian','Arsalan','Arasto','Jafar','Sajad','Javad','Meysam','Erfan','Ashkan','Ashvan','Arshia', 'Kian', 'Shervin', 'Shahrokh', 'Shahram', 'Nima''Omid','Pejman','Hadi', 'Pedram', 'Sohrab','Ardalan','Soheil','Moein','Mobin', 'Davood', 'Rahman','Rahim', 'Foad','Morteza', 'Nasser','Mahyar',]
GName=['Mahtab','Mahya','Fariba','tayebe','Tina','Mahboobe','Mehri','Felor','Faride','Ghazal','Mahshid','Sanaz','Atefe', 'Faeze','Fahime','Parisa','Kimia','Rojin','Roshanak','Roshana','Ainaz','Elham','Elahe','Narges','Nasrin','Nahid','Shahnaz','Soraia','Mahdiye','Mahsa','Goli','Golnaz','Golrokh','Saghar','Kaiana','Tanaz','Bita','Benita','Parmida','Nadia','Somaye','Safiye','Leila','Anahita','Shadi','Nasim','Shohre','Mina','Mina','Hoda','Farnaz','Firoze','Melika','Mojde','Mina','Mino','Atosa','Hadis','Rana','Rozita', 'Sheyda','Shiva', 'Zahra', 'Monir', 'Poone','Sodabe']
SurName=['Nakhei','Hasani','Hosseini','Rahmati','Najib','Rashid','Elahi','Hasannejad','Moradi','Javid','Mohamadi','Motahari','Sasani','Samani','Shirazi','Shafie','Rostami','Rastegari','Ghasemi','Khalaji','Maleki','Saberi','Nadaf','Lak','Zandi','Abasi','Akbarpoor','Farhadi','Jafari','Razavian','Jokar','Rasoli','Momeni','Bazargan','Khoshro','Kheradmand','Mosavi','Gooya','Bakhtiari','Rostampoor','Faramarzi','Motaghi','Pakzad','Bavafa','Aghajani','Soltani','Jafarneja','Mozafari','Fazel','Shiri','Shirmohamadi','Behroznia','Ahrari','Sadeghi','Nikokalam','Nikosokhan','Shojaei','Sirosi','Davodi','Ghazi','Habibi','Hamidian','Gorji','Dehghan','Golchin','Sheybani','Soleymani','Kohanddani','Masinaei','Minaei','Mazlom','Najafi',
         'Azad','Ostadi','Kalhor','Ahmadpoor','Zare','Torabi','Taghizade','Rafie','Roshan','Salimi','Sharifi','Tafreshi','Hamedi','Yekta','Bahman','Shams','Balazade','Azizmi','Farahani','Tavasolian','Rezaei','Sarabi','Rakhshani','Farahmand','Vanaki','Azmode','Pasandide','Alizadeh','Darbadn','Majidi','Asqari','Qaraei','Dadras','Solgi','Heydari','Rad','Sahebi','Salehi','Fard','Babaei','Pedrami','Vazini','Parvini','Saravani','Tosi','Golmohamadi','Mohtasham','Arjmand','Ranjbar','Salehpoor','Negahi','Alipoor']
UserSfx= ['Tak','hichkas','weeed','gngster','pk','asli','tkd','original','org','iw','wn','co','ir','tnt','thc','star','comp','love','rll','dark','black','off','coder','hacker','tm','teh','tehrun','Pishro','CR7','oficial','x']
UserPrfx=['Injaneb','I','its','Im','original']
SpclChar=['_','.',]


# Generating a username
size = 6
chars  = string.ascii_lowercase + random.choice(['.', '_'])


#Generate NAME:
FrstNm= ''.join(random.choice(BName))
LstNm= ''.join(random.choice(SurName))
GngTp= str(random.randint(1,7))
if GngTp == '1':
    Gng= ''.join(random.choice(UserPrfx))
else:
    Gng= ''.join(random.choice(UserSfx))
SpCh= ''.join(random.choice(SpclChar))


#Email
pyautogui.click(828,277)
pyautogui.typewrite(FrstNm + LstNm + str(random.randint(100,9999)), interval=0.25)
pyautogui.typewrite('@mail.com', interval=0.25)


#Fullname
pyautogui.click(828,323)
UserNmTp= str(random.randint(1,12))
if UserNmTp == '1' or UserNmTp == '2' or UserNmTp == '3' or UserNmTp == '12':     #Frst Lst
    pyautogui.typewrite(FrstNm + ' '  + LstNm, interval=0.25)
elif UserNmTp == '4' or UserNmTp == '5' or UserNmTp == '6':     #Frst
    pyautogui.typewrite(FrstNm, interval=0.25)
elif UserNmTp == '7' or UserNmTp == '8':     #Frst Gng
    pyautogui.typewrite(FrstNm + ' ' + Gng, interval=0.25)
elif UserNmTp == '9' or UserNmTp == '10':     #Gng
    pyautogui.typewrite(Gng, interval=0.25)
elif UserNmTp == '11':     #Frst_Gng_Gng
    pyautogui.typewrite(FrstNm + '_' + Gng + '_' + random.choice(UserSfx), interval=0.25)



#Username
UserNmTp= str(random.randint(1,2))

pyautogui.click(828,373)

UserNmTp= str(random.randint(1,11))
if UserNmTp == '1' or UserNmTp == '2':     #FrstLst9999
    pyautogui.typewrite(FrstNm + LstNm + str(random.randint(100,9999)), interval=0.25)
elif UserNmTp == '3' or UserNmTp == '4' or UserNmTp == '5' or UserNmTp == '6':     #FrstLst_9999
    pyautogui.typewrite(FrstNm + LstNm + '_' + str(random.randint(100,9999)), interval=0.25)
elif UserNmTp == '7' or UserNmTp == '8':     #FrstLst_Gng
    pyautogui.typewrite(FrstNm + LstNm + '_' + Gng, interval=0.25)
elif UserNmTp == '9' or UserNmTp == '10':     #Frst_Gng_999
    pyautogui.typewrite(FrstNm + '_' + Gng + '_' + str(random.randint(100,999)), interval=0.25)
elif UserNmTp == '11':     #Frst_Gng_Gng
    pyautogui.typewrite(FrstNm + '_' + Gng + '_' + random.choice(UserSfx), interval=0.25)
elif UserNmTp == '12':     #Gng_Gng_Gng
    pyautogui.typewrite(random.choice(UserSfx) + '_' + Gng + '_' + random.choice(UserSfx), interval=0.25)


pyautogui.click(828,462,clicks=2)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(463,748)
pyautogui.typewrite('\'')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\',')
pyautogui.click(315,741)
#pyautogui.typewrite(''.join(random.choice(chars) for _ in range(size)), interval=0.25)


#Password
pyautogui.click(828,404)
pyautogui.typewrite('falofakeekhale', interval=0.25)

#Signup Button
pyautogui.click(828,456)


