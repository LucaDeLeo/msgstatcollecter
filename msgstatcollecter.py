# TXTloader.py

from plots_functions import msgStatCol
from PyQt5.QtWidgets import *
import sys
class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow,self).__init__()
        TXT=QFileDialog.getOpenFileName(self, 'Open File','',    'TXT files (*.txt)')
        msgStatCol(TXT)
        sys.exit()

app=QApplication(sys.argv)
window=MainWindow()
app.exec_()

