from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

from PyQt5 import QtGui, QtCore, QtWidgets

class Proxy_Toggle_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server

    def install_widgets(self, parent):
        self.combo_box = QtWidgets.QComboBox(parent)
        self.combo_box.addItems(["Enabled/Disabled", "Enabled", "Disabled"])
        self.combo_box.setCurrentText("Enabled/Disabled")
        self.combo_box.currentIndexChanged.connect(self.selection_change)
        self.combo_box.setMaxVisibleItems(3)

    # TODO: Needs more testing.
    def selection_change(self):
        if self.combo_box.currentText() == "Enabled":
            self.proxy_server.init_server()
        else:
            self.proxy_server.stop_server()
