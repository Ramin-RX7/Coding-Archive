
from XFSVTXT import *
from XFSVNOM import *

while True:
    print('Where you want to go in your account? \n (only type number)')
    MC= input('1-SAVED TEXT \n 2-Saved_Numbers \n 3-RIP Website \n \n )
    if MC== '1':
        svtxt= input('Choose which saved TEXT you want? A,B,C,D,E')
        
        if svtxt == 'A':
            svtxtAW= input('What you want to do with it? (EDIT - READ)')
            if svtxtAW== 'READ':
                print(svtxtA)
                AsvtxtA= input('NEXT or QUIT: ')
                if AsvtxtA == 'NEXT':
                    print(svtxtB)
                else:
                    print(quit())
            elif svtxtAW== 'EDIT':
                 CsvtxtA= input('Type what you want to save in SAVED TEXT A?')
                 opeE= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' +'XFSVTXT.py', mode= 'w')
                 opeE.write('svtxtA= ' + '\'' + CsvtxtA+ '\'' + '\n'
                            'svtxtB= ' + '\'' + svtxtB + '\'' + '\n'
                            'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                            'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                            'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                 opeE.close()
                 print('SAVED TEXT A has been successfully Updated.')
                    
        if svtxt == 'B':
            svtxtBW= input('What you want to dowith it? (EDIT - READ)')
            if svtxtBW== 'READ':
                print(svtxtB)
                AsvtxtB= input('NEXT, PREVIOUS or QUIT? ')
                if AsvtxtB == 'NEXT':
                    print(svtxtC)
                elif AsvtxtB == 'PREVIOUS':
                    print(svtxtA)
                else:
                    print(quit())
                    
            elif svtxtBW== 'EDIT':
                CsvtxtB= input('Type what you want to save in SAVED TEXT B?')
                 opeE= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' +'XFSVTXT.py', mode= 'w')
                opeE.write('svtxtA= ' + '\'' + svtxtA + '\'' + '\n'
                           'svtxtB= ' + '\'' + CsvtxtB+ '\'' + '\n'
                           'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                           'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                           'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                opeE.close()
                print('SAVED TEXT B has been successfully Updated.') 

                   
        if svtxt == 'C':
            svtxtCW= input('What you want to dowith it? (EDIT - READ)')
            if svtxtCW== 'READ':
                print(svtxtC)
                AsvtxtC= input('NEXT, PREVIOUS or QUIT? ')
                if AsvtxtC == 'NEXT':
                    print(svtxtD)
                elif AsvyxyC == 'PREVIOUS':
                    print(svtxtB)
                else:
                    print(quit())
                    
            elif svtxtCW== 'EDIT':
                CsvtxtC= input('Type what you want to save in SAVED TEXT C?')
                opeE= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' +'XFSVTXT.py', mode= 'w')
                opeE.write('svtxtA= ' + '\'' + svtxtA + '\'' + '\n'
                           'svtxtB= ' + '\'' + svtxtB + '\'' + '\n'
                           'svtxtC= ' + '\'' + CsvtxtC+ '\'' + '\n'
                           'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                           'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                opeE.close()
                print('SAVED TEXT C has been successfully Updated.')

        
        if svtxt == 'D':
            svtxtDW= input('What you want to do with it? (EDIT - READ)')
            if svtxtDW== 'READ':
                print(svtxtD)
                AsvtxtD= input('NEXT, PREVIOUS or QUIT? ')
                if AsvtxtD == 'NEXT':
                    print(svtxtE)
                elif AsvyxyD == 'PREVIOUS':
                    print(svtxtC)
                else:
                    print(quit())
                    
            elif svtxtDW== 'EDIT':
                CsvtxtD= input('Type what you want to save in SAVED TEXT A?')
                opeE= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' +'XFSVTXT.py', mode= 'w')
                opeE.write('svtxtA= ' + '\'' + svtxtA + '\'' + '\n'
                           'svtxtB= ' + '\'' + svtxtB + '\'' + '\n'
                           'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                           'svtxtD= ' + '\'' + CsvtxtD+ '\'' + '\n'
                           'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                opeE.close()
                print('SAVED TEXT D has been successfully Updated.')
                
                    
        if svtxt == 'E':
            svtxtEW= input('What you want to do with it? (EDIT - READ)')
            if svtxtEW== 'READ':
                print(svtxtE)
                AsvtxtE= input('PREVIOUS or QUIT? ')
                if AsvtxtE == 'PREVIOUS':
                    print(svtxtD)
                else:
                    print(quit())
                    
            elif svtxtEW== 'EDIT':
                CsvtxtE= input('Type what you want to save in SAVED TEXT A?')
                opeE= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' +'XFSVTXT.py', mode= 'w')
                opeE.write('svtxtA= ' + '\'' + svtxtA+ '\''  + '\n'
                           'svtxtB= ' + '\'' + svtxtB + '\'' + '\n'
                           'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                           'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                           'svtxtE= ' + '\'' + CsvtxtE + '\'' + '\n')
                opeE.close()
                print('SAVED TEXT E has been successfully Updated.')
                

        if svtxt != 'A' and svtxt != 'B' and svtxt != 'C' and svtxt != 'D' and svtxt != 'E':
            print('Nothing saved with this name.')    


    if MC== '2':
        svnom= input('Choose which saved NUMBER you want? A,B,C,D,E \n')
        
        if svnom == 'A':
            svnomAW= input('What you want to do with it? (EDIT - READ): ')
            if svnomAW== 'READ':
                print(svnomA)
                AsvnomA= input('NEXT, QUIT? ')
                if AsvnomA == 'NEXT':
                    print(svnomB)
                else:
                    print(quit())
                    
            elif svnomAW== 'EDIT':
                CsvnomA= input('Type what you want to save in SAVED Numbers A?')
                opeP= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + CsvnomA+ '\'' + '\n'
                           'svnomB= ' + '\'' + svnomB + '\'' + '\n'
                           'svnomC= ' + '\'' + svnomC + '\'' + '\n'
                           'svnomD= ' + '\'' + svnomD + '\'' + '\n'
                           'svnomE= ' + '\'' + svnomE + '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS A has been successfully Updated.')        
            else:
                    print(quit())
                    
                    
        if svnom == 'B':
            svnomBW= input('What you want to do with it? (EDIT - READ): ')
            if svnomBW== 'READ':
                print(svnomB)
                AsvnomB= input('NEXT, PREVIOUS or QUIT? ')
                if AsvnomB == 'NEXT':
                    print(svnomC)
                elif AsvnomB == 'PREVIOUS':
                    print(svnomA)
                else:
                    print(quit())
                    
            elif svnomBW== 'EDIT':
                CsvnomB= input('Type what you want to save in SAVED Numbers B?')
                opeP= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA + '\'' + '\n'
                           'svnomB= ' + '\'' + CsvnomB+ '\'' + '\n'
                           'svnomC= ' + '\'' + svnomC + '\'' + '\n'
                           'svnomD= ' + '\'' + svnomD + '\'' + '\n'
                           'svnomE= ' + '\'' + svnomE + '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS B has been successfully Updated.')
                
                    
        if svnom == 'C':
            svnomCW= input('What you want to do with it? (EDIT - READ): ')
            if svnomCW== 'READ':
                print(svnomC)
                AsvnomC= input('NEXT, PREVIOUS or QUIT? ')
                if AsvnomC == 'NEXT':
                    print(svnomD)
                elif AsvnomC == 'PREVIOUS':
                    print(svnomB)
                else:
                    print(quit())
                    
            elif svnomCW== 'EDIT':
                CsvnomC= input('Type what you want to save in SAVED Numbers C?')
                opeP= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA + '\'' + '\n'
                           'svnomB= ' + '\'' + svnomB + '\'' + '\n'
                           'svnomC= ' + '\'' + CsvnomC+ '\'' + '\n'
                           'svnomD= ' + '\'' + svnomD + '\'' + '\n'
                           'svnomE= ' + '\'' + svnomE + '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS C has been successfully Updated.')
                
                    
        if svnom == 'D':
            svnomDW= input('What you want to do with it? (EDIT - READ): ')
            if svnomDW== 'READ':
                print(svnomD)
                AsvnomD= input('NEXT, PREVIOUS or QUIT? ')
                if AsvnomD == 'NEXT':
                    print(svnomE)
                elif AsvnomD == 'PREVIOUS':
                    print(svnomC)
                else:
                    print(quit())
                    
            elif svnomDW== 'EDIT':
                CsvnomD= input('Type what you want to save in SAVED Numbers D?')
                opeP= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA + '\'' + '\n'
                           'svnomB= ' + '\'' + svnomB + '\'' + '\n'
                           'svnomC= ' + '\'' + svnomC + '\'' + '\n'
                           'svnomD= ' + '\'' + CsvnomD+ '\'' + '\n'
                           'svnomE= ' + '\'' + svnomE + '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS D has been successfully Updated.')
                  
                    
        if svnom == 'E':
            svnomEW= input('What you want to do with it? (EDIT - READ): ')
            if svnomEW== 'READ':
                print(svnomE)
                AsvnomE= input('PREVIOUS or QUIT? ')
                if AsvnomE == 'PREVIOUS':
                    print(svnomD)
                else:
                    print(quit())

            elif svnomEW== 'EDIT':
                CsvnomE= input('Type what you want to save in SAVED Numbers E?')
                opeP= open('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib' + '\\' + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA + '\'' + '\n'
                           'svnomB= ' + '\'' + svnomB + '\'' + '\n'
                           'svnomC= ' + '\'' + svnomC + '\'' + '\n'
                           'svnomD= ' + '\'' + svnomD + '\'' + '\n'
                           'svnomE= ' + '\'' + CsvnomE+ '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS E has been successfully Updated.')

                
                    
        if svnom != 'A' and svnom != 'B' and svnom != 'C' and svnom != 'D' and svnom != 'E':
            print('Nothing saved with this name.')






            #os.execl(sys.executable, sys.executable, *sys.argv)
            #We can use code below instead of upper line:
            #os.execv(sys.executable, ['python'] + sys.argv) '''
