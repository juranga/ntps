from scapy.all import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

class Intercept_Queue:

    def __init__(self):
        self.intercept_queue = QStandardItemModel()

    def put(self, elements, icon="root/ntps/UI/Resources/BlueArrow.png"):
        print(elements)
        for text, children in elements:
            print(text)
            item = QStandardItem(QIcon(icon), text)
            self.intercept_queue.appendRow(item)
            if children:
                self.put(self, children, icon="root/ntps/UI/Resources/CircularButton.png")
