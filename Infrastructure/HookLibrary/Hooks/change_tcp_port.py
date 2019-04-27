from scapy.all import * 

def run(packet):
    try:
        if packet.haslayer(UDP):
            del packet.chksum
            del packet.getlayer(UDP).chksum
            packet.getlayer(UDP).sport = 35011
    except:
        raise
    
    packet.show2(dump=True)
    return "Modification"

        
