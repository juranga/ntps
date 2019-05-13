from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Save_Button():

    def __init__(self, proxy_server = Proxy_Server()):
        self.button = QPushButton()
        return

    def install_widgets(self, parent=None):
        self.button = QPushButton("Save Modification", parent)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        print("Saving changes to packet...")
