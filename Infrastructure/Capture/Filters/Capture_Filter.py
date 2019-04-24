from scapy.all import sniff

class Capture_Filter: 

    """
    self.filters = { 
        "bpf": self.bpf
    }
    """

    def __init__(self, cfilter="bpf", input_filter=""):
        self.filters = {
            "bpf": self.bpf
        }
        self.filter = self.filters[cfilter]
        self.input_filter = input_filter

    def change_filter(self, cfilter: str):
            self.filter = self.filters[cfilter]

    def change_input_filter(self, input_filter: str):
            self.input_filter = input_filter

    def bpf(self, packet):
        return sniff(filter=self.input_filter, count=1)
    
