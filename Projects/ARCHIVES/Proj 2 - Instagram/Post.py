from instapy_cli import client
from users import userss
import random
Username = userss[random.randint(0,7)]  #your username
Password = 'falofakeekhale'             #your password 
Image = 'E:\\Print\\other\\Logo\\arssym.jpg' #here you can put the image directory
Text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'
with client(Username, Password) as cli:
    cli.upload(Image, Text)