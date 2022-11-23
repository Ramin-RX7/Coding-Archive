svtxtA= 'A: NO SAVED TEXT HERE.'
svtxtB= 'B: NO SAVED TEXT HERE'
svtxtC= 'C: NO SAVED TEXT HERE'
svtxtD= 'D: NO SAVED TEXT HERE'
svtxtE= 'E: NO SAVED TEXT HERE'

svnomA= 'No saved data'
svnomB= 'No saved data'
svnomC= 'No saved data'
svnomD= 'No saved data'
svnomE= 'No saved data'

MC= input('Where you want to go in your account? \n Saved_Text \n Saved_Numbers \n')
if MC== 'Saved_Text':
    svtxt= input('Choose which saved TEXT you want? A,B,C,D,E')
    if svtxt == 'A':
        print(svtxtA)
        AsvtxtA= input('NEXT or QUIT: ')
        if AsvtxtA == 'NEXT':
                print(svtxtB)
        else:
                print(quit())



                
    if svtxt == 'B':
        print(svtxtB)
        AsvtxtB= input('NEXT, PREVIOUS or QUIT? ')
        if AsvtxtB == 'NEXT':
                print(svtxtC)
        elif AsvtxtB == 'PREVIOUS':
                print(svtxtA)
        else:
                print(quit())

                
    if svtxt == 'C':
        print(svtxtC)
        AsvtxtC= input('NEXT, PREVIOUS or QUIT? ')
        if AsvtxtC == 'NEXT':
                print(svtxtD)
        elif AsvyxyC == 'PREVIOUS':
                print(svtxtB)
        else:
                print(quit())
    
    if svtxt == 'D':
        print(svtxtD)
        AsvtxtD= input('NEXT, PREVIOUS or QUIT? ')
        if AsvtxtD == 'NEXT':
                print(svtxtE)
        elif AsvyxyD == 'PREVIOUS':
                print(svtxtC)
        else:
                print(quit())
                
    if svtxt == 'E':
        print(svtxtE)
        AsvtxtE= input('PREVIOUS or QUIT? ')
        if AsvtxtE == 'PREVIOUS':
                print(svtxtD)
        else:
                print(quit())

    if svtxt != 'A' and svtxt != 'B' and svtxt != 'C' and svtxt != 'D' and svtxt != 'E':
        print('Nothing saved with this name.')    

if MC== 'Saved_Numbers':
    svnom= input('Choose which saved NUMBER you want? A,B,C,D,E')
    if svnom == 'A':
        print(svnomA)
        AsnomA= input('NEXT, QUIT? ')
        if AsnomA == 'NEXT':
                print(svnomB)
        else:
                print(quit())
                
    if svnom == 'B':
        print(svnomB)
        AsvnomB= input('NEXT, PREVIOUS or QUIT? ')
        if AsvnomB == 'NEXT':
                print(svnomC)
        elif AsvnomB == 'PREVIOUS':
                print(svnomA)
        else:
                print(quit())
                
    if svnom == 'C':
        print(svnomC)
        AsvnomC= input('NEXT, PREVIOUS or QUIT? ')
        if AsvnomC == 'NEXT':
                print(svnomD)
        elif AsvnomC == 'PREVIOUS':
                print(svnomB)
        else:
                print(quit())
                
    if svnom == 'D':
        print(svnomD)
        AsvnomD= input('NEXT, PREVIOUS or QUIT? ')
        if AsvnomD == 'NEXT':
                print(svnomE)
        elif AsvnomD == 'PREVIOUS':
                print(svnomC)
        else:
                print(quit())

                
    if svnom == 'E':
        print(svnomE)
        AsvnomE= input('PREVIOUS or QUIT? ')
        if AsvnomE == 'PREVIOUS':
                print(svnomD)
        else:
                print(quit())
                
    if svnom != 'A' and svnom != 'B' and svnom != 'C' and svnom != 'D' and svnom != 'E':
        print('Nothing saved with this name.')






            #os.execl(sys.executable, sys.executable, *sys.argv)
            #We can use code below instead of upper line:
            #os.execv(sys.executable, ['python'] + sys.argv) '''
