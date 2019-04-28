import sys
import os
import importlib.util

class Hook():

    def __init__(self, name, path, sequence_number=0):
        tmp_path = path.split("/")
        self.path = path
        self.name = tmp_path[-1][:-3]
        self.sequence_number = sequence_number
        self.install_hook()
        return

    def get_path(self):
        return self.path

    def get_sequence_number(self):
        return self.sequence_number

    def install_hook(self):
        spec = importlib.util.spec_from_file_location(self.name, self.path)
        self.hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.hook)

    def execute_hook(self, packet):
        return self.hook.run(packet)
        
