from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component

from UI.Components.TopLevelControllers.HookComponents import create_hook_collection_ui
from UI.Components.View.Hook_Collection_View import Hook_Collection_View
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server

class Hook_Collection_Controller():

    def __init__(self):
        self.view = Hook_Collection_View()
