from Flags import *
from InterceptQueue import *

import nfqueue
from scapy.all import *
import os

class ProxyServer:

    __init__():
        capture_filter = ""
        live_pcap_name = ""
        live_traffic_list = []
        intercept_queue = InterceptQueue()

    def change_filter(cfilter: str):
        capture_filter = cfilter

    def change_pcap_name(name: str):
        live_pcap_name = name

    def handle_new_packet(packet: nfqueue.Packet):
        live_traffic_list.append(packet.copy())

        # TODO: Should we block the thread if intercept Q is full, or should we just drop all new packets if it's full?
        if scapy.sniff(filter=this.capture_filter, 0) and interceptFlag:
            intercept_queue.put(packet.copy())

        packet.set_verdict(nfqueue.NF_DROP)

    def drop_packet():
        # TODO: Add code to handle removing dropped packets from Intercept Q
        return

    def forward_packet():
        # 1. To Forward Packets use: scapy.send(packet)
        # 2. After forwarding a packet with scapy, append forward packet(s) to live traffic list; ex: live_traffic_list.append(packet)
        # TODO: Add code to handle forwarding for more than 1 packet.
        return

    # TODO: thread function
    def init_server():
        # TODO: Add code to set iptable rule 
        nfq = nfqueue.queue()
        nfq.open()
        nfq.bind(socket.AF_INET) # Bind to Ipv4 
        nfq.set_callback(handle_new_packet)
        nfq.create_queue(0)
        try:
            nfq.run() # main loop
        except KeyboardInterrupt: 
            nfq.unbind(socket.AF_INET)
            nfq.close()
            # TODO: Add code to return iptables to original state.
           

