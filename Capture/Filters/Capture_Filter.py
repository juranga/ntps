import scapy

def BPF_Filter(packet):
    return scapy.sniff(self.input_filter, 0)