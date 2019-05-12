# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TracktorGraphNew.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

"""
**Module Overview:**

This module will implement the main funtionalities

|- Ui_TrackTor
    - newnym: This function will do funtionality of creating new identity
    - reloadtor: This function will do funtionality of reloading tor
    - torrc: This function will do functionality of Edit_torrc
    - _Disconnect_Tor: This function will do funtionality of disconnecting tor
    - _Reconnect_Tor: This function will do funtionality of reconnecting tor
    - setupUi: : This function will do funtionality of setting the UI
    - retranslateUi: This function will do funtionality of showing the UI
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from TrackTor.Home.DialogBox import box
from TrackTor.Tabs import _Tabs
import TrackTor.Utilities.Logs
import time
from TrackTor.Home.Edit_Torrc import _Edit_Torrc
import stem.descriptor.router_status_entry
import sqlite3
import pkg_resources

DB_FILE = pkg_resources.resource_filename("TrackTor", "Consensus.db")
conn = sqlite3.connect(DB_FILE)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS Relay_Info(fingerprint TEXT PRIMARY KEY, address TEXT, or_port INTEGER, nickname TEXT)''')

TrackTor_Events = ['BW', 'CIRC', 'ADDRMAP', 'BUILDTIMEOUT_SET', 'CELL_STATS', 'CIRC_BW',
'CIRC_MINOR', 'CLIENTS_SEEN', 'CONF_CHANGED', 'CONN_BW', 'DEBUG', 'DESCCHANGED', 'ERR',
'GUARD', 'HS_DESC', 'HS_DESC_CONTENT', 'INFO', 'NETWORK_LIVENESS', 'NEWCONSENSUS', 'NEWDESC',
'NOTICE', 'NS', 'ORCONN', 'SIGNAL', 'STREAM', 'STATUS_CLIENT', 'STATUS_GENERAL', 'STATUS_SERVER',
'STREAM_BW', 'TRANSPORT_LAUNCHED', 'WARN']

class Ui_TrackTor(object):
    #New Identity Function
    def newnym(self):
        box.showAlertBox(box,'Alert', 'Make sure that you want to generate new relays at the moment.')

    #Reload Tor Function
    def reloadtor(self):
        box.showAlertBox1(box,'Alert', 'Are You Sure?')

    #Edit torrc Function
    def torrc(self):
        try:
            from TrackTor.Home.Edit_Torrc import _Open_File
            _Open_File._File_Open()
            _Edit_Torrc.Open_Edit_Torrc(_Edit_Torrc)
        except:
            from  TrackTor.Home import MessageBox
            MessageBox.box.showMessageBox(MessageBox.box,'Alert', 'Provide Permissions to Torrc File to open this Window')

    def _Disconnect_Tor(self):
        from TrackTor.Utilities import StaticInfo
        StaticInfo.controller.close()
        self.OK.click()

    def _Reconnect_Tor(self):
        from TrackTor.Utilities import StaticInfo
        StaticInfo.controller.reconnect()
        self.OK.click()

    def setupUi(self, Tracktor):
        import TrackTor.Logs_Data
        Tracktor.setObjectName("Tracktor")
        Tracktor.resize(850, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tracktor.sizePolicy().hasHeightForWidth())
        Tracktor.setSizePolicy(sizePolicy)
        Tracktor.setMinimumSize(QtCore.QSize(850, 650))
        Tracktor.setMaximumSize(QtCore.QSize(850, 666))
        Tracktor.setStyleSheet("")

        self.Main_Window = QtWidgets.QWidget(Tracktor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Window.sizePolicy().hasHeightForWidth())
        self.Main_Window.setSizePolicy(sizePolicy)
        self.Main_Window.setMinimumSize(QtCore.QSize(850, 666))
        self.Main_Window.setMaximumSize(QtCore.QSize(850, 666))
        self.Main_Window.setObjectName("Main_Window")

        self.gridLayout = QtWidgets.QGridLayout(self.Main_Window)
        self.gridLayout.setObjectName("gridLayout")

        self.Static_bar = QtWidgets.QFrame(self.Main_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Static_bar.sizePolicy().hasHeightForWidth())
        self.Static_bar.setSizePolicy(sizePolicy)
        self.Static_bar.setMinimumSize(QtCore.QSize(825, 40))
        self.Static_bar.setMaximumSize(QtCore.QSize(825, 40))
        self.Static_bar.setStyleSheet("background: white")
        self.Static_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Static_bar.setFrameShadow(QtWidgets.QFrame.Raised)

        #Tabs
        self.Main_Tabs = QtWidgets.QTabWidget(self.Main_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Tabs.sizePolicy().hasHeightForWidth())
        self.Main_Tabs.setSizePolicy(sizePolicy)
        self.Main_Tabs.setMinimumSize(QtCore.QSize(825, 595))
        self.Main_Tabs.setMaximumSize(QtCore.QSize(825, 595))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Main_Tabs.setFont(font)
        self.Main_Tabs.setStyleSheet("background-color:white")
        self.Main_Tabs.setMovable(False)
        self.Main_Tabs.setObjectName("Main_Tabs")

        _Tabs._Static_Bar(self)
        _Tabs._Home(self)
        _Tabs._Data_Statistics(self)
        _Tabs._Connections(self)
        _Tabs._Relay_Info(self)
        _Tabs._Resources(self)
        _Tabs._Logs(self)
        _Tabs._About(self)

        self.gridLayout.addWidget(self.Main_Tabs, 1, 0, 1, 1)
        Tracktor.setCentralWidget(self.Main_Window)
        self.retranslateUi(Tracktor)
        self.Main_Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tracktor)

    def retranslateUi(self, Tracktor):
        _translate = QtCore.QCoreApplication.translate
        Tracktor.setWindowTitle(_translate("Tracktor", "Tracktor"))
        self.Uptime.setText(_translate("Tracktor", "Uptime:"))
        self.PID.setText(_translate("Tracktor", "PID:"))
        self.Control_port.setText(_translate("Tracktor", "Control Port:"))
        self.Tor.setText(_translate("Tracktor", "Tor Version:"))
        self.Main_Tabs.setWhatsThis(_translate("Tracktor", "<html><head/><body><p><br/></p></body></html>"))
        self.New_Identity.setText(_translate("TrackTor", "New Identity"))
        self.Reload_Tor.setText(_translate("TrackTor", "Reload Tor"))
        self.Edit_torrc.setText(_translate("TrackTor", "Edit Torrc"))
        self.Reconnect_Tor.setText(_translate("TrackTor", "Reconnect Tor"))
        self.Disconnect_Tor_Message.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" color:#ef2929;\">Tor Disconnected. Control Port Closed. Reconnect to Resume.</span></p></body></html>"))
        self.Disconnect_Tor.setText(_translate("TrackTor", "Disconnect Tor"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Home), _translate("TrackTor", "Home"))
        self.Uploads_Speed1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.Uploads_Speed.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">Uploads </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.Downloads_Speed1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.Downloads_Speed.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">Downloads </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.Uploads_Play.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Play</span></p></body></html>"))
        self.Uploads_Pause.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pause</span></p></body></html>"))
        self.Uploads_Pause.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Downloads_Play.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Play</span></p></body></html>"))
        self.Downloads_Play.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Downloads_Pause.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pause</span></p></body></html>"))
        self.Downloads_Pause.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Uploads_Interval.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interval</span></p></body></html>"))
        self.Uploads_Interval.setItemText(0, _translate("TrackTor", "Secondly"))
        self.Uploads_Interval.setItemText(1, _translate("TrackTor", "5 Secs"))
        self.Uploads_Interval.setItemText(2, _translate("TrackTor", "10 Secs"))
        self.Uploads_Interval.setItemText(3, _translate("TrackTor", "30 Secs"))
        self.Uploads_Interval.setItemText(4, _translate("TrackTor", "Minutely"))
        self.Uploads_Interval.setItemText(5, _translate("TrackTor", "5 Mins"))
        self.Uploads_Interval.setItemText(6, _translate("TrackTor", "10 Mins"))
        self.Uploads_Interval.setItemText(7, _translate("TrackTor", "30 Mins"))
        self.Uploads_Interval.setItemText(8, _translate("TrackTor", "Hourly"))
        self.Uploads_Interval.setItemText(9, _translate("TrackTor", "Daily"))
        self.Downloads_Interval.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interval</span></p></body></html>"))
        self.Downloads_Interval.setItemText(0, _translate("TrackTor", "Secondly"))
        self.Downloads_Interval.setItemText(1, _translate("TrackTor", "5 Secs"))
        self.Downloads_Interval.setItemText(2, _translate("TrackTor", "10 Secs"))
        self.Downloads_Interval.setItemText(3, _translate("TrackTor", "30 Secs"))
        self.Downloads_Interval.setItemText(4, _translate("TrackTor", "Minutely"))
        self.Downloads_Interval.setItemText(5, _translate("TrackTor", "5 Mins"))
        self.Downloads_Interval.setItemText(6, _translate("TrackTor", "10 Mins"))
        self.Downloads_Interval.setItemText(7, _translate("TrackTor", "30 Mins"))
        self.Downloads_Interval.setItemText(8, _translate("TrackTor", "Hourly"))
        self.Downloads_Interval.setItemText(9, _translate("TrackTor", "Daily"))
        self.Config_Desc1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Configuration Description</span></p></body></html>"))
        self.Config_CurrentVal.setText(_translate("TrackTor", "123"))
        self.Config_CurrentVal.setPlaceholderText(_translate("TrackTor", "Current Value"))
        self.Config_NewVal.setPlaceholderText(_translate("TrackTor", "New Value"))
        self.OK_2.setText(_translate("TrackTor", "OK"))
        self.Conf_Label.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" color:#227319;\">Value has been updated</span></p></body></html>"))
        self.Reset.setText(_translate("TrackTor", "Reset"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Data_Statistics), _translate("TrackTor", "Data Statistics"))
        self.Inbound_Interval.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interval</span></p></body></html>"))
        self.Inbound_Interval.setItemText(0, _translate("TrackTor", "Secondly"))
        self.Inbound_Interval.setItemText(1, _translate("TrackTor", "5 Secs"))
        self.Inbound_Interval.setItemText(2, _translate("TrackTor", "10 Secs"))
        self.Inbound_Interval.setItemText(3, _translate("TrackTor", "30 Secs"))
        self.Inbound_Interval.setItemText(4, _translate("TrackTor", "Minutely"))
        self.Inbound_Interval.setItemText(5, _translate("TrackTor", "5 Mins"))
        self.Inbound_Interval.setItemText(6, _translate("TrackTor", "10 Mins"))
        self.Inbound_Interval.setItemText(7, _translate("TrackTor", "30 Mins"))
        self.Inbound_Interval.setItemText(8, _translate("TrackTor", "Hourly"))
        self.Inbound_Interval.setItemText(9, _translate("TrackTor", "Daily"))
        self.Inbound_Conn1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.Inbound_Conn.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">Inbound Connections </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.Inbound_Play.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Play</span></p></body></html>"))
        self.Inbound_Play.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Inbound_Pause.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pause</span></p></body></html>"))
        self.Inbound_Pause.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Outbound_Play.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Play</span></p></body></html>"))
        self.Outbound_Play.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Outbound_Pause.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pause</span></p></body></html>"))
        self.Outbound_Pause.setWhatsThis(_translate("TrackTor", "<html><head/><body><p align=\"center\">Push</p></body></html>"))
        self.Outbound_Interval.setToolTip(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interval</span></p></body></html>"))
        self.Outbound_Interval.setItemText(0, _translate("TrackTor", "Secondly"))
        self.Outbound_Interval.setItemText(1, _translate("TrackTor", "5 Secs"))
        self.Outbound_Interval.setItemText(2, _translate("TrackTor", "10 Secs"))
        self.Outbound_Interval.setItemText(3, _translate("TrackTor", "30 Secs"))
        self.Outbound_Interval.setItemText(4, _translate("TrackTor", "Minutely"))
        self.Outbound_Interval.setItemText(5, _translate("TrackTor", "5 Mins"))
        self.Outbound_Interval.setItemText(6, _translate("TrackTor", "10 Mins"))
        self.Outbound_Interval.setItemText(7, _translate("TrackTor", "30 Mins"))
        self.Outbound_Interval.setItemText(8, _translate("TrackTor", "Hourly"))
        self.Outbound_Interval.setItemText(9, _translate("TrackTor", "Daily"))
        self.Outbound_Conn1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.Outbound_Conn.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">Outbound Connections </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Connections), _translate("TrackTor", "Connections"))
        self.Relay_Table.setSortingEnabled(True)
        item = self.Relay_Table.horizontalHeaderItem(0)
        item.setText(_translate("TrackTor", "Src_IP"))
        item = self.Relay_Table.horizontalHeaderItem(1)
        item.setText(_translate("TrackTor", "Src_Country"))
        item = self.Relay_Table.horizontalHeaderItem(2)
        item.setText(_translate("TrackTor", "Dest_IP"))
        item = self.Relay_Table.horizontalHeaderItem(3)
        item.setText(_translate("TrackTor", "Dest_Country"))
        item = self.Relay_Table.horizontalHeaderItem(4)
        item.setText(_translate("TrackTor", "Category"))
        item = self.Relay_Table.horizontalHeaderItem(5)
        item.setText(_translate("TrackTor", "Time"))
        self.Guard_Node.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Guard Node</span></p></body></html>"))
        self.End_Node.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">End Node</span></p></body></html>"))
        self.Middle_Node.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Middle Node</span></p></body></html>"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Relay_Info), _translate("TrackTor", "Relay Info"))
        self.CPU_Usage.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">CPU Usage </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.CPU_Tracktor.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.CPU_Tor.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.Tor_Percent.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tor ,</span></p></body></html>"))
        self.TrackTor_Percent.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tracktor</span></p></body></html>"))
        self.RAM_Usage.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#6429d7;\">RAM Usage </span><span style=\" font-size:14pt; color:#6429d7;\">-</span></p></body></html>"))
        self.RAM_Tracktor.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.RAM_Tor.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Tor_Percent1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tor ,</span></p></body></html>"))
        self.TrackTor_Percent1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tracktor</span></p></body></html>"))
        self.Resources_Tracktor1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TrackTor</span></p></body></html>"))
        self.Resources_Tor1.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Tor</span></p></body></html>"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Resources), _translate("TrackTor", "Resources"))
        self.Event_Type.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">EVENT TYPE</span></p></body></html>"))
        #self.Description.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Uploads</span></p></body></html>"))
        self.Run_Level.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">RUN LEVEL :</span></p></body></html>"))
        self.DEBUG.setText(_translate("TrackTor", "DEBUG"))
        self.INFO.setText(_translate("TrackTor", "INFO"))
        self.NOTICE.setText(_translate("TrackTor", "NOTICE"))
        self.WARN.setText(_translate("TrackTor", "WARN"))
        self.ERR.setText(_translate("TrackTor", "ERR"))
        self.CIRC.setText(_translate("TrackTor", "BW"))
        self.ORCONN.setText(_translate("TrackTor", "CIRC"))
        self.ADDRMAP.setText(_translate("TrackTor", "ADDRMAP"))
        self.STATUS_GENERAL.setText(_translate("TrackTor", "STATUS_GENERAL"))
        self.GUARD.setText(_translate("TrackTor", "GUARD"))
        self.CIRC_MINOR.setText(_translate("TrackTor", "CIRC_MINOR"))
        self.BW.setText(_translate("TrackTor", "ORCONN"))
        self.DESCCHANGED.setText(_translate("TrackTor", "DESCCHANGED"))
        self.CIRC_BW.setText(_translate("TrackTor", "CIRC_BW"))
        self.CONN_BW.setText(_translate("TrackTor", "CONN_BW"))
        self.STREAM.setText(_translate("TrackTor", "STREAM"))
        self.NS.setText(_translate("TrackTor", "NS"))
        self.HS_DESC_CONTENT.setText(_translate("TrackTor", "HS_DESC_CONTENT"))
        self.STREAM_BW.setText(_translate("TrackTor", "STREAM_BW"))
        self.CONF_CHANGED.setText(_translate("TrackTor", "CONF_CHANGED"))
        self.STATUS_SERVER.setText(_translate("TrackTor", "STATUS_SERVER"))
        self.STATUS_CLIENT.setText(_translate("TrackTor", "STATUS_CLIENT"))
        self.CLIENTS_SEEN.setText(_translate("TrackTor", "CLIENTS_SEEN"))
        self.NEWDESC.setText(_translate("TrackTor", "NEWDESC"))
        self.HS_DESC.setText(_translate("TrackTor", "HS_DESC"))
        self.TRANSPORT_LAUNCHED.setText(_translate("TrackTor", "TRANSPORT_LAUNCHED"))
        self.SIGNAL.setText(_translate("TrackTor", "SIGNAL"))
        self.CELL_STATS.setText(_translate("TrackTor", "CELL_STATS"))
        self.SELECT_ALL.setText(_translate("TrackTor", "Select All"))
        self.OK.setText(_translate("TrackTor", "OK"))
        self.BUILDTIMEOUT_SET.setText(_translate("TrackTor", "BUILDTIMEOUT_SET"))
        self.NETWORK_LIVENESS.setText(_translate("TrackTor", "NETWORK_LIVENESS"))
        self.NEWCONSENSUS.setText(_translate("TrackTor", "NEWCONSENSUS"))
        self.Save_Logs.setText(_translate("TrackTor", "Save "))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.Logs), _translate("TrackTor", "Logs"))
        self.About_Info.setText(_translate("TrackTor", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">TrackTor is a platform independent tool that provides statistical and analytical data tracked from the tor services exercised by the end user. Some of the highlighting features of TrackTor include detailed Bandwidth, Connections and Resources usage information, Event Logs details and many more. TrackTor finds its significance and wide usage with respect to professional/commercial and research work ongoing in the field of Deep/Dark web. It is an enhanced and versatile Graphical User Interface (GUI) based implementation, providing it an edge over the previously existing contemporary monitoring tools.</span></p></body></html>"))
        self.Main_Tabs.setTabText(self.Main_Tabs.indexOf(self.About), _translate("TrackTor", "About"))


app = QtWidgets.QApplication(sys.argv)
TrackTor = QtWidgets.QMainWindow()
ui = Ui_TrackTor()
ui.setupUi(TrackTor)
TrackTor.show()
sys.exit(app.exec_())
conn.commit()
conn.close()
