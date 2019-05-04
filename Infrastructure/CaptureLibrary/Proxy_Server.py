from Infrastructure.CaptureLibrary.Filters.Capture_Filter import Capture_Filter
from Infrastructure.CaptureLibrary.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP
from Infrastructure.PacketLibrary.Packet import Packet
from Infrastructure.PacketLibrary.Field import Field
from Infrastructure.PacketLibrary import Layer
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
        print("Interception enabled.")

    def stop_intercept(self):
        self.interceptFlag = False
        print("Interception disabled.")

    def handle_new_packet(self, raw_packet):
        packet = IP(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)
        print(packet.summary(),flush=True)

        if(self.interceptFlag):
            print("Packet intercepted", flush=True)    
            self.intercept_queue.put(packet)

            """TRYING TO EXTRACT DATA FROM PACKETS"""
            packet_layers = {}
            field_list = {}
            ip_fields = None
            tcp_fields  = None
            icmp_fields = None
            udp_fields = None
            arp_fields = None

            if IP in packet:
                ip_fnames = [field.name for field in IP.fields_desc]
                ip_fields = {fname: getattr(packet[IP], fname) for fname in ip_fnames}
                #print(ip_fields) #Print statements like this will print all fields in the layer
                """ FIX TO BUILD OBJECTS"""
                #for f in ip_fields:
                    #new_field = Field(f, ip_fields[f], "Dissected", 0)
                    #field_list[f] = new_field

                #new_layer = Layer("IP","IP", 0, 0, True, 0, field_list)
                #packet_layers[IP] = new_layer
                    
                    
            if TCP in packet:
                tcp_fnames =[field.name for field in TCP.fields_desc]
                tcp_fields = {fname: getattr(packet[TCP], fname) for fname in tcp_fnames}
            if UDP in packet:
                udp_fnames =  [field.name for field in UDP.fields_desc]
                udp_fields = {fname: getattr(packet[UDP], fname) for fname in udp_fnames}
            if ICMP in packet:
                icmp_fnames = [field.name for field in ICMP.fields_desc]
                icmp_fields = {fname: getattr(packet[ICMP], fname) for fname in icmp_fnames}
            if ARP in packet:
                arp_fnames  =  [field.name for field in ARP.fields_desc]
                arp_fields = {fname: getattr(packet[ARP], fname) for fname in arp_fnames}
            
        #TODO: Fix Capture Filter
        if self.capture_filter.filter(packet) and self.interceptFlag:
            self.hook_manager.execute_hooks(packet, self.intercept_queue)

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
