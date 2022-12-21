#!/usr/bin/python

"""
# Script Name : Ablette.py
# Author : Frédéric Puren
# Date : Décembre 2022
# Version 1.0


# What better than the faithful Roach to survey a network !
# Quoi de mieux que le fidele Ablette pour arpenter un réseau !

#Alette is a simple network scanner that also tests open ports for each connected machine.
# Ablette est un simple scanner de réseau qui teste également les ports ouverts pour chaque machine connectée.

# Compatible Debian & Windows & Android

version de python utilisée : 
sur windows : 3.11.1
sur Debian : 3.9.2

version du module colorama : 0.4.6
version du module pyroute2 : 0.7.3

prerequisite :
------------

---- DEBIAN ----

- install python and pip with all dependencies :
apt update & apt upgrade
apt install python3-pip3
pip install colorama pyroute2

Run the script :
python3 ./Ablette.py



---- WINDOWS ----

- Installing Python & Pip with all dependencies :
Go to the page https://www.python.org/downloads/

and then open powershell terminal :
pip install colorama

Run the script :
python ./Ablette.py


----
colorama is for producing colored terminal text

module IPRoute from pyroute2 is for Linux network configuration



---- ANDROID ----

Install "Pydroid 3" from playstore

Pydroid 3 is an IDE for python 3. It's a free app with few ads. The premium version is not necessary to launch Ablette.py 

You can install modules with the pip package manager included , when you're going to install pyroute2 it will ask you to install "Pydroid repository plugin", install it and that's it.
then clic on "open" and look for Ablette.py file.
then clic on "play button"



################################################################################
Sources :
-------

module IPAddress (fr) :
https://docs.python.org/fr/3/howto/ipaddress.html
https://docs.python.org/3/library/ipaddress.html

Get IP Address & test port connection (fr) :
https://www.delftstack.com/fr/howto/python/get-ip-address-python/

ping function (en) :
https://itecnote.com/tecnote/python-function-to-test-ping/

"""


#------------ Modules -------------
import socket
import subprocess
import os
import ipaddress
from colorama import Fore, Style
#----------------------------------

# creation of variables for colorama module :
green = Fore.GREEN
red = Fore.RED
Blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
green_L = Fore.LIGHTGREEN_EX
red_L = Fore.LIGHTRED_EX
blue_L = Fore.LIGHTBLUE_EX
cyan_L = Fore.LIGHTCYAN_EX
yellow_L = Fore.LIGHTYELLOW_EX
magenta_L= Fore.LIGHTMAGENTA_EX
#-------------------------------------------


############# FUNCTIONS ##############

####
# fonction qui donne la configuration IP de la machine
# function to Get PC Network Configuration
def conf_IP():



    # nom d'hote de la machine
    # Machine hostname
    computer_name = socket.gethostname ()


    # addresse IP de la machine
    # Machine IP Address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    global IPaddress
    IPaddress = s.getsockname()[0]


    # Récupérer le masque de sous-réseau avec la méthode subprocess pour windows
    # & le module IPRoute de pyroute2 pour Debian

    # Get subnet mask with subprocess method for window
    # & the IPRoute module from pyroute2 for Debian

    #OS type ( windows = 'nt' & Linux = 'posix')
    OS = os.name

    if OS == 'nt':
        proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if IPaddress.encode() in line:
                break
        mask1 = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()

        # conversion du masque sous-réseau en CIDR
        # convert netmask to CIDR
        cidr = sum(bin(int(x)).count('1') for x in mask1.split('.'))
        mask = str(cidr)

    else:
        from pyroute2 import IPRoute

        ip = IPRoute()
        #info = [{'iface': x['index'], 'addr': x.get_attr('IFA_ADDRESS'), 'mask':  x['prefixlen']} for x in ip.get_addr()]
        mask1 = [x['prefixlen'] for x in ip.get_addr()]
        mask = str((mask1)[1])



    # Obtenir l'adresse du réseau avec l'adresse IP et le masque (module ipaddress)
    # Get network address with IP address and netmask (ipaddress module)
    couple = IPaddress + "/" + mask

    host = ipaddress.ip_interface(couple)
    network1 = host.network
    network = str(network1)


    # Obtenir le nombre d'hôte total
    # Get total hosts
    global net
    net = ipaddress.ip_network(network1)
    nb_host1 = net.num_addresses
    nb_host = str(nb_host1)

    # Obtenir la première et la dernière adresse du réseau
    # Get the first and the last Network IP Address
    first = str(net[1])
    last = str(net[-2])
    broadcast = str(net[-1])

    # Affichage dans le Terminal
    print()
    print(green_L + "--------- Configuration IP ----------", end="")
    print(Style.RESET_ALL)
    print()
    print("Machine Name : ", end="")
    print(green_L + computer_name)
    print(Style.RESET_ALL, end="")

    print("Machine IP Address/mask : ", end="")
    print(magenta_L + IPaddress + "/" + mask)
    print(Style.RESET_ALL, end="")

    print("Network Address : ", end="")
    print(magenta_L + network)
    print(Style.RESET_ALL, end="")

    print("First Network Address : ", end="")
    print(green_L + first)
    print(Style.RESET_ALL, end="")

    print("Last Network Address : ", end="")
    print(green_L + last)
    print(Style.RESET_ALL, end="")

    print("Broadcast Network Address : ", end="")
    print(green_L + broadcast)
    print(Style.RESET_ALL, end="")

    print("Total Network hosts : ", end="")
    print(magenta_L + nb_host)
    print(Style.RESET_ALL)

    print(green_L + "-------------------------------------")
    print(Style.RESET_ALL)
    print()
####



####
# fonction Pause/Clear
# function Pause/Clear
def pause_clear():
    input("Press the <ENTER> key to continue...")
    OS = os.name
    if OS == 'nt':
        os.system("cls")
    else:
        os.system("clear")
####


####
# fonction test de connexion port sur une ip
#function for test port connection on IP address
def connexion_port(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)  # test la connexion pendant 0,01 seconde
    #s.setblocking(False)
    
    try:
        s.connect((ip, port))
        return True

    except:
        pass
####
            

####
# fonction ping qui intègre la fonction connexion_port
# function ping which include the port connection function
def ping(ip1):
    OS = os.name
    if OS == "nt":
        if ip1 == IPaddress:
            print(green_L + ip1, end=" ")
            print(Style.RESET_ALL, end="")
            print(": This machine")
            print("------------------------------------------")
        else:
            response = bool(os.system(f"ping -n 1 -w 100 {ip1} > NUL"))
            if response == False:
                print("IP Address ", end="")
                print(cyan_L + ip1, end=" ")
                print(Style.RESET_ALL, end="")
                print("is UP !")
                Liste = []

                for num_port1 in range(1, 1000):
                    a = connexion_port(ip1, num_port1)
                    if a == True:
                        num_port = str(num_port1)
                        print("Port ", end="")
                        print(magenta_L + num_port, end=" ")
                        print(Style.RESET_ALL, end="")
                        print("is open on ", end="")
                        print(cyan_L + x, end="")
                        print(Style.RESET_ALL)

                        # add each True response on "Liste" variable
                        Liste = Liste + [a]

                if Liste == []:
                    print("No open ports between 1 & 1000")

                print("------------------------------------------")

            else:
                pass
    else:
        if ip1 == IPaddress:
            print(green_L + ip1, end=" ")
            print(Style.RESET_ALL, end="")
            print(": This machine")
            print("------------------------------------------")
        else:
            response = bool(os.system(f"ping -c 1 -W 0.1 {ip1} > /dev/null 2>&1"))
            if response == False:
                print("IP address ", end="")
                print(cyan_L + ip1, end=" ")
                print(Style.RESET_ALL, end="")
                print("is UP !")
                Liste = []

                for num_port1 in range(1, 1000):
                    a = connexion_port(ip1, num_port1)
                    if a == True:
                        num_port = str(num_port1)
                        print("Port ", end="")
                        print(magenta_L + num_port, end=" ")
                        print(Style.RESET_ALL, end="")
                        print("is open on ", end="")
                        print(cyan_L+ x, end="")
                        print(Style.RESET_ALL)

                        # add each True response on "Liste" variable
                        Liste = Liste + [a]                        

                if Liste == []:
                    print("No open ports between 1 & 1000")

                print("------------------------------------------")
                        
            else:
                pass
####


############ END FUNCTIONS ############




#################### START OF SCRIPT ######################

OS = os.name
if OS == 'nt':
    os.system("cls")
else:
    os.system("clear")

loop=True      
  
while loop: 


    print()


    print("         888      888          888    888")
    print("         888      888          888    888")
    print("         888      888          888    888")
    print(" 8888b.  88888b.  888  .d88b.  888888 888888  .d88b.")
    print(cyan_L + "    \"88b 888 \"88b 888 d8P  Y8b 888    888    d8P  Y8b")
    print(blue_L + ".d888888 888  888 888 88888888 888    888    88888888")
    print(cyan_L + "888  888 888 d88P 888 Y8b.     Y88b.  Y88b.  Y8b.", end="")
    print(Style.RESET_ALL)
    print("\"Y888888 88888P\"  888  \"Y8888   \"Y888  \"Y888  \"Y8888")
    print()
    print()
    # "1 : Configuration réseau du PC"
    print(blue_L + "1 : PC Network Configuration", end="")
    print(Style.RESET_ALL)
    # "2 : Scan de tout le réseau ( avec scan des port)""
    print(cyan_L + "2 : Scan of the entire network (with port scan)", end="")
    print(Style.RESET_ALL)
    # "3 : Scan réseau sur une plage IP spécifique"
    print(blue_L + "3 : Network scan on a specific IP range", end="")
    print(Style.RESET_ALL)
    print(red_L + "q : Exit", end="")

    print(Style.RESET_ALL)
    print()
    choice = input("Enter your choice : ")
     
    if choice == "1":
        print()
        # fonction conf_IP
        conf_IP()
        pause_clear()


    elif choice == "2":
        print()
        conf_IP()
        print(yellow_L + "################# START Network Scan #################")
        print(Style.RESET_ALL)

        # Liste toutes les adresses que contient le réseau et appelle la fonction ping
        # Lists all addresses in the network and calls the ping function
        for each_IP in net.hosts():
            x = str(each_IP)
            ping(x)

        print()
        print(yellow_L + "################# END Network Scan ##################")
        print(Style.RESET_ALL)
        pause_clear()

    elif choice == "3":
        conf_IP()
        first = input("Enter the first IP address : ")
        last = input("Enter the last IP address : ")

        #convert string in IPv4 Address for if comparaison
        firstIPv4 = ipaddress.ip_address(first)
        lastIPv4 = ipaddress.ip_address(last)

        for each_IP in net.hosts():
            if firstIPv4 <= each_IP <= lastIPv4:
                x = str(each_IP)
                ping(x)

        print()
        print(yellow_L + "################# END Network Scan ##################")
        print(Style.RESET_ALL)
        pause_clear()

    elif choice == "q":
        loop=False # End of loop

    else:
        # Any integer inputs other than values 1,2,3,q print an error message
        input("Wrong option selection. Enter any key to try again..")

    ################### END OF SCRIPT ####################
