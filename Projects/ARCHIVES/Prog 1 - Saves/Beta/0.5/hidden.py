svtxtA= 'NO SAVED TEXT HERE.'
svtxtB= 'NO SAVED TEXT HERE'
svtxtC= 'NO SAVED TEXT HERE'
svtxtD= 'NO SAVED TEXT HERE'
svtxtE= 'NO SAVED TEXT HERE'

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
    
    if svtxt == 'B':
        print(svtxtB)
    
    if svtxt == 'C':
        print(svtxtC)
    
    if svtxt == 'D':
        print(svtxtD)
    
    if svtxt == 'E':
        print(svtxtE)

    if svtxt != 'A' and svtxt != 'B' and svtxt != 'C' and svtxt != 'D' and svtxt != 'E':
        print('Nothing saved with this name.')    

if MC== 'Saved_Numbers':
    svtxt= input('Choose which saved NUMBER you want? A,B,C,D,E')
    if svtxt == 'A':
        print(svnomA)
    
    if svtxt == 'B':
        print(svnomB)
    
    if svtxt == 'C':
        print(svnomC)
    
    if svtxt == 'D':
        print(svnomD)
    
    if svtxt == 'E':
        print(svnomE)

    if svnom != 'A' and svnom != 'B' and svnom != 'C' and svnom != 'D' and svnom != 'E':
        print('Nothing saved with this name.')

else:
    print('No topic have been saved with this name')


