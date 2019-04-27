from scapy.all import send

# Bus refers to the intercept queue, an array of live packets, or a singular packet
# source = keyword for "intercept",  "pcap", or "hook"
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

def forward_pcap_packet(bus, dest):
    # TODO: Return Error
    return

def forward_hook_packet(bus, dest):
    send(bus)


""" Drop Packet Functions """
def drop_packet(source, bus, dest):
    drop_schedule[source](bus, dest)

def drop_intercept_packet(bus, dest):
    for i in range(0, dest):
        bus.get()

def drop_pcap_packet(bus, dest):
    bus_size = len(bus)
    del bus[dest]
    for i in range(dest, bus_size-1):
        bus[i] = bus[i+1]

# Kept this function call in case future use is desired.
# Currently does nothing, as NFQUEUE packets are all set to drop automatically.
def drop_hook_packet(bus, dest):
    return


""" Miscellaneous Packet Transportation """ 
def add_to_intercept(bus, packet):
    bus.put(packet)


