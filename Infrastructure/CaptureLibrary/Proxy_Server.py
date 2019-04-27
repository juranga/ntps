from Infrastructure.CaptureLibrary.Filters.Capture_Filter import Capture_Filter
from Infrastructure.CaptureLibrary.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP

from Infrastructure.HookLibrary.Hook import Hook

from queue import Queue
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

class Proxy_Server:

    def __init__(self, capture_filter=Capture_Filter(), live_pcap=PCAP(), intercept_queue=Queue(100)):
        self.capture_filter = capture_filter
        self.live_pcap = live_pcap
        self.intercept_queue = intercept_queue
        self.interceptFlag = False
        self.hook_test = Hook('hi', 'pathhere')

    def start_intercept(self):
        self.interceptFlag = True

    def stop_intercept(self):
        self.interceptFlag = False

    def handle_new_packet(self, raw_packet):
        packet = Ether(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)

        self.hook_test.execute_hook(packet)
        print(TCP(IP(packet)))

        """ TODO: Fix Capture Filter
        if self.capture_filter.filter(packet) and self.interceptFlag:
            # TODO: Hook Execution before intercept
            # TODO: Put this code in to HookCollectionManager: self.intercept_queue.put(packet)
        """

        raw_packet.drop()

    # TODO: Thread function
    def init_server(self):
        iptablesr = "iptables -I OUTPUT -j NFQUEUE --queue-num 0"
        #iptablesr = "iptables -I INPUT -j NFQUEUE --queue-num 0"
        os.system(iptablesr)

        nfq = NetfilterQueue()
        nfq.bind(0, self.handle_new_packet)
        try:
            print('Listening for packets...')
            nfq.run()
        except KeyboardInterrupt:
            print('Shutting down the NFQUEUE')
        
        # Flush IpTables 
        # TODO: Find a way to NOT flush IPTables, and restore instead
        os.system('iptables -F')
        os.system('iptables -X')
        nfq.unbind()
