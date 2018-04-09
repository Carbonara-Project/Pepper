# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'similars.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimilarsDialog(object):
    def setupUi(self, SimilarsDialog):
        SimilarsDialog.setObjectName("SimilarsDialog")
        SimilarsDialog.resize(1287, 889)
        self.gridLayout_2 = QtWidgets.QGridLayout(SimilarsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(SimilarsDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.renameBtn_2 = QtWidgets.QPushButton(SimilarsDialog)
        self.renameBtn_2.setObjectName("renameBtn_2")
        self.gridLayout.addWidget(self.renameBtn_2, 0, 0, 1, 1)
        self.renameBtn = QtWidgets.QPushButton(SimilarsDialog)
        self.renameBtn.setObjectName("renameBtn")
        self.gridLayout.addWidget(self.renameBtn, 0, 1, 1, 1)
        self.openBtn = QtWidgets.QPushButton(SimilarsDialog)
        self.openBtn.setObjectName("openBtn")
        self.gridLayout.addWidget(self.openBtn, 0, 2, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(SimilarsDialog)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(SimilarsDialog)
        QtCore.QMetaObject.connectSlotsByName(SimilarsDialog)

    def retranslateUi(self, SimilarsDialog):
        _translate = QtCore.QCoreApplication.translate
        SimilarsDialog.setWindowTitle(_translate("SimilarsDialog", "Dialog"))
        self.renameBtn_2.setText(_translate("SimilarsDialog", "Attach Description"))
        self.renameBtn.setText(_translate("SimilarsDialog", "Rename"))
        self.openBtn.setText(_translate("SimilarsDialog", "Open link"))
        self.closeBtn.setText(_translate("SimilarsDialog", "Close"))

