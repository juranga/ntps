from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5 import QtGui, QtCore, QtWidgets
from threading import Thread

class Intercept_Toggle_Component():
    def __init__(self, proxy_server= Proxy_Server()):

        self.proxy_server = proxy_server
        self.thread = None

    def install_widgets(self, parent, sizePolicy, font):
        self.combo_box = QtWidgets.QComboBox(parent)
        self.combo_box.addItems(["Disabled", "Enabled"])
        self.combo_box.setCurrentText("Disabled")
        self.combo_box.currentIndexChanged.connect(self.selection_change)
        self.combo_box.setMaxVisibleItems(2)

    def selection_change(self, idx):
        if self.combo_box.currentText() == "Enabled":
            print("Interception enabled.")
            self.thread = Thread(target=self.proxy_server.start_intercept)
            self.thread.daemon= True
            self.thread.start()
        else:
            print("Interception disabled.")
            if not self.thread == None:
                self.thread.join(5)
                self.proxy_server.stop_intercept
            self.thread = None
