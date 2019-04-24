from scapy.all import sniff

class Capture_Filter: 

    filters = { 
        "bpf": bpf
    }

    def __init__(self, cfilter="bpf"):
        self.filter = self.filters[cfilter]

    def change_filter(self, cfilter: str):
            self.filter = self.filters[cfilter]

    def bpf(self, packet, input_filter=""):
        return sniff(offline=packet, filter=input_filter)
