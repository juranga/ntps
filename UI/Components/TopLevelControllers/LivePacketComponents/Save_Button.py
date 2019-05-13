from UI.Components.TopLevelControllers.LivePacketComponents.Field_Area_Component import Field_Area_Component

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Save_Button():

    def __init__(self, proxy_server = Proxy_Server(), field_area = Field_Area_Component()):
        self.button = QPushButton()
        self.proxy_server = proxy_server
        self.field_area = field_area
        self.new_packets = []
        self.packet_idx = 0

    def install_widgets(self, parent=None):
        self.button = QPushButton("Save Modification", parent)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        print("Saving changes to packet...")
        self.packet_idx = self.field_area.packet_idx
        self.proxy_server.intercept_queue.packet_list[self.packet_idx] = self.field_area.edited_packet_list[self.packet_idx]
        self.proxy_server.intercept_queue.packet_list[self.packet_idx].save_modifications()
        
