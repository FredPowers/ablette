# ablette

Script Name : Ablette.py

Author : Frédéric Puren

Date : Décembre 2022

Version 1.0

------------------------------------

What better than the faithful Roach to survey a network !
Quoi de mieux que le fidele Ablette pour arpenter un réseau !

Alette is a simple network scanner that also tests open ports for each connected machine.
Ablette est un simple scanner de réseau qui teste également les ports ouverts pour chaque machine connectée.

Compatible Debian, Windows & Android

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


![Screenshot_2022-12-21-21-18-04-823_ru iiec pydroid3](https://user-images.githubusercontent.com/105367565/209001942-b08be04e-3b25-4973-b4d9-74f8dcdf1821.jpg)



#######
Sources :
-------

module IPAddress (fr) :
https://docs.python.org/fr/3/howto/ipaddress.html
https://docs.python.org/3/library/ipaddress.html

Get IP Address & test port connection (fr) :
https://www.delftstack.com/fr/howto/python/get-ip-address-python/

ping function (en) :
https://itecnote.com/tecnote/python-function-to-test-ping/
