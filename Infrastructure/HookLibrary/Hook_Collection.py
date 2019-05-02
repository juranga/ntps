from Infrastructure.HookLibrary.Hook import Hook
from Infrastructure.Common.Generators import id_generator

class Hook_Collection():

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
        if hook.sequence_number > self.n_hooks or hook.sequence_number < 0:
            return
        del self.hook_list[hook.sequence_number]
        for i in range(hook.sequence_number, self.n_hooks):
            self.hook_list[i].sequence_number = i
        self.n_hooks -= 1

    def add_hook(self, hook):
        if hook.sequence_number >= self.n_hooks or hook.sequence_number < 0 :
            hook.sequence_number = self.n_hooks
            self.hook_list.append(hook)
        else:
            self.hook_list.append(object)
            for i in reversed(hook.sequence_number, self.n_hooks):
                self.hook_list[i+1] = self.hook_list[i]
                self.hook_list[i+1].sequence_number += 1
            self.hook_list[hook.sequence_number] = hook
        self.n_hooks += 1
