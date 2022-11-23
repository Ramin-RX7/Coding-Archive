import threading, os, platform
from flask import Flask, render_template, render_template_string
import rx7 as rx

rx.style.print('[*] Operations Have Been Started','blue')
rx.style.print('[*] THIS WILL TAKE ABOUT 7 SECONDS','blue')
rx.style.print('[*] Use "Ctrl+C" to Close All Servers and Exit','blue',style='bold')

IP= rx.system.ip_local()
PROGRAMS_PATH= 'Programs/'





# Flask Functions
app= Flask(__name__)
#app.debug= True

@app.route('/')
def index(ip=IP,name='RX',lst=['dsf','dsd']):
    return render_template('index.html',
                                        IP= IP,
                                        PORT= 8080,
                                        name=name,
                                        lst=NEW_PATH,
                                        cwd= rx.system.cwd()
                                  )

# Pages
'''
@app.route('/post-1')
def post1():
    return 'content of Post with ID 1'

@app.route('/prog_list')
def prog_list():
    List= ['phux','dramax']
    dic= {PROG:PROGRAMS_PATH+PROG for PROG in List}
    return render_template('prog_list.html', dic=dic)    

@app.route('/prog/<PROG_NAME>')
def prog(PROG_NAME):
    return render_template('program_page.html', NAME=PROG_NAME)
'''

# Set Password For Page
'''
from functools import wraps
from flask import request, Response

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/program-page')
@requires_auth
def secret_page():
    return render_template('program_page.html')
'''


















NEW_PATH= {} #NEW_PATH:dict = {}
RUNNING_SERVERS= 0
def py_server(location, port, name=None):
    '''
    Run server from location on specifiec port
    '''
    '''try:
        if location[0]=='~': location= location[1:]
        if location[0]=='/': location= location[1:]
    except: pass'''
    global RUNNING_SERVERS
    RUNNING_SERVERS += 1
    t= threading.Thread(target=os.system,name=f"{name+' => ' if name else ''}{location} ==> {port}",
                        kwargs={'command':f'python -m http.server -b {IP} {port} -d {location}'}
                        )
    t.start()
    NEW_PATH[name if name else location]= [location,port]
    #rx.style.print(f'Running on {port} from {location}','yellow')
    rx.wait(0.1)

def console():
    '''
    Console of our app
    (Create Your Commands Here)
    '''
    while True:
        inp= input('CONSOLE> ')
        if inp[:3].lower() == 'new':
            # check if path exists
            py_server(inp[4:-5],int(inp[-4:]))
        elif inp == 'servers':
            '''for thread in threading.enumerate():
                print(thread.name)
            print()'''
            threads= [item.name for item in threading.enumerate()]

            frst_col= 12
            scnd_col= 8
            thrd_col= 4
            for item in threads:
                if '=>' in item:
                    frst_sym= item.index('=>')
                    scnd_sym= item.index('==>')
                    if len(item[:frst_sym])-2 > frst_col:
                        frst_col= len(item[:frst_sym])-2
                    if len(item[frst_sym+2:scnd_sym])-2 > scnd_col:
                        scnd_col= len(item[frst_sym+2:scnd_sym])-2
                    if len(item[scnd_sym+4:]) > thrd_col:
                        thrd_col= len(item[scnd_sym+4:])
            #print(frst_col,scnd_col,thrd_col)


            print((sum([frst_col,scnd_col,thrd_col])+9)*'▄')
            print('█ SERVER NAME ' + ' '*(frst_col-11) + '█ PATH' + ' '*(scnd_col-4) + '█ PORT  █')
            print('█'+ (frst_col+2)*'▄' + '█' + (scnd_col+1)*'▄' + '█' + (thrd_col+2)*'▄' + '█')
            for thread in threads:
                if '=>' in thread:
                    frst_sym= thread.index('=>')
                    scnd_sym= thread.index('==>')       
                    print('█ ' + thread[:frst_sym]           + ' ' + ' '*(frst_col-len(thread[:frst_sym]          )),end='')
                    print('█ ' + thread[frst_sym+3:scnd_sym] + ' ' + ' '*(scnd_col-len(thread[frst_sym+2:scnd_sym])),end='')
                    print('█ ' + thread[scnd_sym+4:]         + ' ' + ' '*(thrd_col-len(thread[scnd_sym+4:]        ))+'█')
            print((sum([frst_col,scnd_col,thrd_col])+9)*'▀')



        elif inp=='exit':
            import pyautogui
            pyautogui.hotkey('ctrl','c')
            return #break


if __name__ == "__main__":

    from LOG_COLOR import colorize
    colorize()

    FLASK_SERVER=  threading.Thread(target=app.run,name='FL_SERVER',
                                    kwargs={'host':IP,'port':8000}
                                    )

    FLASK_SERVER.start()
    #app.run(host=rx.system.ip_local(),port=8000)
    
    # Custom Path
    if rx.files.exists('E:/ramin/coding'):
        py_server('E:/ramin/coding',1407)
    if rx.files.exists('./static'):        
        py_server('static', 5556, 'static dir')


    # 8080 SERVER: Current Directory
    py_server('./',8080, 'SERVER PATH')



    # Creating Server for home (drives)
    home_port= 10000
    # FOR WINDOWS:
    if platform.system() == 'Windows':
        DRIVES:list = []
        for char in 'DEFGHIJKL':
            if rx.files.exists(char+':'):
                py_server(char+':',home_port)
                home_port+=1
        #py_server('C:',40)
    # Linux
    if platform.system() == 'Linux':
        py_server('~/', home_port, 'HOME/')
    # Mac  (I have not used MAC yet So please set home path here)
    if platform.system() == 'Mac':
        rx.style.print('SET YOUR MAC HOME PATH','red')
        ### py_server(HOMEPATH,home_port) ###



    cons= threading.Thread(target=console,name='CONSOLE')
    rx.wait(RUNNING_SERVERS)
    cons.start()


    
