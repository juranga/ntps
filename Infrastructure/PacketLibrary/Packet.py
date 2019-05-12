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

    def get_fields(self):
        return self.fields
    
    def get_layer(self, layer_idx):
        return self.layers[layer_idx]

    def save_modifications(self):
        for layer_idx in range(0, len(self.layers)):
            layer = self.layers[layer_idx]
            for field in self.raw_form.getlayer(layer_idx).fields_desc:
                if field.name in self.fields[layer]:
                    setattr(self.raw_form.getlayer(layer_idx), field.name, self.fields[layer][field.name])