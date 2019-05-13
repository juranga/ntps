from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QListView

class Field_Area_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server
        self.edited_packet_list = []
        self.packet_idx = 0
        self.layer_idx = 0

    def install_widgets(self, parent=None):
        self.list = QListView(parent)
        self.list.setModel(self.proxy_server.intercept_queue.field_list_model)
        self.model = self.list.model()
        self.model.itemChanged.connect(self.on_edit)
        self.list.show()

    def set_selected_packet(self, pidx, lidx):
        self.packet_idx = pidx
        self.layer_idx = lidx

    def on_edit(self, item):
        if ":" not in item.text():
            print("ERROR: malformed field. Changes not saved.")
            print("Please make sure field is in the form 'fieldname:value'.")
            return
        newField = item.text().split(":")
        self.edited_packet_list = self.proxy_server.intercept_queue.packet_list
        layer = self.edited_packet_list[self.packet_idx].get_layer(self.layer_idx)
        fields = self.edited_packet_list[self.packet_idx].fields[layer]
        for k,v in fields.items():
            if (k == newField[0]):
                print("New value {}:{}".format(newField[0],newField[1]))
                print("Replacing: {}:{}".format(k,v))
    
    def on_save():
        return
        
        


