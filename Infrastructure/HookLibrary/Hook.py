from Infrastructure.Common.Generators import id_generator

import sys
import os
import importlib.util

# An object representing a hook in the system. When a hook is loaded from the file system, the path, name, and a sequence number is stored; the script itself can then be installed and executed. Hooks can be enabled and disabled from the interface.
class Hook():

    def __init__(self, path, display_name= id_generator(), enabled=True, sequence_number=0):
        tmp_path = path.split("/")
        self.path = path
        self.display_name = display_name
        self.file_name = tmp_path[-1][:-3]
        self.sequence_number = sequence_number
        self.enabled = enabled
        self.install_hook()
        return

    def get_path(self):
        return self.path

    def enable_hook(self):
        self.enabled = True

    def disable_hook(self):
        self.enabled = False

    def get_sequence_number(self):
        return self.sequence_number

    def install_hook(self):
        spec = importlib.util.spec_from_file_location(self.file_name, self.path)
        self.hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.hook)

    def execute_hook(self, packet):
        if self.enabled:
            return self.hook.run(packet)
        return ""
        
