# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, raw_packet, intercept_queue, capture_filter, hook_manager, live_pcap, interceptFlag):
        QThread.__init__(self, parent)
        self.raw_packet = raw_packet
        self.intercept_queue = intercept_queue
        self.capture_filter = capture_filter
        self.hook_manager = hook_manager
        self.live_pcap = live_pcap
        self.interceptFlag = interceptFlag

    def threaded_packet_handler(self):
        packet = IP(self.raw_packet.get_payload()).copy()
        self.intercept_queue.install_packet(packet)

        #TODO: Fix Capture Filter
        if self.capture_filter.filter(packet):
            self.hook_manager.execute_hooks(packet)
            self.live_pcap.traffic.append(packet)
            with self.intercept_queue.lock:
                if self.interceptFlag and self.intercept_queue.size >= len(self.intercept_queue.packet_list):
                    self.intercept_queue.put(PacketDict(packet))
                    self.intercept_queue.populate(self.intReady) 
        self.raw_packet.drop()
        self.finished.emit()