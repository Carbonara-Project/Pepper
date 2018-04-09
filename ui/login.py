# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(772, 309)
        LoginDialog.setMinimumSize(QtCore.QSize(772, 309))
        LoginDialog.setMaximumSize(QtCore.QSize(772, 309))
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 251, 341, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.mailEdit = QtWidgets.QLineEdit(LoginDialog)
        self.mailEdit.setGeometry(QtCore.QRect(10, 50, 751, 45))
        self.mailEdit.setObjectName("mailEdit")
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 108, 33))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 201, 33))
        self.label_2.setObjectName("label_2")
        self.passEdit = QtWidgets.QLineEdit(LoginDialog)
        self.passEdit.setGeometry(QtCore.QRect(10, 160, 751, 45))
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login to Carbonara"))
        self.label.setText(_translate("LoginDialog", "Mail:"))
        self.label_2.setText(_translate("LoginDialog", "Password:"))

