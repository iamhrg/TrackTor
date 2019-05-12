# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Start_Tor(object):

    def Exit(self):
        sys.exit(1)
    def setupUi(self, Start_Tor):
        Start_Tor.setObjectName("Start_Tor")
        Start_Tor.resize(350, 140)
        self.pushButton = QtWidgets.QPushButton(Start_Tor)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Exit)
        self.label = QtWidgets.QLabel(Start_Tor)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Start_Tor)
        QtCore.QMetaObject.connectSlotsByName(Start_Tor)

    def retranslateUi(self, Start_Tor):
        _translate = QtCore.QCoreApplication.translate
        Start_Tor.setWindowTitle(_translate("Start_Tor", "Alert"))
        self.pushButton.setText(_translate("Start_Tor", "OK"))
        self.label.setText(_translate("Start_Tor", "<html><head/><body><p align=\"center\">TOR Services are disconnected. </p><p align=\"center\">Connect and restart the TrackTor.</p></body></html>"))

class Ui_Logs_Tor(object):

    def Yes(self):
        from TrackTor.Utilities import Save_Logs
        sl = Save_Logs._Save_Logs()
        sl.saveFileDialog1()
        _Logs_Box.Window.close()
    def No(self):
        _Logs_Box.Window.close()
    def setupUi(self, Start_Logs):
        Start_Logs.setObjectName("Start_Logs")
        Start_Logs.resize(450, 140)
        self.pushButton = QtWidgets.QPushButton(Start_Logs)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton1 = QtWidgets.QPushButton(Start_Logs)
        self.pushButton1.setGeometry(QtCore.QRect(340, 100, 89, 25))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton.clicked.connect(self.Yes)
        self.pushButton1.clicked.connect(self.No)
        self.label = QtWidgets.QLabel(Start_Logs)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Start_Logs)
        QtCore.QMetaObject.connectSlotsByName(Start_Logs)

    def retranslateUi(self, Start_Logs):
        _translate = QtCore.QCoreApplication.translate
        Start_Logs.setWindowTitle(_translate("Start_Logs", "Save Logs"))
        self.pushButton.setText(_translate("Start_Logs", "Yes"))
        self.pushButton1.setText(_translate("Start_Logs", "No"))
        self.label.setText(_translate("Start_Logs", "<html><head/><body><p align=\"center\">Do You Want to Save Logs in Background?</p></body></html>"))




class _Start_Box():
    def Open_Alert_Box(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QDialog()
        self.ui = Ui_Start_Tor()
        self.ui.setupUi(self.Window)
        self.Window.show()
        app.exec_()

class _Logs_Box():

    def Open_Logs_Box(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QDialog()
        self.ui = Ui_Logs_Tor()
        self.ui.setupUi(self.Window)
        self.Window.show()
        app.exec_()
