y= '''
Level 1: 
    Try to replace characters with wich is like them.
    e.g:  SE0 ==> $3O
'''
d='''
Level 2:
    Convert Binary to Text
'''
s='''
Level 3:
    Sequence is multiples of 3 which are lower than 100 without order. One of them is not given.
'''
c='''
Level 4:

'''


while True:
    x= input('Type Level Number you want to get hint: ')
    try:
        x=int(x)

        if x==1:
            print(y)
        if x==2:
            print(d)
        if x==3:
            print(d)
        if x==4:
            print(d)
        if x==5:
            print(d)




    except:
        print('Wrong Level Number.')

