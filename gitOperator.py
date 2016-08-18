# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'git-operator.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GitOperator(object):
    def setupUi(self, GitOperator):
        GitOperator.setObjectName("GitOperator")
        GitOperator.resize(515, 388)
        self.textFile = QtWidgets.QTextEdit(GitOperator)
        self.textFile.setGeometry(QtCore.QRect(20, 20, 331, 31))
        self.textFile.setStyleSheet("#textFile {\n"
"padding: 1px;\n"
"}")
        self.textFile.setTabChangesFocus(True)
        self.textFile.setReadOnly(True)
        self.textFile.setObjectName("textFile")
        self.fileBtn = QtWidgets.QPushButton(GitOperator)
        self.fileBtn.setGeometry(QtCore.QRect(370, 20, 121, 31))
        self.fileBtn.setObjectName("fileBtn")
        self.label = QtWidgets.QLabel(GitOperator)
        self.label.setGeometry(QtCore.QRect(370, 75, 121, 21))
        self.label.setObjectName("label")
        self.textMsg = QtWidgets.QTextEdit(GitOperator)
        self.textMsg.setGeometry(QtCore.QRect(20, 70, 331, 31))
        self.textMsg.setStyleSheet("#textMsg {\n"
"padding: 1px;\n"
"}")
        self.textMsg.setTabChangesFocus(True)
        self.textMsg.setObjectName("textMsg")
        self.label_2 = QtWidgets.QLabel(GitOperator)
        self.label_2.setGeometry(QtCore.QRect(20, 128, 91, 17))
        self.label_2.setObjectName("label_2")
        self.comboBranch = QtWidgets.QComboBox(GitOperator)
        self.comboBranch.setGeometry(QtCore.QRect(120, 120, 131, 31))
        self.comboBranch.setEditable(True)
        self.comboBranch.setObjectName("comboBranch")
        self.label_3 = QtWidgets.QLabel(GitOperator)
        self.label_3.setGeometry(QtCore.QRect(280, 128, 91, 17))
        self.label_3.setObjectName("label_3")
        self.commitBtn = QtWidgets.QPushButton(GitOperator)
        self.commitBtn.setGeometry(QtCore.QRect(180, 170, 181, 41))
        self.commitBtn.setObjectName("commitBtn")
        self.textOutput = QtWidgets.QTextEdit(GitOperator)
        self.textOutput.setGeometry(QtCore.QRect(20, 230, 471, 141))
        self.textOutput.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.textOutput.setReadOnly(True)
        self.textOutput.setObjectName("textOutput")
        self.comboTag = QtWidgets.QComboBox(GitOperator)
        self.comboTag.setGeometry(QtCore.QRect(360, 120, 131, 31))
        self.comboTag.setEditable(True)
        self.comboTag.setCurrentText("")
        self.comboTag.setObjectName("comboTag")

        self.retranslateUi(GitOperator)
        QtCore.QMetaObject.connectSlotsByName(GitOperator)

    def retranslateUi(self, GitOperator):
        _translate = QtCore.QCoreApplication.translate
        GitOperator.setWindowTitle(_translate("GitOperator", "GIT OPERATOR"))
        self.textFile.setHtml(_translate("GitOperator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fileBtn.setText(_translate("GitOperator", "Select File"))
        self.label.setText(_translate("GitOperator", "Commit Message"))
        self.label_2.setText(_translate("GitOperator", "Branch Name"))
        self.label_3.setText(_translate("GitOperator", "Tag Name"))
        self.commitBtn.setText(_translate("GitOperator", "Commit and Push"))

