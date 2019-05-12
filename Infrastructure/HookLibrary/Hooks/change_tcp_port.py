from scapy.all import * 

def run(packet):
<<<<<<< Updated upstream
    try:
        if packet.haslayer(TCP):
            del packet.chksum
            del packet.getlayer(TCP).chksum
            packet.getlayer(TCP).src = 55555
    except:
        raise
=======
    if packet.haslayer(TCP):
        del packet.chksum
        del packet.len
        del packet.getlayer(TCP).chksum
        packet.getlayer(TCP).sport = 55555
>>>>>>> Stashed changes
    
    packet.show2(dump=True)
    return "Modification"

        
