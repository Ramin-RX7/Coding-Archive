#from random import choice
import rx7 as rx
choice= rx.rand.choose
import string,os

ALL_CHARS= string.ascii_lowercase+string.ascii_uppercase+string.digits+r"""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""+' '
RANDM_LST= ALL_CHARS+' '*6


##############################
def generateKey(string, key):
    key = list(key) 
    if len(string) == len(key):  return(key) 
    else: 
        for i in range(len(string) - len(key)):  key.append(key[i % len(key)]) 
    return("" . join(key))
def new_ALL_CHARS(ch):
    return ALL_CHARS[ALL_CHARS.index(ch):] + ALL_CHARS[:ALL_CHARS.index(ch)]
def vig_encrypt(text, big_key):
    res = '';i = 1;big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_ALL_CHARS(char)
        for t in text:
            if ALL_CHARS.count(t) == 1: res += new[ALL_CHARS.index(t)];text = text[i:];break
            elif ALL_CHARS.count(t) == 1: res += new[ALL_CHARS.index(t)];text = text[i:];break
            else: res += t;text = text[i:];break
            i += 1    
    return res
def vig_decrypt(text, big_key):
    res = '';i = 1;big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_ALL_CHARS(char)
        for t in text:
            if ALL_CHARS.count(t) == 1 : res += ALL_CHARS[new.index(t)];text = text[i:];break
            elif ALL_CHARS.count(t) == 1:res += ALL_CHARS[new.index(t)];text = text[i:];break
            else: res += t;text = text[i:];break
            i += 1
    return res
##############################

##############################
def ENCRYPT(INPUT):
    NEW=[]
    for char in INPUT:
        Length= choice([5,7,9])
        if   Length==5: #2
            NEW.append(f'{choice(RANDM_LST)}{char}{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST[:-7])}')
        elif Length==7: #4
            NEW.append(f'{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST)}{char}{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST[-7])}')
        elif Length==9: #6
            NEW.append(f'{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST)}{char}{choice(RANDM_LST)}{choice(RANDM_LST)}{choice(RANDM_LST[-7])}')
    def CLOSE(WORD):
        nom= len(WORD)
        if   nom < 32:    CLOSEST= 32
        elif 32<nom<40:   CLOSEST= 40
        elif 40<nom<56:   CLOSEST= 56
        elif 56<nom<64:   CLOSEST= 64
        elif 64<nom<96:   CLOSEST= 96
        elif 96<nom<128:  CLOSEST= 128
        else:             return WORD
        WORD+='`'
        import rx7
        for i in range(CLOSEST-nom-1): WORD+= rx7.rand.choose(RANDM_LST)
        return WORD
    return CLOSE('a/'.join(NEW))         

def DECRYPT(ENCRYPTED):
    DECRYPT_LVL1= ENCRYPTED.split('a/')
    DECRYPTED= ''
    if '`' in DECRYPT_LVL1: DECRYPT_LVL1= DECRYPT_LVL1[:DECRYPT_LVL1.index('`')]
    for member in DECRYPT_LVL1:
        if len(member)==5: DECRYPTED+=member[1]
        if len(member)==7: DECRYPTED+=member[3]
        if len(member)==9: DECRYPTED+=member[5]
    return DECRYPTED
##############################
def HACK(WORD,KEY='UNKNOWN'): 
    WORD= 'h0xr6u;a/dIda sva/Mm)Q#a/>{-iJf.a/+Itn|(b'
    DECRYPT_LVL1= WORD.split('a/')
    DECRYPTED= ''
    for member in DECRYPT_LVL1:
        if len(member)==5: DECRYPTED+=member[1]
        if len(member)==7: DECRYPTED+=member[3]
        if len(member)==9: DECRYPTED+=member[5]
    return DECRYPTED



while True:
    rx.cls()
    print('''

      █   █▀▀█ █▀▀▀ █▀▀█
      █   █  █ █ ▀█ █  █
      ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀  ''')
    print('''
        {1}--Encrypt to NAME
        {2}--Decrypt NAME Cipher
        {3}--NAME Cracker  (Comming Soon...)
    ''')
    vminp= input(' DramaX:Vigenere> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ')
        if Word:
            Key=  input(' Enter Key:  ')
            print(' Encrypted String is:   ', end='')
            if Key: rx.style.print(ENCRYPT(vig_encrypt(Word,Key)),'green')
            else:   rx.style.print(ENCRYPT(Word),'green')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        if Cipher:
            Key=    input(' Enter Key:          ')
            print(' Decrypted String is:   ', end='')
            if Key: rx.style.print(vig_decrypt(DECRYPT(Cipher),Key),'green')
            else:   rx.style.print(DECRYPT(Cipher),'green')
    if vminp=='3':
        print(HACK('.6#rr 0a/:aorza/hmNdUa/*g]  i/R a/*nm~T'))
    os.system('pause')
    