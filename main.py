from Infrastructure.CaptureLibrary.Proxy_Server import Proxy_Server
from Infrastructure.HookLibrary.Hook_Collection_Manager import Hook_Collection_Manager
from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection

from UI.Components.TopLevelControllers.Live_Packet_Controller import Live_Packet_Controller
from UI.Components.TopLevelControllers.Hook_Controller import Hook_Controller
from UI.Components.TopLevelControllers.Hook_Collection_Controller import Hook_Collection_Controller

from UI.Components.View.Live_Packet_View import Live_Packet_View
from UI.Components.View.Hook_Collection_View import Hook_Collection_View
from UI.Components.View.Hook_View import Hook_View
from UI.Components.View.PCAP_View import PCAP_View
from UI.Components.View.Option_View import Option_View


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Main methods; UI set up and execution. You start the system using this script!
class Ui_MainWindow(object):

    def closeMain(self):
        self.proxy_server.stop_server()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 715)

        self.hook_manager = Hook_Collection_Manager()
        self.proxy_server = Proxy_Server(hook_manager=self.hook_manager)

        # Main + Option View
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.option_view = Option_View(parent=self.centralwidget)

        # Stacked Window
        self.stacked_window = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_window.setGeometry(QtCore.QRect(160, 70, 871, 641))
        self.stacked_window.setObjectName("stacked_window")

        # Live Packet View
        self.live_packet_controller = Live_Packet_Controller(proxy_server=self.proxy_server)
        self.stacked_window.addWidget(self.live_packet_controller.view)

        # Hook View
        self.hook_controller = Hook_Controller(self.hook_manager)
        self.stacked_window.addWidget(self.hook_controller.view)
         
        # Hook Collection Widget
        self.hook_collection_controller = Hook_Collection_Controller()
        self.stacked_window.addWidget(self.hook_collection_controller.view)

        # PCAP Page
        self.pcap_view = PCAP_View()
        self.stacked_window.addWidget(self.pcap_view)

        # NTPS Header
        self.system_header = QtWidgets.QFrame(self.centralwidget)
        self.system_header.setGeometry(QtCore.QRect(0, 0, 1041, 71))
        self.system_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.system_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.system_header.setObjectName("system_header")
        self.system_name = QtWidgets.QLabel(self.system_header)
        self.system_name.setGeometry(QtCore.QRect(10, 10, 271, 51))
        self.system_name.setObjectName("system_name")
        self.line = QtWidgets.QFrame(self.system_header)
        self.line.setGeometry(QtCore.QRect(10, 60, 1031, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Set Main Widget and Option View as Central
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stacked_window.setCurrentIndex(0)

        # Option View Listeners
        self.option_view.hook_view_button.clicked.connect(lambda: self.stacked_window.setCurrentIndex(1))
        self.option_view.collection_view_button.clicked.connect(lambda: self.stacked_window.setCurrentIndex(2))
        self.option_view.live_view_button.clicked.connect(lambda: self.stacked_window.setCurrentIndex(0))
        self.option_view.pcap_view_button.clicked.connect(lambda: self.stacked_window.setCurrentIndex(3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # View Retranslates
        self.live_packet_controller.view.retranslateUI()
        self.hook_collection_controller.view.retranslateUI()
        self.hook_controller.view.retranslateUI()
        self.pcap_view.retranslateUI()
        self.option_view.retranslateUI()
        
        # Header Retranslate
        self.system_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff6e07;\">Network Traffic Proxy System</span></p></body></html>"))

    
def appExec():
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    app.exec_()
    ui.closeMain()

if __name__ == "__main__":
    sys.exit(appExec())
