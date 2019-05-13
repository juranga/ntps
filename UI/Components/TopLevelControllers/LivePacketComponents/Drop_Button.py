from UI.Components.TopLevelControllers.LivePacketComponents.Field_Area_Component import Field_Area_Component

from Infrastructure.PacketLibrary.Packet_Bus import drop_packet
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Drop_Button():

    def __init__(self, proxy_server = Proxy_Server(), field_area = Field_Area_Component()):
        self.button = QPushButton()
        self.proxy_server = proxy_server
        self.field_area = field_area
        return

    def install_widgets(self, parent=None):
        self.button = QPushButton("Drop", parent)
        self.button.clicked.connect(self.on_clicked)
        

    def on_clicked(self):
        print("Dropping packet...")
        print(self.field_area.packet_idx)
        drop_packet("intercept", self.proxy_server.intercept_queue, self.field_area.packet_idx)
