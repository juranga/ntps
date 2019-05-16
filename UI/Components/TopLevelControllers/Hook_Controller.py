from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component

from UI.Components.TopLevelControllers.HookComponents import create_edit_hooks
from UI.Components.View.Hook_View import Hook_View
from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection

class Hook_Controller():

    def __init__(self):
        self.view = Hook_View()
