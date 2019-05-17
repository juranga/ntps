from Infrastructure.HookLibrary.Hook import Hook as hook
from Infrastructure.Common.Generators import id_generator

# An object representing a list of hooks; each hook collection contains one to many hooks, each of which s executed in a specified sequence when enabled.
class Hook_Collection:

    def __init__(self, display_name=id_generator(), enabled=True, sequence_number=0):
        self.hook_list = []
        self.display_name = display_name
        self.sequence_number = sequence_number
        self.n_hooks = 0
        self.enabled = enabled

    def get_name(self):
        return self.display_name

    def enable_hook_collection(self):
        self.enabled = True

    def disable_hook_collection(self):
        self.enabled = False

    def get_sequence_number(self):
        return self.sequence_number

    def delete_hook(self, hook):
        if hook.get_sequence_number > self.n_hooks or hook.get_sequence_number < 0:
            return
        del self.hook_list[hook.sequence_number]
        self.n_hooks -= 1
        for i in range(hook.sequence_number, self.n_hooks):
            self.hook_list[i].sequence_number = i

    def add_hook(self, hook):
        if hook.get_sequence_number() >= self.n_hooks or hook.get_sequence_number() < 0 :
            hook.sequence_number = self.n_hooks
            self.hook_list.append(hook)
        else:
            self.hook_list.append(object)
            for i in range(self.n_hooks, hook.sequence_number, -1):
                self.hook_list[i] = self.hook_list[i-1]
                self.hook_list[i].sequence_number += 1
            self.hook_list[hook.sequence_number] = hook
        self.n_hooks += 1
