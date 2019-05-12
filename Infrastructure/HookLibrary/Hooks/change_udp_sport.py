from scapy.all import *

def run(packet):
    if packet.haslayer(UDP):
        del packet.chksum
        del packet.len
        packet.getlayer(UDP).sport = 55555

    packet.show2(dump=True)
    return "Modification"
