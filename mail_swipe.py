import pyperclip
import requests
import random
import string
import time
import sys
import re
import os

temp_mail_adress = " " 
one= (1)

API = 'https://www.1secmail.com/api/v1/'
domainList = ['yoggm.com', 'vddaz.com', 'oosln.com', 'xojxe.com' ] #exluded these as they cannot be registered with miro: '1secmail.net', '1secmail.org', 'esiix.com', 'wwjmp.com'
domain = random.choice(domainList)
# works 'yoggm.com', 'vddaz.com', 'oosln.com', 'xojxe.com'


def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

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

def deleteMail():
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract()[0]}',
        'domain': f'{extract()[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails():
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

        x = 'mails' if length > 1 else 'mail'
        print_statusline(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'All Mails')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

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

            mail_file_path = os.path.join(final_directory, f'{i}.txt')

            with open(mail_file_path,'w') as file:
                file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')
    
try:
    if(one==1):
        newMail = f"{API}?login={generateUserName()}&domain={domain}"
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"
        pyperclip.copy(mail)
        print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
        print(f"---------------------------- | Inbox of {mail} | ----------------------------\n")
        while True: #what does this check for? (it runs until there is a break statement)
            checkMails()
            time.sleep(3)
except(KeyboardInterrupt):
    deleteMail()
    print("\nProgramme Interrupted")
    os.system('cls' if os.name == 'nt' else 'clear')