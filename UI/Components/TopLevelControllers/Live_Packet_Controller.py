from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component
from UI.Components.TopLevelControllers.LivePacketComponents.Intercept_Toggle_Component import Intercept_Toggle_Component
from UI.Components.TopLevelControllers.LivePacketComponents.Packet_Area_Component import Packet_Area_Component
from UI.Components.TopLevelControllers.LivePacketComponents.Packet_Area_Binary_Component import Packet_Area_Binary_Component
from UI.Components.TopLevelControllers.LivePacketComponents.Packet_Area_Hex_Component import Packet_Area_Hex_Component
from UI.Components.TopLevelControllers.LivePacketComponents.Field_Area_Component import Field_Area_Component

from UI.Components.View.Live_Packet_View import Live_Packet_View
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Live_Packet_Controller():

    def __init__(self, proxy_server = Proxy_Server()):
        self.proxy_toggle = Proxy_Toggle_Component(proxy_server)
        self.intercept_toggle = Intercept_Toggle_Component(proxy_server)
        self.packet_area = Packet_Area_Component(proxy_server)
        self.packet_binary_area = Packet_Area_Binary_Component(proxy_server)
        self.packet_hex_area = Packet_Area_Hex_Component(proxy_server)
        self.field_area = Field_Area_Component(proxy_server)
        self.view =  Live_Packet_View(self.proxy_toggle, self.intercept_toggle, self.packet_area, self.packet_binary_area, self.packet_hex_area, self.field_area)
