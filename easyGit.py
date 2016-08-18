# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easyGit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textFile = QtWidgets.QTextEdit(self.centralwidget)
        self.textFile.setGeometry(QtCore.QRect(20, 22, 331, 31))
        self.textFile.setStyleSheet("#textFile {\n"
"padding: 1px;\n"
"}")
        self.textFile.setTabChangesFocus(True)
        self.textFile.setReadOnly(True)
        self.textFile.setObjectName("textFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 77, 121, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 130, 71, 21))
        self.label_3.setObjectName("label_3")
        self.comboTag = QtWidgets.QComboBox(self.centralwidget)
        self.comboTag.setGeometry(QtCore.QRect(360, 122, 131, 31))
        self.comboTag.setEditable(True)
        self.comboTag.setCurrentText("")
        self.comboTag.setObjectName("comboTag")
        self.fileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileBtn.setGeometry(QtCore.QRect(370, 22, 121, 31))
        self.fileBtn.setObjectName("fileBtn")
        self.comboBranch = QtWidgets.QComboBox(self.centralwidget)
        self.comboBranch.setGeometry(QtCore.QRect(120, 122, 131, 31))
        self.comboBranch.setEditable(True)
        self.comboBranch.setObjectName("comboBranch")
        self.commitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.commitBtn.setGeometry(QtCore.QRect(180, 172, 181, 41))
        self.commitBtn.setObjectName("commitBtn")
        self.textOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.textOutput.setGeometry(QtCore.QRect(20, 232, 471, 141))
        self.textOutput.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.textOutput.setReadOnly(True)
        self.textOutput.setObjectName("textOutput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 91, 17))
        self.label_2.setObjectName("label_2")
        self.textMsg = QtWidgets.QTextEdit(self.centralwidget)
        self.textMsg.setGeometry(QtCore.QRect(20, 70, 331, 31))
        self.textMsg.setStyleSheet("#textMsg {\n"
"padding: 1px;\n"
"}")
        self.textMsg.setTabChangesFocus(True)
        self.textMsg.setReadOnly(False)
        self.textMsg.setObjectName("textMsg")
        self.label_errorMsg = QtWidgets.QLabel(self.centralwidget)
        self.label_errorMsg.setGeometry(QtCore.QRect(20, 105, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_errorMsg.setFont(font)
        self.label_errorMsg.setText("")
        self.label_errorMsg.setObjectName("label_errorMsg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Git"))
        self.textFile.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.textFile.setPlaceholderText(_translate("MainWindow", "Path of your selected file"))
        self.label.setText(_translate("MainWindow", "Commit Message"))
        self.label_3.setText(_translate("MainWindow", "Tag Name"))
        self.fileBtn.setText(_translate("MainWindow", "Select Folder"))
        self.commitBtn.setText(_translate("MainWindow", "Commit and Push"))
        self.label_2.setText(_translate("MainWindow", "Branch Name"))
        self.textMsg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.textMsg.setPlaceholderText(_translate("MainWindow", "Enter your commit message"))

