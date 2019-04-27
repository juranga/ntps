import sys

class Hook():

    def __init__(self, name, path):
        self.name = name
        self.path = path
        return

    def install_hook(self):
        sys.path.append(self.path)

    # TO DO: Figure out execution of hook.
    def execute_hook(self, packet):
        execute = globals()[self.path]
        execute(packet)