from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection
from Infrastructure.PacketLibrary.Packet_Bus import forward_packet, drop_packet, add_to_intercept, add_to_live

# A class representing a hook collection manager. This object is, essentially, a list of hook collections; it keeps track of all hook collections loaded into the system and executes them in their designated sequence.
class Hook_Collection_Manager:

    def __init__(self):
        self.hook_collection = []
        self.n_hook_collections = 0

    # Execute every hook in every hook collection in the system.
    def execute_hooks(self, packet, intercept_queue=None, live_traffic_list=None):
        order = ""
        for i in range(0, self.n_hook_collections):
            if not self.hook_collection[i].enabled:
                continue
            for j in range(0, self.hook_collection[i].n_hooks):
                hook = self.hook_collection[i].hook_list[j]
                order = hook.execute_hook(packet.raw_form) # Give Packet's Raw form for Hooks, which is the Scapy
                if order == "Forward":
                    forward_packet("hook", packet)
                    return
                elif order == "Drop":
                    drop_packet("hook", packet)
                    return
        # Dissect the packet and add the raw packet changes
        # We dissect the packet after because we don't want to implement the chksum or length recalculation functions.
        packet.dissect_packet() 
        if not intercept_queue == None:
            add_to_intercept(intercept_queue, packet)
        add_to_live(live_traffic_list, packet)

    # Add a hook collection to the list of hook collections.
    def add_hook_collection(self, hook_collection):
        if int(hook_collection.sequence_number) >= self.n_hook_collections or int(hook_collection.sequence_number) < 0:
            hook_collection.sequence_number = self.n_hook_collections
            self.hook_collection.append(hook_collection)
        else:
            self.hook_collection.append(Hook_Collection())
            for i in range(self.n_hook_collections, hook_collection.sequence_number, -1):
                self.hook_collection[i] = self.hook_collection[i-1]
                self.hook_collection[i].sequence_number += 1
            self.hook_collection[hook_collection.sequence_number] = hook_collection
        self.n_hook_collections += 1

    # Remove a hook collection from the list of hook collections.
    def remove_hook_collection(self, hook_collection):
        if int(hook_collection.sequence_number) > self.n_hook_collections or hook_collection.sequence_number < 0:
            return
        del self.hook_collection[hook_collection.sequence_number]
        self.n_hook_collections -= 1
        for i in range(hook_collection.sequence_number, self.n_hook_collections):
            self.hook_collection[i].sequence_number -= 1
