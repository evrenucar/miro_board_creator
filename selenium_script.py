from turtle import down
from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##adds the ability to use keys such as enter and space
import time


email_adress = "Email will come here"
username = "username will be generated from email_adress"
password = "Password wil be generated"

email_adress = "ful6dvfls5@oosln.com"
username = email_adress[:8]
print (username)


### Random Password Generator Code
import random   
import string  
import secrets  
num = 10 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
password = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
# Print the Secure string with the combination of ascii letters and digits  
print("Password:"+" "+password)  
 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://miro.com/signup/")
print("loaded" + " " + (driver.title))

#Enter username
name_field = driver.find_element_by_name("signup[name]")
name_field.send_keys(username)

#Enter email_address
email_field = driver.find_element_by_name("signup[email]")
email_field.send_keys(email_adress)

#Enter password
password_field = driver.find_element_by_name("signup[password]")
password_field.send_keys(password)

driver.find_element_by_class_name("mr-checkbox-1__icon").click()
password_field.send_keys(Keys.RETURN)

# driver.get("https://miro.com/login/")
    
# print("loaded" + " " + (driver.title))
# email_field = driver.find_element_by_name("email")
# email_field.send_keys(email_adress)
# email_field.send_keys(Keys.TAB)

# password_field = driver.find_element_by_name("password")
# password_field.send_keys(password) 
# password_field.send_keys(Keys.TAB)
# driver.find_element_by_class_name("signup__submit").click()

#time.sleep(6)

# # email = driver.find_element_by_name("email")
# # email.send_keys("evrenucar1999@gmail.com")

#driver.quit()

