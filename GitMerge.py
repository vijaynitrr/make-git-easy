# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gitMerge.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog, BranchNames):
        self.branchNames = BranchNames
        self.info = ""
        Dialog.setObjectName("Dialog")
        Dialog.resize(372, 214)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 131, 20))
        self.label_2.setObjectName("label_2")
        self.comboUpBranch = QtWidgets.QComboBox(Dialog)
        self.comboUpBranch.setGeometry(QtCore.QRect(160, 85, 181, 31))
        self.comboUpBranch.setEditable(True)
        self.comboUpBranch.setObjectName("comboUpBranch")
        self.comboCurBranch = QtWidgets.QComboBox(Dialog)
        self.comboCurBranch.setGeometry(QtCore.QRect(160, 35, 181, 31))
        self.comboCurBranch.setEditable(True)
        self.comboCurBranch.setObjectName("comboCurBranch")
        self.mergeBtn = QtWidgets.QPushButton(Dialog)
        self.mergeBtn.setGeometry(QtCore.QRect(130, 145, 111, 31))
        self.mergeBtn.setObjectName("mergeBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 131, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog
        self.setBranchNames()
        self.mergeBtn.clicked.connect(self.mergeInformation)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Merge with Branch"))
        self.mergeBtn.setText(_translate("Dialog", "Merge"))
        self.label.setText(_translate("Dialog", "Current Branch"))

    def mergeInformation(self):
        self.info = str(self.comboCurBranch.currentText()).lstrip(" ") + " " + str(self.comboUpBranch.currentText()).lstrip(" ")
        self.Dialog.close()

    def setBranchNames(self):
        for branch in self.branchNames[1].split('\n'):
            branch = branch.lstrip("*")
            self.comboCurBranch.addItem(branch)
            self.comboUpBranch.addItem(branch)