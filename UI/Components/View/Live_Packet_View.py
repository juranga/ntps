from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from UI.Components.TopLevelControllers.LivePacketComponents.Proxy_Toggle_Component import Proxy_Toggle_Component

class Live_Packet_View(QWidget):

    def __init__(self, proxy_toggle, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setObjectName("live_packet_page")
        self.live_packet_frame = QtWidgets.QFrame(self)
        self.live_packet_frame.setGeometry(QtCore.QRect(0, 0, 871, 641))
        self.live_packet_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.live_packet_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.live_packet_frame.setObjectName("live_packet_frame")
        self.layoutWidget = QtWidgets.QWidget(self.live_packet_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 871, 641))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalFrame_6 = QtWidgets.QFrame(self.layoutWidget)
        self.horizontalFrame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.horizontalFrame_6.setObjectName("horizontalFrame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.proxy_toggle_label = QtWidgets.QLabel(self.horizontalFrame_6)
        self.proxy_toggle_label.setObjectName("proxy_toggle_label")
        self.horizontalLayout_7.addWidget(self.proxy_toggle_label)
        font = QtGui.QFont()
        font.setPointSize(10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        """ Adding the Proxy Toggle """
        proxy_toggle.install_widgets(self.horizontalFrame_6, sizePolicy, font)
        self.proxy_toggle = proxy_toggle.combo_box
        sizePolicy.setHeightForWidth(self.proxy_toggle.sizePolicy().hasHeightForWidth())
        self.proxy_toggle.setSizePolicy(sizePolicy)
        self.horizontalLayout_7.addWidget(self.proxy_toggle)

        self.intercet_toggle_label = QtWidgets.QLabel(self.horizontalFrame_6)
        self.intercet_toggle_label.setObjectName("intercet_toggle_label")
        self.horizontalLayout_7.addWidget(self.intercet_toggle_label)
        self.intercept_toggle = QtWidgets.QComboBox(self.horizontalFrame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intercept_toggle.sizePolicy().hasHeightForWidth())
        self.intercept_toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.intercept_toggle.setFont(font)
        self.intercept_toggle.setMaxVisibleItems(2)
        self.intercept_toggle.setObjectName("intercept_toggle")
        self.intercept_toggle.addItem("")
        self.intercept_toggle.addItem("")
        self.intercept_toggle.addItem("")
        self.horizontalLayout_7.addWidget(self.intercept_toggle)
        self.queue_size_label = QtWidgets.QLabel(self.horizontalFrame_6)
        self.queue_size_label.setObjectName("queue_size_label")
        self.horizontalLayout_7.addWidget(self.queue_size_label)
        self.queue_size_input = QtWidgets.QLineEdit(self.horizontalFrame_6)
        self.queue_size_input.setObjectName("queue_size_input")
        self.horizontalLayout_7.addWidget(self.queue_size_input)
        self.gridLayout_6.addWidget(self.horizontalFrame_6, 0, 0, 1, 3)
        self.capture_filter_area = QtWidgets.QFrame(self.layoutWidget)
        self.capture_filter_area.setFrameShape(QtWidgets.QFrame.Box)
        self.capture_filter_area.setObjectName("capture_filter_area")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.capture_filter_area)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_27 = QtWidgets.QLabel(self.capture_filter_area)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_12.addWidget(self.label_27)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.capture_filter_label = QtWidgets.QLabel(self.capture_filter_area)
        self.capture_filter_label.setObjectName("capture_filter_label")
        self.horizontalLayout_6.addWidget(self.capture_filter_label)
        self.capture_filter_expression = QtWidgets.QLineEdit(self.capture_filter_area)
        self.capture_filter_expression.setObjectName("capture_filter_expression")
        self.horizontalLayout_6.addWidget(self.capture_filter_expression)
        self.capture_filter_apply = QtWidgets.QPushButton(self.capture_filter_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_filter_apply.sizePolicy().hasHeightForWidth())
        self.capture_filter_apply.setSizePolicy(sizePolicy)
        self.capture_filter_apply.setObjectName("capture_filter_apply")
        self.horizontalLayout_6.addWidget(self.capture_filter_apply)
        self.capture_filter_clear = QtWidgets.QPushButton(self.capture_filter_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_filter_clear.sizePolicy().hasHeightForWidth())
        self.capture_filter_clear.setSizePolicy(sizePolicy)
        self.capture_filter_clear.setObjectName("capture_filter_clear")
        self.horizontalLayout_6.addWidget(self.capture_filter_clear)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.gridLayout_6.addWidget(self.capture_filter_area, 1, 0, 1, 3)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.horizontalFrame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.packet_area = QtWidgets.QFrame(self.horizontalFrame_2)
        self.packet_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.packet_area.setObjectName("packet_area")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.packet_area)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.packet_area_label = QtWidgets.QLabel(self.packet_area)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.packet_area_label.setFont(font)
        self.packet_area_label.setObjectName("packet_area_label")
        self.verticalLayout_4.addWidget(self.packet_area_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.packet_area_tab = QtWidgets.QTabWidget(self.packet_area)
        self.packet_area_tab.setObjectName("packet_area_tab")

        self.packet_area_dissected = QtWidgets.QWidget()
        self.packet_area_dissected.setObjectName("packet_area_dissected")
        
        
        self.verticalScrollBar = QtWidgets.QScrollBar(self.packet_area_dissected)
        self.verticalScrollBar.setGeometry(QtCore.QRect(470, 0, 16, 71))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.packet_area_tab.addTab(self.packet_area_dissected, "")
        self.packet_area_binary = QtWidgets.QWidget()
        self.packet_area_binary.setObjectName("packet_area_binary")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.packet_area_binary)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(470, 0, 16, 71))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.packet_area_tab.addTab(self.packet_area_binary, "")
        self.packet_area_hex = QtWidgets.QWidget()
        self.packet_area_hex.setObjectName("packet_area_hex")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.packet_area_hex)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(470, 0, 16, 71))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.packet_area_tab.addTab(self.packet_area_hex, "")
        self.verticalLayout_4.addWidget(self.packet_area_tab)
        self.horizontalLayout_3.addWidget(self.packet_area)
        self.packet_area_clear = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_area_clear.sizePolicy().hasHeightForWidth())
        self.packet_area_clear.setSizePolicy(sizePolicy)
        self.packet_area_clear.setObjectName("packet_area_clear")
        self.horizontalLayout_3.addWidget(self.packet_area_clear, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.gridLayout_6.addWidget(self.horizontalFrame_2, 2, 0, 1, 3)
        self.field_area = QtWidgets.QFrame(self.layoutWidget)
        self.field_area.setFrameShape(QtWidgets.QFrame.Box)
        self.field_area.setObjectName("field_area")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.field_area)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(-1, 1, -1, 1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.field_area_label = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_area_label.sizePolicy().hasHeightForWidth())
        self.field_area_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.field_area_label.setFont(font)
        self.field_area_label.setObjectName("field_area_label")
        self.verticalLayout_6.addWidget(self.field_area_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 80)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.display_format_label = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_format_label.sizePolicy().hasHeightForWidth())
        self.display_format_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_format_label.setFont(font)
        self.display_format_label.setObjectName("display_format_label")
        self.gridLayout_5.addWidget(self.display_format_label, 0, 3, 1, 1)
        self.mask_label = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_label.sizePolicy().hasHeightForWidth())
        self.mask_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mask_label.setFont(font)
        self.mask_label.setObjectName("mask_label")
        self.gridLayout_5.addWidget(self.mask_label, 0, 2, 1, 1)
        self.field_name_label = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_name_label.sizePolicy().hasHeightForWidth())
        self.field_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.field_name_label.setFont(font)
        self.field_name_label.setObjectName("field_name_label")
        self.gridLayout_5.addWidget(self.field_name_label, 0, 0, 1, 1)
        self.value_label = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_label.sizePolicy().hasHeightForWidth())
        self.value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.value_label.setFont(font)
        self.value_label.setObjectName("value_label")
        self.gridLayout_5.addWidget(self.value_label, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 2, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 2, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setMaxVisibleItems(2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_3, 2, 3, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 3, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_5.addWidget(self.label_37, 3, 2, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setMaxVisibleItems(2)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_6, 3, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_5)
        self.verticalScrollBar_5 = QtWidgets.QScrollBar(self.field_area)
        self.verticalScrollBar_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_5.setObjectName("verticalScrollBar_5")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.save_modification_button = QtWidgets.QPushButton(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_modification_button.sizePolicy().hasHeightForWidth())
        self.save_modification_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_modification_button.setFont(font)
        self.save_modification_button.setObjectName("save_modification_button")
        self.horizontalLayout.addWidget(self.save_modification_button, 0, QtCore.Qt.AlignBottom)
        self.forward_button = QtWidgets.QPushButton(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forward_button.sizePolicy().hasHeightForWidth())
        self.forward_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.forward_button.setFont(font)
        self.forward_button.setObjectName("forward_button")
        self.horizontalLayout.addWidget(self.forward_button, 0, QtCore.Qt.AlignBottom)
        self.drop_button = QtWidgets.QPushButton(self.field_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drop_button.sizePolicy().hasHeightForWidth())
        self.drop_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drop_button.setFont(font)
        self.drop_button.setObjectName("drop_button")
        self.horizontalLayout.addWidget(self.drop_button, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.gridLayout_6.addWidget(self.field_area, 3, 0, 2, 1)
        self.add_to_fuzzer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_to_fuzzer.sizePolicy().hasHeightForWidth())
        self.add_to_fuzzer.setSizePolicy(sizePolicy)
        self.add_to_fuzzer.setObjectName("add_to_fuzzer")
        self.gridLayout_6.addWidget(self.add_to_fuzzer, 3, 1, 1, 1)
        self.fuzzing_area = QtWidgets.QFrame(self.layoutWidget)
        self.fuzzing_area.setFrameShape(QtWidgets.QFrame.Box)
        self.fuzzing_area.setObjectName("fuzzing_area")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fuzzing_area)
        self.verticalLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fuzzing_area_label = QtWidgets.QLabel(self.fuzzing_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fuzzing_area_label.sizePolicy().hasHeightForWidth())
        self.fuzzing_area_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.fuzzing_area_label.setFont(font)
        self.fuzzing_area_label.setObjectName("fuzzing_area_label")
        self.verticalLayout_5.addWidget(self.fuzzing_area_label)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.return_type = QtWidgets.QLabel(self.fuzzing_area)
        self.return_type.setObjectName("return_type")
        self.gridLayout_4.addWidget(self.return_type, 2, 0, 1, 1)
        self.selected_field_name = QtWidgets.QLabel(self.fuzzing_area)
        self.selected_field_name.setObjectName("selected_field_name")
        self.gridLayout_4.addWidget(self.selected_field_name, 1, 0, 1, 1)
        self.maximum_field = QtWidgets.QLabel(self.fuzzing_area)
        self.maximum_field.setObjectName("maximum_field")
        self.gridLayout_4.addWidget(self.maximum_field, 4, 0, 1, 1)
        self.selected_packet_name = QtWidgets.QLabel(self.fuzzing_area)
        self.selected_packet_name.setObjectName("selected_packet_name")
        self.gridLayout_4.addWidget(self.selected_packet_name, 0, 0, 1, 1)
        self.minimum_field = QtWidgets.QLabel(self.fuzzing_area)
        self.minimum_field.setObjectName("minimum_field")
        self.gridLayout_4.addWidget(self.minimum_field, 3, 0, 1, 1)
        self.selected_packet_input = QtWidgets.QLineEdit(self.fuzzing_area)
        self.selected_packet_input.setObjectName("selected_packet_input")
        self.gridLayout_4.addWidget(self.selected_packet_input, 0, 1, 1, 1)
        self.selected_field_input = QtWidgets.QLineEdit(self.fuzzing_area)
        self.selected_field_input.setObjectName("selected_field_input")
        self.gridLayout_4.addWidget(self.selected_field_input, 1, 1, 1, 1)
        self.return_type_input = QtWidgets.QLineEdit(self.fuzzing_area)
        self.return_type_input.setObjectName("return_type_input")
        self.gridLayout_4.addWidget(self.return_type_input, 2, 1, 1, 1)
        self.minimum_field_input = QtWidgets.QLineEdit(self.fuzzing_area)
        self.minimum_field_input.setObjectName("minimum_field_input")
        self.gridLayout_4.addWidget(self.minimum_field_input, 3, 1, 1, 1)
        self.maximum_field_input = QtWidgets.QLineEdit(self.fuzzing_area)
        self.maximum_field_input.setObjectName("maximum_field_input")
        self.gridLayout_4.addWidget(self.maximum_field_input, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fuzz_button = QtWidgets.QPushButton(self.fuzzing_area)
        self.fuzz_button.setObjectName("fuzz_button")
        self.horizontalLayout_5.addWidget(self.fuzz_button, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.stop_fuzz_button = QtWidgets.QPushButton(self.fuzzing_area)
        self.stop_fuzz_button.setObjectName("stop_fuzz_button")
        self.horizontalLayout_5.addWidget(self.stop_fuzz_button, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout_6.addWidget(self.fuzzing_area, 3, 2, 2, 1)
        self.remove_from_fuzzer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_from_fuzzer.sizePolicy().hasHeightForWidth())
        self.remove_from_fuzzer.setSizePolicy(sizePolicy)
        self.remove_from_fuzzer.setObjectName("remove_from_fuzzer")
        self.gridLayout_6.addWidget(self.remove_from_fuzzer, 4, 1, 1, 1)

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.proxy_toggle_label.setText(_translate("MainWindow", "Proxy Behavior"))

        self.proxy_toggle.setCurrentText(_translate("MainWindow", "Enabled/Disabled"))
        self.proxy_toggle.setItemText(0, _translate("MainWindow", "Enabled/Disabled"))
        self.proxy_toggle.setItemText(1, _translate("MainWindow", "Enabled"))
        self.proxy_toggle.setItemText(2, _translate("MainWindow", "Disabled"))

        self.intercet_toggle_label.setText(_translate("MainWindow", "Intercept Behavior"))
        self.intercept_toggle.setCurrentText(_translate("MainWindow", "Enabled/Disabled"))
        self.intercept_toggle.setItemText(0, _translate("MainWindow", "Enabled/Disabled"))
        self.intercept_toggle.setItemText(1, _translate("MainWindow", "Enabled"))
        self.intercept_toggle.setItemText(2, _translate("MainWindow", "Disabled"))
        self.queue_size_label.setText(_translate("MainWindow", "Queue Size"))
        self.queue_size_input.setPlaceholderText(_translate("MainWindow", "Queue Size"))
        self.label_27.setText(_translate("MainWindow", "Capture Filter"))
        self.capture_filter_label.setText(_translate("MainWindow", "Filter"))
        self.capture_filter_expression.setPlaceholderText(_translate("MainWindow", "Filter Expression"))
        self.capture_filter_apply.setText(_translate("MainWindow", "Apply"))
        self.capture_filter_clear.setText(_translate("MainWindow", "Clear"))
        self.packet_area_label.setText(_translate("MainWindow", "Packet Area"))
        self.packet_area_tab.setTabText(self.packet_area_tab.indexOf(self.packet_area_dissected), _translate("MainWindow", "Dissected"))
        self.packet_area_tab.setTabText(self.packet_area_tab.indexOf(self.packet_area_binary), _translate("MainWindow", "Binary"))
        self.packet_area_tab.setTabText(self.packet_area_tab.indexOf(self.packet_area_hex), _translate("MainWindow", "HEX"))
        self.packet_area_clear.setText(_translate("MainWindow", "Clear"))
        self.field_area_label.setText(_translate("MainWindow", "Field Area"))
        self.checkBox_3.setText(_translate("MainWindow", "icmp.type"))
        self.display_format_label.setText(_translate("MainWindow", "Display Format"))
        self.mask_label.setText(_translate("MainWindow", "Mask"))
        self.field_name_label.setText(_translate("MainWindow", "Field Name"))
        self.value_label.setText(_translate("MainWindow", "Value"))
        self.label_34.setText(_translate("MainWindow", "08"))
        self.label_35.setText(_translate("MainWindow", "0"))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "Format"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Format"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Dissected"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Binary"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "HEX"))
        self.checkBox_4.setText(_translate("MainWindow", "icmp.code"))
        self.label_36.setText(_translate("MainWindow", "00"))
        self.label_37.setText(_translate("MainWindow", "0"))
        self.comboBox_6.setCurrentText(_translate("MainWindow", "Format"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Format"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Dissected"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Binary"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "HEX"))
        self.save_modification_button.setText(_translate("MainWindow", "Save Modification"))
        self.forward_button.setText(_translate("MainWindow", "Forward"))
        self.drop_button.setText(_translate("MainWindow", "Drop"))
        self.add_to_fuzzer.setText(_translate("MainWindow", "+"))
        self.fuzzing_area_label.setText(_translate("MainWindow", "Fuzzing Area"))
        self.return_type.setText(_translate("MainWindow", "Expected Return Type"))
        self.selected_field_name.setText(_translate("MainWindow", "Selected Field Name"))
        self.maximum_field.setText(_translate("MainWindow", "Maximum"))
        self.selected_packet_name.setText(_translate("MainWindow", "Selected Packet Name"))
        self.minimum_field.setText(_translate("MainWindow", "Minimum"))
        self.fuzz_button.setText(_translate("MainWindow", "Fuzz"))
        self.stop_fuzz_button.setText(_translate("MainWindow", "Stop"))
        self.remove_from_fuzzer.setText(_translate("MainWindow", "-"))
        self.packet_area_tab.setCurrentIndex(2)