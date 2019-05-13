from UI.Components.TopLevelControllers.LivePacketComponents.Field_Area_Component import Field_Area_Component

from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

class Packet_Area_Component():

    def __init__(self, proxy_server= Proxy_Server(), field_area = Field_Area_Component()):
        self.proxy_server = proxy_server
        self.field_area = field_area

    def install_widgets(self, parent=None):
        self.list = QTreeView(parent)
        self.list.setModel(self.proxy_server.intercept_queue.packet_list_model)
        self.list.clicked.connect(self.on_clicked)
        self.list.show()

    def on_clicked(self, index):
        self.list.expand(index)
        item = index.model().itemFromIndex(index)
        if item.parent() != None:
            self.field_area.set_selected_packet(item.parent().row(), index.row())
            self.proxy_server.intercept_queue.populate_field_area(item.parent().row(), index.row())

