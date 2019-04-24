
class PCAP:

    def __init__(self, name=""):
        self.name = name
        self.traffic = []

    def change_name(self, name):
        self.name = name

    def save(self, addr):
        # TODO: Save PCAP to addr specified
        return

    def load(self, addr):
        # TODO: Load PCAP from addr specified
        return