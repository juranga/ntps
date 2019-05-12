from scapy.all import * 

def run(packet):
    if packet.haslayer(TCP):
        del packet.chksum
        del packet.getlayer(TCP).chksum
        packet.getlayer(TCP).src = 55555
    
    packet.show2(dump=True)
    return "Modification"

        
