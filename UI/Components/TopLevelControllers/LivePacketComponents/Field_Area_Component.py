from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QListView

class Field_Area_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server

    def install_widgets(self, parent=None):
        self.list = QListView(parent)
        self.list.setModel(self.proxy_server.intercept_queue.field_list_model)
        self.list.show()


