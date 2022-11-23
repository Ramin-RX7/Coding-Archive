from win10toast import ToastNotifier
import time
import PySimpleGUI as sg


toaster = ToastNotifier()
toaster.show_toast("Suspicious action:",
                   "Something is happening in the background.",
                   duration=7)
time.sleep(3)

toaster = ToastNotifier()
toaster.show_toast("Possibility of threat",
                   "There are several requests to have permission on PC.",
                   duration=7,
                   threaded=True)

time.sleep(4)


layout = [  [sg.Text('Do you give permission to UNKNOWN to controll your device?')],
            [sg.OK(button_text='Yes'), sg.Cancel(button_text='No')]]

# Create the Window
"""window = sg.Window('Title', layout, size=(475,100), no_titlebar=True)
window.close()  # if user closes window or clicks cancel
time.sleep(3)
# Event Loop to process "events"

event, values = window.read()
if event in (None, 'Cancel'):
    sg.Popup('Action Blocked', 'They do not have any permission on your PC.',no_titlebar=True)
else:
    sg.Popup('Request accepted', 'They have permission to access everything in your PC.',no_titlebar=True)
 
    

window.close()
time.sleep(6)
"""
toaster = ToastNotifier()
toaster.show_toast("Frequent requests', 'َAnother device is trying to get permission.",duration=7,threaded=True)
toaster = ToastNotifier()
toaster.show_toast("Threat action founded.","We are trying to find threat source.",duration=7,threaded=True)
time.sleep(4)
toaster = ToastNotifier()
toaster.show_toast("Files Downloaded completely.","4 MB - 2MB/min",duration=4,)
sg.Popup('Files downloaded successfully', 'َNo way back. They are moving everywhere in PC.',no_titlebar=True)
toaster = ToastNotifier()
toaster.show_toast("We can not find downloaded files","Searching...",duration=6,)
time.sleep(4)
toaster = ToastNotifier()
toaster.show_toast("Suspicious action founded in DOWNLOADS folder","Searching...",duration=6,)
time.sleep(6)
toaster = ToastNotifier()
toaster.show_toast("UNKNOWN device ignored", "A device called UNKNOWN requests are ignored from now.",duration=6,)
sg.PopupTimed('Files downloaded successfully', 'َNo way back. They are moving everywhere in PC.',no_titlebar=True,auto_close_duration=5)
sg.PopupTimed('Trying to getting access...', 'َWorking on system setting for permissions...',no_titlebar=True,auto_close_duration=5)

layout = [[sg.Text('Getting access...')],
          [sg.ProgressBar(650, orientation='h', size=(20, 20), key='progressbar',bar_color=('green','white'))],
          [sg.Cancel()]]
window = sg.Window('Custom Progress Meter', layout,no_titlebar=True)
progress_bar = window['progressbar']
for i in range(650):
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        print('It does not work now.')
        pass
    progress_bar.UpdateBar(i + 1)
window.close()

sg.PopupTimed('Access allowed.',no_titlebar=True,auto_close_duration=5)
toaster = ToastNotifier()
toaster.show_toast("5 threats founded", "Windows defender is trying to remove threats.",duration=6,)










