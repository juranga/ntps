# An object representing a packet in the system.
import datetime

class NTPS_Packet:

    def __init__(self, layer_list = {}, packet_name = "", timestamp = datetime.datetime.now().time()):
        self.layers = layer_list
        self.packet_name = packet_name
        self.timestamp = timestamp

    def set_name(self, new_name):
        self.packet_name = new_name

    def get_name(self):
        return packet_name

    def set_time(self, new_time):
        self.timestamp = new_time

    def get_time(self):
        return self.timestamp
        
    def get_packet_layers(self):
        return self.layer_list

    def set_packet_layers(self, new_list):
        self.layers = new_list
    
