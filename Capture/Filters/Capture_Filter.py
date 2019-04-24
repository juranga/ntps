from scapy.all import * 

def BPF_Filter(packet, input_filter=""):
    return sniff(input_filter, 0)
