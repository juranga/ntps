interceptFlag = True

from Filters import Capture_Filter
from InterceptQueue import *
import socket
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

class ProxyServer:

    def __init__(self):
        self.capture_filter = ""
        self.live_pcap_name = ""
        self.live_traffic_list = []
        self.intercept_queue = InterceptQueue()

    def change_filter(self, cfilter: str):
        capture_filter = cfilter

    def change_pcap_name(self, name: str):
        live_pcap_name = name

    def handle_new_packet(self, p):
        packet = p.get_payload()
        #self.live_traffic_list.append(packet.copy())
        
        #print(Capture_Filter.BPF_Filter(packet))

        # TODO: Hook Execution before intercept
        if sniff(filter=self.capture_filter) and interceptFlag:
            self.intercept_queue.put(packet.copy())
        print(self.intercept_queue)
        import time
        time.sleep(10)
        packet.drop()

    def drop_packet(self):
        # TODO: Add code to handle removing dropped packets from Intercept Q
        return

    def forward_packet(self):
        # 1. To Forward Packets use: scapy.send(packet)
        # 2. After forwarding a packet with scapy, append forward packet(s) to live traffic list; ex: live_traffic_list.append(packet)
        # TODO: Add code to handle forwarding for more than 1 packet.
        return

    # TODO: thread function
    def init_server(self):
        iptablesr = "iptables -I OUTPUT -j NFQUEUE --queue-num 0"
        os.system(iptablesr)

        nfq = NetfilterQueue()
        nfq.bind(0, self.handle_new_packet)
        try:
            print('Listening for packets...')
            nfq.run()
        except KeyboardInterrupt:
            print('Exiting \n')
        
        #flush 
        os.system('iptables -F')
        os.system('iptables -X')
        nfq.unbind()

ps = ProxyServer()
ps.init_server()
