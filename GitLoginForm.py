# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'git-form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.details = ''
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(372, 214)
        Dialog.setModal(False)
        self.submitBtn = QtWidgets.QPushButton(Dialog)
        self.submitBtn.setGeometry(QtCore.QRect(120, 150, 111, 31))
        self.submitBtn.setObjectName("submitBtn")
        self.textName = QtWidgets.QLineEdit(Dialog)
        self.textName.setGeometry(QtCore.QRect(130, 40, 210, 31))
        self.textName.setAcceptDrops(True)
        self.textName.setStyleSheet("#textName {\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"}")
        self.textName.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textName.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textName.setTabChangesFocus(True)
        self.textName.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textName.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.textName.setObjectName("textName")
        self.textPassword = QtWidgets.QLineEdit(Dialog)
        self.textPassword.setGeometry(QtCore.QRect(130, 90, 210, 31))
        self.textPassword.setStyleSheet("#textPassword {\n"
"padding-left: 1px;\n"
"padding-top: 1px;\n"
"}")
        self.textPassword.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textPassword.setTabChangesFocus(True)
        self.textPassword.setObjectName("textPassword")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 45, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 95, 81, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.Dialog = Dialog
        self.submitBtn.clicked.connect(self.userDetails)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Git Login"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.textName.setPlaceholderText(_translate("Dialog", "Enter your gitub username"))
        self.textPassword.setPlaceholderText(_translate("Dialog", "Enter your github password"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))

    def userDetails(self):
        self.details = self.textName.toPlainText() + " " + self.textPassword.toPlainText()
        self.Dialog.close()
