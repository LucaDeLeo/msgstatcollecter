import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open File','','TXT files (*.txt)')
        self.filename.setText(fname[0])



app=QApplication(sys.argv)
window=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(400)
widget.setFixedHeight(150)
widget.show()
sys.exit(app.exec_())
