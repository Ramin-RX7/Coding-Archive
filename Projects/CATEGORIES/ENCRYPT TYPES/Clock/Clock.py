import string
LC=string.ascii_lowercase+string.ascii_uppercase
# \\ \
DIC_CHARS={}
for i in range(10,62):
    DIC_CHARS[LC[i-10]]=i
#print(CHARS_DIC,end='\n\n')
NOMS='0123456789'
DIC_SYM={}
#syms='!"$%^&*()-=_+#@~;:?/><.,[]}{'
#for i in range(20):
#    DIC_SYM[syms[i]]=i


INP= input('Type: ')

SWITCH=[]
for char in INP:
    if char in DIC_CHARS:
        SWITCH.append(DIC_CHARS[char])
    if char in NOMS:
        SWITCH.append(char)
#print(SWITCH)

LST_ENC=[]
from rx7 import rand
for nom in SWITCH:
    if len(str(nom))==1:
        nom='0'+str(nom)
    LST_ENC.append(f'{rand.integer(1,23)}:{nom}')
    LST_ENC.append(f'{rand.integer(1,23)}:{rand.integer(1,59)}')
print(LST_ENC)



#REVERSE DICTS
l= DIC_CHARS.items()
DIC_CHARS={}
for item in l:
    DIC_CHARS[item[1]]=item[0]
l= DIC_NOM.items()

##############



DEL_EXT=[]
for item in LST_ENC:
    if LST_ENC.index(item)%2==0:
        NOM=item[item.index(':')+1:]
        if int(NOM) in DIC_CHARS:
            x= DIC_CHARS[int(NOM)]
        if int(NOM) in DIC_NOM:
            x= DIC_NOM[int(NOM)]
        DEL_EXT.append(x)
print(''.join(DEL_EXT))