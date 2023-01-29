import os
import colorama
from colorama import Fore
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import Email_Spammer 
import InstaStats
import maxphisher
import NetworkScanner
import PortScanner
import Sniffer
import WebScraper
import WifiFlooder
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clear():
    os.system('clear')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Function1():
    clear()
    selection = ''
    selection = input('Do you want to load saved email info OR type it in manualy? [L or M] >>> ')
    print('')
    if(selection == 'L'):
        a = open("Email", "r")
        b = open("AppPassword", "r")
        print('Loading from file...')
        Email_Spammer.Run(pe = a.read(), password = b.read())
    elif(selection == 'M'):
        email = input('Type the email that is being used to spam emails? >>> ')
        print('')
        appPassword = input('Type in the app password for your email >>> ')        
        a = open("Email", "w")
        a.write(email)
        a.close()    
        b = open("AppPassword", "w")
        b.write(appPassword)
        b.close()   
        clear()
        Email_Spammer.Run(pe = email, password = appPassword)
    else:
        print('That is not a correct selection, please select again >>> ')
        Function1()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Function2():
	os.system('clear')
	d = input('What is the name of the device capturing the packets? EX wlan >>> ')
	print('')
	a = int(input('How many packets do you want to capture? >>> '))
	Sniffer.Start(device = d, amount = a)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Function3():
	os.system('clear')
	i = input('Type in the ip address of the ports you want scanned >>> ')
	print('')
	a = int(input('Type in the range of ports you want scanned form 1 to ? >>> '))
	print('')
	t = float(input('Type in the wait time for each port scan >>> '))	
	PortScanner.Start(ip = i, amount = a, timeout = t)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
def Function4():
	os.system('clear')
	URL = input('Type in or paste the url you want the data from  (https://) is needed >>> ')
	WebScraper.Start(url = URL)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def StartMenu():
	clear()
	print(Fore.RED + '███████████████████████████████████████████████████████████████████████████████████████████████')
	print('█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█')
	print('█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
	print('█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█')
	print('█░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████')
	print('█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█')
	print('█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
	print('█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█')
	print('█░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████')
	print('█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█')
	print('█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█')
	print('█░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█████░░░░░░█████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█')
	print('███████████████████████████████████████████████████████████████████████████████████████████████')
	print('')
	print(Fore.CYAN + "1) Email Spammer	2) Instagram Scraper	3) Phisher	4) Network Scanner 	5) Port Scanner		6) Packet Sniffer	7) Web Scraper	 8) Wifi Flooder")
	print('')
	choice = int(input(Fore.WHITE + 'What program is being run? >>> '))

	if((choice == 1)):
   	    Function1()
	elif((choice == 2)):
            InstaStats.Start()
	elif((choice == 3)):
            os.system('python3 maxphisher.py')
	elif((choice == 4)):
	    NetworkScanner.Start()
	elif((choice == 5)):
	    Function3()
	elif((choice == 6)):
	    Function2()
	elif((choice == 7)):
	    Function4()
	elif((choice == 8)):
	    WifiFlooder.Start()
	else:
            StartMenu()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                        
StartMenu()
