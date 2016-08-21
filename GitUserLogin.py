# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'git-form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(372, 214)
        Dialog.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        Dialog.setModal(False)
        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(120, 150, 111, 31))
        self.submitBtn.setObjectName("submitBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 45, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 95, 81, 20))
        self.label_2.setObjectName("label_2")
        self.textName = QtWidgets.QLineEdit(Dialog)
        self.textName.setGeometry(QtCore.QRect(130, 40, 210, 31))
        self.textName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.textName.setObjectName("textName")
        self.textPassword = QtWidgets.QLineEdit(Dialog)
        self.textPassword.setGeometry(QtCore.QRect(130, 90, 210, 31))
        self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textPassword.setObjectName("textPassword")

        self.retranslateUi(Dialog)
        self.Dialog = Dialog
        self.submitBtn.clicked.connect(self.userDetails)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Git Login"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.textName.setPlaceholderText(_translate("Dialog", "Enter your github username"))
        self.textPassword.setPlaceholderText(_translate("Dialog", "Enter your github password"))

    def userDetails(self):
        self.details = self.textName.text() + " " + self.textPassword.text()
        self.Dialog.close()
