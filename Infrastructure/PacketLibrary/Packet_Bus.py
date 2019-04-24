from scapy.all import sendp 

# Bus refers to the intercept queue or an array of live packets.
# source = keyword for "intercept" or "pcap"
# dest = the index of the packet within the queue or list

forward_schedule = {
    "intercept": forward_intercept_packet,
    "pcap": forward_pcap_packet
}

drop_schedule = {
    "intercept": drop_intercept_packet,
    "pcap": drop_pcap_packet
}

def forward_packet(source, bus, dest):
    forward_schedule[source](bus, dest)

def drop_packet(source, bus, dest):
    drop_schedule[source](bus, dest)

def forward_intercept_packet(bus, dest):
    for i in range(0, dest):
        sendp(bus.get())
    return 

def drop_intercept_packet(bus, dest):
    for i in range(0, dest):
        bus.get()

def forward_pcap_packet(bus, dest):
    # TODO: Return Error
    return

def drop_pcap_packet(bus, dest):
    del bus[0:dest]
    bus = bus[dest:-1]


