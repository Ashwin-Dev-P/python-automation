from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

MYUSERNAME = "8056150426"
MYPASSWORD = "Ashwin@14instagram"

#Variables and constants
WEBSITE_LINK = "http://instagram.com"
CHROME_DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(WEBSITE_LINK)

try:
    driver.implicitly_wait(10)

    username= driver.find_element_by_name('username')
    username.send_keys(MYUSERNAME);

    password = driver.find_element_by_name('password')
    password.send_keys(MYPASSWORD);
    
    driver.find_element_by_css_selector('button[type=submit]').click()

    driver.implicitly_wait(10)
    if(not driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()):
        print("Turn on notification dismissed for now.")
    else:
        print("Turn on notification did not pop up.")

except:
    print("Error occured.")

#driver.quit()
exit()