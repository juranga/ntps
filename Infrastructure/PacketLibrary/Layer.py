# An object representing a layer in the system.

class NTPS_Layer:
    
    def __init__(self, layer_field_name, layer_showname,layer_size,layer_position, layer_show, layer_value, field_list):
        self.layer_field_name  = layer_field_name
        self.layer_showname = layer_showname
        self.layer_size = layer_size
        self.layer_position = layer_position
        self.layer_show = layer_show
        self.layer_value = layer_value
        self.field_list = field_list

    def get_layer_fields(self):
        return self.field_list

    def add_field(self, field_name, field_value):
        self.field_list[field_name] = field_value

