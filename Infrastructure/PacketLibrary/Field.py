# An object representing a field in a packet.

class NTPS_Field:
    
    def __init__(self, field_name, field_value, field_display_format, field_mask):
        self.field_name = field_name
        self.field_value = field_value
        self.field_display_format = field_display_format
        self.field_mask = field_mask
        
    def get_name(self):
        return self.field_name
        
    def get_value(self):
        return self.field_value

    def set_value(self, new_value):
        self.field_value = new_value

    def set_name(self, new_name):
        self.field_name = new_name

    def set_format(self, new_format):
        self.field_display_format = new_format

