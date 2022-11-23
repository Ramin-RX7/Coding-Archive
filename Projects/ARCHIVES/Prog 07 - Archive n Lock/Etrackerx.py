import rx7 as rx
import zipfile

main=True
while main:
    try:
        FILENAME= input('Enter File Name:  ')
        if FILENAME.endswith('.rx'):
            FILENAME=FILENAME[:-3]
        #print(FILENAME)
        if rx.file.exists(FILENAME+'.rx'):
            x=True
            i=0
            while x:
                PASW=input('Enter Password  (Old School)\n$ ')
                if PASW=='askaramp.r.e':
                    x=False
                else:
                    print('WORNG PASSWORD!')
                    i+=1                    
                    if i==4:
                        rx.file.delete(FILENAME+'.rx')
                        print('You Decided to Delete "'+FILENAME+'.rx"')
                        main=False
                        import getpass 
                        getpass.getpass(prompt='') 
                        exit()
            rx.file.rename(FILENAME+'.rx',FILENAME+'.zip')
            with zipfile.ZipFile(FILENAME+'.zip', 'r') as zipobj:
                #print(zipobj.namelist())
                zipobj.extractall(path=FILENAME)
            rx.file.rename(FILENAME+'.zip',FILENAME+'.rx')
            input(FILENAME+' Has Been Extracked.')
        else:
            print('Not Found!')
    except:
        print('Failed!')
    print()