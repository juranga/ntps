from Infrastructure.Common.Generators import id_generator
from Infrastructure.PacketLibrary.Packet import Dissected_Packet

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import QThread
from threading import Lock
from multiprocessing import Value

## An object representing an intercept queue in the network traffic proxy system.

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"
class Intercept_Queue:

    def __init__(self, size=100):
        self.size = size
        self.packet_list_model = QStandardItemModel()
        self.field_list_model = QStandardItemModel()
        self.packet_list = []
        self.lock = Lock()

    #Populates the main model with packets.
    def populate(self):
        parent = QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ': '.join(self.packet_list[-1].layers)
            ))
        self.packet_list_model.appendRow(parent)

        for layer in self.packet_list[-1].layers:
            self.packet_list_model.itemFromIndex(self.packet_list_model.indexFromItem(parent)).appendRow(QStandardItem(QIcon(circle),
                ", ".join("{}:{}".format(k,v) for k,v in self.packet_list[-1].fields[layer].items())
            ))
            
    # Populates the field list model with a given packet
    def populate_fields(self, packet_idx, layer_idx):
        self.field_list_model.removeRows(0,self.field_list_model.rowCount())
        layers = self.packet_list[packet_idx].get_layers()
        layer = layers[layer_idx]
        fields = self.packet_list[packet_idx].fields[layer]

        for k,v in fields.items():
            self.field_list_model.appendRow(QStandardItem("".join("{}:{}".format(k,v))
            ))
            
    # Place a dissected packet in the list of stored packets.    
    def install_packet(self, raw_packet):
        self.packet_list.append(Dissected_Packet(raw_packet))

    # Setting the fields and their values
    def put(self, packet, idx = -1, icon=arrow):
        for key, value in packet.items():
            if type(value) is dict:
                self.packet_list[-1].layers.append(key)
                self.put(value, idx+1, circle)
                break
            else:
                self.packet_list[-1].fields[self.packet_list[-1].layers[idx]][key] = value

    # Same as put, but in hex: EXPERIMENTAL            
    def put_convert(self, packet, idx = -1, icon=circle):

        for key, value in packet.items():
            if type(value) is dict:
                self.packet_list[-1].layers.append(key)
                self.put_convert(value, idx+1, arrow)
                break
            else:
                if ((value != None) and (value.isdigit())):
                    value = int(value)
                    self.packet_list[-1].fields[self.packet_list[-1].layers[idx]][key] = hex(value)
                else:
                    self.packet_list[-1].fields[self.packet_list[-1].layers[idx]][key] = value

    # Get a packet from the list of packets.                
    def get(self):
        packet = self.packet_list[0]
        del self.packet_list[0]
        return packet


            


