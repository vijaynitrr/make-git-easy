from PyQt5 import QtCore, QtGui, QtWidgets
import sys  
import commands
import GitMerge
import os  


class GitMergeBranches(QtWidgets.QMainWindow, GitMerge.Ui_Dialog): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = ''
        self._want_to_close = False
        #self.branches = branchNames
        self.setupUi(self)
        self.mergeBtn.clicked.connect(self.mergeInformation)
                                                            
    def mergeInformation(self):
        self.info = str(self.comboCurBranch.currentText()) + " " + str(self.comboUpBranch.currentText())
        #self.close()
    
    def closeEvent(self, event):
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    objGitMergeBranches = GitMergeBranches()  
    objGitMergeBranches.show()  
    sys.exit(app.exec_())  
