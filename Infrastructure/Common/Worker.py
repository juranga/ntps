# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Worker(QObject):
    finished = pyqtSignal()

    def threaded_packet_handler(self, raw_packet, proxy_server):
        packet = IP(raw_packet.get_payload()).copy()
        proxy_server.intercept_queue.install_packet(packet)

        #TODO: Fix Capture Filter
        if proxy_server.capture_filter.filter(packet):
            proxy_server.hook_manager.execute_hooks(packet)
            proxy_server.live_pcap.traffic.append(packet)
            with proxy_server.intercept_queue.lock:
                if proxy_server.interceptFlag and proxy_server.intercept_queue.size >= len(proxy_server.intercept_queue.packet_list):
                    proxy_server.intercept_queue.put(PacketDict(packet))
                    proxy_server.intercept_queue.populate(self.intReady) 
        raw_packet.drop()
        self.finished.emit()