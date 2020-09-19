import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi



class MainWindow(QDialog):


    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        self.cancel.clicked.connect(self.LoadCancel)
        self.ok.clicked.connect(self.LoadOk)


    def browsefiles(self):
        global fname
        fname=QFileDialog.getOpenFileName(self, 'Open File','','TXT files (*.txt)')
        self.filename.setText(fname[0])


    def LoadCancel(self):
        sys.exit()


    def LoadOk(self):
        print(fname)
        sys.exit()


app=QApplication(sys.argv)
window=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setWindowTitle("MsgStatCollecter")
widget.setFixedWidth(400)
widget.setFixedHeight(180)
widget.show()
app.exec_()
