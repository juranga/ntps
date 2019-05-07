from scapy.all import * 

def run(packet):
    if packet.haslayer(TCP):
        return "Drop"
        
    return "Modification"
