from PyQt5.QtWidgets import (QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QApplication, QGridLayout)
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtCore import Qt, QEvent
import sys, subprocess, socket, time, os

class MainClass(QWidget):
	def __init__(self):
		super().__init__()

		self.mainUI()
	def mainUI(self):
		self.listItem = QListWidget(self)
		self.lineBox = QLineEdit()
		self.pathLabel = QLabel("Path: ")
		self.addButton = QPushButton("Add")
		self.removeButton = QPushButton("Remove")
		self.browseButton = QPushButton("Browse")
		self.mainLayout = QGridLayout()
		# self.mainLayout.setSpacing()
		self.mainLayout.addWidget(self.pathLabel, 2, 0)
		self.mainLayout.addWidget(self.listItem, 1, 0, 1, 5)
		self.mainLayout.addWidget(self.addButton, 2, 4)
		self.mainLayout.addWidget(self.removeButton, 2, 3)
		self.mainLayout.addWidget(self.browseButton, 2, 2)
		self.mainLayout.addWidget(self.lineBox, 2, 1)
		self.setLayout(self.mainLayout)
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle("Quick Access")
		self.show()
		self.showMaximized()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainClass()
	app.exec_()