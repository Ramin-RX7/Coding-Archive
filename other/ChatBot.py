import re
from rx import *
LHello= ['hey','hi','hello']
LHow= ['How are you','How are u','how is it going','what\'s up','wassap']
LThanx= ['Thanks','Thank you', 'Good']
LReask= ['What about you?','And you?',]
# Check Fosh at first:   : fuck you => f**k u

def rmv(item):
    rmv_l= ['more','day','week','month','year',]
    cnvrtd=item
    if cnvrtd[-1][-2:]=='ly':
        cnvrtd= cnvrtd[:-1]+cnvrtd[-1][:-2]
    for word in rmv_l:
        if item[-1]==word:
            cnvrtd.remove(item[-1])
    return cnvrtd



def ch():
    Inp= input(': ').lower()
    spl= Inp.split()
    cnvrt= rmv(spl)
    if len(spl)>5:
        p('I Can not understand.')
        ch()
    for patt in LHello:
        find_hello= re.search(patt,cnvrt[0])
        if find_hello!=None:
            p(rx.rand.choice(LHello))
           
    for patt in LHow:
        find_how= re.search(patt,Inp)
        if find_how!=None:
            p(rx.rand.choice(LThanx))
            p(rx.rand.choice(LReask))
        
    find_too= re.search('too',spl[-1])
    if find_too!=None:
        p('great!')

    ch()    



ch()
