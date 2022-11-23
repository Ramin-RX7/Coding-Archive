'''
This Module is One to Make Your Code Shorter.
High API Will Make You Feel You're Ordering And Machine Is Doing!
Also There is Collection of most usefull function and methods from popular modules of python.
(Read Help of Functions)
Official Documention Will Be Added Soon.
'''
'''
Written By RX
Last Update: 06-01-2020
'''

__version__='2.2.2'




#START
import os,time,sys,socket,psutil,subprocess,shutil
import random as _Random
from typing import Any, Union

OS =  __import__('platform').system()

#######        8888888888                         888    d8b                                   ####### 
 #####         888                                888    Y8P                                    #####  
  ###          888                                888                                            ###   
   #           8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b            #    
   #           888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K                #    
  ###          888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b.          ###   
 #####         888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88         #####  
#######        888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'        ####### 


p= print

def repeat(function,n: int, **kwargs):
    '''
    Repeat function for n times
    for more info see the example below.
    Example:
        re(Func_Name, 3)
        ==> "function Func_Name will launch 3 times."
    '''
    for _ in range(n):
        function(**kwargs)

def rev(var:Any):
    '''
    This function is for reversing Strings, Lists, Tuples And also Integers.
    Example:
        b= rev('Football')
        print(b)
        ==> llabtooF
    '''
    ret=var
    if type(ret)==int or type(ret)==float:
        ret= str(ret)
        ret= ret[::-1]
        if type(var)==int:
            ret= int(ret)
        else:
            ret=float(ret)
    else:
        ret= ret[::-1]
    return ret

wait = time.sleep

def cls():
    '''
    You can use this function if you want to clear the environment.
    '''
    if OS == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def progressbar(total=100,dashes_nom=100,delay=1,dashes_shape=' ',complete_shape='█',pre_text='Loading: ',
                left_port='|',right_port='|'):
    '''
    Use this function to make a custom in-app progress bar.
    Example:
        progressbar(Total=100,Dashes_Nom=10,Time=1,Dashes_Shape='-',Complete_Shape='#', Pre_Text='Loading')
        ==>   Loading|####------| 40/100
    '''
    def Progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write("%s%s%s%s%s %i/%i\r" % (prefix, right_port, complete_shape*x, dashes_shape*(size-x), left_port, j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()
    for i in Progressbar(range(total), pre_text, dashes_nom):
        wait(delay)

def wait_for(button):
    '''
    If You Want to Wait For the User to Press a Key (Keyboard or Mouse) Use This Function.
    '''
    if button.lower() in ('middle','left','right','back','forward'):
        if button.lower()[:1]=='b':
            button='x'
        if button.lower()[:1]=='f':
            button='x2'
        import mouse
        mouse.wait(button)
    else:
        import keyboard
        try:
            keyboard.wait(button)
        except:
            raise ValueError('Incorrect Button Name.')

call_later = __import__('keyboard').call_later


def Input(prompt='', default_value=''):
    '''
    Make Default Value For Your Input!  
    (THIS ONLY WORK ON WINDOWS (SORRY))
    prompt is what you want and it's input(prompt) .
    default_value is what there should be after prompt.
    E.g: 
       >>> Input('Is rx7 Library Easy to Learn?  ', 'Yes')
       Is rx7 Library Easy to Learn?  Yes
    '''
    import win32console
    _stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
    keys = []
    for c in default_value:
        evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
        evt.Char = c
        evt.RepeatCount = 1
        evt.KeyDown = True
        keys.append(evt)
    _stdin.WriteConsoleInput(keys)
    return input(prompt)

def restart_app():
    '''
    This Function Close App and Recall it From Terminal
    '''
    os.system('clear')
    os.execv(sys.executable, ['python'] + sys.argv)

import pyautogui
active_window_title = pyautogui.getActiveWindowTitle()

def open_image(path):
    '''
    Open image file with default image viewer.  
    (Mac OS is not supported yet)
    '''
    if OS == 'Windows':
        os.system(str(path))
    elif OS == 'Linux':
        subprocess.getoutput(f'xdg-open {path}')
    else:
        raise OSError('OS X is not supported for this function.')

URL_BASENAME=''
def download(url,filename=URL_BASENAME, save_memory=True, progressbar=True, prefix='Downloading'):
    '''
    Use this function to download files.  
    if filename is not given, it will be last part of the url.  
    filename can be path for saving file.  
    save_ram parameter is used to save memory in large files (save directly to storage)

    '''
    import requests,urllib
    if not filename: filename = url.split('/')[-1]
    pass
    if save_memory:
        '''with urllib.request.urlopen(url) as response, open(filename, 'wb') as f:
            shutil.copyfileobj(response, f)'''
        '''r = requests.get(url, stream = True)
        with open(filename,"wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)'''
        if progressbar:
            with open(filename, "wb") as f:
                response = requests.get(url, stream=True)
                total_length = response.headers.get('content-length')
                if total_length is None:
                    f.write(response.content)
                else:
                    dl = 0
                    done=0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(33 * dl / total_length)
                        sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| {100-((33-done)*3)}%")
                        sys.stdout.flush()
                    if 100-((33-done)*3) == 96:
                        sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| 100%")
                        sys.stdout.flush()
        else:
            with open(filename, "wb") as f:
                response = requests.get(url, stream=True)
                for data in response.iter_content(chunk_size=4096):
                    f.write(data)               
    else:
        def report(blocknr, blocksize, size):
            if progressbar:
                current = blocknr*blocksize
                sys.stdout.write("\rDownloading {1}:  {0:.2f}%".format(100.0*current/size,filename))
        def downloadFile(url):
            urllib.request.urlretrieve(url, filename, report)
        downloadFile(url)
    pass
    if progressbar: print()

def convert_bytes(num:int) -> str :
    """
    Convert num to idiomatic byte unit.
    num is the input number (bytes).
    
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0




######################
#  TUPLE FUNCSTIONS  #
######################
def force(tpl: Any, *var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    It returns tpl with adding var(s) to it.
    '''
    return tuple(list(tpl)+[v for v in var])
#force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])

def erase(tpl: tuple, *var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    It returns tpl with removing var(s) from it.
    '''
    #lstv= [v for v in var if v in tpl]
    lstt= list(tpl)
    for th in [v for v in var if v in tpl]:
        lstt.remove(th)
    return tuple(lstt)

def replace(tpl: tuple, ind: Union[int,str], var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Replace tpl[ind] with var
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl[ind]=var
    return tuple(tpl)

def insert(tpl: tuple, ind: Union[int,str], var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Exactly like tpl[ind]=var in lists but for tuples.
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl.insert(ind,var)
    return tuple(tpl)   


class Check_Type:
    """
    Function decorator for developers\n
    Use this decorator to check if user gives right argument type\n
    You need to annotate argument type when defining it.\n
    Supported Types:
    * str
    * list
    * set
    * dict
    * tuple
    * User-Defined Objects
    Typing Module Supported Types:
    * Iterable
    * Callable
    * Generatr
    * Container
    * Any
    (MORE TYPES SOON ...)
    """
    auto_correct = False

    def __init__(self, function): 
        self.function = function


    def __call__(self, *args, **kwargs): 
        special_types = ('callable', 'iterable', 'generator','container', 'any')

        i=-1
        __local__= list(locals()['args'])
        annots= list(self.function.__annotations__.keys())

        def extra_remover(correct):
            # Typing module annots check
            if correct.startswith('typing.'):
                correct = correct[7:].lower()

            # built-in types check
            elif correct.startswith('<class '):
                correct = correct[8:-2]

            return correct

        def check_specials(TYPE, LOCAL_I):
            import inspect
            wrong = ''
            if TYPE == 'generator':
                if inspect.isgeneratorfunction(LOCAL_I) or inspect.isgenerator(LOCAL_I):
                    return
                else:
                    correct = 'generator'

            elif TYPE == 'callable':
                if callable(LOCAL_I):
                    return
                else:
                    correct = 'callable'
            
            elif TYPE == 'iterable':
                if type(LOCAL_I) in (list, tuple, set, str):
                    print(type(LOCAL_I))
                    return
                else:
                    correct = 'iterable'

            elif TYPE == 'container':
                if type(LOCAL_I) in (list,set,dict,tuple):
                    return
                else:
                    correct = 'container'

            elif TYPE == 'any':
                return

            wrong = extra_remover(str(type(LOCAL_I))) if not wrong else wrong
            func_name = self.function.__name__
            Error= TypeError(f"'{func_name}()' argument '{ARG}' must be '{correct}' (not '{wrong}')")
            raise Error

        for ARG in annots:
            i += 1
            try:
                LOCAL_I = __local__[i]
                correct = str(self.function.__annotations__[ARG])
                
                '''if correct.startswith('typing.Union'):
                    correct = eval(correct[12:])
                if type(correct) != list:
                    correct = [correct]'''

                correct = extra_remover(correct)
                
                if correct in special_types:
                    print(type(LOCAL_I))
                    check_specials(correct,LOCAL_I)
                
                # Builtins and other Libraries objects
                elif not eval(correct) == type(LOCAL_I):
                    if Check_Type.auto_correct:
                        try:
                            __local__[i] = eval(correct)(LOCAL_I)
                            continue
                        except ValueError:
                            pass

                    wrong = extra_remover(str(type(LOCAL_I)))
                    #correct = str(self.function.__annotations__[ARG])#[8:-2]
                    correct = extra_remover(correct)
                    func_name = self.function.__name__
                    Error= TypeError(f"'{func_name}()' argument '{ARG}' must be '{correct}' (not '{wrong}')")
                    raise Error
            
            except (ValueError,IndexError):
                pass#raise
            except NameError:
                raise

            
        
        return self.function(*__local__, **kwargs)








#######         .d8888b.   888  888                                                         #######
 #####         d88P  Y88b  888  888                                                          ##### 
  ###          888    888  888  888                                                           ###  
   #           888         888  888   8888b.   .d8888b   .d8888b    .d88b.   .d8888b           #   
   #           888         888  888      "88b  88K       88K       d8P  Y8b  88K               #
  ###          888    888  888  888  .d888888  "Y8888b.  "Y8888b.  88888888  "Y8888b.         ###  
 #####         Y88b  d88P  888  888  888  888       X88       X88  Y8b.           X88        ##### 
#######         "Y8888P"   888  888  "Y888888   88888P'   88888P'   "Y8888    88888P'       #######


class system:
    '''
    Some system actions and information.
    - Information about ram, ip, terminal, etc.
    - Some System Actions like Shutdown and Restart
    '''

    accname       =  os.getlogin
    pid           =  os.getpid
    chdir         =  os.chdir
    cwd           =  os.getcwd
    terminal_size =  shutil.get_terminal_size    
    boot_time     =  psutil.boot_time
    device_name   =  socket.gethostname
    ip_website    =  socket.gethostbyname

    #RAM = psutil.virtual_memory()
    #ram_total        = RAM[0] 
    #ram_used         = RAM[3]
    #ram_free         = RAM[1]
    #ram_free_percent = RAM[2]
    def ram_total(convert=True):
        """
        Return total ram of board as string
        parameter convert: flag for convert mode (using of convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[0]))
        return str(response[0])
    @staticmethod
    def ram_used(convert=True):
        """
        Return how much ram is using.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[3]))
        return str(response[3])
    @staticmethod
    def ram_free(convert=True):
        """
        Return how much ram is available.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[1]))
        return str(response[1])
    @staticmethod
    def ram_percent(ONLY_NOM=False):
        """
        Return available ram percentage as an integer if ONLY_NOM, as string with % if not ONLY_NOM
        Parameter ONLY_NOM: flag for return type and value.
        """
        response = list(psutil.virtual_memory())
        if ONLY_NOM:
            return response[2]    
        return str(response[2]) + " %"
    


    @staticmethod
    def convert_bytes(num:int) -> str :
        """
        Convert num to idiomatic byte unit.
        num is the input number (bytes).

        >>> convert_bytes(200)
        '200.0 bytes'
        >>> convert_bytes(6000)
        '5.9 KB'
        >>> convert_bytes(80000)
        '78.1 KB'
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0
    @staticmethod
    def SHUT_DOWN():
        '''
        Shut down the PC.
        '''
        os.system("shutdown /s /t 1")
    @staticmethod
    def RESTART():
        '''
        Restart the PC.
        '''
        os.system("shutdown /r /t 1")

    @staticmethod
    def ip_global():
        """
        Return ip with by http://ipinfo.io/ip api.
        returns global ip as string
        """
        import requests,re
        try:
            new_session = requests.session()
            response = new_session.get("http://ipinfo.io/ip")
            ip_list = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
            new_session.close()
            return ip_list[0]
        except:
            class ConnectionError(requests.exceptions.ConnectionError):
                def __init__(self, message): super().__init__(message)
            raise ConnectionError('No Internet Connection')
    @staticmethod
    def ip_local():
        """
        Return local ip of computer in windows by socket module
        and in unix with hostname command in shell.
        """
        #return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
        '''
        class NetworkError(Exception):
            def __init__(self, message): super().__init__(message)
        try:
            ip = socket.gethostbyname(socket.gethostname())
            if ip and ip != "127.0.1.1":
                return ip
            elif OS != "Windows":
                command = subprocess.Popen(["hostname", "-I"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise ###!!!

    @staticmethod
    def win10_notification(title,message,icon=None, duration=5) -> None:
        '''
        (THIS ONLY WORKS FOR "WINDOWS 10")\n
        Display Notification with title, message and icon for speciefic time.
        '''
        from win10toast import ToastNotifier
        ToastNotifier().show_toast(title,message,duration=duration)


class files:
    '''
    Actions and information about files.\n
    (READ FUNCTIONS DOCSTRING)

    GET INFORMATION:
      - exists()
      - size()
      - abspath()
      - mdftime()
      - acstime()
      - content (read function)()
      - is file()
      - is dir()
      - is readonly()
      - is hidden()

    ACTIONS:
      - remove()
      - rename()
      - move()
      - copy()
      - hide()
      - read only()
      - write()

    TODO: self.info: size-atime-mtime-hide-ronly
    '''
    
    size    = os.path.getsize
    rename  = os.rename
    abspath = os.path.abspath
    exists  = os.path.exists
    mdftime = os.path.getmtime
    acstime = os.path.getatime
    move    = shutil.move
    isdir = os.path.isdir
    isfile = os.path.isfile

    @staticmethod
    def remove(path,force=False):
        '''
        Use this to delete a file or a directory.
        If force is True it will delete non-empty directories.
        '''
        if os.path.isfile(path):
            os.remove(path)
        else:
            if force: 
                shutil.rmtree(path)
            else:
                try:
                    os.rmdir(path)
                except OSError:
                    raise OSError(f"[WinError 145] The directory is not empty: '{path}'" + '\n' + ' '*23 + 
                                   '(Use force=True as an argument of remove function to remove non-empty directories.)')               
    @staticmethod
    def copy(src,dest,preserve_metadata= True):
        '''
        Copy the file from src to destination.  
        preserve_metadata is for preserving metadata of file when copying.
        (You can use it instead of rename too.
         e.g:
            copy('D:\\Test.py','E:\\Ali.py')
            (It copies Test.py to E drive and renames it to Ali.py)
         )
        '''
        if files.isdir(src):
            shutil.copytree(src,dest)
        else:
            if preserve_metadata: shutil.copy2(src,dest)
            else: shutil.copy(src,dest)
    @staticmethod
    def hide(path, mode:bool =True):
        '''
        Hide file or folder.
        If mode==False: makes 'not hide'
        '''
        if mode:
            os.system("attrib -h "+path)
        else:
            subprocess.check_call(["attrib","+H",path])
    @staticmethod
    def read_only(path, mode:bool =True):
        '''
        Make file attribute read_only.
        If mode==False: makes 'not read_only'
        '''
        from stat import S_IREAD,S_IWUSR
        if mode==True:
            os.chmod(path, S_IREAD)
        elif mode==False:
            os.chmod(path, S_IWUSR)
    @staticmethod
    def read(path):
        '''
        This can help you to read your file faster.
        Example:
            read('C:\\users\\Jack\\test.txt')
            ==> "Content of 'test.txt' will be shown."
        '''
        op= open(path,mode='r')
        FileR= op.read()
        op.close()
        return FileR
    @staticmethod
    def write(file, text='',mode='replace',start=''):
        '''
        With this method you can change content of the file.  
        file:   File you want to change its content.
        content:   Content you want to add to file.
        mode:   Type of writing method.
             'a' or 'continue' for add content to end of the file. 
             'w' or 'replace'  for overwriting to file content.
        start: I use this when I use mode='continue'
        '''
        if not text:
            text = ''
        if not start:
            start = ''
        pass
        if mode in ('replace', 'w', 'continue', 'a'):
            if mode in ('replace', 'w'):
                mode = 'w'
            elif mode in ('continue', 'a'):
                mode = 'a'

            with open(file, mode=mode) as f:
                f.write(str(start)+str(text))

        else:   
            raise ValueError(f'mode can only be: 1-replace(default)  2-continue\nNot "{mode}"') 

    @staticmethod
    def is_readonly(path):
        '''
        Return True if path is readonly else False.
        (May Not Work in Linux)
        '''
        return subprocess.getoutput(f'dir /ar {path} >nul 2>nul && echo True || echo False')
    @staticmethod
    def is_hidden(path):
        """
        Check whether a file is presumed hidden, either because
        the pathname starts with dot or because the platform
        indicates such.
        Return True if File or Directory is hidden.
        (Work on both Linux and Windows)
        """
        full_path = files.abspath(path)
        name = os.path.basename(full_path)
        def no(path): return False
        platform_hidden = globals().get('is_hidden_' + OS, no)
        return name.startswith('.') or platform_hidden(full_path)
    @staticmethod
    def is_hidden_Windows(path):
        import ctypes
        res = ctypes.windll.kernel32.GetFileAttributesW(path)
        assert res != -1
        return bool(res & 2)
    @staticmethod
    def search_file(pattern, path='.\\',return_mode: Union['list','generator']= 'list'):
        '''
        Search for files in path.
        Return list or generator.
        pattern:
        -  'x.py'  :    search for 'x.py' in path.
        -  '*.py'  :    search for all files with .py extension in path.
        -  '*.*'   :    search for all files in path
        -  '**/*'  :    search for any file in path and also all sub-directories.
        -  '**/*.py:    search for all python files in path and also sub-directories.
        -  'mydir/**/*.py'   :    search for all python files in path/mydir/ and all of its sub-directories.
        '''
        import glob
        if str(return_mode).lower() in ('list','generator'):
            if return_mode=='list':
                return glob.glob(pattern, recursive=True)
            else:
                return glob.iglob(pattern, recursive=True)
        else:
            if type(return_mode)==str:
                raise ValueError(f"return_mode van be  'list'  or  'generator'  not {return_mode}")
            else:
                raise TypeError(f"return_mode type should be str and it should be in ['list', 'generator']")
    @staticmethod
    def search_content(path,word):
        ALL= [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(path)] for val in sublist]
        '''lst=[]
        for file in ALL:
            if word in rx.read(file):
                lst.append(file)
        return lst'''
        return [FILE for FILE in ALL if word in open(FILE).read()]
    @staticmethod
    def mkdir(path):
        path = os.path.normpath(path)
        NEW= ''
        for FILE in path.split('\\'):
            NEW+= FILE+'\\'
            try: os.mkdir(NEW)
            except (FileExistsError,FileNotFoundError): pass
    @staticmethod
    def generate_tree(dir_path, level: int=-1, limit_to_directories: bool=False,
            length_limit: int=1000, print_info: bool=True):
        """Given a directory Path object return a visual tree structure"""
        from pathlib import Path
        from itertools import islice
        space= '    '; branch = '│   '; tee= '├── '; last= '└── '
        dir_path = Path(dir_path) # accept string coerceable to Path
        files = 0
        directories = 0
        def inner(dir_path: Path, prefix: str='', level=-1):
            nonlocal files, directories
            if not level:  return # 0, stop iterating
            if limit_to_directories: contents = [d for d in dir_path.iterdir() if d.is_dir()]
            else:  contents = list(dir_path.iterdir())
            pointers = [tee] * (len(contents) - 1) + [last]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield prefix + pointer + path.name
                    directories += 1
                    extension = branch if pointer == tee else space 
                    yield from inner(path, prefix=prefix+extension, level=level-1)
                elif not limit_to_directories:
                    yield prefix + pointer + path.name
                    files += 1
        RETURN=''
        RETURN+=dir_path.name+'\n'
        iterator = inner(dir_path, level=level)
        for line in islice(iterator, length_limit): RETURN+=line+'\n'
        if next(iterator, None): RETURN+=f'... length_limit, {length_limit}, reached, counted:'
        if print_info: RETURN+=f'\n{directories} directories' + (f', {files} files' if files else '')
        return RETURN

    class MEMBERS:
        @staticmethod
        def all_exactdir(dir):
            return os.listdir(dir)
        @staticmethod
        def all_all_sep(dir):
            return [i for i in os.walk(dir)]
        @staticmethod
        def files_exactdir(dir):
            return [i for i in os.walk(dir)][0][2]
        @staticmethod
        def files_all(dir):
            return [val for sublist in [[os.dir.join(i[0], j) for j in i[2]] for i in os.walk(dir)] for val in sublist]
        @staticmethod
        def files_all_sep(dir):
            return [[os.dir.join(i[0], j) for j in i[2]] for i in os.walk(dir)]
        @staticmethod
        def dirs_exactdir(dir):
            return sorted([i for i in os.listdir(dir) if i not in [i for i in os.walk(dir)][0][2]])
        @staticmethod
        def dirs_all(dir):
            return [TPL[0] for TPL in [i for i in os.walk(dir)]]
read= files.read
write= files.write

class random:
    '''
    Random Variable Generator Class.
    '''
    @staticmethod
    def choose(iterator,k: int =1,duplicate=True):
        '''
        Return a random element from a non-empty sequence.
        '''
        if type(k)!=int: raise TypeError('k must be integer.')
        pass
        if k==1:
            return _Random.choice(iterator)
        elif k>1:
            if duplicate:
                return _Random.choices(iterator,k=k)
            else:
                return _Random.sample(iterator,k=k)
        else:
            raise ValueError('k Must Be Higher 0')
        
    integer = _Random.randint

    @staticmethod
    def O1(decimal_number=17):
        '''
        return x in the interval [0, 1)
        '''
        return round(_Random.random(),decimal_number)
        
    number =  _Random.uniform


class style:
    '''
    This class is for Changing text Color,BG & Style.
    - style.print  to customize your print.
    - style.switch to change terminal colors.
    - style.switch_default for making everything default.
    '''
    def __init__(self,text,color='default',BG='black'):
        from colored import fg,bg,attr
        try: color= color.lower();BG=BG.lower()#;style=style.lower()
        except:pass        
        if color=='default':
            color=7 #188
        self.text= text     
        self.content= f"{fg(color)}{bg(BG)}{text}{attr(0)}"
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content
    def __add__(self,other):
        #print(type(other))
        if type(other)!=style:
            return self.content+other
        else:
            return self.content+other.content
    def __mul__(self,nom):
        return self.content*nom
    def __getitem__(self,index):
        return self.text[index]


    @staticmethod
    def print(text='',color='default',BG='default',style='None',end='\n'):
        '''
        text(text='Hello World',color='red',BG='white')
        output ==> 'Hello World' (With red color and white BG)
        Styles: bold - underline - reverse - hidden
         *bold and underline may not work. (Depends on terminal and OS)
        '''
        from colored import fg,bg,attr
        try: color= color.lower();BG=BG.lower();style=style.lower()
        except:pass
        if color=='default':
            color=7 #188
        if style=='none':
            style=0
        if color=='default' and BG!='default':
            print('%s%s%s%s' % (attr(style),bg(BG),text,attr(0)),end=end)
        if color!='default' and BG=='default':
            print('%s%s%s%s' % (attr(style),fg(color),text,attr(0)),end=end)
        if color=='default' and BG=='default':
            print('%s%s%s%s%s' % (attr(style),bg(BG),fg(color),text,attr(0)),end=end)

    @staticmethod
    def switch(color='default',BG='black',style='None'):
        '''
        Change color,BG and style untill you call it again and change them.
        '''
        try: color= color.lower();BG=BG.lower();style=style.lower()
        except:pass        
        if style=='none':
            style=0
        if color=='default':
            color=7
        from colored import fg,bg,attr
        print('%s%s%s' % (attr(style),bg(BG),fg(color)),end='')
    @staticmethod
    def switch_default():
        '''Switch Terminal Attributes to its defaults'''
        from colored import attr
        print('%s' % (attr(0)),end='')


class record:
    '''
    Use this method to record an action time in second.
    Usage:
        Start= record()
        #Some codes here...
        Finnish= Start.lap()
        print(Finnish) ==> 0.25486741
        #Some more codes here...
        Finnish= Start.lap() ==> 0.4502586
        Start.laps -->  [0.25486741, 0.4502586]
    Use Start.stop() to finnish recording and save memory.
    (after self.stop() using self.lap will cause error.)
    '''
    def __init__(self):
        self.__start= time.time()
        self.__end__=False
        self.laps=[]
    def __str__(self):
        if not self.__end__:
            running=True
        else:
            running=False
        return f'Running={str(running)} \nLaps: {self.laps}'
    def __repr__(self):
        if not self.__end__:
            running=True
        else:
            running=False
        return f'Running={str(running)} \nLaps: {self.laps}'

    class EndError(Exception):
        def __init__(self, message='Recording Has Been Finnished. Can Not Add a Lap.'):
            super().__init__(message)
    def lap(self,save=True, Round=15):
        '''
        Return time passed from creating time of self.
        (Read 'record' Doc String)
        If save is True, time will be added to self.laps
        '''        
        if not self.__end__:
            lp= round(time.time()-self.__start,Round)
            if save:
                self.laps.append(lp)
            return lp
        raise self.EndError
    def stop(self):
        self.__end__=True
        '''del self
        return self.laps'''
    def reset(self,reset_start= False):
        '''
        This will erase self.laps 
        If reset_start is True, start time will reset too.
        '''
        self.laps= []
        if reset_start: self.__start= time.time()


class Tuple:
    '''
    (Note That This is tuple of RX7 Module So it Has More Features!)\n
    (This is Not Built-in immutable sequence.)\n
    If no argument is given, the constructor returns an empty tuple.\n
    There is *var argumant that you can add object as much as you need.\n
    Any Built-in object is accepted. (Not tested on third-party objects.)\n
    Beside built-in features of tuple, this supports:
    + You Can Add objects to your tuple now.
    + Also You Can Delete Them.
    + Replace Them.
    + Like lists, Tuple supports item assigning. ( tpl[2]='hello' )
    (Tuple Unpacking is Supported.)
    '''
    #############################
    def __init__(self,*var: Any, one_item=False):
        if not one_item:
            self.__content= tuple(var)
        else:
            self.__content=[]
            for item in var:
                for member in item:
                    self.__content.append(member)
            self.__content= tuple(self.__content)
    def __str__(self):
        return str(self.__content)
    def __repr__(self):
        return str(self.__content)
    #############################
    #############################
    def add(self,*var: Any):
        '''
        This will add var(s) to self.
        '''
        self.__content= tuple(list(self.__content)+[v for v in var])
        #force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])
    force= add
    def remove(self,*var: Any):
        '''
        It will remove var(s) from self.
        '''
        #lstv= [v for v in var if v in tpl]
        lstt= list(self.__content)
        for th in [v for v in var if v in self.__content]:
            lstt.remove(th)
        self.__content= tuple(lstt)
    erase= remove
    #############################
    #############################
    def replace(self, ind: Union[int,Any], var: Any):
        '''
        Replace self[ind] with var.
        '''
        tpl=list(self.__content)
        if type(ind) == str:
            ind= tpl.index(ind)
        tpl[ind]=var
        self.__content= tuple(tpl)
    def __setitem__(self,index,value,replace=False):
        if not replace:
            tpl=list(self.__content)
            if type(index) == str:
                ind= tpl.index(ind)
            tpl.insert(index,value)
            self.__content= tuple(tpl)            
        else:
            self.replace(index,value)
    def __getitem__(self,index):
        return self.__content[index]
    #############################
    def __add__(self,other):
        return self.__content + other
    #############################
    #############################
    def __bool__(self):
        return bool(len(self.__content))
    '''def __contains__(self,obj):
        return bool(obj in self.__content)'''
    def __hash__(self):
        return hash(self.__content)
    def __len__(self):
        return len(self.__content)
    #############################
    #############################


class Terminal:

    run = os.system

    getoutput = subprocess.getoutput
terminal = Terminal

#END
