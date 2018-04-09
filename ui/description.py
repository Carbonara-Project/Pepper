# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'description.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DescrForm(object):
    def setupUi(self, DescrForm):
        DescrForm.setObjectName("DescrForm")
        DescrForm.resize(1483, 673)
        self.textEdit = QtWidgets.QTextEdit(DescrForm)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 1461, 611))
        self.textEdit.setObjectName("textEdit")
        self.uploadBtn = QtWidgets.QPushButton(DescrForm)
        self.uploadBtn.setGeometry(QtCore.QRect(10, 10, 153, 45))
        self.uploadBtn.setObjectName("uploadBtn")
        self.browserBtn = QtWidgets.QPushButton(DescrForm)
        self.browserBtn.setGeometry(QtCore.QRect(170, 10, 241, 45))
        self.browserBtn.setObjectName("browserBtn")

        self.retranslateUi(DescrForm)
        QtCore.QMetaObject.connectSlotsByName(DescrForm)

    def retranslateUi(self, DescrForm):
        _translate = QtCore.QCoreApplication.translate
        DescrForm.setWindowTitle(_translate("DescrForm", "Procedure Description"))
        self.uploadBtn.setText(_translate("DescrForm", "Upload"))
        self.browserBtn.setText(_translate("DescrForm", "View in browser"))

