import os
from scapy.all import *
import colorama
from colorama import Fore
import subprocess

addresses = []

def scan(ip_range):		
	arp = ARP(pdst=ip_range)
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = ether/arp

	result = srp(packet, timeout=3, verbose=0)[0]
	
	clients = []
	for sent, received in result:
		clients.append({'ip': received.psrc, 'mac': received.hwsrc})
	return clients
	
def Fullscan(subnet, time, interface, frequency):	
	counter = 0
	mac = 0
	
	new_mac = ("00:11:22:33:44:55")
	new_ip = ("192.168.0.0")
	os.system("ifconfig " + interface + " down")
	os.system("ifconfig " + interface + " hw ether " + new_mac)
	os.system("ifconfig " + interface + " " + new_ip)
	os.system("ifconfig " + interface + " up")
	
	for i in range(1, 256):
		ip_range = (subnet + "." + str(i) + ".1/24")
		print(Fore.WHITE + 'Scanning Hosts on '+ Fore.RED + ip_range + Fore.MAGENTA)
		
		counter = counter + 1
		mac = mac + 1
		
		if mac >= 100:
			mac = 1
		
		if counter >= 256:
			counter = 0

		if ((counter % frequency) == 0):
			new_mac = ("00:11:22:33:44:" + str(mac))
			new_ip = ("192.168.0." + str(counter))
			os.system("ifconfig " + interface + " down")
			os.system("ifconfig " + interface + " hw ether " + new_mac)
			os.system("ifconfig " + interface + " " + new_ip)
			os.system("ifconfig " + interface + " up")
			print('\n Info Changed \n')

		send(ARP(op=2, pdst=new_ip, psrc=new_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=new_mac))

		os.system("ifconfig " + interface + " promisc")

		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), iface=interface, timeout=time)

		results = []

		for sent, received in ans:
		    results.append({"ip": received.psrc, "mac": received.hwsrc})
		    addresses.append({"ip": received.psrc, "mac": received.hwsrc})

		# Print the results
		for host in results:
		    print(host)
	
def SpecificScan():
	os.system('clear')
	baseip = input('Type in the first 7 numbers of the ip. EX 192.168.1  >>> ')
	print('Scanning...')		
	print('')
	clients = scan(baseip + '.1/24')
	
	for client in clients:
		print(Fore.YELLOW +"IP: " + Fore.MAGENTA + client["ip"] + Fore.WHITE)
		print(Fore.YELLOW +"MAC: " + Fore.BLUE + client["mac"] + Fore.WHITE)
		print("")

	choice = input('Would you like to save these to a file? y/n >>> ')
	if(choice == 'y'):
		print('Saving to file')
		with open("IP_SAVED_DATA.txt", "a") as file:
			for client in clients:
				file.write("IP: " + client["ip"])
				file.write("   MAC: " + client["mac"] + '\n')
				file.write("")
		print('')
		print('Done!')
		print('')
		input(Fore.RED+"Press Enter to continue...")
		os.system('sudo python RAVAGE.py')
	if(choice == 'n'):
		input(Fore.RED+"Press Enter to continue...")
		os.system('sudo python RAVAGE.py')
		
def FullScan():
	os.system('clear')
	address = input('Type in the first 6 numbers of the ip. EX 192.168  >>> ')
	print('')
	timeout = float(input('Type the amount of connection wait time for each host >>> '))
	print('')
	device = input('Type in the interface that you are using. EX wlan0 >>> ')
	print('')
	Frequency = int(input('Type in how many packets should be sent till changing your IP and MAC >>> '))
	print('')
	print('Scanning...')		
	print('')
	Fullscan(subnet = address, time = timeout, interface = device, frequency = Frequency)

	choice = input(Fore.WHITE + 'Would you like to save these to a file? y/n >>> ')
	if(choice == 'y'):
		print('Saving to file')
		with open("IP_SAVED_DATA.txt", "a") as file:
			for client in addresses:
				file.write("IP: " + client["ip"])
				file.write("   MAC: " + client["mac"] + '\n')
				file.write("")
		print('')
		print('Done!')
		print('')
		input(Fore.RED+"Press Enter to continue...")
		os.system('sudo python RAVAGE.py')
	if(choice == 'n'):
		input(Fore.RED+"Press Enter to continue...")
		os.system('sudo python RAVAGE.py')

def Start():
	os.system('clear')
	print(Fore.MAGENTA + '██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print('█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███')
	print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███')
	print('█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('█░░░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███')
	print('█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████')
	print('█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█')
	print('█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█')
	print('█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█')
	print('██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print(Fore.WHITE+'')
	#
	print(Fore.CYAN + '1) Full Scan		2) Specific Scan')
	print('')
	selection = int(input(Fore.WHITE + 'What program is being run? >>> '))
	#
	if selection == 1:
		FullScan()
	if selection == 2:
		SpecificScan()
	elif (selection != 1) or (selection != 2):
		Start()
