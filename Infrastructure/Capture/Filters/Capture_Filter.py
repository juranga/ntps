from scapy.all import sniff

class Capture_Filter: 

    """
    self.filters = { 
        "bpf": self.bpf
    }
    """

    def __init__(self, cfilter="bpf"):
        self.filters = {
            "bpf": self.bpf
        }
        self.filter = self.filters[cfilter]

    def change_filter(self, cfilter: str):
            self.filter = self.filters[cfilter]

    def bpf(self, packet, input_filter=""):
        return sniff(offline=packet, filter=input_filter)
    
