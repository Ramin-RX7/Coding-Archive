import webbrowser
import os
import shutil

import XFSVTXT
#from XFSVTXT import *
#from XFSVNOM import *

Src= 'C:\\RIP\\Programs\\Saves\\'
PyLib= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\'
PyLibSvPhts= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Photos\\'
PyLibSvVids= 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Videos\\'
PyLibSvFls = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'

while True:
    print('Where you want to go in your account? \n(only type number) \n')
    MC= input('1-Saved TEXTS \n2-Saved NUMBERS \n3-Saved PHOTOS \n4-Saved VIDEOS \n5-Saved FILES \n6-RIP Website 0-Exit \n \n')
    if MC== '1':
        svtxt= input('Choose which saved TEXT you want? A,B,C,D,E: ')
        
        if svtxt == 'A':
            svtxtAW= input('What you want to do with it? (EDIT - READ)')
            if svtxtAW== 'READ':             
                print(svtxtA)
                AsvtxtA= input('NEXT? ')
                if AsvtxtA == 'NEXT':
                    print(svtxtB)
                else:
                    print('Invalid request.')
            elif svtxtAW== 'EDIT':
                 CsvtxtA= input('Type what you want to save in SAVED TEXT A? ')
                 opeE= open(PyLib +'XFSVTXT.py', mode= 'w')
                 opeE.write('svtxtA= ' + '\'' + CsvtxtA+ '\'' + '\n'
                            'svtxtB= ' + '\'' + svtxtB + '\'' + '\n'
                            'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                            'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                            'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                 opeE.close()
                 print('SAVED TEXT A has been successfully Updated.')
                    
        if svtxt == 'B':
            svtxtBW= input('What you want to do with it? (EDIT - READ)')
            if svtxtBW== 'READ':
                print(svtxtB)
                AsvtxtB= input('NEX or PREVIOUS? ')
                if AsvtxtB == 'NEXT':
                    print(svtxtC)
                elif AsvtxtB == 'PREVIOUS':
                    print(svtxtA)
                else:
                    print('Invalid request.')
                    
            elif svtxtBW== 'EDIT':
                CsvtxtB= input('Type what you want to save in SAVED TEXT B?')
                opeE= open(PyLib +'XFSVTXT.py', mode= 'w')
                opeE.write('svtxtA= ' + '\'' + svtxtA + '\'' + '\n'
                           'svtxtB= ' + '\'' + CsvtxtB+ '\'' + '\n'
                           'svtxtC= ' + '\'' + svtxtC + '\'' + '\n'
                           'svtxtD= ' + '\'' + svtxtD + '\'' + '\n'
                           'svtxtE= ' + '\'' + svtxtE + '\'' + '\n')
                opeE.close()
                print('SAVED TEXT B has been successfully Updated.') 

                   
        if svtxt == 'C':
            svtxtCW= input('What you want to do with it? (EDIT - READ)')
            if svtxtCW== 'READ':
                print(svtxtC)
                AsvtxtC= input('NEXT or PREVIOUS? ')
                if AsvtxtC == 'NEXT':
                    print(svtxtD)
                elif AsvyxyC == 'PREVIOUS':
                    print(svtxtB)
                else:
                    print('Invalid request.')
                    
            elif svtxtCW== 'EDIT':
                CsvtxtC= input('Type what you want to save in SAVED TEXT C?')
                opeE= open(PyLib +'XFSVTXT.py', mode= 'w')
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
                AsvtxtD= input('NEXT or PREVIOUS? ')
                if AsvtxtD == 'NEXT':
                    print(svtxtE)
                elif AsvyxyD == 'PREVIOUS':
                    print(svtxtC)
                else:
                    print('Invalid request.')
                    
            elif svtxtDW== 'EDIT':
                CsvtxtD= input('Type what you want to save in SAVED TEXT A?')
                opeE= open(PyLib +'XFSVTXT.py', mode= 'w')
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
                AsvtxtE= input('PREVIOUS? ')
                if AsvtxtE == 'PREVIOUS':
                    print(svtxtD)
                else:
                    print('Invalid request.')
                    
            elif svtxtEW== 'EDIT':
                CsvtxtE= input('Type what you want to save in SAVED TEXT A?')
                opeE= open(PyLib +'XFSVTXT.py', mode= 'w')
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
                AsvnomA= input('NEXT? ')
                if AsvnomA == 'NEXT':
                    print(svnomB)
                else:
                    print('Invalid request.')
                    
            elif svnomAW== 'EDIT':
                NMsvnomA= input('Type name of the contact:')
                NOsvnomA= input('Type the PHONE NUMBER of' + 'NMsvnomA')
                opeP= open(PyLib + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + NMsvnomA + ' : ' + NOsvnomA + '\'' + '\n'
                           'svnomB= ' + '\'' + svnomB   + '\''  + '\n'
                           'svnomC= ' + '\'' + svnomC   + '\''  + '\n'
                           'svnomD= ' + '\'' + svnomD   + '\''  + '\n'
                           'svnomE= ' + '\'' + svnomE   + '\''  + '\n'
                           )
                opeP.close()
                print('SAVED NUMBERS A has been successfully Updated.')        
            else:
                    print('Invalid request.')
                    
                    
        if svnom == 'B':
            svnomBW= input('What you want to do with it? (EDIT - READ): ')
            if svnomBW== 'READ':
                print(svnomB)
                AsvnomB= input('NEXT or PREVIOUS? ')
                if AsvnomB == 'NEXT':
                    print(svnomC)
                elif AsvnomB == 'PREVIOUS':
                    print(svnomA)
                else:
                    print('Invalid request.')
                    
            elif svnomBW== 'EDIT':
                NMsvnomB= input('Type name of the contact:')
                NOsvnomB= input('Type the PHONE NUMBER of' + NMsvnomB)
                opeP= open(PyLib + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA   + '\''  + '\n'
                           'svnomB= ' + '\'' + NMsvnomB + ' : ' + NOsvnomB + '\'' + '\n'
                           'svnomC= ' + '\'' + svnomC   + '\''  + '\n'
                           'svnomD= ' + '\'' + svnomD   + '\''  + '\n'
                           'svnomE= ' + '\'' + svnomE   + '\''  + '\n')
                opeP.close()
                print('SAVED NUMBERS B has been successfully Updated.')
                
                    
        if svnom == 'C':
            svnomCW= input('What you want to do with it? (EDIT - READ): ')
            if svnomCW== 'READ':
                print(svnomC)
                AsvnomC= input('NEXT or PREVIOUS? ')
                if AsvnomC == 'NEXT':
                    print(svnomD)
                elif AsvnomC == 'PREVIOUS':
                    print(svnomB)
                else:
                    print('Invalid request.')
                    
            elif svnomCW== 'EDIT':
                NMsvnomC= input('Type name of the contact:')
                NOsvnomC= input('Type the PHONE NUMBER of' + NMsvnomC)
                opeP= open(PyLib + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA   + '\''  + '\n'
                           'svnomB= ' + '\'' + svnomB   + '\''  + '\n'
                           'svnomC= ' + '\'' + NMsvnomC + ' : ' + NOsvnomC + '\'' + '\n'
                           'svnomD= ' + '\'' + svnomD   + '\''  + '\n'
                           'svnomE= ' + '\'' + svnomE   + '\''  + '\n')
                opeP.close()
                print('SAVED NUMBERS C has been successfully Updated.')
                
                    
        if svnom == 'D':
            svnomDW= input('What you want to do with it? (EDIT - READ): ')
            if svnomDW== 'READ':
                print(svnomD)
                AsvnomD= input('NEXT or PREVIOUS? ')
                if AsvnomD == 'NEXT':
                    print(svnomE)
                elif AsvnomD == 'PREVIOUS':
                    print(svnomC)
                else:
                    print('Invalid request.')
                    
            elif svnomDW== 'EDIT':
                NMsvnomD= input('Type name of the contact:')
                NOsvnomD= input('Type the PHONE NUMBER of' + NMsvnomD)
                opeP= open(PyLib + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA   + '\''  + '\n'
                           'svnomB= ' + '\'' + svnomB   + '\''  + '\n'
                           'svnomC= ' + '\'' + svnomC   + '\''  + '\n'
                           'svnomD= ' + '\'' + NMsvnomD + ' : ' + NOsvnomD + '\'' + '\n'
                           'svnomE= ' + '\'' + svnomE   + '\''  + '\n')
                opeP.close()
                print('SAVED NUMBERS D has been successfully Updated.')
                  
                    
        if svnom == 'E':
            svnomEW= input('What you want to do with it? (EDIT - READ): ')
            if svnomEW== 'READ':
                print(svnomE)
                AsvnomE= input('PREVIOUS? ')
                if AsvnomE == 'PREVIOUS':
                    print(svnomD)
                else:
                    print('Invalid request.')

            elif svnomEW== 'EDIT':
                NMsvnomE= input('Type name of the contact:')
                NOsvnomE= input('Type the PHONE NUMBER of' + NMsvnomE)
                opeP= open(PyLib + 'XFSVNOM.py', mode='w')
                opeP.write('svnomA= ' + '\'' + svnomA   + '\''  + '\n'
                           'svnomB= ' + '\'' + svnomB   + '\''  + '\n'
                           'svnomC= ' + '\'' + svnomC   + '\''  + '\n'
                           'svnomD= ' + '\'' + svnomD   + '\''  + '\n'
                           'svnomE= ' + '\'' + NMsvnomE + ' : ' + NOsvnomE + '\'' + '\n')
                opeP.close()
                print('SAVED NUMBERS E has been successfully Updated.')

                
                    
        if svnom != 'A' and svnom != 'B' and svnom != 'C' and svnom != 'D' and svnom != 'E':
            print('Nothing saved with this name.')
    
    
    
    if MC== '3':
        print('Please do not forget your PHOTO\'s names.')
        Convert= input('OK. Now let us know what you want to do? \n1-Hide Photo \n2-Show Photo')
        if Convert == '1':
            print('First of all copy image that you want to hide in source folder \n(C:\RIP\Programs\Saves\)')
            HNoP= input('Now type name of your photo without extention: ')       #HNoP means: Name of Photo
            HEoP= input('And now type your photo\'s extention: ')                #HEoP means: Extentation of Photo
                                                                                 #H means to HIDE
        
            PDest= Src + HNoP + HEoP
        
            if os.path.exists(PDest)== True:
                os.rename(PDest, 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Photos\\'+HNoP)
                print('Photo has been successfully converted & It\'s hidden now.')
           
           
            else:
                print('File name is incorrect.')

        # This paragraph is for Showing PHOTO
        if Convert == '2':
            print('We hope that you didn\'t forget your PHOTO\'s names.')
            SNoP= input('Type your PHOTO\'s name to convert and show it: ')
            if os.path.exists(PyLibSvPhts + SNoP) == True:
                shutil.copy(PyLibSvPhts + SNoP, Src)
                os.rename(Src + SNoP, Src + SNoP +'.jpg')
                print('Photo has been successfully converted and it\'s in the source folder and you can check it now.')
                WTD= input('OK. What you want to do with it? \n1-Keep it. \n2-Delete it.')
                if WTD == '1':
                    pass
                if WTD == '2':
                    os.remove(Src + SNoP + '.jpg')
                    print('PHOTO has been deleted from source folder.')
                else:
                    print('Invalid request')
            else:
                print('PHOTO not found with this name. Check your PHOTO name again.')







    if MC== '4':
        print('Please do not forget your Video\'s names.')
        Convert= input('OK. Now let us know what you want to do? \n1-Hide Video \n2-Show Video')
        if Convert == '1':
            print('First of all copy Video that you want to hide in source folder \n(C:\RIP\Programs\Saves\)')
            HNoV= input('Now type name of your Video without extention: ')       #HNoP means: Name of Video
            HEoV= input('And now type your Video\'s extention: ')                #HEoP means: Extentation of Video
                                                                                 #H means to HIDE
        
            VDest= Src + HNoV + HEoV
        
            if os.path.exists(PDest)== True:
                os.rename(VDest, PyLibSvVids + HNoV)
                print('Video has been successfully converted & It\'s hidden now.')
           
           
            else:
                print('File name is incorrect.')

        # This paragraph is for Showing Videos
        if Convert == '2':
            print('We hope that you didn\'t forget your VIDEO\'s names.')
            SNoV= input('Type your VIDEO\'s name to convert and show it: ')
            if os.path.exists(PyLibSvVids + SNoV) == True:
                shutil.copy(PyLibSvVids + SNoV, Src)
                os.rename(Src + SNoV, Src + SNoV + '.mp4')
                print('Video has been successfully converted and it\'s in the source folder and you can check it now.')
                WTD= input('OK. What you want to do with it? \n1-Keep it. \n2-Delete it.')
                if WTD == '1':
                    pass
                if WTD == '2':
                    os.remove(Src + SNoV + '.mp4')
                    print('VIDEO has been deleted from source folder.')
                else:
                    print('Invalid request')
            else:
                print('VIDEO not found with this name. Check your VIDEO name again.')


    if MC == '5':
        svfl= input('Choose which saved FILES you want? A,B,C: ')
        if svfl == 'A':
            Convert= input('OK. Now let us know what you want to do with file A? \n1-Convert and Hide file \n2-Show file')
            
            if Convert== '1':
                print('First of all copy Video that you want to hide in source folder \n(C:\RIP\Programs\Saves\)')
                print('Note that you have to know your file name to open it.')
                HNoFA= input('Now type name of the file you want to convert it without it\'s extention: ')
                HEoFA= input('And now type it\'s extention (REAL): ')
            
                FDest= Src + HNoFA + '.' + HEoFA            
            
                if os.path.exists(FDest)== True:
                    NFEA= input('Finally type each extention you want to convert your file: ')   #NFE means New File Extention
                    if len (NFEA) >= 2 and len (NFEA) <= 4:
                        os.rename(FDest, Src + HNoFA + '.' + NFEA)
                        opeE= open(PyLib + 'XFSVTXT.py', mode= 'w')
                        opeE.write(
                                   'svflAN=  ' + '\''  + HNoFA + '\'' + '\n'     #Name
                                   'svflARE= ' + '\''  + HEoFA + '\'' + '\n'     #Real  Extention
                                   'svflANE=  ' + '\'' + NFEA  + '\'' + '\n \n'  #New Extention
                                   
                                   'svflBN = ' + '\'' + svflBN  + '\'' + '\n'
                                   'svflBRE= ' + '\'' + svflBRE + '\'' + '\n'
                                   'svflBNE= ' + '\'' + svflBNE + '\'' + '\n\n'
                                   
                                   'svflCN = ' + '\'' + svflCN  + '\'' + '\n'
                                   'svflCRE= ' + '\'' + svflCRE + '\'' + '\n'
                                   'svflCNE= ' + '\'' + svflCNE + '\'' + '\n\n'
                                                                                )
                        opeE.close()
                        print('File has been successfully converted.')
                        HorN= input('Now do you want to hide it? \n 1-YES \n2-NO\n\n')
                        if HorN == '1':
                            shutil.move(Src + HNoFA + '.' + NFEA, 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\' )
                            print('Your file is hidden now.')
                        if HorN == '2':
                            pass
                        else:
                            print('Invalid request.')
                    else:
                        print('New file extention is incorrect.')
                else:
                    print('File name is incorrect.')
                          
            if Convert== '2':
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflAN + '.' + svflANE) == True:
                    shutil.copy('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflAN + '.' + svflANE, Src )
                    os.rename(Src + svflAN + '.' + svflANE, Src + svflAN + '.' + svflARE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease DELETE your file after your work.')
                
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflAN + '.' + svflANE) == False:
                    if os.path.exists(Src + svflAN + '.' + svflANE) == True:
                        os.rename(Src + svflAN + '.' + svflANE, Src + svflAN + '.' + svflARE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease re-convert your file after your work.')                        
                    if os.path.exists(Src + svflAN + '.' + svflANE) == False:
                        print('We couldn\'t find file name with this name. Re-check your file name.')
            else:
                print('Invalid request.')
                
                
                
        if svfl == 'B':
            Convert= input('OK. Now let us know what you want to do with file B? \n1-Convert and Hide file \n2-Show file')
            
            if Convert== '1':
                print('First of all copy Video that you want to hide in source folder \n(C:\RIP\Programs\Saves\)')
                print('Note that you have to know your file name to open it.')
                HNoFB= input('Now type name of the file you want to convert it without it\'s extention: ')
                HEoFB= input('And now type it\'s extention (REAL): ')
            
                FDest= Src + HNoFB + '.' + HEoFB            
            
                if os.path.exists(FDest)== True:
                    NFEB= input('Finally type each extention you want to convert your file: ')   #NFE means New File Extention
                    if len (NFEB) >= 2 and len (NFEB) <= 4:
                        os.rename(FDest, Src + HNoFB + '.' + NFEB)
                        opeE= open(PyLib + 'XFSVTXT.py', mode= 'w')
                        opeE.write('svflAN = ' + '\'' + svflAN  + '\'' + '\n'
                                   'svflARE= ' + '\'' + svflARE + '\'' + '\n'
                                   'svflANE= ' + '\'' + svflANE + '\'' + '\n\n'
                                   
                                   'svflBN=  ' + '\''  + HNoFB + '\'' + '\n'     #Name
                                   'svflBRE= ' + '\''  + HEoFB + '\'' + '\n'     #Real  Extention
                                   'svflBNE=  ' + '\'' + NFEB  + '\'' + '\n \n'  #New Extention
                                   
                                   'svflCN = ' + '\'' + svflCN  + '\'' + '\n'
                                   'svflCRE= ' + '\'' + svflCRE + '\'' + '\n'
                                   'svflCNE= ' + '\'' + svflCNE + '\'' + '\n\n'
                                                                                )
                        opeE.close()
                        print('File has been successfully converted.')
                        HorN= input('Now do you want to hide it? \n 1-YES \n2-NO\n\n')
                        if HorN == '1':
                            shutil.move(Src + HNoFB + '.' + NFEB, 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\' )
                            print('Your file is hidden now.')
                        if HorN == '2':
                            pass
                        else:
                            print('Invalid request.')
                    else:
                        print('New file extention is incorrect.')
                else:
                    print('File name is incorrect.')
                          
            if Convert== '2':
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflBN + '.' + svflBNE) == True:
                    shutil.copy('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflBN + '.' + svflBNE, Src)
                    os.rename(Src + svflBN + '.' + svflBNE, Src + svflBN + '.' + svflBRE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease DELETE your file after your work.')
                
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflBN + '.' + svflBNE) == False:
                    if os.path.exists(Src+ svflBN + '.' + svflBNE) == True:
                        os.rename(Src + svflBN + '.' + svflBNE, Src + svflBN + '.' + svflBRE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease re-convert your file after your work.')                        
                    if os.path.exists(Src + svflBN + '.' + svflBNE) == False:
                        print('We couldn\'t find file name with this name. Re-check your file name.')
            else:
                print('Invalid request.')
                
                
                
        if svfl == 'C':
            Convert= input('OK. Now let us know what you want to do with file C? \n1-Convert and Hide file \n2-Show file')
            
            if Convert== '1':
                print('First of all copy Video that you want to hide in source folder \n(C:\RIP\Programs\Saves\)')
                print('Note that you have to know your file name to open it.')
                HNoFC= input('Now type name of the file you want to convert it without it\'s extention: ')
                HEoFC= input('And now type it\'s extention (REAL): ')
            
                FDest= Src + HNoFC + '.' + HEoFC            
            
                if os.path.exists(FDest)== True:
                    NFEC= input('Finally type each extention you want to convert your file: ')   #NFE means New File Extention
                    if len (NFEC) >= 2 and len (NFEC) <= 4:
                        os.rename(FDest, Src + HNoFC + '.' + NFEC)
                        opeE= open(PyLib + '\\' +'XFSVTXT.py', mode= 'w')
                        opeE.write('svflAN = ' + '\'' + svflAN  + '\'' + '\n'
                                   'svflARE= ' + '\'' + svflARE + '\'' + '\n'
                                   'svflANE= ' + '\'' + svflANE + '\'' + '\n\n'
                                   
                                   'svflCN = ' + '\'' + svflBN  + '\'' + '\n'
                                   'svflCRE= ' + '\'' + svflBRE + '\'' + '\n'
                                   'svflCNE= ' + '\'' + svflBNE + '\'' + '\n\n'
                                   
                                   'svflCN=  ' + '\''  + HNoFC + '\'' + '\n'     #Name
                                   'svflCRE= ' + '\''  + HEoFC + '\'' + '\n'     #Real  Extention
                                   'svflCNE=  ' + '\'' + NFEC  + '\'' + '\n \n'  #New Extention
                                                                               )
                        opeE.close()
                        print('File has been successfully converted.')
                        HorN= input('Now do you want to hide it? \n 1-YES \n2-NO\n\n')
                        if HorN == '1':
                            shutil.move(Src + HNoFC + '.' + NFEC, 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\' )
                            print('Your file is hidden now.')
                        if HorN == '2':
                            pass
                        else:
                            print('Invalid request.')
                    else:
                        print('New file extention is incorrect.')
                else:
                    print('File name is incorrect.')
                          
            if Convert== '2':
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflCN + '.' + svflCNE) == True:
                    shutil.copy('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflCN + '.' + svflCNE, Src )
                    os.rename(Src + svflCN + '.' + svflCNE, Src + svflCN + '.' + svflCRE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease DELETE your file after your work.')
                
                if os.path.exists('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\XFSAVES\\Files\\'+ svflCN + '.' + svflCNE) == False:
                    if os.path.exists(Src + svflCN + '.' + svflCNE) == True:
                        os.rename(Src + svflCN + '.' + svflCNE, Src + svflCN + '.' + svflCRE)
                    print('Your file is in source folder now. We have it in our secret folder. \nPlease re-convert your file after your work.')                        
                    if os.path.exists(Src + svflCN + '.' + svflCNE) == False:
                        print('We couldn\'t find file name with this name. Re-check your file name.')
            else:
                print('Invalid request.')    





    if MC== '6':
        RIP_WEB= 'http://RIPgroup.ir/'
        webbrowser.open_new_tab(RIP_WEB)
        print('Browser is opening... \n')
        
        
        
        
        
        
        


        '''
            #os.execl(sys.executable, sys.executable, *sys.argv)
            #We can use code below instead of upper line:
            #os.execv(sys.executable, ['python'] + sys.argv)
                                                                '''
