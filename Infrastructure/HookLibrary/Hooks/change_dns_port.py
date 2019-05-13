from scapy.all import * 

def run(packet):
    if packet.haslayer(DNS):
        del packet.chksum
        del packet.len
        del packet.getlayer(UDP).chksum
        packet.getlayer(UDP).sport = 44444

    packet.show2(dump=True)
    return "Modification"
