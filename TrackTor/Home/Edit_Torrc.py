"""
**Module Overview:**

This module will implement the funtionality of Edit_Torrc

|- Ui_Edit_Torrc
	- _Display_Torrc: This function will generate new identity
	- _Edit_Torrc_Display: This function will reload tor
    - _Add_Line: This function will add new line
    - _Delete_Line: This function will delete any particular line
    - _Edit_Torrc_Apply: This function will apply changes of edit torrc
    - _Reset_Changes: This function will reset the changes
    - _Reload_Tor: This function will reload tor
    - _ReloadTor: This function will reload tor
    - setupUi: This funtion will initialize all the UI methods
    - retranslateUi: This funtion will show the UI

|- _Edit_Torrc
    - Open_Edit_Torrc: This function will open Edit torrc file
    - Close_Edit_Torrc: This function will close Edit torrc file
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import sys
import TrackTor.Icons.TorrcIcon
import time
import os
from TrackTor.Home.DialogBox import box

modified_Torrc = []
original_Torrc = []
original_Torrc1 = []
class _Open_File():
	def _File_Open():
		if sys.platform == "win32":
		    file = open ("C:/Tor Browser/Browser/TorBrowser/Data/Tor/torrc-defaults", "r+")
		elif sys.platform in ["linux1", "linux2", "linux"]:
		    file = open ("/etc/tor/torrc", "r+")
		elif sys.platform == "darwin":
		    file = open ("/usr/local/etc/tor/torrc.sample", "r+")
		global original_Torrc
		global original_Torrc1
		original_Torrc = file.readlines()
		original_Torrc1 = file.readlines()
		file.close()

		for line in original_Torrc:
		    if line in ['\n','##\n','#\n']:
		        original_Torrc.remove(line)
		global modified_Torrc
		modified_Torrc = list(original_Torrc)


class Ui_Edit_Torrc(object):

    def _Display_Torrc(self, list):
        global modified_Torrc
        global original_Torrc
        self.Display_Torrc.setRowCount(len(list))
        for line in range (len(list)):
            item = QtWidgets.QTableWidgetItem(str(line+1))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item1 = QtWidgets.QTableWidgetItem(list[line].rstrip())
            item1.setTextAlignment(QtCore.Qt.AlignVCenter)
            self.Display_Torrc.setItem(line, 0, item)
            self.Display_Torrc.setItem(line, 1, item1)
        self.Display_Torrc.resizeRowsToContents()

    def _Edit_Torrc_Display(self, a, b):
        self.Input_Text.setText(modified_Torrc[a])
        self.Line_Selected1.setText(str(a+1))

    def _Add_Line(self):
        global modified_Torrc
        if (self.Input_Text.text() != ''):
            modified_Torrc.append(self.Input_Text.text())
            self._Display_Torrc(modified_Torrc)
            self.Alert_Add.show()
            QtCore.QTimer.singleShot(2000, self.Alert_Add.hide)
        else:
            self.Alert.show()
            QtCore.QTimer.singleShot(2000, self.Alert.hide)

    def _Delete_Line(self):
        global modified_Torrc
        if ((self.Input_Text.text() != '') and int(self.Line_Selected1.text()) != 0):
            content = modified_Torrc[int(self.Line_Selected1.text())-1]
            modified_Torrc.remove(content)
            self._Display_Torrc(modified_Torrc)
            self.Alert_Delete.show()
            QtCore.QTimer.singleShot(2000, self.Alert_Delete.hide)
        else:
            self.Alert.show()
            QtCore.QTimer.singleShot(2000, self.Alert.hide)

    def _Edit_Torrc_Apply(self):
        global modified_Torrc
        if ((self.Input_Text.text() != '') and (int(self.Line_Selected1.text()) != 0)):
            self.Alert.hide()
            modified_Torrc[int(self.Line_Selected1.text())-1] = self.Input_Text.text()
            self._Display_Torrc(modified_Torrc)
        else:
            self.Alert.show()
            QtCore.QTimer.singleShot(2000, self.Alert.hide)

    def _Reset_Changes(self):
        global modified_Torrc
        global original_Torrc
        if sys.platform == "win32":
            file = open(os.path.join("TrackTor\\Home", "Win_Torrc_Original"), "r")
        else:
            file = open(os.path.join("TrackTor/Home", "Linux_Torrc_Original"), "r")
        modified_Torrc = file.readlines()
        original_Torrc = list(modified_Torrc)

        self.Line_Selected1.clear()
        self.Input_Text.clear()
        self._Display_Torrc(modified_Torrc)
        self.Alert_Reset.show()
        QtCore.QTimer.singleShot(2000, self.Alert_Reset.hide)

    def _Reload_Tor(self):
        box.showAlertBox2(box,'Alert', 'Are You Sure?')

    def _ReloadTor(self):
        global modified_Torrc
        print (modified_Torrc)
        if sys.platform == "win32":
            file = open ("C:/Tor Browser/Browser/TorBrowser/Data/Tor/torrc-defaults", "r+")
        elif sys.platform in ["linux1", "linux2", "linux"]:
            file = open ("/etc/tor/torrc", "r+")
        elif sys.platform == "darwin":
            file = open ("/usr/local/etc/tor/torrc.sample", "r+")
        file.truncate(0)
        file.close()
        if sys.platform == "win32":
            file = open ("C:/Tor Browser/Browser/TorBrowser/Data/Tor/torrc-defaults", "r+")
        elif sys.platform in ["linux1", "linux2", "linux"]:
            file = open ("/etc/tor/torrc", "r+")
        elif sys.platform == "darwin":
            file = open ("/usr/local/etc/tor/torrc.sample", "r+")
        file.writelines(modified_Torrc)
        file.close()
        from TrackTor.Home.Actions import actions
        actions.ReloadTor(actions)

    def setupUi(self, Edit_Torrc):

        Edit_Torrc.setObjectName("Edit_Torrc")
        Edit_Torrc.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Edit_Torrc.sizePolicy().hasHeightForWidth())
        Edit_Torrc.setSizePolicy(sizePolicy)
        Edit_Torrc.setMinimumSize(QtCore.QSize(800, 600))
        Edit_Torrc.setMaximumSize(QtCore.QSize(800, 600))

        self.Torrc = QtWidgets.QWidget(Edit_Torrc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Torrc.sizePolicy().hasHeightForWidth())
        self.Torrc.setSizePolicy(sizePolicy)
        self.Torrc.setMinimumSize(QtCore.QSize(800, 600))
        self.Torrc.setMaximumSize(QtCore.QSize(800, 600))
        self.Torrc.setObjectName("Torrc")

        self.Torrc_Frame = QtWidgets.QFrame(self.Torrc)
        self.Torrc_Frame.setGeometry(QtCore.QRect(10, 5, 781, 591))
        self.Torrc_Frame.setStyleSheet("background-color: white")
        self.Torrc_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Torrc_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Torrc_Frame.setObjectName("Torrc_Frame")

        self.Input_Text = QtWidgets.QLineEdit(self.Torrc_Frame)
        self.Input_Text.setGeometry(QtCore.QRect(70, 18, 361, 31))
        self.Input_Text.setInputMask("")
        self.Input_Text.setText("")
        self.Input_Text.setObjectName("Input_Text")

        self.Reload_Tor = QtWidgets.QPushButton(self.Torrc_Frame)
        self.Reload_Tor.setGeometry(QtCore.QRect(670, 20, 89, 25))
        self.Reload_Tor.setObjectName("Reload_Tor")

        self.Alert = QtWidgets.QLabel(self.Torrc_Frame)
        self.Alert.setGeometry(QtCore.QRect(230, 60, 281, 17))
        self.Alert.setObjectName("Alert")
        self.Alert.hide()

        self.Alert_Reset = QtWidgets.QLabel(self.Torrc_Frame)
        self.Alert_Reset.setGeometry(QtCore.QRect(230, 60, 291, 17))
        self.Alert_Reset.setObjectName("Alert_Reset")
        self.Alert_Reset.hide()

        self.Alert_Delete = QtWidgets.QLabel(self.Torrc_Frame)
        self.Alert_Delete.setGeometry(QtCore.QRect(230, 60, 281, 17))
        self.Alert_Delete.setObjectName("Alert_Delete")
        self.Alert_Delete.hide()

        self.Alert_Add = QtWidgets.QLabel(self.Torrc_Frame)
        self.Alert_Add.setGeometry(QtCore.QRect(230, 60, 281, 17))
        self.Alert_Add.setObjectName("Alert_Add")
        self.Alert_Add.hide()

        self.Apply = QtWidgets.QPushButton(self.Torrc_Frame)
        self.Apply.setGeometry(QtCore.QRect(570, 20, 89, 25))
        self.Apply.setObjectName("Apply")

        self.Display_Torrc = QtWidgets.QTableWidget(self.Torrc_Frame)
        self.Display_Torrc.setGeometry(QtCore.QRect(10, 90, 761, 490))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display_Torrc.sizePolicy().hasHeightForWidth())
        self.Display_Torrc.setSizePolicy(sizePolicy)
        self.Display_Torrc.setMinimumSize(QtCore.QSize(761, 490))
        self.Display_Torrc.setMaximumSize(QtCore.QSize(761, 490))
        font = QtGui.QFont()
        font.setPointSize(10.5)
        self.Display_Torrc.setFont(font)
        self.Display_Torrc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Display_Torrc.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Display_Torrc.setDragDropOverwriteMode(False)
        self.Display_Torrc.setAlternatingRowColors(True)
        self.Display_Torrc.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Display_Torrc.setWordWrap(False)
        self.Display_Torrc.setRowCount(0)
        self.Display_Torrc.setObjectName("Display_Torrc")
        self.Display_Torrc.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Display_Torrc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Display_Torrc.setHorizontalHeaderItem(1, item)
        self.Display_Torrc.horizontalHeader().setCascadingSectionResizes(False)
        self.Display_Torrc.horizontalHeader().setDefaultSectionSize(75)
        self.Display_Torrc.horizontalHeader().setMinimumSectionSize(75)
        self.Display_Torrc.horizontalHeader().setStretchLastSection(True)
        self.Display_Torrc.verticalHeader().setVisible(False)
        self.Display_Torrc.verticalHeader().setDefaultSectionSize(50)
        self.Display_Torrc.verticalHeader().setMinimumSectionSize(50)

        self.Line_Selected1 = QtWidgets.QLineEdit(self.Torrc_Frame)
        self.Line_Selected1.setGeometry(QtCore.QRect(20, 18, 41, 31))
        self.Line_Selected1.setObjectName("Line_Selected1")

        self.Add = QtWidgets.QPushButton(self.Torrc_Frame)
        self.Add.setGeometry(QtCore.QRect(440, 20, 31, 25))
        self.Add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Images/Plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add.setIcon(icon)
        self.Add.setIconSize(QtCore.QSize(18, 18))
        self.Add.setObjectName("Add")

        self.Minus = QtWidgets.QPushButton(self.Torrc_Frame)
        self.Minus.setGeometry(QtCore.QRect(480, 20, 31, 25))
        self.Minus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Images/Minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minus.setIcon(icon1)
        self.Minus.setIconSize(QtCore.QSize(18, 18))
        self.Minus.setObjectName("Minus")

        self.Reset = QtWidgets.QPushButton(self.Torrc_Frame)
        self.Reset.setGeometry(QtCore.QRect(520, 20, 31, 25))
        self.Reset.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Images/Reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reset.setIcon(icon2)
        self.Reset.setIconSize(QtCore.QSize(18, 18))
        self.Reset.setObjectName("Reset")
        Edit_Torrc.setCentralWidget(self.Torrc)

        self.retranslateUi(Edit_Torrc)
        QtCore.QMetaObject.connectSlotsByName(Edit_Torrc)

        self.Add.clicked.connect(self._Add_Line)
        self.Minus.clicked.connect(self._Delete_Line)
        self.Reset.clicked.connect(self._Reset_Changes)
        self.Apply.clicked.connect(self._Edit_Torrc_Apply)
        self.Reload_Tor.clicked.connect(self._Reload_Tor)
        QtCore.QMetaObject.connectSlotsByName(Edit_Torrc)
        self.Display_Torrc.cellClicked.connect(self._Edit_Torrc_Display)
        self._Display_Torrc(modified_Torrc)

    def retranslateUi(self, Edit_Torrc):
        _translate = QtCore.QCoreApplication.translate
        Edit_Torrc.setWindowTitle(_translate("Edit_Torrc", "MainWindow"))
        self.Input_Text.setPlaceholderText(_translate("Edit_Torrc", "Type Here"))
        self.Reload_Tor.setText(_translate("Edit_Torrc", "Reload Tor"))
        self.Alert.setText(_translate("Edit_Torrc", "<html><head/><body><p align=\"center\"><span style=\" color:#ef2929;\">No Input Detected or Invalid Input.</span></p></body></html>"))
        self.Alert_Delete.setText(_translate("Edit_Torrc", "<html><head/><body><p align=\"center\"><span style=\" color:#ef2929;\">Selected line has been deleted.</span></p></body></html>"))
        self.Alert_Reset.setText(_translate("Edit_Torrc", "<html><head/><body><p align=\"center\"><span style=\" color:#ef2929;\">Torrc has been reconfigured to its original form.</span></p></body></html>"))
        self.Alert_Add.setText(_translate("Edit_Torrc", "<html><head/><body><p align=\"center\"><span style=\" color:#ef2929;\">Line has been added at the end.</span></p></body></html>"))
        self.Apply.setText(_translate("Edit_Torrc", "Apply"))
        self.Display_Torrc.setSortingEnabled(True)
        item = self.Display_Torrc.horizontalHeaderItem(0)
        item.setText(_translate("Edit_Torrc", "Line"))
        item = self.Display_Torrc.horizontalHeaderItem(1)
        item.setText(_translate("Edit_Torrc", "Content"))

class _Edit_Torrc():

    def Open_Edit_Torrc(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Edit_Torrc()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def Close_Edit_Torrc(self):
        self.Window.close()
