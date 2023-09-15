import os
import keyboard
import pyautogui
import webbrowser
from time import sleep



def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    elif "slideshow" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "ppt" in Nameoftheapp:
            os.startfile(r"C:\\Users\\kr031\\OneDrive\\Desktop\\AIT project\\Jarvis ppt.pptx")
            return True
    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True
        
    elif "take" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "attendance" in Nameoftheapp:
            os.startfile(r"C:\Users\kr031\OneDrive\Desktop\attendance\attendance.exe")
            return True

    elif "my site" in Query:
        
        Link = f"https://profoundcore.tk/"
        webbrowser.open(Link)
        return True 
    
    elif "screenshot" in Query:
        kk = pyautogui.screenshot()
        kk.save("C:\\Users\\kr031\\OneDrive\\Desktop\\AIT project\\screenshots")

    elif "make folder" in Query:
        folder_path = "C:\\Users\\kr031\\OneDrive\\Desktop\\"
        os.makedirs(folder_path, exist_ok=True)
    

   