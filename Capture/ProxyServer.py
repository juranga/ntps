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

    def handle_new_packet(self, packet):
        live_traffic_list.append(packet.copy())
        print(packet)
        print(Capture_Filter.BPF_Filter(packet))

        # TODO: Hook Execution before intercept
        if scapy.sniff(filter=self.capture_filter) and interceptFlag:
            self.intercept_queue.put(packet.copy())
        print(self.intercept_queue)

        packet.set_verdict(nfqueue.NF_DROP)

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
        nfq = NetfilterQueue()
        nfq.bind(0, self.handle_new_packet)
        s = socket.fromfd(nfq.get_fd(), socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            print('Listening for packets...')
            nfq.run_socket(s)
        except KeyboardInterrupt:
            print('Exiting \n')
        s.close()
        nfq.unbind()

ps = ProxyServer()
ps.init_server()
