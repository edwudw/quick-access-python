from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QApplication, QVBoxLayout, QHBoxLayout)
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtCore import Qt, QEvent
import sys, subprocess, socket, time, os

class MainClass(QWidget):
    def __init__(self):
        super().__init__()

        self.mainUI()
    def mainUI(self):
    	self.mainLayout = QVBoxLayout()
    	self.setGeometry(300, 300, 300, 300)
    	self.setWindowTitle("Quick Access")
    	self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainClass()
	app.exec_()