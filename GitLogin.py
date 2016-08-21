from PyQt5 import QtCore, QtGui, QtWidgets
import sys  
import commands
import GitLoginForm
import os  


class GitLogin(QtWidgets.QMainWindow, GitLoginForm.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.command = self.output = ''
        self.setupUi(self)
        self.fileBtn.clicked.connect(self.selectFile)
        self.pullBtn.clicked.connect(self.takePull)
        self.mergeBtn.clicked.connect(self.takeMerge)
        self.commitBtn.clicked.connect(self.validateAndPush)  
                                                            
    def selectFile(self):
        self.directoryName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory', '/home/motu/Downloads/python-content')
        self.textFile.setText(self.directoryName)
        self.getBranchNames()

    def takePull(self):
        self.command = 'git pull --rebase'
        self.output = commands.getstatusoutput('git pull')
        self.textOutput.append('> '+self.command+"\r\n"+self.output[1])

    def takeMerge(self):
        app = QtWidgets.QApplication(sys.argv)  
        GitLogin = EasyGitApp()  
        MakeGitEasy.show()
        sys.exit(app.exec_())

    def getBranchNames(self):
        os.chdir(self.textFile.toPlainText())
        self.command = 'git branch'
        self.output = commands.getstatusoutput('git branch')
        for branch in self.output[1].split('\n'):
            branch = branch.lstrip("*")
            self.comboBranch.addItem(branch)

        item = self.comboBranch.model().item(0)
        item.setData(QtGui.QColor('green'), QtCore.Qt.ForegroundRole)
        self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
        self.getTags()

    def getTags(self):
        self.command = 'git tag'
        self.output = commands.getstatusoutput('git tag')
        for tag in self.output[1].split('\n'):
            self.comboTag.addItem(tag)

        self.textOutput.append('> '+self.command+"\r\n"+self.output[1])

    def validateAndPush(self):
        self.message = self.textMsg.toPlainText()
        if len(self.message) < 20:
            self.label_errorMsg.setText("Please enter more than 20 character message")
            self.label_errorMsg.setStyleSheet('color: red')
        else:
            self.label_errorMsg.clear()
            self.message = '"' + self.message + '"';
            self.command = 'git add .'
            self.output = commands.getstatusoutput('git add .')
            self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
            self.command = 'git commit -m ' + self.message
            self.output = commands.getstatusoutput(self.command)
            self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
            self.output = commands.getstatusoutput('grep -i "machine github.com" ~/.netrc | wc -l')
            if self.output[1] == '0':
                self.username = 'vijaynitrr'
                self.password = 'vk@#9717'
                self.pushLine = 'machine github.com login ' + self.username + ' password '+self.password
                self.output = commands.getstatusoutput('echo ' + self.pushLine + ' | cat > ~/.netrc')
                self.output = commands.getstatusoutput('chmod 0600 ~/.netrc')

            self.command = 'git push origin ' + str(self.comboBranch.currentText())
            self.output = commands.getstatusoutput(self.command)
            self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
            self.command = 'git tag ' + str(self.comboTag.currentText())
            self.output = commands.getstatusoutput(self.command)
            self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
            self.command = 'git push origin ' + str(self.comboTag.currentText())
            self.output = commands.getstatusoutput(self.command)
            self.textOutput.append('> '+self.command+"\r\n"+self.output[1])
            self.textOutput.moveCursor(QtGui.QTextCursor.End)
