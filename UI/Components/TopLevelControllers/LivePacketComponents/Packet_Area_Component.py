from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

from PyQt5.QtWidgets import QTreeView

class Packet_Area_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server

    def install_widgets(self, parent=None):
        self.list = QTreeView(parent)
        self.list.setModel(self.proxy_server.intercept_queue.model)
        self.list.clicked.connect(self.on_clicked)
        self.list.show()

    def on_clicked(self):
        return
        

