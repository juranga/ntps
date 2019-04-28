from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component
from UI.Components.View.Live_Packet_View import Live_Packet_View
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Live_Packet_Controller():

    def __init__(view = Live_Packet_View(), proxy_server = Proxy_Server()):
        self.view = view
        self.proxy_server = proxy_server
        self.view.proxy_toggle = Proxy_Toggle_Component(view.horizontalFrame_6, view.sizePolicy, view.font, proxy_server = self.proxy_server)
        self.view.horizontalLayout_7.addWidget(self.proxy_toggle)
