from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

from PyQt5 import QtGui, QtCore, QtWidgets
from threading import Thread

class Proxy_Toggle_Component():

    def __init__(self, parent, sizePolicy, font, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server
        self.proxy_thread = None

    def install_widgets(self, parent, sizePolicy, font)
        self.combo_box = QtWidgets.QComboBox(parent)
        self.combo_box.addItems(["Enabled/Disabled", "Enabled", "Disabled"])
        self.combo_box.setCurrentText("Enabled/Disabled")
        self.combo_box.currentIndexChanged.connect(self.selection_change)
        self.combo_box.setMaxVisibleItems(3)

    # TODO: Not sure if this will work. Needs testing.
    def selection_change(self, idx):
        if not self.combo_box.currentText() == "Enabled" and not self.proxy_thread == None:
            print("Thread Disabled")
            self.proxy_thread._stop()
            self.proxy_thread = None
        elif self.combo_box.currentText() == "Enabled":
            print("Thread Enabled")
            self.proxy_thread = Thread(target=self.proxy_server.init_server)
            self.proxy_thread.start()
        