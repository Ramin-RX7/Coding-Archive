import getpass, hashlib, os
import rx7 as rx

print = rx.style.print


def pause(prompt='Press Enter To Continue ...'):
    '''
    Disable terminal echo and wait for 'Enter' button
    '''
    print(prompt)#,end='')
    getpass.getpass('')


def get_files(prompt='Enter File Name:  ', check_if_exists=True, sort= False, times=100):
    '''
    Prompt repeated  'Enter File Name:'  input until user enter 'end'
    if check_if_exists is false it will add files even if they do not exist
    by default list of files are sorted by input order 
    but if sort=True they will be sorted by their name
    '''
    List = set()
    i = 1
    while i <= times:
        filename = rx.io.wait_for_input(prompt)
        if filename == 'end':
            break
        pass
        if check_if_exists:
            if rx.files.exists(filename):
                List.add(filename)
                i+=1
            else:
                rx.style.print('File Does Not Exist.')
        else:
            i+=1
            List.add(filename)
    if sort:
        return sorted(list(List))
    return list(List)


def set_title(title):
    rx.terminal.getoutput(f'title {title}')


def minimize():
    import ctypes
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )


def readable_num(num):
    num = [str(a) for a in str(num)]
    length = len(num)
    i = int(length)
    while i > 3:
        num.insert(i-3,',')
        i -= 3
    return "".join(num)
