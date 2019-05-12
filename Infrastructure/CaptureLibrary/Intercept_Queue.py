from Infrastructure.Common.Generators import id_generator
from Infrastructure.PacketLibrary.Packet import Dissected_Packet

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from threading import Lock

## An object representing an intercept queue in the network traffic proxy system.

arrow = "/root/ntps/UI/Resources/BlueArrow.png"
circle = "/root/ntps/UI/Resources/CircularButton.png"
class Intercept_Queue:

    def __init__(self, size=100):
        self.queue = Queue(size)
        self.size = size
        self.packet_list_model = QStandardItemModel()
        self.field_list_model = QStandardItemModel()
        self.packet_list = []
        self.lock = Lock()

    # Populates the packet area component with packets.
    def populate_packet_area(self):
        print('Populating to GUI...', flush=True)

        """ Populate Parent Node """
        layer_dict = self.packet_list[-1].layer_dict
        
        parent = QStandardItem(QIcon(arrow), 
                "Frame {}, {}".format(id_generator(size=3), ', '.join(self.packet_list[-1].layers)
                ))
        parent.setEditable(False)
        self.packet_list_model.appendRow(parent)

        """ Populate Children of Parent """
        for layer in self.packet_list[-1].layers:
            display_layer = layer
            if layer in layer_dict:
                display_layer = layer_dict[layer]
            if "src" in self.packet_list[-1].fields[layer] and "dst" in self.packet_list[-1].fields[layer]:
                src = self.packet_list[-1].fields[layer]["src"]
                dst = self.packet_list[-1].fields[layer]["dst"]
                child = QStandardItem(QIcon(circle),
                    "{}, Src:{}, Dst:{}".format(display_layer, src, dst))
            elif "sport" in self.packet_list[-1].fields[layer] and "dport" in self.packet_list[-1].fields[layer]:
                src = self.packet_list[-1].fields[layer]["sport"]
                dst = self.packet_list[-1].fields[layer]["dport"]
                child = QStandardItem(QIcon(circle),
                    "{}, Src Port:{}, Dst Port:{}".format(display_layer, src, dst))
            else:
                child = QStandardItem(QIcon(circle),
                    "{}".format(display_layer))
            child.setEditable(False)
            self.packet_list_model.itemFromIndex(self.packet_list_model.indexFromItem(parent)).appendRow(child)

     # Populates the field list model with fields from the selected layer.
    def populate_field_area(self, packet_idx, layer_idx):        
        self.field_list_model.removeRows(0,self.field_list_model.rowCount())
        layer = self.packet_list[packet_idx].get_layer(layer_idx)
        fields = self.packet_list[packet_idx].fields[layer]
        for k,v in fields.items():
            self.field_list_model.appendRow(QStandardItem("".join("{}:{}".format(k,v))
            ))
            
    def put(self, packet):
        with self.lock:
            if self.size > len(self.packet_list):
                self.packet_list.append(packet)
                self.populate_packet_area()

    # Get a packet from the list of packets.                
    def get(self):
        with self.lock:
            packet = self.packet_list[0]
            del self.packet_list[0]
            self.packet_list_model.removeRow(0)
            return packet