from Infrastructure.CaptureLibrary.Filters.Capture_Filter import Capture_Filter
from Infrastructure.CaptureLibrary.Intercept_Queue import Intercept_Queue
from Infrastructure.PacketLibrary.PCAP import PCAP
from Infrastructure.PacketLibrary.Packet import NTPS_Packet
from Infrastructure.PacketLibrary.Field import NTPS_Field
from Infrastructure.PacketLibrary.Layer import NTPS_Layer
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

    # Parse a recieved packet into Field, Layer, and packet objects.
    def parse_packet(self, p):
        
        packet_layers = {}
        field_list = {}
        ip_fields = None
        tcp_fields  = None
        icmp_fields = None
        udp_fields = None
        arp_fields = None

        if IP in p:
            ip_fnames = [field.name for field in IP.fields_desc]
            ip_fields = {fname: getattr(p[IP], fname) for fname in ip_fnames}

            #print(ip_fields) #Print statements like this will print all fields in the layer
            for f in ip_fields:
                new_field = NTPS_Field(f, ip_fields[f], "Dissected", 0)
                field_list[f] = new_field

            new_layer = NTPS_Layer("IP","IP", 0, 3, True, 0, field_list)
            packet_layers[IP] = new_layer

        if TCP in p:
            tcp_fnames =[field.name for field in TCP.fields_desc]
            tcp_fields = {fname: getattr(p[TCP], fname) for fname in tcp_fnames}
            for f in tcp_fields:
                new_field = NTPS_Field(f, tcp_fields[f], "Dissected", 0)
                field_list[f] = new_field

            new_layer = NTPS_Layer("TCP","TCP", 0, 4, True, 0, field_list)
            packet_layers[TCP] = new_layer

        if UDP in p:
            udp_fnames =  [field.name for field in UDP.fields_desc]
            udp_fields = {fname: getattr(p[UDP], fname) for fname in udp_fnames}
               
            for f in udp_fields:
                new_field = NTPS_Field(f, udp_fields[f], "Dissected", 0)
                field_list[f] = new_field

            new_layer = NTPS_Layer("UDP","UDP", 0, 4, True, 0, field_list)
            packet_layers[UDP] = new_layer
                
        if ICMP in p:
            icmp_fnames = [field.name for field in ICMP.fields_desc]
            icmp_fields = {fname: getattr(p[ICMP], fname) for fname in icmp_fnames}

            for f in icmp_fields:
                new_field = NTPS_Field(f, icmp_fields[f], "Dissected", 0)
                field_list[f] = new_field

            new_layer = NTPS_Layer("ICMP","ICMP", 0, 3, True, 0, field_list)
            packet_layers[ICMP] = new_layer
                
        if ARP in p:
            arp_fnames  =  [field.name for field in ARP.fields_desc]
            arp_fields = {fname: getattr(p[ARP], fname) for fname in arp_fnames}

            for f in arp_fields:
                new_field = NTPS_Field(f, arp_fields[f], "Dissected", 0)
                field_list[f] = new_field

            new_layer = NTPS_Layer("ARP","ARP", 0, 1, True, 0, field_list)
            packet_layers[ARP] = new_layer

        layer_fields = packet_layers[IP].get_layer_fields()
        new_packet = NTPS_Packet(packet_layers, p.summary())

    def handle_new_packet(self, raw_packet):
        packet = IP(raw_packet.get_payload()).copy()
        self.live_pcap.traffic.append(packet)
        print(packet.summary(),flush=True)

        if self.interceptFlag:
            self.parse_packet(packet)

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
