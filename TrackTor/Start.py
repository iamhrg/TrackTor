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




class _Start_Box():
    def Open_Alert_Box(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QDialog()
        self.ui = Ui_Start_Tor()
        self.ui.setupUi(self.Window)
        self.Window.show()
        app.exec_()
