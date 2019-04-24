from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFrame

class Option_View(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.parent = parent
        self.option_view_frame = QtWidgets.QFrame(self.parent)
        self.option_view_frame.setGeometry(QtCore.QRect(0, 70, 161, 651))
        self.option_view_frame.setStyleSheet("background: rgb(255, 255, 255)")
        self.option_view_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_view_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_view_frame.setObjectName("option_view_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.option_view_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hook_view_button = QtWidgets.QPushButton(self.option_view_frame)
        self.hook_view_button.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.hook_view_button.setObjectName("hook_view_button")
        self.verticalLayout_2.addWidget(self.hook_view_button)
        self.collection_view_button = QtWidgets.QPushButton(self.option_view_frame)
        self.collection_view_button.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.collection_view_button.setObjectName("collection_view_button")
        self.verticalLayout_2.addWidget(self.collection_view_button)
        self.live_view_button = QtWidgets.QPushButton(self.option_view_frame)
        self.live_view_button.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.live_view_button.setObjectName("live_view_button")
        self.verticalLayout_2.addWidget(self.live_view_button)
        self.pcap_view_button = QtWidgets.QPushButton(self.option_view_frame)
        self.pcap_view_button.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.pcap_view_button.setObjectName("pcap_view_button")
        self.verticalLayout_2.addWidget(self.pcap_view_button)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.option_view_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 3, 1)
        self.label = QtWidgets.QLabel(self.option_view_frame)
        self.label.setStyleSheet("background-color: rgb(75, 151, 226);\n"
        "font: 8pt \"MS Reference Sans Serif\";\n"
        "")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.hook_view_button.setText(_translate("MainWindow", "Hook"))
        self.collection_view_button.setText(_translate("MainWindow", "Hook Collection"))
        self.live_view_button.setText(_translate("MainWindow", "Live Packet"))
        self.pcap_view_button.setText(_translate("MainWindow", "Packet from PCAP"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Option View</span></p></body></html>"))
    