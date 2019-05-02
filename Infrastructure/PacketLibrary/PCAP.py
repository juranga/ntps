from Infrastructure.Common.Generators import id_generator

from scapy.all import *

class PCAP:

    def __init__(self, name=id_generator(), path="./"):
        self.name = name
        self.path = path + self.name
        self.traffic = []

    def change_name(self, name):
        self.name = name

    def save(self):
        wrpcap(self.path, self.traffic)
        return

    def load(self):
        pcap = rdpcap(self.path)
        for packet in pcap:
            self.traffic.append(packet)
        return
