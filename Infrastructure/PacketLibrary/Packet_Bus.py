from scapy.all import sendp 

# Bus refers to the intercept queue or an array of live packets.
# source = keyword for "intercept" or "pcap"
# dest = the index of the packet within the queue or list

forward_schedule = {
    "hook": forward_hook_packet,
    "intercept": forward_intercept_packet,
    "pcap": forward_pcap_packet
}

drop_schedule = {
    "hook": drop_hook_packet,
    "intercept": drop_intercept_packet,
    "pcap": drop_pcap_packet
}

""" Forward Packet Function """
def forward_packet(source, bus, dest):
    forward_schedule[source](bus, dest)

def forward_intercept_packet(bus, dest):
    for i in range(0, dest):
        send(bus.get())
    return 

def forward_pcap_packet(bus, dest):
    # TODO: Return Error
    return

def forward_hook_packet(packet, dest):
    # TODO: Add to Intercept Queue
    return


""" Drop Packet Functions """
def drop_packet(source, bus, dest):
    drop_schedule[source](bus, dest)

def drop_intercept_packet(bus, dest):
    for i in range(0, dest):
        bus.get()

def drop_pcap_packet(bus, dest):
    del bus[0:dest]
    bus = bus[dest:-1]

def drop_hook_packet(packet, dest):
    # TODO: Do not add to Intercept Queue
    return


""" Miscellaneous Packet Transportation """ 
def add_to_intercept(bus, packet):
    bus.put(packet)


