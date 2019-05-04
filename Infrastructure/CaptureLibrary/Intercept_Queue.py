from Infrastructure.Common.Generators import id_generator

from scapy.all import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from collections import defaultdict

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"

class Intercept_Queue:

    def __init__(self):
        self.model = QStandardItemModel()
        self.layers = []
        self.fields = defaultdict(dict)

    def populate(self):
        self.model.appendRow(QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ', '.join(self.layers))
                ))
        for layer in self.layers:
            self.model.appendRow(QStandardItem(QIcon(circle),
                ", ".join("{}:{}".format(k,v) for k,v in self.fields[layer].items())
                ))

    def install_packet(self, packet):
        self.packet = packet

    def put(self, elements, idx = -1, icon=arrow):
        for key, value in elements.items():
            if type(value) is dict:
                self.layers.append(key)
                self.put(value, idx+1, circle)
                break
            else:
                self.fields[self.layers[idx]][key] = value
        self.populate()

