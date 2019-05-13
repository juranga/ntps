from scapy.all import * 

def run(packet):
    if packet.haslayer(TCP):
        del packet.chksum
        del packet.len
        del packet.getlayer(TCP).chksum
        del packet.getlayer(TCP).len
        packet.getlayer(TCP).sport = 55555
    
    packet.show2(dump=True)
    return "Modification"

        
