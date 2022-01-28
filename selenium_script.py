
### Imports for selenium
from msilib.schema import Class
from pydoc import locate
from tokenize import Name
from turtle import down
from selenium import webdriver
from selenium.webdriver.common.keys import Keys ##adds the ability to use keys such as enter and space
from selenium.webdriver.common.action_chains import ActionChains ##adds the ability to enter keys without specifying an element
import time

### Random Password Generator Imports
import random   
import string  
import secrets


### Imports for mail-api
import pyperclip
import requests
import random
import string
import time
import sys
import re
import os
import tkinter as tk #used for getting clipboard 


### Defining all variables
email_adress = "Email will come here"
username = "username will be generated randomly by generateUserName function"
password = "Password wil be generated"
team_name = "team_x"

confirmation_code = "0"

email_adress = "placeholder"

team_invite_link ="dis a link"


### Variables for mail-api
temp_mail_adress = " " 
one= (1)

API = 'https://www.1secmail.com/api/v1/'
domainList = ['yoggm.com', 'vddaz.com', 'oosln.com', 'xojxe.com' ] #exluded these as they cannot be registered with miro: '1secmail.net', '1secmail.org', 'esiix.com', 'wwjmp.com'
domain = random.choice(domainList)

### mail-api functions
def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]
# Got this from https://stackoverflow.com/a/43952192/13276219
def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def checkMails():
    global confirmation_code
    print("entered check mails")
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print_statusline("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        print_statusline(f"You received mail")

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v
            confirmation_code = subject
            print(confirmation_code) 
            break
            
  
### mail-api executable
while True:
    newMail = f"{API}?login={generateUserName()}&domain={domain}"
    reqMail = requests.get(newMail)
    email_adress = f"{extract()[0]}@{extract()[1]}"
    # pyperclip.copy(mail)
    print("\nYour temporary email is " + email_adress + " (Email address copied to clipboard.)" + "\n")
    print(f"---------------------------- | Inbox of {email_adress} | ----------------------------\n")
    

    ###Random Password Generator Code  
    num = 10 # define the length of the string  
    # define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
    password = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
    # Print the Secure string with the combination of ascii letters and digits  
    print("Password:"+" "+password)  
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)


    ### Sign up to Miro
    driver.get("https://miro.com/signup/")
    print("loaded" + " " + (driver.title))

    #Enter username
    username = generateUserName()
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
    while (confirmation_code=="0"): #what does this check for? (it runs until there is a break statement)
        checkMails()
        print(confirmation_code) 
    
    print("hey  I'm here")
    print("hey  I'm here")
    print("hey  I'm here")
    print("hey  I'm here")

    
    #Enter confirmation code
    driver.find_element_by_name("code").send_keys(confirmation_code[-6:])
    #confirmation_code_field.send_keys(confirmation_code[-6:])
    time.sleep(10)
    print("hey  I've slept well")
    print("hey  I've slept well")
    print("hey  I've slept well")
    teamname_field = driver.find_element_by_class_name("setup-team-slide-content__section").click()
    #driver.find_element_by_tag_name('body').send_keys('dummydata')
    actions = ActionChains(driver)
    actions.send_keys(team_name)
    actions.perform()
    actions.send_keys(Keys.RETURN)
    actions.perform()

    time.sleep(3)
    ### Skip invite teammates
    actions.send_keys(Keys.TAB)
    actions.perform()
    actions.send_keys(Keys.TAB)
    actions.perform()
    actions.send_keys(Keys.RETURN)
    actions.perform()
    
    ### Skip this for now
    driver.find_element_by_tag_name("a").click()
    # //div[@id='a']// h4 a
    print("What do you want to do")
    print("What do you want to do")
    
    time.sleep(8) #could add an on load event or something here

    actions.send_keys(Keys.ESCAPE)
    actions.perform()

    time.sleep(4)
    ### Click Share button 
    driver.find_element_by_class_name("permissionPanel-2N0Gv").click()
    print("clicked Share")
    print("clicked Share")

    ### Copy Team Invıte Link
    time.sleep(5)
    driver.find_element_by_class_name("share-option__additional-content").click()
    time.sleep(1)

    ### Quits the Driver
    driver.quit()
    print("Process Complete")
    print("Shutting down driver")

    ###  Prints Team Invite Link
    root = tk.Tk()
    team_invite_link = root.clipboard_get()
    print("#####################################")
    print("Team Invite Link copied to your clipboard"+ " " + team_invite_link)
    print("#####################################")

    break



