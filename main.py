import subprocess
import os
import sys
from pathlib import Path
import threading
import pyautogui
import pyperclip
import time

#CONSTS
DEFAULT_DOWNLOAD_ADRESS = "croc yourfriendname" #Adress that will be used to receive, if clipboard is empty. Suitable if you download from the same person every time.
USER_NAME = "yourname" #Adress that will be used to send.
DOWNLOAD_FOLDER = str(Path.home() / "Downloads") #str(Path.home() / "Downloads")   to use default system download folder. Use "\" between folders in your custom path.
TIME_TO_SEND_Y = 2 #croc needs confirmation to start downloading, so after opening the console it simulates pressing y in certain amount of seconds. Use 0 to disable. 2 by default.
OPEN_DOWNLOADS = 1 #opens download folder after downloading complete. Use 0 to disable. 1 by default.


def press_y():
    if TIME_TO_SEND_Y > 0:
        time.sleep(TIME_TO_SEND_Y)
        pyautogui.write('y')
        pyautogui.press('enter')


threads = []
data = pyperclip.paste()
try:
    buffer_temp = data.split()[0]
except IndexError:
    buffer_temp = ""
arg = " ".join(sys.argv[1:])
cmd = "powershell croc send --code " + USER_NAME + " \'" + arg + "\'"
if arg != "":
    os.system(cmd)
else:
    if buffer_temp == "croc":
        sender_name = data
    else:
        sender_name = DEFAULT_DOWNLOAD_ADRESS
    thread = threading.Thread(target=press_y)
    thread.start()
    threads.append(thread)
    os.system("powershell cd \'" + DOWNLOAD_FOLDER + "\'; " + sender_name)
    if OPEN_DOWNLOADS == 1:
        os.system("explorer \"" + DOWNLOAD_FOLDER + "\"")
