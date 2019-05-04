"""
Code for this entire file was obtained from : https://stackoverflow.com/questions/25657220/how-to-read-whole-ip-layer-and-tcp-layer-from-a-packet-when-using-scapy
Author: Zhi Yuan

"""

from scapy.all import *
from cStringIO import StringIO
import sys

class Capturing(list):
    
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
        
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio# free up some memory
        sys.stdout = self._stdout

class PacketDict(dict):
    
    def __init__(self, pkt):
        self.packet = pkt
        self.__packet_to_dict()

    def __extract_key(self, line):
        a = line.lstrip("###[ ").rstrip(" ]### ")
        return a

    def __extract_value_to_dict(self, line):
        if line.find("=") > -1:
            b = line.replace(" ","")
            a = b.split("=")
            return {a[0]: a[1]}
            return {line.replace(" ",""): None}


    def __packet_to_dict(self, packet):
        with Capturing() as packet_in_list:
            self.packet.show2()
            current_dict = self
        for line in packet_in_list:
            if line.strip() != "":
                line = line.replace("|","")
                if line.find('###[') > -1:
                    key = self.__extract_key(line)
                    current_dict[key] = {}
                    current_dict = current_dict[key]
                    continue
                    current_dict.update(self.__extract_value_to_dict(line))

    def haslayer(self, pkt_cls):
        return self.packet.haslayer(pkt_cls)