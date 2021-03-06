# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figure5_createedithooks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog

class Ui_CEHook(QDialog):
    def setupUi(self, CEHook):
        CEHook.setObjectName("CEHook")
        CEHook.resize(400, 219)
        self.hNInput = QtWidgets.QLineEdit(CEHook)
        self.hNInput.setGeometry(QtCore.QRect(110, 40, 251, 22))
        self.hNInput.setObjectName("hNInput")
        self.hDInput = QtWidgets.QTextEdit(CEHook)
        self.hDInput.setGeometry(QtCore.QRect(110, 70, 251, 51))
        self.hDInput.setObjectName("hDInput")
        self.hPInput = QtWidgets.QLineEdit(CEHook)
        self.hPInput.setGeometry(QtCore.QRect(110, 130, 191, 22))
        self.hPInput.setObjectName("hPInput")
        self.browseButton = QtWidgets.QPushButton(CEHook)
        self.browseButton.setGeometry(QtCore.QRect(310, 130, 51, 21))
        self.browseButton.setObjectName("browseButton")
        self.saveButton = QtWidgets.QPushButton(CEHook)
        self.saveButton.setGeometry(QtCore.QRect(170, 160, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(CEHook)
        self.cancelButton.setGeometry(QtCore.QRect(270, 160, 93, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.widget = QtWidgets.QWidget(CEHook)
        self.widget.setGeometry(QtCore.QRect(30, 30, 67, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hNLabel = QtWidgets.QLabel(self.widget)
        self.hNLabel.setObjectName("hNLabel")
        self.verticalLayout.addWidget(self.hNLabel)
        self.dLabel = QtWidgets.QLabel(self.widget)
        self.dLabel.setObjectName("dLabel")
        self.verticalLayout.addWidget(self.dLabel)
        self.hPLabel = QtWidgets.QLabel(self.widget)
        self.hPLabel.setObjectName("hPLabel")
        self.verticalLayout.addWidget(self.hPLabel)
        
        #self.roiGroups = {}
        self.retranslateUi(CEHook)
        QtCore.QMetaObject.connectSlotsByName(CEHook)
        self.saveButton.clicked.connect(lambda:self.saveClicked())
        self.cancelButton.clicked.connect(lambda:self.cancelClicked())
        self.saveButton.clicked.connect(CEHook.accept)
        self.cancelButton.clicked.connect(CEHook.reject)
        self.browseButton.clicked.connect(lambda:self.browseClicked())
    
    def openFileNameDialogs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.hPInput.setText(fileName)
            
    def saveClicked(self):
        print("Save Clicked:")
        print("Name:",self.hNInput.text())
        print("Description:",self.hDInput.toPlainText())
        print("Path:",self.hPInput.text())
        self.roiGroups = dict(Name = str(self.hNInput.text()),Description = str(self.hDInput.toPlainText()),Path = str(self.hPInput.text()))
        print(self.roiGroups)
        #self.accept

    def cancelClicked(self):
        print ("Cancel Clicked")
        
    def browseClicked(self):
        print ("Browse Clicked")
        (self.openFileNameDialogs())

    def retranslateUi(self, CEHook):
        _translate = QtCore.QCoreApplication.translate
        CEHook.setWindowTitle(_translate("CEHook", "Create/Edit Hook"))
        self.browseButton.setText(_translate("CEHook", "Browse"))
        self.saveButton.setText(_translate("CEHook", "Save"))
        self.cancelButton.setText(_translate("CEHook", "Cancel"))
        self.hNLabel.setText(_translate("CEHook", "Hook Name"))
        self.dLabel.setText(_translate("CEHook", "Description"))
        self.hPLabel.setText(_translate("CEHook", "Hook Path"))

