
"""
**Module Overview:**

This module will implement the tab funtionalities

|- _Tabs
    - __init__: This function will initialize UI object and other class variables in all files
    - _Static_Bar: This function will do the functionality of static bar
    - _Home: This function will do the functionality of home tab
    - _Data_Statistics: This function will do the functionality of data statistics tab
    - Uploads_Play_Button: This function will do the functionality of play button of uploads graph
    - Uploads_Pause_Button: This function will do the functionality of pause button of uploads graph
    - Downloads_Play_Button: This function will do the functionality of play button of downloads graph
    - Downloads_Pause_Button: This function will do the functionality of pause button of downloads graph
    - _Connections: This function will do the functionality of connections tab
    - Inbound_Play_Button: This function will do the functionality of play button of inbound graph
    - Inbound_Pause_Button: This function will do the functionality of pause button of inbound graph
    - Outbound_Play_Button: This function will do the functionality of play button of outbound graph
    - Outbound_Pause_Button: This function will do the functionality of pause button of outbound graph
    - _Relay_Info: This function will do the functionality of relay info tab
    - _Node_Details: This function will do the functionality of showing node info
    - _Show_Node_Details: This function will do the functionality of showing node info
    - _Display_Fingerprint: This function will do the functionality of showing fingerprint
    - _Resources: This function will do the functionality of resources tab
    - _Logs: This function will do the functionality of logs tab
    - _About: This function will do the functionality of about tab
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from TrackTor.Utilities import Graphs
from TrackTor.Utilities import Interval_Change
from pyqtgraph import PlotWidget
from TrackTor.Icons import Icons
from TrackTor.Utilities import StaticInfo
from TrackTor.Utilities import Logs
from TrackTor.Utilities import Relay_Info
from TrackTor.Utilities import Save_Logs
import pycountry
import stem.util.str_tools
import time
import calendar
import sys

class _Tabs():

        def __init__(self, ui):
            self.ui = ui

        def _Static_Bar(self):
            self.Static_bar.setObjectName("Static_bar")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.Static_bar)
            self.gridLayout_2.setObjectName("gridLayout_2")

            #Control Port
            self.Control_port = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Control_port.setFont(font)
            self.Control_port.setObjectName("Control_port")
            self.gridLayout_2.addWidget(self.Control_port, 0, 10, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_2.addItem(spacerItem, 0, 8, 1, 1)

            self.Control_port1 = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Control_port1.setFont(font)
            self.Control_port1.setText(str(StaticInfo.control_port))
            self.Control_port1.setObjectName("Control_port1")
            self.gridLayout_2.addWidget(self.Control_port1, 0, 11, 1, 1)

            #Uptime
            self.Uptime = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Uptime.setFont(font)
            self.Uptime.setObjectName("Uptime")
            self.gridLayout_2.addWidget(self.Uptime, 0, 4, 1, 1)

            self.si = StaticInfo.Tor_Usage_Info(self)
            self.uptime_timer = QtCore.QTimer()
            self.uptime_timer.timeout.connect(self.si.Info)
            self.uptime_timer.start(2000)

            self.Uptime1 = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Uptime1.setFont(font)
            self.Uptime1.setObjectName("Uptime1")
            self.gridLayout_2.addWidget(self.Uptime1, 0, 7, 1, 1)

            #Tor Version
            self.Tor = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Tor.setFont(font)
            self.Tor.setObjectName("Tor")
            self.gridLayout_2.addWidget(self.Tor, 0, 1, 1, 1)
            self.Tor_version1 = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)

            self.Tor_version1.setFont(font)
            self.Tor_version1.setText(StaticInfo.version)
            self.Tor_version1.setObjectName("Tor_version1")
            self.gridLayout_2.addWidget(self.Tor_version1, 0, 2, 1, 1)

            #PID
            self.PID = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.PID.setFont(font)
            self.PID.setObjectName("PID")
            self.gridLayout_2.addWidget(self.PID, 0, 13, 1, 1)

            self.PID1 = QtWidgets.QLabel(self.Static_bar)
            font = QtGui.QFont()
            font.setPointSize(11)
            self.PID1.setFont(font)
            self.PID1.setText(str(StaticInfo.pid))
            self.PID1.setObjectName("PID1")
            self.gridLayout_2.addWidget(self.PID1, 0, 14, 1, 1)

            #Spacerscontrol_port1
            spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
            spacerItem2 = QtWidgets.QSpacerItem(71, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
            spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_2.addItem(spacerItem3, 0, 12, 1, 1)
            spacerItem4 = QtWidgets.QSpacerItem(71, 12, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_2.addItem(spacerItem4, 0, 15, 1, 1)
            self.gridLayout.addWidget(self.Static_bar, 2, 0, 1, 1)

        def _Home(self):
            #Home Tab
            self.Home = QtWidgets.QWidget()
            self.Home.setMinimumSize(QtCore.QSize(825, 575))
            self.Home.setMaximumSize(QtCore.QSize(825, 575))
            self.Home.setObjectName("Home")

            #New Identity
            self.New_Identity = QtWidgets.QPushButton(self.Home)
            self.New_Identity.setGeometry(QtCore.QRect(81, 270, 130, 25))
            self.New_Identity.setMouseTracking(True)
            self.New_Identity.setObjectName("New_Identity")
            self.New_Identity.clicked.connect(self.newnym)

            #Reload Tor
            self.Reload_Tor = QtWidgets.QPushButton(self.Home)
            self.Reload_Tor.setGeometry(QtCore.QRect(434, 270, 130, 25))
            self.Reload_Tor.setMouseTracking(True)
            self.Reload_Tor.setObjectName("Reload_Tor")
            self.Reload_Tor.clicked.connect(self.reloadtor)

            #Edit Torrc
            self.Edit_torrc = QtWidgets.QPushButton(self.Home)
            self.Edit_torrc.setGeometry(QtCore.QRect(257, 270, 130, 25))
            self.Edit_torrc.setMouseTracking(True)
            self.Edit_torrc.setObjectName("Edit_torrc")
            self.Edit_torrc.clicked.connect(self.torrc)

            #Disconnect Tor
            self.Reconnect_Tor = QtWidgets.QPushButton(self.Home)
            self.Reconnect_Tor.setGeometry(QtCore.QRect(610, 270, 130, 25))
            self.Reconnect_Tor.setMouseTracking(True)
            self.Reconnect_Tor.setObjectName("Disconnect_Tor")
            self.Reconnect_Tor.setText("Reconnect Tor")
            self.Reconnect_Tor.clicked.connect(self._Reconnect_Tor)

            #Disconnect Tor
            self.Disconnect_Tor = QtWidgets.QPushButton(self.Home)
            self.Disconnect_Tor.setGeometry(QtCore.QRect(610, 270, 130, 25))
            self.Disconnect_Tor.setMouseTracking(True)
            self.Disconnect_Tor.setObjectName("Disconnect_Tor")
            self.Disconnect_Tor.setText("Disconnect Tor")
            self.Disconnect_Tor.clicked.connect(self._Disconnect_Tor)

            self.Disconnect_Tor_Message = QtWidgets.QLabel(self.Home)
            self.Disconnect_Tor_Message.setGeometry(QtCore.QRect(210, 320, 421, 17))
            self.Disconnect_Tor_Message.setObjectName("Disconnect_Tor_Message")
            self.Disconnect_Tor_Message.hide()

            #Welcome Image
            self.Splashscreen = QtWidgets.QLabel(self.Home)
            self.Splashscreen.setGeometry(QtCore.QRect(-10, -30, 841, 601))
            self.Splashscreen.setText("")
            self.Splashscreen.setPixmap(QtGui.QPixmap(":/Splashscreen/Images/Splashscreen.png"))
            self.Splashscreen.setScaledContents(True)
            self.Splashscreen.setObjectName("label")


            self.Splashscreen.raise_()
            self.Edit_torrc.raise_()
            self.Reload_Tor.raise_()
            self.New_Identity.raise_()
            self.Disconnect_Tor_Message.raise_()
            #self.Reconnect_Tor.raise_()
            self.Disconnect_Tor.raise_()
            self.Disconnect_Tor.clicked['bool'].connect(self.Reconnect_Tor.raise_)
            self.Reconnect_Tor.clicked['bool'].connect(self.Disconnect_Tor.raise_)
            self.Disconnect_Tor.clicked['bool'].connect(self.Disconnect_Tor_Message.show)
            self.Reconnect_Tor.clicked['bool'].connect(self.Disconnect_Tor_Message.hide)


            self.Main_Tabs.addTab(self.Home, "")

        def _Data_Statistics(self):
            self.Data_Statistics = QtWidgets.QWidget()
            self.Data_Statistics.setMinimumSize(QtCore.QSize(825, 575))
            self.Data_Statistics.setMaximumSize(QtCore.QSize(825, 575))
            self.Data_Statistics.setStyleSheet("")
            self.Data_Statistics.setObjectName("Data_Statistics")
            self.Data_Statistics_Frame = QtWidgets.QFrame(self.Data_Statistics)
            self.Data_Statistics_Frame.setGeometry(QtCore.QRect(10, 10, 801, 551))
            self.Data_Statistics_Frame.setStyleSheet("background-color:None")
            self.Data_Statistics_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Data_Statistics_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Data_Statistics_Frame.setObjectName("Data_Statistics_Frame")

            #Class For Interval change
            self.ic = Interval_Change._Interval_Change(self)

            #Class for Data Statistics
            self.ds = Graphs.Data_Statistics(self)

            #Uploads Graph
            self.Uploads = PlotWidget(self.Data_Statistics_Frame)
            self.Uploads.setGeometry(QtCore.QRect(0, 90, 391, 271))
            self.Uploads.setObjectName("Uploads")
            self.Uploads.setLabel('left', 'Data Sent', 'Bytes')
            self.Uploads.setLabel('bottom', 'Refreshing every Second')
            self.uploads_curve = self.Uploads.plot(Graphs.uploads_x, Graphs.uploads_y, pen=(255,0,0))

            # QTimer
            self.uploads_timer = QtCore.QTimer()
            def Uploads_Play_Button():
                    self.uploads_timer.timeout.connect(self.ds.Uploads)
                    self.uploads_timer.start(Interval_Change.Uploads_Interval)
                    self.Uploads_Play.setEnabled(False)
                    self.Uploads_Pause.setEnabled(True)

            def Uploads_Pause_Button():
                    self.uploads_timer.stop()
                    self.Uploads_Play.setEnabled(True)
                    self.Uploads_Pause.setEnabled(False)


            #Uploads Text
            self.Uploads_Frame = QtWidgets.QFrame(self.Data_Statistics_Frame)
            self.Uploads_Frame.setGeometry(QtCore.QRect(0, 0, 391, 42))
            self.Uploads_Frame.setStyleSheet("background-color:white")
            self.Uploads_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Uploads_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Uploads_Frame.setObjectName("Uploads_Frame")

            self.gridLayout_3 = QtWidgets.QGridLayout(self.Uploads_Frame)
            self.gridLayout_3.setObjectName("gridLayout_3")

            #Uploads Speed Text
            self.Uploads_Speed = QtWidgets.QLabel(self.Uploads_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Uploads_Speed.sizePolicy().hasHeightForWidth())
            self.Uploads_Speed.setSizePolicy(sizePolicy)
            self.Uploads_Speed.setObjectName("Uploads_Speed")
            self.gridLayout_3.addWidget(self.Uploads_Speed, 0, 1, 1, 1)

            #Uploads Speed Value
            self.Uploads_Speed1 = QtWidgets.QLabel(self.Uploads_Frame)
            sizePolicy.setHeightForWidth(self.Uploads_Speed1.sizePolicy().hasHeightForWidth())
            self.Uploads_Speed1.setSizePolicy(sizePolicy)
            self.Uploads_Speed1.setObjectName("Uploads_Speed1")
            self.Uploads_Speed1.setText('0.0' + " kB/s")
            self.font = QtGui.QFont()
            self.font.setPointSize(12)
            self.Uploads_Speed1.setFont(self.font)
            self.gridLayout_3.addWidget(self.Uploads_Speed1, 0, 2, 1, 1)

            self.spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_3.addItem(self.spacerItem8, 0, 0, 1, 1)
            self.spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_3.addItem(self.spacerItem9, 0, 3, 1, 1)

            #Uploads Play Button
            self.Uploads_Play = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.Uploads_Play.setEnabled(True)
            self.Uploads_Play.setGeometry(QtCore.QRect(0, 50, 31, 31))
            self.Uploads_Play.setStyleSheet("background-color:white\n""")
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap(":/Play/Pause/Images/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Uploads_Play.setIcon(self.icon)
            self.Uploads_Play.setIconSize(QtCore.QSize(35, 23))
            self.Uploads_Play.setCheckable(False)
            self.Uploads_Play.setChecked(False)
            self.Uploads_Play.setObjectName("Uploads_Play")
            self.Uploads_Play.setEnabled(False)
            self.Uploads_Play.clicked.connect(Uploads_Play_Button)

            #Uploads Pause Button
            self.Uploads_Pause = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.Uploads_Pause.setEnabled(True)
            self.Uploads_Pause.setWhatsThis("")
            self.Uploads_Pause.setGeometry(QtCore.QRect(0, 50, 31, 31))
            self.Uploads_Pause.setStyleSheet("background-color:white\n""")
            self.Uploads_Pause.setText("")
            self.icon1 = QtGui.QIcon()
            self.icon1.addPixmap(QtGui.QPixmap(":/Play/Pause/Images/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Uploads_Pause.setIcon(self.icon1)
            self.Uploads_Pause.setIconSize(QtCore.QSize(35, 23))
            self.Uploads_Pause.setCheckable(False)
            self.Uploads_Pause.setObjectName("Uploads_Pause")
            self.Uploads_Pause.clicked.connect(Uploads_Pause_Button)

            self.Uploads_Pause.raise_()
            self.Uploads_Pause.clicked['bool'].connect(self.Uploads_Play.raise_)
            self.Uploads_Play.clicked['bool'].connect(self.Uploads_Pause.raise_)

            if self.Uploads_Pause.isEnabled():
                    self.uploads_timer.timeout.connect(self.ds.Uploads)
                    self.uploads_timer.start(Interval_Change.Uploads_Interval)

            #Uploads Interval
            self.Uploads_Interval = QtWidgets.QComboBox(self.Data_Statistics_Frame)
            if sys.platform == 'darwin':
                self.Uploads_Interval.setGeometry(QtCore.QRect(300, 50, 97, 27))
            else:
                self.Uploads_Interval.setGeometry(QtCore.QRect(290, 50, 97, 27))
            self.Uploads_Interval.setMinimumSize(QtCore.QSize(97, 27))
            self.Uploads_Interval.setMaximumSize(QtCore.QSize(97, 27))
            self.Uploads_Interval.setFrame(True)
            self.Uploads_Interval.setObjectName("Uploads_Interval")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.addItem("")
            self.Uploads_Interval.currentIndexChanged.connect(self.ic.Uploads)

            #Downloads Graph
            self.Downloads = PlotWidget(self.Data_Statistics_Frame)
            self.Downloads.setGeometry(QtCore.QRect(410, 90, 401, 271))
            self.Downloads.setObjectName("Downloads")
            self.Downloads.setLabel('left', 'Data Sent', 'Bytes')
            self.Downloads.setLabel('bottom', 'Refreshing every Second')
            self.downloads_curve = self.Downloads.plot(Graphs.downloads_x, Graphs.downloads_y, pen=(255,0,0))

            # QTimer
            self.downloads_timer = QtCore.QTimer()
            def Downloads_Play_Button():
                    self.downloads_timer.timeout.connect(self.ds.Downloads)
                    self.downloads_timer.start(Interval_Change.Downloads_Interval)
                    self.Downloads_Play.setEnabled(False)
                    self.Downloads_Pause.setEnabled(True)

            def Downloads_Pause_Button():
                    self.downloads_timer.stop()
                    self.Downloads_Play.setEnabled(True)
                    self.Downloads_Pause.setEnabled(False)


            #Downloads Text
            self.Downloads_Frame = QtWidgets.QFrame(self.Data_Statistics_Frame)
            self.Downloads_Frame.setGeometry(QtCore.QRect(410, 0, 391, 42))
            self.Downloads_Frame.setStyleSheet("background-color:white")
            self.Downloads_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Downloads_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Downloads_Frame.setObjectName("Downloads_Frame")

            self.gridLayout_4 = QtWidgets.QGridLayout(self.Downloads_Frame)
            self.gridLayout_4.setObjectName("gridLayout_4")

            #Downloads Speed
            self.Downloads_Speed1 = QtWidgets.QLabel(self.Downloads_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Downloads_Speed1.sizePolicy().hasHeightForWidth())
            self.Downloads_Speed1.setSizePolicy(sizePolicy)
            self.Downloads_Speed1.setObjectName("Downloads_Speed1")
            self.Downloads_Speed1.setText(str(0.0) + " kB/s")
            self.Downloads_Speed1.setFont(self.font)
            self.gridLayout_4.addWidget(self.Downloads_Speed1, 0, 2, 1, 1)

            self.Downloads_Speed = QtWidgets.QLabel(self.Downloads_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Downloads_Speed.sizePolicy().hasHeightForWidth())
            self.Downloads_Speed.setSizePolicy(sizePolicy)
            self.Downloads_Speed.setObjectName("Downloads_Speed")
            self.gridLayout_4.addWidget(self.Downloads_Speed, 0, 1, 1, 1)

            self.spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_4.addItem(self.spacerItem10, 0, 0, 1, 1)
            self.spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_4.addItem(self.spacerItem11, 0, 3, 1, 1)

            #Downloads Play
            self.Downloads_Play = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.Downloads_Play.setGeometry(QtCore.QRect(410, 50, 31, 31))
            self.Downloads_Play.setStyleSheet("background-color:white\n""")
            self.Downloads_Play.setText("")
            self.Downloads_Play.setIcon(self.icon)
            self.Downloads_Play.setIconSize(QtCore.QSize(35, 23))
            self.Downloads_Play.setObjectName("Downloads_Play")
            self.Downloads_Play.setEnabled(False)
            self.Downloads_Play.clicked.connect(Downloads_Play_Button)

            #Downloads Pause
            self.Downloads_Pause = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.Downloads_Pause.setGeometry(QtCore.QRect(410, 50, 31, 31))
            self.Downloads_Pause.setStyleSheet("background-color:white\n""")
            self.Downloads_Pause.setText("")
            self.Downloads_Pause.setIcon(self.icon1)
            self.Downloads_Pause.setIconSize(QtCore.QSize(35, 23))
            self.Downloads_Pause.setObjectName("Downloads_Pause")
            self.Downloads_Pause.clicked.connect(Downloads_Pause_Button)

            self.Downloads_Pause.raise_()
            self.Downloads_Pause.clicked['bool'].connect(self.Downloads_Play.raise_)
            self.Downloads_Play.clicked['bool'].connect(self.Downloads_Pause.raise_)

            if self.Downloads_Pause.isEnabled():
                    self.downloads_timer.timeout.connect(self.ds.Downloads)
                    self.downloads_timer.start(Interval_Change.Downloads_Interval)

            #Downloads Interval
            self.Downloads_Interval = QtWidgets.QComboBox(self.Data_Statistics_Frame)
            if sys.platform == 'darwin':
                self.Downloads_Interval.setGeometry(QtCore.QRect(710, 50, 97, 27))
            else:
                self.Downloads_Interval.setGeometry(QtCore.QRect(700, 50, 97, 27))
            self.Downloads_Interval.setMinimumSize(QtCore.QSize(97, 27))
            self.Downloads_Interval.setMaximumSize(QtCore.QSize(97, 27))
            self.Downloads_Interval.setFrame(True)
            self.Downloads_Interval.setObjectName("Downloads_Interval")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.addItem("")
            self.Downloads_Interval.currentIndexChanged.connect(self.ic.Downloads)

            self.Config_Desc = QtWidgets.QListWidget(self.Data_Statistics_Frame)
            self.Config_Desc.setGeometry(QtCore.QRect(0, 440, 801, 91))
            self.Config_Desc.setObjectName("Config_Desc")
            self.Config_Desc1 = QtWidgets.QLabel(self.Data_Statistics_Frame)
            self.Config_Desc1.setGeometry(QtCore.QRect(270, 440, 261, 21))
            self.Config_Desc1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Config_Desc1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Config_Desc1.setObjectName("Config_Desc1")
            #self.Config_Desc1.setText("Configuration Description")

            self.Config_Options = QtWidgets.QComboBox(self.Data_Statistics_Frame)
            self.Config_Options.setGeometry(QtCore.QRect(80, 380, 171, 25))
            self.Config_Options.setObjectName("Config_Options")

            self.Config_CurrentVal = QtWidgets.QLineEdit(self.Data_Statistics_Frame)
            self.Config_CurrentVal.setGeometry(QtCore.QRect(260, 380, 131, 25))
            self.Config_CurrentVal.setObjectName("Config_CurrentVal")
            self.Config_CurrentVal.setReadOnly(True)

            self.Config_NewVal = QtWidgets.QLineEdit(self.Data_Statistics_Frame)
            self.Config_NewVal.setGeometry(QtCore.QRect(400, 380, 131, 25))
            self.Config_NewVal.setObjectName("Config_NewVal")

            self.OK_2 = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.OK_2.setGeometry(QtCore.QRect(540, 380, 89, 25))
            self.OK_2.setObjectName("OK_2")

            self.Conf_Label = QtWidgets.QLabel(self.Data_Statistics_Frame)
            self.Conf_Label.setGeometry(QtCore.QRect(200, 410, 501, 20))
            self.Conf_Label.setObjectName("Conf_Label")
            self.Conf_Label.hide()

            self.Reset = QtWidgets.QPushButton(self.Data_Statistics_Frame)
            self.Reset.setGeometry(QtCore.QRect(640, 380, 89, 25))
            self.Reset.setObjectName("Reset")

            from TrackTor.Utilities import Configurations
            self.config = Configurations._Configurations(self)
            self.config._Config_DropDown()
            self.Config_Options.currentIndexChanged.connect(self.config._Config_CurrentVal)
            self.OK_2.clicked.connect(self.config._Config_ChangeVal)
            self.Reset.clicked.connect(self.config._Config_Reset)

            self.Main_Tabs.addTab(self.Data_Statistics, "")

        def _Connections(self):

            self.Connections = QtWidgets.QWidget()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Connections.sizePolicy().hasHeightForWidth())
            self.Connections.setSizePolicy(sizePolicy)
            self.Connections.setMinimumSize(QtCore.QSize(825, 575))
            self.Connections.setMaximumSize(QtCore.QSize(825, 575))
            self.Connections.setObjectName("Connections")
            self.Connections_Frame = QtWidgets.QFrame(self.Connections)
            self.Connections_Frame.setGeometry(QtCore.QRect(10, 20, 811, 561))
            self.Connections_Frame.setStyleSheet("background-color:None")
            self.Connections_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Connections_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Connections_Frame.setObjectName("Connections_Frame")

            #Inbound Text Frame
            self.Inbound_Frame = QtWidgets.QFrame(self.Connections_Frame)
            self.Inbound_Frame.setGeometry(QtCore.QRect(0, -10, 391, 42))
            self.Inbound_Frame.setStyleSheet("background-color:white")
            self.Inbound_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Inbound_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Inbound_Frame.setObjectName("Inbound_Frame")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.Inbound_Frame)
            self.gridLayout_5.setObjectName("gridLayout_5")

            #Text Inbound connections
            self.Inbound_Conn = QtWidgets.QLabel(self.Inbound_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Inbound_Conn.sizePolicy().hasHeightForWidth())
            self.Inbound_Conn.setSizePolicy(sizePolicy)
            self.Inbound_Conn.setObjectName("Inbound_Conn")
            self.gridLayout_5.addWidget(self.Inbound_Conn, 0, 1, 1, 1)

            #Number of Inbound Connections
            self.Inbound_Conn1 = QtWidgets.QLabel(self.Inbound_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Inbound_Conn1.sizePolicy().hasHeightForWidth())
            self.Inbound_Conn1.setSizePolicy(sizePolicy)
            self.Inbound_Conn1.setObjectName("Inbound_Conn1")
            self.Inbound_Conn1.setText('0' + " /Sec")
            self.Inbound_Conn1.setFont(self.font)
            self.gridLayout_5.addWidget(self.Inbound_Conn1, 0, 2, 1, 1)

            spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_5.addItem(spacerItem12, 0, 0, 1, 1)
            spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_5.addItem(spacerItem13, 0, 3, 1, 1)

            #Class for Connections
            self.conn = Graphs.Connections(self)

            #Inbound Graph
            self.Inbound = PlotWidget(self.Connections_Frame)
            self.Inbound.setGeometry(QtCore.QRect(0, 90, 391, 271))
            self.Inbound.setObjectName("Inbound")
            self.Inbound.setLabel('left', 'Inbound Connections', 'Nos')
            self.Inbound.setLabel('bottom', 'Refreshing every Second')
            self.inbound_curve = self.Inbound.plot(Graphs.inbound_x, Graphs.inbound_y, pen=(255,0,0))

            # QTimer
            self.inbound_timer = QtCore.QTimer()
            def Inbound_Play_Button():
                    self.inbound_timer.timeout.connect(self.conn.Inbound)
                    self.inbound_timer.start(Interval_Change.Inbound_Interval)
                    self.Inbound_Play.setEnabled(False)
                    self.Inbound_Pause.setEnabled(True)

            def Inbound_Pause_Button():
                    self.inbound_timer.stop()
                    self.Inbound_Play.setEnabled(True)
                    self.Inbound_Pause.setEnabled(False)

            #Inbound Play Button
            self.Inbound_Play = QtWidgets.QPushButton(self.Connections_Frame)
            self.Inbound_Play.setGeometry(QtCore.QRect(0, 50, 31, 31))
            self.Inbound_Play.setStyleSheet("background-color:white\n""")
            self.Inbound_Play.setText("")
            self.Inbound_Play.setIcon(self.icon)
            self.Inbound_Play.setIconSize(QtCore.QSize(35, 23))
            self.Inbound_Play.setObjectName("Inbound_Play")
            self.Inbound_Play.setEnabled(False)
            self.Inbound_Play.clicked.connect(Inbound_Play_Button)

            #Inbound Pause Button
            self.Inbound_Pause = QtWidgets.QPushButton(self.Connections_Frame)
            self.Inbound_Pause.setGeometry(QtCore.QRect(0, 50, 31, 31))
            self.Inbound_Pause.setStyleSheet("background-color:white\n""")
            self.Inbound_Pause.setText("")
            self.Inbound_Pause.setIcon(self.icon1)
            self.Inbound_Pause.setIconSize(QtCore.QSize(35, 23))
            self.Inbound_Pause.setObjectName("Inbound_Pause")
            self.Inbound_Pause.clicked.connect(Inbound_Pause_Button)

            self.Inbound_Pause.raise_()
            self.Inbound_Pause.clicked['bool'].connect(self.Inbound_Play.raise_)
            self.Inbound_Play.clicked['bool'].connect(self.Inbound_Pause.raise_)

            if self.Inbound_Pause.isEnabled():
                    self.inbound_timer.timeout.connect(self.conn.Inbound)
                    self.inbound_timer.start(Interval_Change.Inbound_Interval)

            #Inbound Interval
            self.Inbound_Interval = QtWidgets.QComboBox(self.Connections_Frame)
            if sys.platform == 'darwin':
                self.Inbound_Interval.setGeometry(QtCore.QRect(300, 50, 97, 27))
            else:
                self.Inbound_Interval.setGeometry(QtCore.QRect(290, 50, 97, 27))
            self.Inbound_Interval.setMinimumSize(QtCore.QSize(97, 27))
            self.Inbound_Interval.setMaximumSize(QtCore.QSize(97, 27))
            self.Inbound_Interval.setFrame(True)
            self.Inbound_Interval.setObjectName("Inbound_Interval")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.addItem("")
            self.Inbound_Interval.currentIndexChanged.connect(self.ic.Inbound)

            #Outbound Graph
            self.Outbound = PlotWidget(self.Connections_Frame)
            self.Outbound.setGeometry(QtCore.QRect(410, 90, 391, 271))
            self.Outbound.setObjectName("Outbound")
            self.Outbound.setLabel('left', 'Outbound Connections', 'Nos')
            self.Outbound.setLabel('bottom', 'Refreshing every Second')
            self.outbound_curve = self.Outbound.plot(Graphs.outbound_x, Graphs.outbound_y, pen=(255,0,0))

            #Outbound Text Frame
            self.Outbound_Frame = QtWidgets.QFrame(self.Connections)
            self.Outbound_Frame.setGeometry(QtCore.QRect(410, 10, 391, 42))
            self.Outbound_Frame.setStyleSheet("background-color:white")
            self.Outbound_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Outbound_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Outbound_Frame.setObjectName("Outbound_Frame")
            self.gridLayout_6 = QtWidgets.QGridLayout(self.Outbound_Frame)
            self.gridLayout_6.setObjectName("gridLayout_6")

            #Text Outbound Connections
            self.Outbound_Conn = QtWidgets.QLabel(self.Outbound_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Outbound_Conn.sizePolicy().hasHeightForWidth())
            self.Outbound_Conn.setSizePolicy(sizePolicy)
            self.Outbound_Conn.setObjectName("Outbound_Conn")
            self.gridLayout_6.addWidget(self.Outbound_Conn, 0, 1, 1, 1)

            #Number of OutBound Connections
            self.Outbound_Conn1 = QtWidgets.QLabel(self.Outbound_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Outbound_Conn1.sizePolicy().hasHeightForWidth())
            self.Outbound_Conn1.setSizePolicy(sizePolicy)
            self.Outbound_Conn1.setObjectName("Outbound_Conn1")
            self.Outbound_Conn1.setText('0' + " /Sec")
            self.Outbound_Conn1.setFont(self.font)
            self.gridLayout_6.addWidget(self.Outbound_Conn1, 0, 2, 1, 1)

            # QTimer
            self.outbound_timer = QtCore.QTimer()
            def Outbound_Play_Button():
                    self.outbound_timer.timeout.connect(self.conn.Outbound)
                    self.outbound_timer.start(Interval_Change.Outbound_Interval)
                    self.Outbound_Play.setEnabled(False)
                    self.Outbound_Pause.setEnabled(True)

            def Outbound_Pause_Button():
                    self.outbound_timer.stop()
                    self.Outbound_Play.setEnabled(True)
                    self.Outbound_Pause.setEnabled(False)

            #Outbound Play Button
            self.Outbound_Play = QtWidgets.QPushButton(self.Connections_Frame)
            self.Outbound_Play.setGeometry(QtCore.QRect(410, 50, 31, 31))
            self.Outbound_Play.setStyleSheet("background-color:white\n""")
            self.Outbound_Play.setText("")
            self.Outbound_Play.setIcon(self.icon)
            self.Outbound_Play.setIconSize(QtCore.QSize(35, 23))
            self.Outbound_Play.setObjectName("Outbound_Play")
            self.Outbound_Play.setEnabled(False)
            self.Outbound_Play.clicked.connect(Outbound_Play_Button)

            #Outbound Pause Button
            self.Outbound_Pause = QtWidgets.QPushButton(self.Connections_Frame)
            self.Outbound_Pause.setGeometry(QtCore.QRect(410, 50, 31, 31))
            self.Outbound_Pause.setStyleSheet("background-color:white\n""")
            self.Outbound_Pause.setText("")
            self.Outbound_Pause.setIcon(self.icon1)
            self.Outbound_Pause.setIconSize(QtCore.QSize(35, 23))
            self.Outbound_Pause.setObjectName("Outbound_Pause")
            self.Outbound_Pause.clicked.connect(Outbound_Pause_Button)

            self.Outbound_Pause.raise_()
            self.Outbound_Pause.clicked['bool'].connect(self.Outbound_Play.raise_)
            self.Outbound_Play.clicked['bool'].connect(self.Outbound_Pause.raise_)

            if self.Outbound_Pause.isEnabled():
                self.outbound_timer.timeout.connect(self.conn.Outbound)
                self.outbound_timer.start(Interval_Change.Outbound_Interval)
            #Outbound Interval
            self.Outbound_Interval = QtWidgets.QComboBox(self.Connections_Frame)
            if sys.platform == 'darwin':
                self.Outbound_Interval.setGeometry(QtCore.QRect(710, 50, 97, 27))
            else:
                self.Outbound_Interval.setGeometry(QtCore.QRect(700, 50, 97, 27))
            self.Outbound_Interval.setMinimumSize(QtCore.QSize(97, 27))
            self.Outbound_Interval.setMaximumSize(QtCore.QSize(97, 27))
            self.Outbound_Interval.setFrame(True)
            self.Outbound_Interval.setObjectName("Outbound_Interval")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.addItem("")
            self.Outbound_Interval.currentIndexChanged.connect(self.ic.Outbound)

            spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_6.addItem(spacerItem14, 0, 0, 1, 1)
            spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout_6.addItem(spacerItem15, 0, 3, 1, 1)
            self.Main_Tabs.addTab(self.Connections, "")

        def _Relay_Info(self):

            self.controller = StaticInfo.controller
            self.Relay_Info = QtWidgets.QWidget()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Relay_Info.sizePolicy().hasHeightForWidth())
            self.Relay_Info.setSizePolicy(sizePolicy)
            self.Relay_Info.setMinimumSize(QtCore.QSize(821, 565))
            self.Relay_Info.setMaximumSize(QtCore.QSize(821, 565))
            self.Relay_Info.setObjectName("Relay_Info")
            self.Relay_Info_frame = QtWidgets.QFrame(self.Relay_Info)
            self.Relay_Info_frame.setGeometry(QtCore.QRect(10, 10, 801, 551))
            self.Relay_Info_frame.setStyleSheet("background-color:None")
            self.Relay_Info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Relay_Info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Relay_Info_frame.setObjectName("Relay_Info_frame")
            self.Relay_Table = QtWidgets.QTableWidget(self.Relay_Info_frame)
            self.Relay_Table.setGeometry(QtCore.QRect(0, 0, 801, 251))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.Relay_Table.setFont(font)
            self.Relay_Table.setStyleSheet("selection-background-color: rgb(100, 41, 215);")
            self.Relay_Table.setInputMethodHints(QtCore.Qt.ImhNone)
            self.Relay_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.Relay_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.Relay_Table.setDragEnabled(False)
            self.Relay_Table.setDragDropOverwriteMode(False)
            self.Relay_Table.setAlternatingRowColors(True)
            self.Relay_Table.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
            self.Relay_Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.Relay_Table.setGridStyle(QtCore.Qt.SolidLine)
            self.Relay_Table.setCornerButtonEnabled(False)
            self.Relay_Table.setObjectName("Relay_Table")
            self.Relay_Table.setColumnCount(6)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Relay_Table.setVerticalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.Relay_Table.setVerticalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            self.Relay_Table.setHorizontalHeaderItem(5, item)
            self.Relay_Table.horizontalHeader().setCascadingSectionResizes(True)
            self.Relay_Table.horizontalHeader().setDefaultSectionSize(133)
            self.Relay_Table.horizontalHeader().setMinimumSectionSize(70)
            self.Relay_Table.horizontalHeader().setStretchLastSection(True)
            self.Relay_Table.verticalHeader().setVisible(False)
            self.Relay_Table.verticalHeader().setDefaultSectionSize(30)
            self.Relay_Table.verticalHeader().setHighlightSections(False)
            self.Relay_Table.verticalHeader().setMinimumSectionSize(25)
            self.Relay_Table.verticalHeader().setSortIndicatorShown(True)
            self.Relay_Table.verticalHeader().setStretchLastSection(False)
            self.Node_Frame = QtWidgets.QFrame(self.Relay_Info_frame)
            self.Node_Frame.setGeometry(QtCore.QRect(0, 250, 801, 41))
            self.Node_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Node_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Node_Frame.setObjectName("Node_Frame")
            self.Guard_Node = QtWidgets.QLabel(self.Node_Frame)
            self.Guard_Node.setGeometry(QtCore.QRect(90, 12, 91, 17))
            self.Guard_Node.setObjectName("Guard_Node")
            self.End_Node = QtWidgets.QLabel(self.Node_Frame)
            self.End_Node.setGeometry(QtCore.QRect(630, 12, 81, 17))
            self.End_Node.setObjectName("End_Node")
            self.Middle_Node = QtWidgets.QLabel(self.Node_Frame)
            self.Middle_Node.setGeometry(QtCore.QRect(360, 12, 101, 17))
            self.Middle_Node.setObjectName("Middle_Node")
            self.Guard_Info = QtWidgets.QListWidget(self.Relay_Info_frame)
            self.Guard_Info.setGeometry(QtCore.QRect(0, 290, 261, 251))
            self.Guard_Info.setObjectName("Guard_Info")
            self.Guard_Info.setSpacing(6)
            self.Middle_Info = QtWidgets.QListWidget(self.Relay_Info_frame)
            self.Middle_Info.setGeometry(QtCore.QRect(270, 290, 261, 251))
            self.Middle_Info.setObjectName("Middle_Info")
            self.Middle_Info.setSpacing(6)
            self.End_Info = QtWidgets.QListWidget(self.Relay_Info_frame)
            self.End_Info.setGeometry(QtCore.QRect(540, 290, 261, 251))
            self.End_Info.setObjectName("End_Info")
            self.End_Info.setSpacing(6)
            self.Main_Tabs.addTab(self.Relay_Info, "")

            self.Guard_Node.hide()
            self.Guard_Info.hide()
            self.End_Info.hide()
            self.End_Node.hide()
            self.Middle_Info.setGeometry(QtCore.QRect(0, 300, 801, 241))
            self.Middle_Node.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Relay Info</span></p></body></html>")

            self.io = Relay_Info._Relay_Info(self)
            self.RI_timer = QtCore.QTimer()
            self.RI_timer.timeout.connect(self.io._Inbound_Outbound)
            self.RI_timer.start(2000)

            def _Node_Details(fingerprint):
                import sqlite3
                import pkg_resources
                router_status_entry = self.controller.get_network_status(fingerprint, None)
                Fingerprint = 'Fingerprint : ' + fingerprint
                DB_FILE = pkg_resources.resource_filename("TrackTor", "Consensus.db")
                conn = sqlite3.connect(DB_FILE)

                c = conn.cursor()
                address = c.execute('SELECT address FROM Relay_Info WHERE fingerprint=?', (fingerprint,)).fetchone()
                if address:
                    Address = 'Address : ' + str(address[0])
                    locale = self.controller.get_info('ip-to-country/%s' %address , None)
                    if locale != '??':
                        locale1 = pycountry.countries.get(alpha_2 = str.upper(locale))
                        Locale = 'Locale : ' + locale1.name
                    else:
                        Locale = 'Locale : ' + 'NA'
                else:
                    #address[0] = 'NA'
                    Address = 'Address : ' + 'NA'
                    Locale = 'Locale : ' + 'NA'

                DirPort = 'DirPort : ' + str(router_status_entry.dir_port)
                OrPort = 'OrPort : ' + str(router_status_entry.or_port)
                NickName = 'NickName : ' + str(router_status_entry.nickname)
                Published = 'Published : ' + str(router_status_entry.published.strftime("%H:%M %m/%d/%Y"))
                Flags = 'Flags : ' + str(router_status_entry.flags)
                All_Details = [Address, Locale, Fingerprint, NickName, OrPort, DirPort, Published, Flags]
                return All_Details

            def _Show_Node_Details(fingerprint, Type, Node_Type):

                if(Type == 'Circuit'):
                    All_Details = _Node_Details(fingerprint)
                    if (Node_Type == 'Guard'):
                        self.Guard_Info.clear()
                        for i in All_Details:
                            item = QtWidgets.QListWidgetItem(i)
                            self.Guard_Info.addItem(item)
                    elif (Node_Type == 'Middle'):
                        self.Middle_Info.clear()
                        for i in All_Details:
                            item = QtWidgets.QListWidgetItem(i)
                            self.Middle_Info.addItem(item)
                    elif (Node_Type == 'End'):
                        self.End_Info.clear()
                        for i in All_Details:
                            item = QtWidgets.QListWidgetItem(i)
                            self.End_Info.addItem(item)
                            #item1 = QtWidgets.QListWidgetItem(' ')
                            #self.End_Info.addItem(item1)
                elif (Type == 'OHT_Circuit'):
                    if (Node_Type == 'Guard'):
                        self.Guard_Info.clear()
                    elif (Node_Type == 'Middle'):
                        self.Middle_Info.clear()
                    elif(Node_Type == 'End'):
                        self.End_Info.clear()
                        All_Details = _Node_Details(fingerprint)
                        for i in All_Details:
                            item = QtWidgets.QListWidgetItem(i)
                            self.End_Info.addItem(item)

                else:
                    self.Middle_Info.clear()
                    if (fingerprint == None):
                        item = QtWidgets.QListWidgetItem('Address : ' + self.Display_Address)
                        self.Middle_Info.addItem(item)
                        item = QtWidgets.QListWidgetItem('No Consensus Data Found!')
                        self.Middle_Info.addItem(item)
                    else:
                        All_Details = _Node_Details(fingerprint)
                        for i in All_Details:
                            item = QtWidgets.QListWidgetItem(i)
                            self.Middle_Info.addItem(item)

            def _Display_Fingerprint():
                if (not self.controller.is_alive()):
                    item = QtWidgets.QListWidgetItem('Unable to connect to Tor! Hence can not retrieve data!')
                    self.Middle_Info.addItem(item)
                else:
                    self.Display_Address = self.Relay_Table.selectedItems()[2].text()
                    self.Type = self.Relay_Table.selectedItems()[5].text()
                    if (self.Type == 'Circuit'):
                        self.Guard_Node.show()
                        self.Guard_Info.show()
                        self.End_Info.show()
                        self.End_Node.show()
                        self.Middle_Info.setGeometry(QtCore.QRect(270, 290, 261, 251))
                        self.Middle_Node.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Middle Info</span></p></body></html>")
                        _Show_Node_Details(Relay_Info.Node_Info[self.Display_Address][0], self.Type, 'Guard')
                        _Show_Node_Details(Relay_Info.Node_Info[self.Display_Address][1], self.Type, 'Middle')
                        _Show_Node_Details(Relay_Info.Node_Info[self.Display_Address][2], self.Type, 'End')
                    else:
                        self.Guard_Node.hide()
                        self.Guard_Info.hide()
                        self.End_Info.hide()
                        self.End_Node.hide()
                        self.Middle_Info.setGeometry(QtCore.QRect(0, 300, 801, 241))
                        self.Middle_Node.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Relay Info</span></p></body></html>")
                        self.Display_Fingerprint = None
                        if (self.Display_Address.split(':')[0] == self.controller.get_info('address',None)):
                            self.Display_Fingerprint = self.controller.get_info('fingerprint',None)
                        _Show_Node_Details(self.Display_Fingerprint, self.Type, None)

            self.Relay_Table.itemSelectionChanged.connect(_Display_Fingerprint)

        def _Resources(self):
            #Resources Tab
            self.Resources = QtWidgets.QWidget()
            self.Resources.setMinimumSize(QtCore.QSize(825, 575))
            self.Resources.setMaximumSize(QtCore.QSize(825, 575))
            self.Resources.setObjectName("Resources")
            self.Resources_Frame = QtWidgets.QFrame(self.Resources)
            self.Resources_Frame.setGeometry(QtCore.QRect(10, 10, 801, 531))
            self.Resources_Frame.setStyleSheet("background-color:None\n""")
            self.Resources_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Resources_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Resources_Frame.setObjectName("Resources_Frame")

            #Memory Graph
            self.Memory = PlotWidget(self.Resources_Frame)
            self.Memory.setGeometry(QtCore.QRect(410, 70, 391, 271))
            self.Memory.setObjectName("Memory")
            self.memory_curve = self.Memory.plot(Graphs.outbound_x, Graphs.outbound_y, pen=(255,0,0))

            #Class for Resources
            self.res = Graphs.Resources(self)
            #Qtimer
            self.memory_timer = QtCore.QTimer()
            self.memory_timer.timeout.connect(self.res.Memory)
            self.memory_timer.start(2000)

            #CPU Graph
            self.CPU = PlotWidget(self.Resources_Frame)
            self.CPU.setGeometry(QtCore.QRect(0, 70, 391, 271))
            self.CPU.setObjectName("CPU")
            self.cpu_curve = self.CPU.plot(Graphs.outbound_x, Graphs.outbound_y, pen=(255,0,0))

            #Qtimer
            self.cpu_timer = QtCore.QTimer()
            self.cpu_timer.timeout.connect(self.res.CPU)
            self.cpu_timer.start(2000)

            #CPU Text Frame
            self.CPU_Frame = QtWidgets.QFrame(self.Resources_Frame)
            self.CPU_Frame.setGeometry(QtCore.QRect(0, 10, 391, 42))
            self.CPU_Frame.setStyleSheet("background-color:white")
            self.CPU_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.CPU_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.CPU_Frame.setObjectName("CPU_Frame")
            self.gridLayout_8 = QtWidgets.QGridLayout(self.CPU_Frame)
            self.gridLayout_8.setObjectName("gridLayout_8")

            #CPU Usage Text
            self.CPU_Usage = QtWidgets.QLabel(self.CPU_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.CPU_Usage.sizePolicy().hasHeightForWidth())
            self.CPU_Usage.setSizePolicy(sizePolicy)
            self.CPU_Usage.setObjectName("CPU_Usage")
            self.gridLayout_8.addWidget(self.CPU_Usage, 0, 0, 1, 1)

            #Value CPU Usage by TrackTor
            self.CPU_Tracktor = QtWidgets.QLabel(self.CPU_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.CPU_Tracktor.sizePolicy().hasHeightForWidth())
            self.CPU_Tracktor.setSizePolicy(sizePolicy)
            self.CPU_Tracktor.setObjectName("CPU_Tracktor")
            self.CPU_Tracktor.setFont(self.font)
            self.gridLayout_8.addWidget(self.CPU_Tracktor, 0, 3, 1, 1)

            #Value CPU Usage by Tor
            self.CPU_Tor = QtWidgets.QLabel(self.CPU_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.CPU_Tor.sizePolicy().hasHeightForWidth())
            self.CPU_Tor.setSizePolicy(sizePolicy)
            self.CPU_Tor.setObjectName("CPU_Tor")
            self.CPU_Tor.setFont(self.font)
            self.gridLayout_8.addWidget(self.CPU_Tor, 0, 1, 1, 1)

            #Text CPU Usage by Tor
            self.Tor_Percent = QtWidgets.QLabel(self.CPU_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Tor_Percent.sizePolicy().hasHeightForWidth())
            self.Tor_Percent.setSizePolicy(sizePolicy)
            self.Tor_Percent.setObjectName("Tor_Percent")
            self.gridLayout_8.addWidget(self.Tor_Percent, 0, 2, 1, 1)

            #Text CPU Usage by TrackTor
            self.TrackTor_Percent = QtWidgets.QLabel(self.CPU_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.TrackTor_Percent.sizePolicy().hasHeightForWidth())
            self.TrackTor_Percent.setSizePolicy(sizePolicy)
            self.TrackTor_Percent.setObjectName("TrackTor_Percent")
            self.gridLayout_8.addWidget(self.TrackTor_Percent, 0, 4, 1, 1)

            #Memory Text
            self.RAM_Frame = QtWidgets.QFrame(self.Resources_Frame)
            self.RAM_Frame.setGeometry(QtCore.QRect(410, 10, 391, 42))
            self.RAM_Frame.setStyleSheet("background-color:white")
            self.RAM_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.RAM_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.RAM_Frame.setObjectName("RAM_Frame")
            self.gridLayout_9 = QtWidgets.QGridLayout(self.RAM_Frame)
            self.gridLayout_9.setObjectName("gridLayout_9")

            #Text RAM_Usage
            self.RAM_Usage = QtWidgets.QLabel(self.RAM_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.RAM_Usage.sizePolicy().hasHeightForWidth())
            self.RAM_Usage.setSizePolicy(sizePolicy)
            self.RAM_Usage.setObjectName("RAM_Usage")
            self.gridLayout_9.addWidget(self.RAM_Usage, 0, 0, 1, 1)

            #RAM Usage by TrackTor Value
            self.RAM_Tracktor = QtWidgets.QLabel(self.RAM_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.RAM_Tracktor.sizePolicy().hasHeightForWidth())
            self.RAM_Tracktor.setSizePolicy(sizePolicy)
            self.RAM_Tracktor.setObjectName("RAM_Tracktor")
            self.RAM_Tracktor.setFont(self.font)
            self.gridLayout_9.addWidget(self.RAM_Tracktor, 0, 3, 1, 1)

            #RAM Usage by Tor Value
            self.RAM_Tor = QtWidgets.QLabel(self.RAM_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.RAM_Tor.sizePolicy().hasHeightForWidth())
            self.RAM_Tor.setSizePolicy(sizePolicy)
            self.RAM_Tor.setObjectName("RAM_Tor")
            self.RAM_Tor.setFont(self.font)
            self.gridLayout_9.addWidget(self.RAM_Tor, 0, 1, 1, 1)

            #Text RAM Usage by Tor
            self.Tor_Percent1 = QtWidgets.QLabel(self.RAM_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Tor_Percent1.sizePolicy().hasHeightForWidth())
            self.Tor_Percent1.setSizePolicy(sizePolicy)
            self.Tor_Percent1.setObjectName("Tor_Percent1")
            self.gridLayout_9.addWidget(self.Tor_Percent1, 0, 2, 1, 1)

            #Text RAM Usage by Tracktor
            self.TrackTor_Percent1 = QtWidgets.QLabel(self.RAM_Frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.TrackTor_Percent1.sizePolicy().hasHeightForWidth())
            self.TrackTor_Percent1.setSizePolicy(sizePolicy)
            self.TrackTor_Percent1.setObjectName("TrackTor_Percent1")
            self.gridLayout_9.addWidget(self.TrackTor_Percent1, 0, 4, 1, 1)

            #Resources Additional
            self.Resources_Tor = QtWidgets.QListWidget(self.Resources_Frame)
            self.Resources_Tor.setGeometry(QtCore.QRect(410, 360, 391, 171))
            self.Resources_Tor.setObjectName("Resources_Tor")
            self.Resources_Tracktor = QtWidgets.QListWidget(self.Resources_Frame)
            self.Resources_Tracktor.setGeometry(QtCore.QRect(0, 360, 391, 171))
            self.Resources_Tracktor.setObjectName("Resources_Tracktor")

            self.Resources_Tracktor1 = QtWidgets.QLabel(self.Resources_Frame)
            self.Resources_Tracktor1.setGeometry(QtCore.QRect(130, 360, 111, 21))
            self.Resources_Tracktor1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Resources_Tracktor1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Resources_Tracktor1.setObjectName("Resources_Tracktor1")
            self.Resources_Tor1 = QtWidgets.QLabel(self.Resources_Frame)
            self.Resources_Tor1.setGeometry(QtCore.QRect(560, 360, 111, 21))
            self.Resources_Tor1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Resources_Tor1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Resources_Tor1.setObjectName("Resources_Tor1")

            from TrackTor.Utilities import Resources
            self.rs = Resources._Resources(self)
            self.resource_timer = QtCore.QTimer()
            self.resource_timer.timeout.connect(self.rs.Resources_Stats)
            self.resource_timer.start(1000)

            self.Main_Tabs.addTab(self.Resources, "")

        def _Logs(self):

            self.Logs = QtWidgets.QWidget()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Logs.sizePolicy().hasHeightForWidth())
            self.Logs.setSizePolicy(sizePolicy)
            self.Logs.setMinimumSize(QtCore.QSize(821, 565))
            self.Logs.setMaximumSize(QtCore.QSize(821, 565))
            self.Logs.setObjectName("Logs")
            self.Log_Frame1 = QtWidgets.QFrame(self.Logs)
            self.Log_Frame1.setGeometry(QtCore.QRect(10, 10, 801, 71))
            self.Log_Frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Log_Frame1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Log_Frame1.setObjectName("Log_Frame1")
            self.Event_Type = QtWidgets.QLabel(self.Log_Frame1)
            self.Event_Type.setGeometry(QtCore.QRect(340, 0, 111, 21))
            self.Event_Type.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Event_Type.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Event_Type.setObjectName("Event_Type")
            self.Description = QtWidgets.QLabel(self.Log_Frame1)
            self.Description.setGeometry(QtCore.QRect(10, 30, 781, 31))
            self.Description.setObjectName("Description")
            self.Log_Frame2 = QtWidgets.QFrame(self.Logs)
            self.Log_Frame2.setGeometry(QtCore.QRect(10, 90, 801, 41))
            self.Log_Frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Log_Frame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Log_Frame2.setObjectName("Log_Frame2")
            self.Run_Level = QtWidgets.QLabel(self.Log_Frame2)
            self.Run_Level.setGeometry(QtCore.QRect(20, 10, 91, 17))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.Run_Level.setFont(font)
            self.Run_Level.setObjectName("Run_Level")
            self.DEBUG = QtWidgets.QCheckBox(self.Log_Frame2)
            self.DEBUG.setGeometry(QtCore.QRect(140, 8, 71, 23))
            self.DEBUG.setObjectName("DEBUG")
            self.INFO = QtWidgets.QCheckBox(self.Log_Frame2)
            self.INFO.setGeometry(QtCore.QRect(240, 8, 61, 23))
            self.INFO.setObjectName("INFO")
            self.NOTICE = QtWidgets.QCheckBox(self.Log_Frame2)
            self.NOTICE.setGeometry(QtCore.QRect(320, 8, 71, 23))
            self.NOTICE.setObjectName("NOTICE")
            self.WARN = QtWidgets.QCheckBox(self.Log_Frame2)
            self.WARN.setGeometry(QtCore.QRect(420, 8, 71, 23))
            self.WARN.setObjectName("WARN")
            self.ERR = QtWidgets.QCheckBox(self.Log_Frame2)
            self.ERR.setGeometry(QtCore.QRect(510, 8, 51, 23))
            self.ERR.setObjectName("ERR")
            self.Log_Frame3 = QtWidgets.QFrame(self.Logs)
            self.Log_Frame3.setGeometry(QtCore.QRect(10, 140, 801, 221))
            self.Log_Frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Log_Frame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Log_Frame3.setObjectName("Log_Frame3")
            self.CIRC = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CIRC.setGeometry(QtCore.QRect(10, 70, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CIRC.setFont(font)
            self.CIRC.setObjectName("CIRC")
            self.ORCONN = QtWidgets.QCheckBox(self.Log_Frame3)
            self.ORCONN.setGeometry(QtCore.QRect(10, 130, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.ORCONN.setFont(font)
            self.ORCONN.setObjectName("ORCONN")
            self.ADDRMAP = QtWidgets.QCheckBox(self.Log_Frame3)
            self.ADDRMAP.setGeometry(QtCore.QRect(10, 10, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.ADDRMAP.setFont(font)
            self.ADDRMAP.setObjectName("ADDRMAP")
            self.STATUS_GENERAL = QtWidgets.QCheckBox(self.Log_Frame3)
            self.STATUS_GENERAL.setGeometry(QtCore.QRect(560, 10, 151, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.STATUS_GENERAL.setFont(font)
            self.STATUS_GENERAL.setObjectName("STATUS_GENERAL")
            self.GUARD = QtWidgets.QCheckBox(self.Log_Frame3)
            self.GUARD.setGeometry(QtCore.QRect(200, 130, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.GUARD.setFont(font)
            self.GUARD.setObjectName("GUARD")
            self.CIRC_MINOR = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CIRC_MINOR.setGeometry(QtCore.QRect(10, 190, 111, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CIRC_MINOR.setFont(font)
            self.CIRC_MINOR.setObjectName("CIRC_MINOR")
            self.BW = QtWidgets.QCheckBox(self.Log_Frame3)
            self.BW.setGeometry(QtCore.QRect(390, 130, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.BW.setFont(font)
            self.BW.setObjectName("BW")
            self.DESCCHANGED = QtWidgets.QCheckBox(self.Log_Frame3)
            self.DESCCHANGED.setGeometry(QtCore.QRect(200, 100, 131, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.DESCCHANGED.setFont(font)
            self.DESCCHANGED.setObjectName("DESCCHANGED")
            self.CIRC_BW = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CIRC_BW.setGeometry(QtCore.QRect(10, 160, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CIRC_BW.setFont(font)
            self.CIRC_BW.setObjectName("CIRC_BW")
            self.CONN_BW = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CONN_BW.setGeometry(QtCore.QRect(200, 70, 151, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CONN_BW.setFont(font)
            self.CONN_BW.setObjectName("CONN_BW")
            self.STREAM = QtWidgets.QCheckBox(self.Log_Frame3)
            self.STREAM.setGeometry(QtCore.QRect(560, 70, 141, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.STREAM.setFont(font)
            self.STREAM.setObjectName("STREAM")
            self.NS = QtWidgets.QCheckBox(self.Log_Frame3)
            self.NS.setGeometry(QtCore.QRect(390, 100, 141, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.NS.setFont(font)
            self.NS.setObjectName("NS")
            self.HS_DESC_CONTENT = QtWidgets.QCheckBox(self.Log_Frame3)
            self.HS_DESC_CONTENT.setGeometry(QtCore.QRect(200, 190, 161, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.HS_DESC_CONTENT.setFont(font)
            self.HS_DESC_CONTENT.setObjectName("HS_DESC_CONTENT")
            self.STREAM_BW = QtWidgets.QCheckBox(self.Log_Frame3)
            self.STREAM_BW.setGeometry(QtCore.QRect(560, 100, 111, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.STREAM_BW.setFont(font)
            self.STREAM_BW.setObjectName("STREAM_BW")
            self.CONF_CHANGED = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CONF_CHANGED.setGeometry(QtCore.QRect(200, 40, 141, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CONF_CHANGED.setFont(font)
            self.CONF_CHANGED.setObjectName("CONF_CHANGED")
            self.STATUS_SERVER = QtWidgets.QCheckBox(self.Log_Frame3)
            self.STATUS_SERVER.setGeometry(QtCore.QRect(560, 40, 141, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.STATUS_SERVER.setFont(font)
            self.STATUS_SERVER.setObjectName("STATUS_SERVER")
            self.STATUS_CLIENT = QtWidgets.QCheckBox(self.Log_Frame3)
            self.STATUS_CLIENT.setGeometry(QtCore.QRect(390, 190, 131, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.STATUS_CLIENT.setFont(font)
            self.STATUS_CLIENT.setObjectName("STATUS_CLIENT")
            self.CLIENTS_SEEN = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CLIENTS_SEEN.setGeometry(QtCore.QRect(200, 10, 121, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CLIENTS_SEEN.setFont(font)
            self.CLIENTS_SEEN.setObjectName("CLIENTS_SEEN")
            self.NEWDESC = QtWidgets.QCheckBox(self.Log_Frame3)
            self.NEWDESC.setGeometry(QtCore.QRect(390, 70, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.NEWDESC.setFont(font)
            self.NEWDESC.setObjectName("NEWDESC")
            self.HS_DESC = QtWidgets.QCheckBox(self.Log_Frame3)
            self.HS_DESC.setGeometry(QtCore.QRect(200, 160, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.HS_DESC.setFont(font)
            self.HS_DESC.setObjectName("HS_DESC")
            self.TRANSPORT_LAUNCHED = QtWidgets.QCheckBox(self.Log_Frame3)
            self.TRANSPORT_LAUNCHED.setGeometry(QtCore.QRect(560, 130, 201, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.TRANSPORT_LAUNCHED.setFont(font)
            self.TRANSPORT_LAUNCHED.setObjectName("TRANSPORT_LAUNCHED")
            self.SIGNAL = QtWidgets.QCheckBox(self.Log_Frame3)
            self.SIGNAL.setGeometry(QtCore.QRect(390, 160, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.SIGNAL.setFont(font)
            self.SIGNAL.setObjectName("SIGNAL")
            self.CELL_STATS = QtWidgets.QCheckBox(self.Log_Frame3)
            self.CELL_STATS.setGeometry(QtCore.QRect(10, 100, 92, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.CELL_STATS.setFont(font)
            self.CELL_STATS.setObjectName("CELL_STATS")
            self.BUILDTIMEOUT_SET = QtWidgets.QCheckBox(self.Log_Frame3)
            self.BUILDTIMEOUT_SET.setGeometry(QtCore.QRect(10, 40, 171, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.BUILDTIMEOUT_SET.setFont(font)
            self.BUILDTIMEOUT_SET.setObjectName("BUILDTIMEOUT_SET")
            self.NETWORK_LIVENESS = QtWidgets.QCheckBox(self.Log_Frame3)
            self.NETWORK_LIVENESS.setGeometry(QtCore.QRect(390, 10, 161, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.NETWORK_LIVENESS.setFont(font)
            self.NETWORK_LIVENESS.setObjectName("NETWORK_LIVENESS")
            self.NEWCONSENSUS = QtWidgets.QCheckBox(self.Log_Frame3)
            self.NEWCONSENSUS.setGeometry(QtCore.QRect(390, 40, 141, 23))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.NEWCONSENSUS.setFont(font)
            self.NEWCONSENSUS.setObjectName("NEWCONSENSUS")

            self.Logs_Info = QtWidgets.QListWidget(self.Logs)
            self.Logs_Info.setGeometry(QtCore.QRect(10, 370, 801, 181))
            self.Logs_Info.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.Logs_Info.setWordWrap(True)
            self.Logs_Info.setSelectionRectVisible(True)
            self.Logs_Info.setObjectName("Logs_Info")
            self.Logs_Info.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
            self.Logs_Info.show()

            self.lg = Logs._Logs(self)
            self.sl = Save_Logs._Save_Logs()

            self.DESELECT = QtWidgets.QPushButton(self.Log_Frame3)
            self.DESELECT.setGeometry(QtCore.QRect(600, 190, 89, 25))
            self.DESELECT.setObjectName("DESELECT")
            self.DESELECT.setText("Deselect")
            self.DESELECT.raise_()
            self.DESELECT.clicked.connect(self.lg._Deselect)
            self.DESELECT.clicked['bool'].connect(self.DESELECT.lower)

            self.SELECT_ALL = QtWidgets.QPushButton(self.Log_Frame3)
            self.SELECT_ALL.setGeometry(QtCore.QRect(600, 190, 89, 25))
            self.SELECT_ALL.setObjectName("SELECT_ALL")
            self.SELECT_ALL.setText("Select All")
            self.SELECT_ALL.raise_()
            self.SELECT_ALL.clicked.connect(self.lg._Select_All)
            self.SELECT_ALL.clicked['bool'].connect(self.SELECT_ALL.lower)

            self.OK = QtWidgets.QPushButton(self.Log_Frame3)
            self.OK.setGeometry(QtCore.QRect(700, 190, 89, 25))
            self.OK.setObjectName("OK")
            self.OK.clicked.connect(self.lg._Ok_Button)

            self.Save_Logs = QtWidgets.QPushButton(self.Logs)
            self.Save_Logs.setGeometry(QtCore.QRect(745, 375, 60, 25))
            self.Save_Logs.setObjectName("Save_Logs")
            self.Save_Logs.clicked.connect(self.sl.saveFileDialog)


            self.Description.setText("Check any of the options to see the corresponding Logs.")
            self.DEBUG.stateChanged.connect(self.lg._DEBUG_Desc)
            self.INFO.stateChanged.connect(self.lg._INFO_Desc)
            self.NOTICE.stateChanged.connect(self.lg._NOTICE_Desc)
            self.WARN.stateChanged.connect(self.lg._WARN_Desc)
            self.ERR.stateChanged.connect(self.lg._ERR_Desc)
            self.CIRC.stateChanged.connect(self.lg._CIRC_Desc)
            self.ORCONN.stateChanged.connect(self.lg._ORCONN_Desc)
            self.ADDRMAP.stateChanged.connect(self.lg._ADDRMAP_Desc)
            self.STATUS_GENERAL.stateChanged.connect(self.lg._STATUS_GENERAL_Desc)
            self.GUARD.stateChanged.connect(self.lg._GUARD_Desc)
            self.CIRC_MINOR.stateChanged.connect(self.lg._CIRC_MINOR_Desc)
            self.BW.stateChanged.connect(self.lg._BW_Desc)
            self.NEWCONSENSUS.stateChanged.connect(self.lg._NEWCONSENSUS_Desc)
            self.DESCCHANGED.stateChanged.connect(self.lg._DESCCHANGED_Desc)
            self.CIRC_BW.stateChanged.connect(self.lg._CIRC_BW_Desc)
            self.CONN_BW.stateChanged.connect(self.lg._CONN_BW_Desc)
            self.STREAM.stateChanged.connect(self.lg._STREAM_Desc)
            self.NS.stateChanged.connect(self.lg._NS_Desc)
            self.HS_DESC_CONTENT.stateChanged.connect(self.lg._HS_DESC_CONTENT_Desc)
            self.STREAM_BW.stateChanged.connect(self.lg._STREAM_BW_Desc)
            self.CONF_CHANGED.stateChanged.connect(self.lg._CONF_CHANGED_Desc)
            self.STATUS_SERVER.stateChanged.connect(self.lg._STATUS_SERVER_Desc)
            self.STATUS_CLIENT.stateChanged.connect(self.lg._STATUS_CLIENT_Desc)
            self.CLIENTS_SEEN.stateChanged.connect(self.lg._CLIENTS_SEEN_Desc)
            self.NEWDESC.stateChanged.connect(self.lg._NEWDESC_Desc)
            self.HS_DESC.stateChanged.connect(self.lg._HS_DESC_Desc)
            self.TRANSPORT_LAUNCHED.stateChanged.connect(self.lg._TRANSPORT_LAUNCHED_Desc)
            self.SIGNAL.stateChanged.connect(self.lg._SIGNAL_Desc)
            self.CELL_STATS.stateChanged.connect(self.lg._CELL_STATS_Desc)
            self.BUILDTIMEOUT_SET.stateChanged.connect(self.lg._BUILDTIMEOUT_SET_Desc)
            self.NETWORK_LIVENESS.stateChanged.connect(self.lg._NETWORK_LIVENESS_Desc)

            self.Main_Tabs.addTab(self.Logs, "")

        def _About(self):
            #About Tab
            self.About = QtWidgets.QWidget()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.About.sizePolicy().hasHeightForWidth())
            self.About.setSizePolicy(sizePolicy)
            self.About.setMinimumSize(QtCore.QSize(825, 575))
            self.About.setMaximumSize(QtCore.QSize(825, 575))
            self.About.setObjectName("About")
            self.About_Image = QtWidgets.QLabel(self.About)
            self.About_Image.setGeometry(QtCore.QRect(0, -50, 821, 601))
            self.About_Image.setText("")
            self.About_Image.setPixmap(QtGui.QPixmap(":/Splashscreen/Images/Splashscreen.png"))
            self.About_Image.setScaledContents(True)
            self.About_Image.setObjectName("About_Image")
            self.About_Info = QtWidgets.QLabel(self.About)
            self.About_Info.setGeometry(QtCore.QRect(40, 220, 741, 121))
            font = QtGui.QFont()
            font.setPointSize(11)
            self.About_Info.setFont(font)
            self.About_Info.setAlignment(QtCore.Qt.AlignCenter)
            self.About_Info.setWordWrap(True)
            self.About_Info.setObjectName("About_Info")
            self.Main_Tabs.addTab(self.About, "")
            self.gridLayout.addWidget(self.Main_Tabs, 1, 0, 1, 1)
