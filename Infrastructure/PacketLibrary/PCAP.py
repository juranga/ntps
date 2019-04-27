from scapy.all import *

class PCAP:

    def __init__(self, name=""):
        self.name = name
        self.traffic = []

    def change_name(self, name):
        self.name = name

    def save(self, addr):
        wrpcap(addr)
        return

    def load(self, addr):
        pcap = rdpcap(addr)
        for packet in pcap:
            self.traffic.append(packet)
        return