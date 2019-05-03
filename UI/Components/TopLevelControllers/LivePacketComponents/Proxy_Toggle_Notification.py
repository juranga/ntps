import UI.Notificatons.*
from PyQt5 import QtGui, QtGui, uic
from threading import Thread
import sys

class Proxy_Toggle_Notification(QtGui.QMainWindow):
    def __init__(self):
        super(Proxy_Toggle_Notification,self).__int__()
        uic.loadUi(ProxyEnabledNotifcation.ui,self)
        self.show()

    
        
