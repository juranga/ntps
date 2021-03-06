from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from UI.Components.TopLevelControllers.Edit_Hook_Controller import Edit_Hook_Controller
#from UI.Components.TopLevelControllers.HookComponents import create_edit_hooks
import os
import sys
class Hook_View(QWidget):

    def __init__(self, hook_manager, parent=None):
        QWidget.__init__(self, parent=parent)
        self.hook_manager = hook_manager
        self.setObjectName("hook_page")
        self.frame_7 = QtWidgets.QFrame(self)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 871, 641))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.FormName_2 = QtWidgets.QLabel(self.frame_7)
        self.FormName_2.setGeometry(QtCore.QRect(0, 0, 871, 51))
        self.FormName_2.setStyleSheet("background-color: rgb(75, 151, 226);\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"")
        self.FormName_2.setObjectName("FormName_2")
        self.TopFrame_2 = QtWidgets.QFrame(self.frame_7)
        self.TopFrame_2.setGeometry(QtCore.QRect(0, 50, 871, 631))
        self.TopFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame_2.setObjectName("TopFrame_2")
        self.frame_8 = QtWidgets.QFrame(self.TopFrame_2)
        self.frame_8.setGeometry(QtCore.QRect(30, 90, 771, 501))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_38 = QtWidgets.QLabel(self.frame_8)
        self.label_38.setGeometry(QtCore.QRect(10, 10, 741, 51))
        self.label_38.setStyleSheet("background-color: rgb(75, 151, 226);\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"")
        self.label_38.setObjectName("label_38")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_8)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 741, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(741, 0))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(741, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("gridline-color: white;\n"
"border-right-color: white;\n"
"border-left-color: white;\n"
"\n"
"")
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(1)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/root/ntps/UI/Resources/CircularButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.TopFrame_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 821, 39))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_29.setStyleSheet("font: 8pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(232, 232, 232)")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_7.addWidget(self.pushButton_29, 0, 2, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_30.setStyleSheet("font: 8pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(232, 232, 232)")
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_7.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_31.setStyleSheet("font: 8pt \"MS Reference Sans Serif\";\n"
"background-color: rgb(232, 232, 232)")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_7.addWidget(self.pushButton_31, 0, 1, 1, 1)
        self.Search_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Search_2.setStyleSheet("font: 8pt \"MS Reference Sans Serif\";")
        self.Search_2.setObjectName("Search_2")
        self.gridLayout_7.addWidget(self.Search_2, 0, 4, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_16.setStyleSheet("font: 8pt \"MS Reference Sans Serif\";\n"
"color: rgb(179, 179, 179);\n"
"")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_7.addWidget(self.lineEdit_16, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 3, 1, 1)

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.FormName_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hook View</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hook Properties</span></p></body></html>"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hook"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Association to Hook Collection"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tableWidget_2.cellClicked.connect(self.cellClick)
        #self.tableWidget_2.cellClicked.connect(self.itemClick)
        #self.tableWidget_2.itemClicked.connect(lambda:self.handle_item_clicked())
        self.pushButton_29.setText(_translate("MainWindow", "Delete"))
        self.pushButton_30.setText(_translate("MainWindow", "+Hook"))
        self.pushButton_31.setText(_translate("MainWindow", "Edit"))

        self.pushButton_29.clicked.connect(lambda:self.deleteHookClicked())
        self.pushButton_30.clicked.connect(lambda:self.addHookClicked())
        self.pushButton_31.clicked.connect(lambda:self.editHookClicked())
        self.tableWidget_2.setRowCount(0)
        #self.populateHookTable()
        #self.edit_hook_controller = Edit_Hook_Controller()
        #self.stacked_window.addWidget(self.edit_hook_controller.view)
        from Infrastructure.HookLibrary.Hook_Collection import Hook_Collection
        self.hook_manager.add_hook_collection(Hook_Collection())
        self.Search_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Search</span></p></body></html>"))
        self.lineEdit_16.setText(_translate("MainWindow", "Name of Hook"))

    def deleteHookClicked(self):
        print ("Delete Hook Clicked")    

    def addHookClicked(self):
        print ("Adding Hook Clicked")
        Edit_Hook_Controller.startEditHook(self, self.hook_manager.hook_collection[0])
        #self.main.Main.showOverlay()
        #self.edit_hooks_dialog()

    def edit_hooks_dialog(self): #This Method opens the Overlay
        dialog = QtWidgets.QDialog()
        dialog.ui= create_edit_hooks.Ui_CEHook()
        dialog.ui.setupUi(dialog)
        dialog.show()
        sys.exit(dialog.exec())

    def editHookClicked(self):
        print ("Edit Hook Clicked")

    def itemClick(self, item):
        print (str(item))

    def cellClick(self,row,col):
        print ("Click on " + str(row) + " " + str(col))
        item = self.tableWidget_2.itemAt(row,col)
        itemID = item.text()
        #print (itemID)

    def handle_item_clicked(self):
        print(self)

    #def populateHookTable(self):
        #currDir = os.getcwd()
        #os.chdir('Infrastructure/HookLibrary/Hooks') #Change directory to find Hook Files
        #from PyQt5.QtWidgets import QTableWidgetItem
        #self.tableWidget_2.setItem(0,0, QTableWidgetItem("Hook"))
        #self.tableWidget_2.setItem(0,1, QTableWidgetItem("Description"))
        #self.tableWidget_2.setItem(0,2, QTableWidgetItem("Association to Hook Collection"))  
        #fileIndex = 1
        #hooklist = os.listdir()
        #for file in hooklist:
            #self.tableWidget_2.setItem(fileIndex,0, QTableWidgetItem(file)) #Populating every table cell
            #fileIndex+=1
        #os.chdir(currDir) #Returns to primary directory
