from Infrastructure.PacketLibrary.Packet_Bus import forward_packet, forward_intercept_packet
from UI.Components.TopLevelControllers.LivePacketComponents.Field_Area_Component import Field_Area_Component

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Forward_Button():

    def __init__(self):
        self.button = QPushButton()
        return

    def install_widgets(self, parent=None):
        self.button = QPushButton("Forward", parent)
        self.button.clicked.connect(self.on_clicked)
        

    def on_clicked(self):
        print("Forwarding packet...")
