# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoiceForm(object):
    def setupUi(self, ChoiceForm):
        ChoiceForm.setObjectName("ChoiceForm")
        ChoiceForm.resize(616, 262)
        ChoiceForm.setMinimumSize(QtCore.QSize(616, 262))
        ChoiceForm.setMaximumSize(QtCore.QSize(616, 262))
        self.label = QtWidgets.QLabel(ChoiceForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 108, 33))
        self.label.setObjectName("label")
        self.yesBtn = QtWidgets.QPushButton(ChoiceForm)
        self.yesBtn.setGeometry(QtCore.QRect(150, 210, 153, 45))
        self.yesBtn.setObjectName("yesBtn")
        self.noBtn = QtWidgets.QPushButton(ChoiceForm)
        self.noBtn.setGeometry(QtCore.QRect(310, 210, 153, 45))
        self.noBtn.setObjectName("noBtn")

        self.retranslateUi(ChoiceForm)
        QtCore.QMetaObject.connectSlotsByName(ChoiceForm)

    def retranslateUi(self, ChoiceForm):
        _translate = QtCore.QCoreApplication.translate
        ChoiceForm.setWindowTitle(_translate("ChoiceForm", "Choice"))
        self.label.setText(_translate("ChoiceForm", "TextLabel"))
        self.yesBtn.setText(_translate("ChoiceForm", "Yes"))
        self.noBtn.setText(_translate("ChoiceForm", "No"))

