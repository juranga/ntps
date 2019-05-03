from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItemModel

class Packet_Area_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server

    def install_widgets(self, parent=None):
        self.list = QListView(parent)
        self.model = QStandardItemModel(self.proxy_server.live_pcap.traffic)
        self.list.setModel(model)
        self.list.show()


