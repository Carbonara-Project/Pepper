# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'description.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1483, 673)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 1461, 611))
        self.textEdit.setObjectName("textEdit")
        self.uploadBtn = QtWidgets.QPushButton(Form)
        self.uploadBtn.setGeometry(QtCore.QRect(10, 10, 153, 45))
        self.uploadBtn.setObjectName("uploadBtn")
        self.browserBtn = QtWidgets.QPushButton(Form)
        self.browserBtn.setGeometry(QtCore.QRect(170, 10, 241, 45))
        self.browserBtn.setObjectName("browserBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Procedure Description"))
        self.uploadBtn.setText(_translate("Form", "Upload"))
        self.browserBtn.setText(_translate("Form", "View in browser"))

