from Infrastructure.CaptureLibrary.Filters.Capture_Filter import Capture_Filter
from Infrastructure.CaptureLibrary.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP
from Infrastructure.HookLibrary.Hook_Collection_Manager import Hook_Collection_Manager

from queue import Queue
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

class Proxy_Server:

    def __init__(self, capture_filter=Capture_Filter(), live_pcap=PCAP(), 
                       intercept_queue=Queue(100), hook_manager=Hook_Collection_Manager(),
                       nfq=NetfilterQueue()):
        self.capture_filter = capture_filter
        self.live_pcap = live_pcap
        self.intercept_queue = intercept_queue
        self.interceptFlag = False
        self.hook_manager = hook_manager
        self.nfq = nfq

    def start_intercept(self):
        self.interceptFlag = True

    def stop_intercept(self):
        self.interceptFlag = False

    def handle_new_packet(self, raw_packet):
<<<<<<< Updated upstream
        packet = IP(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)
        print(packet.summary())

        #TODO: Fix Capture Filter
        if self.capture_filter.filter(packet) and self.interceptFlag:
            self.hook_manager.execute_hooks(packet, self.intercept_queue)

=======
        packet = Dissected_Packet(raw_packet)
        
        print('Captured packet...', flush=True)
        # TODO: Fix Capture Filter
        # if self.capture_filter.filter(packet):
        self.hook_manager.execute_hooks(packet, 
                intercept_queue=self.intercept_queue if self.intercept_flag else None,
                live_traffic_list=self.live_pcap.traffic
                )
>>>>>>> Stashed changes
        raw_packet.drop()

    def stop_server(self):
        os.system('iptables -F')
        os.system('iptables -X')
        self.nfq.unbind()
        print("Unbinded")

    # TODO: Thread function
    def init_server(self):
        iptablesr = "iptables -I OUTPUT -j NFQUEUE --queue-num 0"
        #iptablesr = "iptables -I INPUT -j NFQUEUE --queue-num 0"
        
        os.system(iptablesr)
        self.nfq.bind(0, self.handle_new_packet)
        
        try:
            print('Listening for packets...')
            self.nfq.run(block=False)
        except KeyboardInterrupt:
            self.stop_server()
