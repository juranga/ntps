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
                       intercept_queue=Queue(100), hook_manager= Hook_Collection_Manager()):
        self.capture_filter = capture_filter
        self.live_pcap = live_pcap
        self.intercept_queue = intercept_queue
        self.interceptFlag = False
        self.hook_manager = hook_manager

    def start_intercept(self):
        self.interceptFlag = True

    def stop_intercept(self):
        self.interceptFlag = False

    def handle_new_packet(self, raw_packet):
        packet = IP(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)
        
        #TODO: Fix Capture Filter
        if self.capture_filter.filter(packet) and self.interceptFlag:
            self.hook_manager.execute_hooks(packet, self.intercept_queue)

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
        except (KeyboardInterrupt, SystemExit):
            print('Shutting down the NFQUEUE')
            os.system('iptables -F')
            os.system('iptables -X')
            nfq.unbind()
        
        """
        print('Stopping intercept')
        # Flush IpTables 
        # TODO: Find a way to NOT flush IPTables, and restore instead
        os.system('iptables -F')
        os.system('iptables -X')
        nfq.unbind()
        """
