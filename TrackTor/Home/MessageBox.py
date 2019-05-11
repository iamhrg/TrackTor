"""
**Module Overview:**

This module will show the massage boxes

|- box
	- showMessageBox: This function will show message box
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class box():

	def showMessageBox(self,title,message):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.exec_()
