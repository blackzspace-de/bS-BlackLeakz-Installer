import os 
import sys 


import subprocess

import platform as pl

import requests





import PyQt6


from PyQt6 import QtCore, QtGui, QtWidgets

from mainui import Ui_MainWindow








class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        
        
        
        
        
        
        self.consoleLog.append("Console > BlackLeakz installer started!")
        
        
        
        
        self.detect()
        
        
    
    
    def detect(self):
        sysx = pl.system()
        mach = pl.machine()
        self.consoleLog.append(f"Console > Detected: \n {mach} \n {sysx}")
        if sysx == "Windows":
            self.consoleLog.append(f"Console > OS: {sysx} SUPPORTED!")
        if sysx == "Linux":
            self.consoleLog.append(f"Console > OS: {sysx} SUPPORTED!")
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()