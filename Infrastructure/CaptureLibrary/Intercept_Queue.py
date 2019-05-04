from Infrastructure.Common.Generators import id_generator
from Infrastructure.PacketLibrary.Packet import Dissected_Packet

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import QThread
from threading import Lock

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"
class Intercept_Queue:

    def __init__(self, size=100):
        self.size = size
        self.model = QStandardItemModel()
        self.packet_list = []
        self.lock = Lock()

    def populate(self):
        parent = QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ', '.join(self.packet_list[-1].layers)
            ))
        self.model.appendRow(parent)

        for layer in self.packet_list[-1].layers:
            self.model.itemFromIndex(self.model.indexFromItem(parent)).appendRow(QStandardItem(QIcon(circle),
                ", ".join("{}:{}".format(k,v) for k,v in self.packet_list[-1].fields[layer].items())
            ))
        
    def install_packet(self, raw_packet):
        self.packet_list.append(Dissected_Packet(raw_packet))

    def put(self, packet, idx = -1, icon=arrow):
        for key, value in packet.items():
            if type(value) is dict:
                self.packet_list[-1].layers.append(key)
                self.put(value, idx+1, circle)
                break
            else:
                self.packet_list[-1].fields[self.packet_list[-1].layers[idx]][key] = value

    def get(self):
        packet = self.packet_list[0]
        del self.packet_list[0]
        return packet
