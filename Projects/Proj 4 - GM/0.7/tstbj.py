"""
import os
import time

def Y():
    print('''
    |
    | 
    | 
    | 
    | 
    | 
    | 
    | 
    | 
    | 
    |#____________  1.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def D():
    print('''
    |
    |  
    |  
    |  
    |  
    |  
    |  
    |  
    |  
    | #
    |#____________ 2.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def S():
    print('''
    |
    |   
    |   
    |   
    |   
    |   
    |   
    |   
    |  #
    | #
    |#____________ 3.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def C():
    print('''
    |
    |    
    |    
    |    
    |    
    |    
    |    
    |   #
    |  #
    | #
    |#____________ 4.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def P():
    print('''
    |
    |     
    |     
    |     
    |     
    |     
    |    #
    |   #
    |  #
    | #
    |#____________ 5.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def Sh():
    print('''
    |
    |      
    |      
    |      
    |      
    |     #
    |    #
    |   #
    |  #
    | #
    |#____________ 6.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def Hf():
    print('''
    |
    |       
    |       
    |       
    |      #
    |     #
    |    #
    |   #
    |  #
    | #
    |#____________ 7.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def Hs():
    print('''
    |
    |        
    |        
    |       #
    |      #
    |     #
    |    #
    |   #
    |  #
    | #
    |#____________ 8.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def N():
    print('''
    |
    |         
    |        #
    |       #
    |      #
    |     #
    |    #
    |   #
    |  #
    | #
    |#____________ 9.00
    ''')
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
def Dh(nom):
    print('''
    |
    |         #
    |        #
    |       #
    |      #
    |     #
    |    #
    |   #
    |  #
    | #
    |#____________''' + str(nom))
    time.sleep(0.75)
    #os.system('cls')
    #time.sleep(0.75)
i=0
def GMF(zrib):
    global i
    if zrib > 1:
        Y()
        os.system('cls')
        i+=1
    if zrib > 2:
        D()
        os.system('cls')
        i+=1
    if zrib > 3:
        S()
        os.system('cls')
        i+=1
    if zrib > 4:
        C()
        i+=1
        os.system('cls')
    if zrib > 5:
        P()
        i+=1
        os.system('cls')
    if zrib > 6:
        Sh()
        i+=1
        os.system('cls')
    if zrib > 7:
        Hf()
        i+=1
        os.system('cls')
    if zrib > 8:
        Hs()
        i+=1
        os.system('cls')
    if zrib > 9:
        N()
        i+=1
        os.system('cls')
    if zrib > 10:
        Dh(zrib)
    


import random
zrib= random.uniform(1,10)
while zrib >= i:
    GMF(zrib)
    #os.system('cls')
    if i < zrib:
        time.sleep(2)
        print('finifhs') 
        time.sleep(3)
        break
"""