from Infrastructure.PacketLibrary.Packet_Bus import drop_packet, drop_intercept_packet
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Save_Button():

    def __init__(self):
        self.button = QPushButton()
        return

    def install_widgets(self, parent=None):
        self.button = QPushButton("Save Modification", parent)
        self.button.clicked.connect(self.on_clicked)
        

    def on_clicked(self):
        print("Saving changes to packet...")
