from Infrastructure.PacketLibrary.Packet_Dict import PacketDict
from Infrastructure.PacketLibrary.Packet import Dissected_Packet

# An object that can convert a given value to hexidecimal, dissected, and binary format. Incomplete!
class DisplayFormat:

    valid_formats = {"dissected", "binary", "hex"}
    
    def __init__(self, selected_format = "dissected"):
        if selected_format in valid_formats:
            self.selected_format = selectedFormat
        else:
            print("Format invalid!")
            self.selected_format = "dissected"

    def convert(self, value):
        if self.selected_format ==  "binary":
            return bin(value)
        if self.selected_format == "hex":
            return hex(value)
        
