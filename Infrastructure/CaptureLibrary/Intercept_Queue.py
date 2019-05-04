from scapy.all import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

class Intercept_Queue:

    def __init__(self):
        self.intercept_queue = QStandardItemModel()

    def put(self, elements, icon="root/ntps/UI/Resources/BlueArrow.png"):
        for key, value in elements:
            if type(value) is dict:
                yield from self.put(self, value, icon="root/ntps/UI/Resources/CircularButton.png")
            else:
                item = QStandardItem(QIcon(icon), key)
                self.intercept_queue.appendRow(item)
