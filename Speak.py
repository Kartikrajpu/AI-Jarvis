from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep

# Specify the path to the Chrome WebDriver executable
webdriver_path = "DataBase\\chromedriver.exe"  # Update with your actual path

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True

# Use the Service class to specify the executable path
service = Service(webdriver_path)

# Pass the service and options to the webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lengthoftext = len(str(Text))

    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/form/textarea").clear()

        if lengthoftext >= 30:
            sleep(8)
        elif lengthoftext >= 40:
            sleep(15)
        elif lengthoftext >= 55:
            sleep(20)
        elif lengthoftext >= 70:
            sleep(23)
        elif lengthoftext >= 100:
            sleep(27)
        elif lengthoftext >= 120:
            sleep(30)
        else:
            sleep(2)
