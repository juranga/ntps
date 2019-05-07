from collections import defaultdict

class Dissected_Packet:

    def __init__(self, raw_packet):
        self.raw_form = raw_packet
        self.layer_dict = {
            "IP": "Internet Control Message Protocol",
            "TCP": "Transmission Control Protocol",
            "UDP": "User Datagram Protocol",
            "DNS": "Domain Name System"
        }
        self.layers = []
        self.fields = defaultdict(dict)

    def get_layers(self):
        return self.layers

    def get_layer(self, layer_idx):
        return self.layers[layer_idx]