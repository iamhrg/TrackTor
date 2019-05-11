"""
**Module Overview:**

This module will implement the funtionality of all dialog boxes

|- box: Different boxes show different messages
	- showAlertBox: This function will show alert box
	- showAlertBox1: This function will show alert box
	- showAlertBox2: This function will show alert box
	- showMessageBox: This function will show message box
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from TrackTor.Home import Actions


class box():

	def showAlertBox(self,title,message):
		alertBox = QMessageBox()
		alertBox.setIcon(QMessageBox.Warning)
		alertBox.setWindowTitle(title)
		alertBox.setText(message)
		alertBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		result=alertBox.exec_()
		if (result == QMessageBox.Yes):
			Actions.actions.NewIdentity(Actions.actions)

	def showAlertBox1(self,title,message):
		alertBox = QMessageBox()
		alertBox.setIcon(QMessageBox.Warning)
		alertBox.setWindowTitle(title)
		alertBox.setText(message)
		alertBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		result=alertBox.exec_()
		if (result == QMessageBox.Yes):
			Actions.actions.ReloadTor(Actions.actions)

	def showAlertBox2(self,title,message):
		alertBox = QMessageBox()
		alertBox.setIcon(QMessageBox.Warning)
		alertBox.setWindowTitle(title)
		alertBox.setText(message)
		alertBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		result=alertBox.exec_()
		if (result == QMessageBox.Yes):
			from TrackTor.Home.Edit_Torrc import Ui_Edit_Torrc
			Ui_Edit_Torrc._ReloadTor(self)


	def showMessageBox(self,title,message):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.exec_()
