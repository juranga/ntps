from Components.Live_Packet_View import Live_Packet_View
from Components.Hook_Collection_View import Hook_Collection_View
from Components.Hook_View import Hook_View
from Components.PCAP_View import PCAP_View
from Components.Option_View import Option_View

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 715)

        # Main + Option View
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.option_view = Option_View(parent=self.centralwidget)

        # Stacked Window
        self.stacked_window = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_window.setGeometry(QtCore.QRect(160, 70, 871, 641))
        self.stacked_window.setObjectName("stacked_window")

        # Live Packet View
        self.live_packet_view = Live_Packet_View()
        self.stacked_window.addWidget(self.live_packet_view)

        # Hook View
        self.hook_view = Hook_View()
        self.stacked_window.addWidget(self.hook_view)
        
        # Hook Collection Widget
        self.hook_collection_view = Hook_Collection_View()
        self.stacked_window.addWidget(self.hook_collection_view)

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
        self.live_packet_view.retranslateUI()
        self.hook_collection_view.retranslateUI()
        self.hook_view.retranslateUI()
        self.pcap_view.retranslateUI()
        self.option_view.retranslateUI()
        
        # Header Retranslate
        self.system_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff6e07;\">Network Traffic Proxy System</span></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())