import os
import instaloader
import re
import pandas as pd
import colorama
from colorama import Fore
import sys
sys.path.append('/home/ian/.local/lib/python3.10/site-packages')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot = instaloader.Instaloader()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Profile():
	os.system('clear')
	print(Fore.MAGENTA+"Profile:")
	username = input(Fore.WHITE+"What is the exact username of the instagram account? >>> ")
	profile = instaloader.Profile.from_username(bot.context, username)
	print("Username: ", profile.username)
	print("User ID: ", profile.userid)
	print("Number of Posts: ", profile.mediacount)
	print("Followers Count: ", profile.followers)
	print("Following Count: ", profile.followees)
	print("Bio: ", profile.biography)
	print("External URL: ", profile.external_url)
	input(Fore.RED+"Press Enter to continue...")
	Start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Email():
	os.system('clear')
	print(Fore.MAGENTA+"Email:")
	username = input(Fore.WHITE+"What is the exact username of the instagram account? >>> ")
	profile = instaloader.Profile.from_username(bot.context, username)
	print("Username: ", profile.username)
	print("Bio: ", profile.biography)
	emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
	print("Emails extracted from the bio:")
	print(emails)
	input(Fore.RED+"Press Enter to continue...")
	Start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def TopSearch():
	os.system('clear')
	print(Fore.MAGENTA+"Top Search:")
	text = input(Fore.WHITE+'Type the word that you want the top search resulst for >>> ')
	search_results = instaloader.TopSearchResults(bot.context, text)
	print('')
	print('Loading...')
	print('')
	for username in search_results.get_profiles():
		print(username)

	for hashtag in search_results.get_hashtags():
		print(hashtag)
	print('')
	input(Fore.RED+"Press Enter to continue...")
	Start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def PostDownload():
	os.system('clear')
	print(Fore.MAGENTA+"Post Download:")
	print('Careful when useing account, chance of disabling, use account that you are willing to risk a disable on')
	print('')	
	username = input(Fore.WHITE+'Type in the username of the account to download data with >>> ')
	print('')
	password = input('Type in the password for that account >>> ')
	print('')
	UsernameTarget = input('Type in the username that you want to download the posts from >>> ')
	os.system('clear')
	print('')
	print('Loading...')
	print('')
	bot.login(user=username,passwd=password)

	profile = instaloader.Profile.from_username(bot.context, UsernameTarget)

	posts = profile.get_posts()

	for index, post in enumerate(posts, 1):
		bot.download_post(post, target=f"{profile.username}_{index}")
		print('')

	input(Fore.RED+"Press Enter to continue...")
	Start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def FFExtracter():
	os.system('clear')
	print(Fore.MAGENTA+"Follower and Following Extractor:")
	print('Careful when useing account, chance of disabling, use account that you are willing to risk a disable on')
	print('')	
	username = input(Fore.WHITE+'Type in the username of the account to download data with >>> ')
	print('')
	password = input('Type in the password for that account >>> ')
	print('')
	
	bot.login(user=username,passwd=password)
	UsernameTarget = input('Type in the username that you want to get the follwers and folling data from >>> ')
	os.system('clear')
	print('')
	print('Loading...')
	print('')
	profile = instaloader.Profile.from_username(bot.context, UsernameTarget)
	followers = [follower.username for follower in profile.get_followers()]
	followers_df = pd.DataFrame(followers)
	followers_df.to_csv('followers.csv', index=False)
	followings = [followee.username for followee in profile.get_followees()]
	followings_df = pd.DataFrame(followings)
	followings_df.to_csv('followings.csv', index=False)
	print('Done')
	print('')
	input(Fore.RED+"Press Enter to continue...")
	Start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Start():
	os.system('clear')	
	print(Fore.MAGENTA+'█████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print('░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███')
	print('░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███')
	print('░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███')
	print('░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███')
	print('░░░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███')
	print('████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████')
	print('░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█')
	print('░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█')
	print('░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█')
	print('█████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
	print('')
	print(Fore.CYAN + "a) Profile Details   b) Bio Email Finder   c) Top Search Result Finder   d) Post Download   e) Follower and Following Data Extracter  f) Main Menu")
	#print(Fore.CYAN + "")
	print('')
	choice = input(Fore.WHITE + 'What program is being run? >>> ')
	
	if((choice == 'a')):
		Profile()
	elif((choice == 'b')):
		Email()
	elif((choice == 'c')):
		TopSearch()
	elif((choice == 'd')):
		PostDownload()
	elif((choice == 'e')):
		FFExtracter()
	elif((choice == 'f')):
		os.system('sudo python RAVAGE.py')
	else:
		Start()
