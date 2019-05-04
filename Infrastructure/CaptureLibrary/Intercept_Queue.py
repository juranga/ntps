from Infrastructure.PacketLibrary.Qt_Packet_Item import Qt_Packet_Item
from scapy.all import *

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

class Intercept_Queue():

    def __init__(self):
        self.intercept_queue = QStandardItemModel()

    def put(self, elements, parent=self.intercept_queue, icon="C:\Users\msftb\work\ntps\UI\Resources\BlueArrow.png"):
        for text, children in elements:
            item = QStandardItem(QIcon(icon), text)
            parent.appendRow(item)
            if children:
                self.put(children, item, "C:\Users\msftb\work\ntps\UI\Resources\CircularButton.png")

    """

    def put(self, packet):
        #TODO: Add a function to handle dissected view correctly according to SRS
        dissected_packet = QStandardItem(QIcon("C:\Users\msftb\work\ntps\UI\Resources\CircularButton.png"), str(packet))

        # Make packets not editable via double click or single click.
        dissected_packet.setEditable(False)
        binary_packet.setEditable(False)
        hex_packet.setEditable(False)

        if self.list_len < self.size:
            self.dissected_list.appendRow(dissected_packet)
        self.list_len += 1

    def get(self):
        item = self.list.itemFromIndex(0)
        self.dissected_list.removeRow(0)
        self.list_len -= 1
        return item

    """
