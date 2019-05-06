from collections import defaultdict

class Dissected_Packet:

    def __init__(self, raw_packet):
        self.raw_form = raw_packet
        self.layers = []
        self.fields = defaultdict(dict)

    def get_layers(self):
        return self.layers

    def get_fields(self):
        return self.fields
