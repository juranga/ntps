from Infrastructure.PacketLibrary.Dissector import Dissector

from collections import defaultdict
from scapy.all import *
"""
As it currently stands, the Ether layer has to be dissected in a different way than every other layer.
This is because the Ether class in scapy does not have a "haslayer" function, and thus must be handled differently.

"""

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"

# An object storing information on a packet in our system; it stores the layers and the fields (and their values) within them.
class Dissected_Packet:

    def __init__(self, raw_packet):
        self.ether_layer = Ether(raw_packet.get_payload()).copy()
        self.raw_form = IP(raw_packet.get_payload()).copy()
        self.layer_dict = {
            "ETHER": "Ethernet II",
            "IP": "Internet Control Message Protocol",
            "TCP": "Transmission Control Protocol",
            "UDP": "User Datagram Protocol",
            "DNS": "Domain Name System"
        }
        self.proto = {
            "udp": 17,
            "tcp": 6
        }
        self.tcp_flags = {
            "F": "FIN",
            "S": "SYN",
            "R": "RST",
            "P": "PSH",
            "A": "ACK",
            "U": "URG",
            "E": "ECE",
            "C": "CWR"
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
                
    # Save modifications to the packet. This gives the raw packet the new values and updates the checksum.
    def save_modifications(self):
        for layer_idx in range(0, len(self.layers)):
            layer = self.layers[layer_idx]
            if layer == "Ether":
                raw_layer = self.ether_layer
            else:
                raw_layer = self.raw_form.getlayer(layer_idx-1)
            if raw_layer == None:
                continue
            for field in raw_layer.fields_desc:
                if field.name in self.fields[layer]:
                    if field.name == None:
                        continue
                    field_type = type(getattr(raw_layer, field.name))
                    try:
                        # If  Protocol, then attribute must be converted to a scapy req
                        if field.name == "proto":
                            setattr(raw_layer, field.name, self.proto[self.fields[layer][field.name]])
                            continue
                        # Skip if Options for now: Uncertain how to manually edit options field
                        if field.name == "options":
                            continue
                        # Skip if field type is None 
                        if field_type == type(None): 
                            continue
                        # Skip if flag value for now: Uncertain how to manually edit Flags field
                        elif field_type == scapy.fields.FlagValue:
                            continue
                        # Convert to string to check if hexadecimal or decimal notation
                        elif field_type == int: 
                            setattr(raw_layer, field.name, int(str(self.fields[layer][field.name]), 0))
                        # Convert string to bytes with utf encoding
                        elif field_type == bytes:
                            setattr(raw_layer, field.name, bytes(self.fields[layer][field.name], "utf-8"))
                        else:
                            setattr(raw_layer, field.name, field_type(self.fields[layer][field.name]))
                    except ValueError:
                        #DEBUG:
                        #print("Field value at {} requires a typing that is currently not supported in this system.".format(field.name))
                        continue

        # Recalculate Changes to Length & Chksum
        del self.raw_form.chksum
        del self.raw_form.len
        del self.raw_form.getlayer(1).chksum
        self.raw_form.show2(dump=True)
        # Have to re-dissect packet after recalculation
        del self.layers[1::] 
        self.dissect_IP(Dissector(self.raw_form))

    def convert_to_raw(self):
        return self.raw_form
