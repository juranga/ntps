from scapy.all import * 

def run(packet):
    try:
        if packet.haslayer(TCP):
            return "Modification"
    except:
        raise
        
return "Drop"
