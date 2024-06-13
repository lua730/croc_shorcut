# croc shortcut
Small program that you can use as shortcut on your desktop to use croc library for P2P File transfer.

# usage
When you drag a file onto the shortcut on desktop, croc will send the file.

When you open a shortcut, if there is a copied address in the clipboard (for example "croc yourfriendname"), croc will begin downloading.

When opening a shortcut without a copied address in the clipboard, the default download address will be used, which can be specified in the settings in the top of the program.

# installing croc
Windows

   Paste comand below into Powershell.
   ```
    winget search Microsoft.PowerShell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
    scoop install croc
    exit
    exit
   ```



# required python libraries
```pip install pyperclip```

```pip install pyautogui```

# settings on program top
DEFAULT_DOWNLOAD_ADRESS - Adress that will be used to receive, if clipboard is empty. Suitable if you download from the same person every time. For example "croc yourfriendname".

USER_NAME - Adress that will be used to send.

DOWNLOAD_FOLDER - ```str(Path.home() / "Downloads")``` to use default system download folder. Use "\" between folders in your custom path.

TIME_TO_SEND_Y - croc needs confirmation to start downloading, so after opening the console it simulates pressing y in certain amount of seconds. Use 0 to disable. 2 by default.

OPEN_DOWNLOADS - opens download folder after downloading complete. Use 0 to disable. 1 by default.
