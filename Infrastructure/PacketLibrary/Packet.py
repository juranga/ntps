from Infrastructure.PacketLibrary.Dissector import Dissector

from collections import defaultdict
from scapy.all import *
"""
As it currently stands, the Ether layer has to be dissected in a different way than every other layer.
This is because the Ether class in scapy does not have a "haslayer" function, and thus must be handled differently.

"""

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"

class Dissected_Packet:

    def __init__(self, raw_packet):
        self.ether_layer = Ether(raw_packet.get_payload())
        self.raw_form = IP(self.ether_layer).copy()
        self.layer_dict = {
            "ETH": "Ethernet II",
            "IP": "Internet Control Message Protocol",
            "TCP": "Transmission Control Protocol",
            "UDP": "User Datagram Protocol",
            "DNS": "Domain Name System"
        }
        self.layers = ["Ether"]
        self.fields = defaultdict(dict)

    def get_layers(self):
        return self.layers

    def get_fields(self):
        return self.fields
    
    def get_layer(self, layer_idx):
        return self.layers[layer_idx]

    def dissect_packet(self):
        self.dissect_ether()
        self.dissect_IP(Dissector(self.raw_form))

    def dissect_ether(self):
        self.fields["Ether"]["dst"] = self.ether_layer.dst
        self.fields["Ether"]["src"] = self.ether_layer.src
        self.fields["Ether"]["type"] = self.ether_layer.type

    def dissect_IP(self, packet, idx = 0, icon=arrow):
        for key, value in packet.items():
            if type(value) is dict:
                self.layers.append(key)
                self.dissect_IP(value, idx+1, circle)
                break
            else:
                self.fields[self.layers[idx]][key] = value

    def save_modifications(self):
        del self.raw_form.chksum
        del self.raw_form.len
        del self.raw_form.getlayer(2).chksum #this deletes the TCP or UDP chksum
        for layer_idx in range(0, len(self.layers)):
            layer = self.layers[layer_idx]
            raw_layer = self.ether_layer if layer == "Ether" else self.raw_form.getlayer(layer_idx) 
            for field in raw_layer.fields_desc:
                if field.name in self.fields[layer]:
                    setattr(raw_layer, field.name, self.fields[layer][field.name])

        # Recalculate Changes to Length & Chksum
        self.raw_form.show2(dump=True)
        self.fields["IP"]["chksum"] = self.raw_form.chksum
        self.fields["IP"]["len"] = self.raw_form.len
        self.fields[self.layers[2]]["chksum"] = self.raw_form.getlayer(2).chksum

    def convert_to_raw(self):
        return self.ether_layer / self.raw_form
