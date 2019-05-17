from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit

# Class for the interface component that changes the size of the intercept queue!

class Queue_Size_Component():

    def __init__(self, proxy_server= Proxy_Server()):
        self.proxy_server = proxy_server

    def install_widgets(self, parent=None):
        self.line = QLineEdit()
        self.line.textChanged.connect(self.on_edit)
        self.intCheck = QtGui.QIntValidator()
        self.line.setValidator(self.intCheck) # Only allow integers!
        self.line.setText("100")

    # Update queue size whenever field edited.
    def on_edit(self):

        # If input is empty, replace with a 0
        if(self.line.text() == ''):
            try:
                (int(''))
            except ValueError:
                self.line.setText("0")
        
        # Don't let user decrease queue size below number of packets currently in queue
        if (len(self.proxy_server.intercept_queue.packet_list) > int(self.line.text())):
            print("Error: queue size cannot be less than the number of packets in the queue. Forward or drop packets before decreasing the queue size.")
            self.line.setText(str(self.proxy_server.intercept_queue.size))
        else:
            self.proxy_server.intercept_queue.size = int(self.line.text())
        

