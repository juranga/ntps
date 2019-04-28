from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component
from UI.Components.View.Live_Packet_View import Live_Packet_View
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Live_Packet_Controller():

    def __init__(self, proxy_server = Proxy_Server()):
        self.proxy_toggle = None
        self.view =  Live_Packet_View(self.proxy_toggle)
        self.proxy_server = proxy_server
