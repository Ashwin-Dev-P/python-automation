import pyautogui
import webbrowser
import time
import platform
import os

#Variables and constants
whatsapp_url = "web.whatsapp.com"
message_file_location = "message.txt"
common_OS = True
entered_chrome = False
entered_other_browser = False

#Google Chrome paths
windows_chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
macOS_chrome_path = "open -a /Applications/Google\ Chrome.app %s"
linux_chrome_path = "/usr/bin/google-chrome %s"

#OS determination
OS = platform.system()
print("OS = "+platform.system())


if(OS == 'Windows'):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
elif(OS == 'Darwin'):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
elif(OS == 'Linux'):
    chrome_path = '/usr/bin/google-chrome %s'
else:
    common_OS = False

#Opening web browser.
if(common_OS):
    if(webbrowser.get(chrome_path).open(whatsapp_url)):
        print("Entered Chrome.")
        entered_chrome = True
    else:
        print("Unable to enter Chrome.")
elif(not common_OS or entered_chrome == False):
    
    #Open default browser.
    print("Entering Default browser....")
    
    if(webbrowser.open(whatsapp_url)):
        print("Entered default browser.")
        entered_other_browser = True
    else:
        print("Error entering default browser.");

#Reading text file
if(entered_other_browser or entered_chrome):
    file = open(message_file_location, "r")
    content = file.read()
    file.close()
    time.sleep(10)

    #Typing
    for i in content:
        pyautogui.press(i)
    pyautogui.press('enter')
    


#Close browser       
if(entered_chrome or entered_other_browser):
    if(entered_chrome):
        os.system("taskkill /im chrome.exe /f")
        print("Chrome closed.")
    else:
        print("Default browser not programmed to be closed.")
else:
    print("No browser is available to close.")
    
        

exit()