class Hook_Collection():

    def __init__(self, path="", sequence_number=0):
        self.hook_list = []
        self.path = path
        self.sequence_number = sequence_number
        self.n_hooks = 0

    def get_path(self):
        return self.path

    def get_sequence_number(self):
        return self.sequence_number

    def delete_hook(self, idx):
        del self.hook_list[idx]
        self.n_hooks -= 1
        for i in range(idx, self.n_hooks):
            self.hook_list[i].sequence_number = i

    def add_hook(self, hook):
        self.hook_list.append(hook)
