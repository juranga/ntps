from scapy.all import * 

def run(packet):
<<<<<<< Updated upstream
    try:
        if packet.haslayer(DNS):
            del packet.chksum
            del packet.getlayer(DNS).chksum
            packet.getlayer(DNS).src = 44444
    except:
        raise
    
=======
    if packet.haslayer(DNS):
        del packet.chksum
        del packet.len
        del packet.getlayer(UDP).chksum
        packet.getlayer(UDP).sport = 44444

>>>>>>> Stashed changes
    packet.show2(dump=True)
    return "Modification"
