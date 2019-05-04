from collections import defaultdict

class Packet:

    def __init__(self, raw_packet):
        self.raw_form = raw_packet
        self.layers = []
        self.fields = defaultdict(dict)

    def get_layers():
        return self.layers

    def get_fields():
        return self.fields