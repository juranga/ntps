# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, q):
        QThread.__init__(self, None)

    def threaded_packet_handler(self):
        self.q.populate()
        finished.emit()