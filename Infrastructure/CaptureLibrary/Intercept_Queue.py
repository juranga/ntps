from Infrastructure.Common.Generators import id_generator
from Infrastructure.PacketLibrary.Packet import Dissected_Packet
from Infrastructure.PacketLibrary.Dissector import Dissector

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import QThread
from threading import Lock
from multiprocessing import Value

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"
class Intercept_Queue:

    def __init__(self, size=100):
        self.size = size
        self.model = QStandardItemModel()
        self.packet_list = []
        self.lock = Lock()

    def populate_gui(self):
        print('Populating to GUI...', flush=True)
        layer_dict = self.packet_list[-1].layer_dict

        parent = QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ', '.join(self.packet_list[-1].layers)
            ))
        parent.setEditable(False)
        self.model.appendRow(parent)

        for layer in self.packet_list[-1].layers:
            display_layer = layer
            if layer in layer_dict:
                display_layer = layer_dict[layer]
            if "src" in self.packet_list[-1].fields[layer] and "dst" in self.packet_list[-1].fields[layer]:
                src = self.packet_list[-1].fields[layer]["src"]
                dst = self.packet_list[-1].fields[layer]["dst"]
                child = QStandardItem(QIcon(circle),
                    "{}, Src:{}, Dst:{}".format(display_layer, src, dst))
            else:
                child = QStandardItem(QIcon(circle),
                    "{}".format(display_layer))
            child.setEditable(False)
            self.model.itemFromIndex(self.model.indexFromItem(parent)).appendRow(child)
        
    def put(self, raw_packet):
        with self.lock:
            if self.size > len(self.packet_list):
                self.packet_list.append(Dissected_Packet(raw_packet))
                self.dissect_put(Dissector(raw_packet))
                self.populate_gui()

    def dissect_put(self, packet, idx = -1, icon=arrow):
        packet_layers = self.packet_list[-1].layers
        packet_fields = self.packet_list[-1].fields
        for key, value in packet.items():
            if type(value) is dict:
                packet_layers.append(key)
                self.dissect_put(value, idx+1, circle)
                break
            else:
                packet_fields[packet_layers[idx]][key] = value

    def get(self):
        packet = self.packet_list[0]
        del self.packet_list[0]
        self.model.removeRow(0)
        return packet
