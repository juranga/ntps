from Infrastructure.CaptureLibrary.Filters.Capture_Filter import Capture_Filter
from Infrastructure.CaptureLibrary.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP
from Infrastructure.PacketLibrary.Packet_Dict import PacketDict
from Infrastructure.HookLibrary.Hook_Collection_Manager import Hook_Collection_Manager

from queue import Queue
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

class Proxy_Server:

    def __init__(self, capture_filter=Capture_Filter(), live_pcap=PCAP(), 
                       intercept_queue=Intercept_Queue(100), hook_manager=Hook_Collection_Manager(),
                       nfq=NetfilterQueue()):
        self.capture_filter = capture_filter
        self.live_pcap = live_pcap
        self.intercept_queue = intercept_queue
        self.interceptFlag = True
        self.hook_manager = hook_manager
        self.nfq = nfq

    def start_intercept(self):
        self.interceptFlag = True

    def stop_intercept(self):
        self.interceptFlag = False

    def handle_new_packet(self, raw_packet):
        packet = IP(raw_packet.get_payload()).copy()
        self.intercept_queue.install_packet(packet)

        #TODO: Fix Capture Filter
        if self.capture_filter.filter(packet):
            self.hook_manager.execute_hooks(packet)
            self.live_pcap.traffic.append(packet)
            with self.intercept_queue.lock:
                if self.interceptFlag and self.intercept_queue.size >= len(self.intercept_queue.packet_list):
                    self.intercept_queue.put(PacketDict(packet))
                    self.intercept_queue.populate()
        raw_packet.drop()

    def stop_server(self):
        self.nfq.unbind()
        os.system("iptables -D OUTPUT -j NFQUEUE --queue-num 0")
        print("Unbinded")

    # TODO: Thread function
    def init_server(self):
        iptablesr = "iptables -A OUTPUT -j NFQUEUE --queue-num 0"
        
        os.system(iptablesr)
        self.nfq.bind(0, self.handle_new_packet)
        
        try:
            print('Listening for packets...')
            self.nfq.run(block=False)
        except KeyboardInterrupt:
            self.stop_server()
