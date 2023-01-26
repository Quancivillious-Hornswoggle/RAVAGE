import os
from scapy.all import ARP, Ether, srp
import colorama
from colorama import Fore

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
	
def Fullscan(subnet, time):		
	for i in range(1, 255):
		ip_range = (subnet + '.' + str(i) + '.0/24')
		print('Scanning Hosts on: ' + ip_range)
		arp = ARP(pdst=ip_range)
		ether = Ether(dst="ff:ff:ff:ff:ff:ff")
		packet = ether/arp

# Send the packet on the network and receive the response
		result = srp(packet, timeout=time, verbose=0)[0]

# Print the host IPs that responded
		for sent, received in result:
			addresses.append({'ip': received.psrc, 'mac': received.hwsrc})

	for client in addresses:
		print(f"IP: {client['ip']}   MAC: {client['mac']}")

	
def SpecificScan():
	os.system('clear')
	baseip = input('Type in the first 7 numbers of the ip. EX 192.168.1  >>> ')
	print('Scanning...')		
	print('')
	clients = scan(baseip + '.1/24')
	
	for client in clients:
		print("IP: " + client["ip"])
		print("MAC: " + client["mac"])
		print("")

	choice = input('Would you like to save these to a file? y/n >>> ')
	if(choice == 'y'):
		print('Saving to file')
		with open("IP_SAVED_DATA.txt", "a") as file:
			for client in adresses:
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
	timeout = int(input('Type the amount of connection wait time for each host >>> '))
	print('Scanning...')		
	print('')
	Fullscan(subnet = address, time = timeout)

	choice = input('Would you like to save these to a file? y/n >>> ')
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
	print(Fore.GREEN + '██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
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
