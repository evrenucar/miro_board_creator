username = "test111"
email_adress = "nonita7632@altcen.com"
password = "zZ75Z278m9k6WHJ"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##adds the ability to use keys such as enter and space
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://miro.com/login/")
    
print("loaded" + " " + (driver.title))
email = driver.find_element_by_name("email")
email.send_keys("test")
email.send_keys(Keys.TAB)
time.sleep(3)
# email = driver.find_element_by_name("email")
# email.send_keys("evrenucar1999@gmail.com")

driver.quit()