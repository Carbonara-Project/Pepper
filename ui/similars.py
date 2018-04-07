# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'similars.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1287, 891)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.renameBtn_2 = QtWidgets.QPushButton(Dialog)
        self.renameBtn_2.setObjectName("renameBtn_2")
        self.gridLayout.addWidget(self.renameBtn_2, 0, 0, 1, 1)
        self.renameBtn = QtWidgets.QPushButton(Dialog)
        self.renameBtn.setObjectName("renameBtn")
        self.gridLayout.addWidget(self.renameBtn, 0, 1, 1, 1)
        self.openBtn = QtWidgets.QPushButton(Dialog)
        self.openBtn.setObjectName("openBtn")
        self.gridLayout.addWidget(self.openBtn, 0, 2, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(Dialog)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.renameBtn_2.setText(_translate("Dialog", "Attach Description"))
        self.renameBtn.setText(_translate("Dialog", "Rename"))
        self.openBtn.setText(_translate("Dialog", "Open link"))
        self.closeBtn.setText(_translate("Dialog", "Close"))

