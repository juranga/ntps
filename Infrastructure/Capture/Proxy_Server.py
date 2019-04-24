from Infrastructure.Capture.Filters.Capture_Filter import Capture_Filter
from Infrastructure.Capture.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP

from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

class Proxy_Server:

    def __init__(self, capture_filter=Capture_Filter(), live_pcap=PCAP(), intercept_queue=Intercept_Queue()):
        self.capture_filter = capture_filter
        self.live_pcap = live_pcap
        self.intercept_queue = intercept_queue
        self.interceptFlag = False

    def start_intercept(self):
        self.interceptFlag = True

    def stop_intercept(self):
        self.interceptFlag = False

    def handle_new_packet(self, raw_packet):
        packet = IP(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)

        if self.capture_filter.filter(raw_packet) and self.interceptFlag:
            # TODO: Hook Execution before intercept
            self.intercept_queue.put(packet)

        raw_packet.drop()

    # TODO: Thread function
    def init_server(self):
        iptablesr = "iptables -I OUTPUT -j NFQUEUE --queue-num 0"
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

ps = Proxy_Server()
ps.init_server()
