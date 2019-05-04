from Infrastructure.Common.Generators import id_generator
from Infrastructure.PacketLibrary.Packet import Packet

from scapy.all import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"

class Intercept_Queue:

    def __init__(self, size=100):
        self.size = size
        self.model = QStandardItemModel()
        self.packet_list = []

    def populate(self):
        self.model.appendRow(QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ', '.join(self.packet_list[-1].layers))
            ))

        for layer in range(0, self.packet_list[-1].layers):
            print(layer)
            self.model.itemFromIndex(layer).appendRow(QStandardItem(QIcon(circle),
                ", ".join("{}:{}".format(k,v) for k,v in self.packet_list[-1].fields[layer].items())
            ))

    def install_packet(self, raw_packet):
        self.packet_list.append(Packet(raw_packet))

    def put(self, packet, idx = -1, icon=arrow):
        for key, value in packet.items():
            if type(value) is dict:
                self.packet_list[-1].layers.append(key)
                self.put(value, idx+1, circle)
                break
            else:
                self.packet_list[-1].fields[self.packet_list[-1].layers[idx]][key] = value
        self.populate()

