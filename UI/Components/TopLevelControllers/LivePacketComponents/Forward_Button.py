from Infrastructure.PacketLibrary.Packet_Bus import forward_packet, forward_intercept_packet
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QListView
from threading import Thread

class Forward_Button():

    def __init__(self):

    def install_widgets(self, parent=None):
        self.button = QtGui.QPushButton("Forward", parent)

    def on_clicked(self, index):
        
