"""
**Module Overview:**

This module will implement the funtionality of showing Logs

|- _Logs
    - __init__: This function will initialize UI object and other class variables in all files
    - print_event: This function will print the event
    - listen_for_events: This function will the listen
    - _Select_All: This function will select all the events
    - _Deselect: This function will deselect all the events
    - _Ok_Button: This function will implement the funtionality of ok button
    - _DEBUG_Desc: This function will implement the funtionality of debug event
    - _INFO_Desc: This function will implement the funtionality of info event
    - _NOTICE_Desc: This function will implement the funtionality of notice event
    - _WARN_Desc: This function will implement the funtionality of warn event
    - _ERR_Desc: This function will implement the funtionality of err event
    - _CIRC_Desc: This function will implement the funtionality of circ event
    - _ORCONN_Desc: This function will implement the funtionality of orconn event
    - _ADDRMAP_Desc: This function will implement the funtionality of addrmap event
    - _STATUS_GENERAL_Desc: This function will implement the funtionality of status general event
    - _GUARD_Desc: This function will implement the funtionality of guard event
    - _CIRC_MINOR_Desc: This function will implement the funtionality of circ minor event
    - _BW_Desc: This function will implement the funtionality of bw event
    - _NEWCONSENSUS_Desc: This function will implement the funtionality of new Newconsensus event
    - _DESCCHANGED_Desc: This function will implement the funtionality of descchanged event
    - _CIRC_BW_Desc: This function will implement the funtionality of circ bw desc event
    - _CONN_BW_Desc: This function will implement the funtionality of conn bw desc event
    - _STREAM_Desc: This function will implement the funtionality of stream desc event
    - _NS_Desc: This function will implement the funtionality of ns desc event
    - _HS_DESC_CONTENT_Desc: This function will implement the funtionality of hs desc event
    - _STREAM_BW_Desc: This function will implement the funtionality of stream bw desc event
    - _CONF_CHANGED_Desc: This function will implement the funtionality of conf changed desc event
    - _STATUS_SERVER_Desc: This function will implement the funtionality of status server desc event
    - _STATUS_CLIENT_Desc: This function will implement the funtionality of status client desc event
    - _CLIENTS_SEEN_Desc: This function will implement the funtionality of clients seen desc  event
    - _NEWDESC_Desc: This function will implement the funtionality of newdesc desc event
    - _HS_DESC_Desc: This function will implement the funtionality of hs desc event
    - _TRANSPORT_LAUNCHED_Desc: This function will implement the funtionality of transport launched event
    - _SIGNAL_Desc: This function will implement the funtionality of signal desc event
    - _CELL_STATS_Desc: This function will implement the funtionality of cell stats desc event
    - _BUILDTIMEOUT_SET_Desc: This function will implement the funtionality of buildtimeout set desc event
    - _NETWORK_LIVENESS_Desc: This function will implement the funtionality of network liveness desc event

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from stem.control import Controller, EventType
from stem.util import enum
import stem
import threading
from TrackTor.Utilities import StaticInfo

LogsArray = []
#controller = StaticInfo.controller
controller = Controller.from_port(port = int(StaticInfo.control_port))
controller.authenticate()
tor_events = []
Event_Data = ''

class _Logs():

    def __init__(self, ui):
        self.ui = ui

    def print_event(self, event):
        time.sleep(2)
        global Event_Data
        global LogsArray
        Uptime = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
        LogsArray.append((Uptime, str(event)))
        Event_Data = time.strftime("%H:%M:%S", time.localtime()) + ' | ' + str(event)
        item = QtWidgets.QListWidgetItem(Event_Data)
        self.ui.Logs_Info.addItem(item)
        count = self.ui.Logs_Info.count()
        if count > 25:
            self.ui.Logs_Info.takeItem(self.ui.Logs_Info.row(self.ui.Logs_Info.item(0)))
        '''if count != 1:
            self.ui.Logs_Info.item(count-2).setSelected(False)
        self.ui.Logs_Info.item(count-1).setSelected(True)
        self.ui.Logs_Info.scrollToBottom()'''

    def listen_for_events(self,listener, events):
        global tor_events
        controller.remove_event_listener(listener)
        for event_type in list(tor_events):
            try:
                controller.add_event_listener(listener, event_type)
            except stem.ProtocolError:
                stem.util.log.warn("%s isn't an event tor supports" % event_type)
                tor_events.remove(event_type)

    def _Select_All(self):
        self.ui.ADDRMAP.setChecked(True)
        self.ui.BUILDTIMEOUT_SET.setChecked(True)
        self.ui.BW.setChecked(True)
        self.ui.CELL_STATS.setChecked(True)
        self.ui.CIRC.setChecked(True)
        self.ui.CIRC_BW.setChecked(True)
        self.ui.CIRC_MINOR.setChecked(True)
        self.ui.CLIENTS_SEEN.setChecked(True)
        self.ui.CONF_CHANGED.setChecked(True)
        self.ui.CONN_BW.setChecked(True)
        self.ui.DESCCHANGED.setChecked(True)
        self.ui.GUARD.setChecked(True)
        self.ui.HS_DESC.setChecked(True)
        self.ui.HS_DESC_CONTENT.setChecked(True)
        self.ui.NETWORK_LIVENESS.setChecked(True)
        self.ui.NEWCONSENSUS.setChecked(True)
        self.ui.NEWDESC.setChecked(True)
        self.ui.NS.setChecked(True)
        self.ui.ORCONN.setChecked(True)
        self.ui.SIGNAL.setChecked(True)
        self.ui.STATUS_CLIENT.setChecked(True)
        self.ui.STATUS_GENERAL.setChecked(True)
        self.ui.STATUS_SERVER.setChecked(True)
        self.ui.STREAM.setChecked(True)
        self.ui.STREAM_BW.setChecked(True)
        self.ui.TRANSPORT_LAUNCHED.setChecked(True)

    def _Deselect(self):
        self.ui.ADDRMAP.setChecked(False)
        self.ui.BUILDTIMEOUT_SET.setChecked(False)
        self.ui.BW.setChecked(False)
        self.ui.CELL_STATS.setChecked(False)
        self.ui.CIRC.setChecked(False)
        self.ui.CIRC_BW.setChecked(False)
        self.ui.CIRC_MINOR.setChecked(False)
        self.ui.CLIENTS_SEEN.setChecked(False)
        self.ui.CONF_CHANGED.setChecked(False)
        self.ui.CONN_BW.setChecked(False)
        self.ui.DESCCHANGED.setChecked(False)
        self.ui.GUARD.setChecked(False)
        self.ui.HS_DESC.setChecked(False)
        self.ui.HS_DESC_CONTENT.setChecked(False)
        self.ui.NETWORK_LIVENESS.setChecked(False)
        self.ui.NEWCONSENSUS.setChecked(False)
        self.ui.NEWDESC.setChecked(False)
        self.ui.NS.setChecked(False)
        self.ui.ORCONN.setChecked(False)
        self.ui.SIGNAL.setChecked(False)
        self.ui.STATUS_CLIENT.setChecked(False)
        self.ui.STATUS_GENERAL.setChecked(False)
        self.ui.STATUS_SERVER.setChecked(False)
        self.ui.STREAM.setChecked(False)
        self.ui.STREAM_BW.setChecked(False)
        self.ui.TRANSPORT_LAUNCHED.setChecked(False)

    def _Ok_Button(self):

        self.ui.Description.setText("Logs of the selected options are shown below.")
        if not (StaticInfo.controller.is_alive()):
            global controller
            controller.close()
            item = QtWidgets.QListWidgetItem('Sorry! Unable to connect to Tor to collect Logs!')
            self.ui.Logs_Info.addItem(item)
            return
        else:
            controller.reconnect()
        global tor_events
        tor_events = []
        if self.ui.BW.isChecked():
            tor_events.append('BW')
        if self.ui.CIRC.isChecked():
            tor_events.append('CIRC')
        if self.ui.ADDRMAP.isChecked():
            tor_events.append('ADDRMAP')
        if self.ui.BUILDTIMEOUT_SET.isChecked():
            tor_events.append('BUILDTIMEOUT_SET')
        if self.ui.CELL_STATS.isChecked():
            tor_events.append('CELL_STATS')
        if self.ui.CIRC_BW.isChecked():
            tor_events.append('CIRC_BW')
        if self.ui.CIRC_MINOR.isChecked():
            tor_events.append('CIRC_MINOR')
        if self.ui.CLIENTS_SEEN.isChecked():
            tor_events.append('CLIENTS_SEEN')
        if self.ui.CONF_CHANGED.isChecked():
            tor_events.append('CONF_CHANGED')
        if self.ui.CONN_BW.isChecked():
            tor_events.append('CONN_BW')
        if self.ui.DEBUG.isChecked():
            tor_events.append('DEBUG')
        if self.ui.DESCCHANGED.isChecked():
            tor_events.append('DESCCHANGED')
        if self.ui.ERR.isChecked():
            tor_events.append('ERR')
        if self.ui.GUARD.isChecked():
            tor_events.append('GUARD')
        if self.ui.HS_DESC.isChecked():
            tor_events.append('HS_DESC')
        if self.ui.HS_DESC_CONTENT.isChecked():
            tor_events.append('HS_DESC_CONTENT')
        if self.ui.INFO.isChecked():
            tor_events.append('INFO')
        if self.ui.NETWORK_LIVENESS.isChecked():
            tor_events.append('NETWORK_LIVENESS')
        if self.ui.NEWCONSENSUS.isChecked():
            tor_events.append('NEWCONSENSUS')
        if self.ui.NEWDESC.isChecked():
            tor_events.append('NEWDESC')
        if self.ui.NOTICE.isChecked():
            tor_events.append('NOTICE')
        if self.ui.NS.isChecked():
            tor_events.append('NS')
        if self.ui.ORCONN.isChecked():
            tor_events.append('ORCONN')
        if self.ui.SIGNAL.isChecked():
            tor_events.append('SIGNAL')
        if self.ui.STREAM.isChecked():
            tor_events.append('STREAM')
        if self.ui.STATUS_CLIENT.isChecked():
            tor_events.append('STATUS_CLIENT')
        if self.ui.STATUS_GENERAL.isChecked():
            tor_events.append('STATUS_GENERAL')
        if self.ui.STATUS_SERVER.isChecked():
            tor_events.append('STATUS_SERVER')
        if self.ui.STREAM_BW.isChecked():
            tor_events.append('STREAM_BW')
        if self.ui.TRANSPORT_LAUNCHED.isChecked():
            tor_events.append('TRANSPORT_LAUNCHED')
        if self.ui.WARN.isChecked():
            tor_events.append('WARN')

        if not controller.is_alive():
            return
        self.listen_for_events(self.print_event,tor_events)

    def _DEBUG_Desc(self):
        self.ui.Description.setText('Tor logging event. These are the most visible kind of event.')

    def _INFO_Desc(self):
        self.ui.Description.setText('Tor logging event. These are the most visible kind of event.')

    def _NOTICE_Desc(self):
        self.ui.Description.setText('Tor logging event. These are the most visible kind of event.')

    def _WARN_Desc(self):
        self.ui.Description.setText('Tor logging event. These are the most visible kind of event.')

    def _ERR_Desc(self):
        self.ui.Description.setText('Tor logging event. These are the most visible kind of event.')

    def _CIRC_Desc(self):
        self.ui.Description.setText('Event that indicates that a circuit has changed.')

    def _ORCONN_Desc(self):
        self.ui.Description.setText('Event that indicates a change in a relay connection. The endpoint could be any of several things including a fingerprint, nickname ,fingerprint=nickname pair, address:port.')

    def _ADDRMAP_Desc(self):
        self.ui.Description.setText('Event that indicates a new address mapping.')

    def _STATUS_GENERAL_Desc(self):
        self.ui.Description.setText('Notification of a change in tor\'s state. These are generally triggered for the same sort of things as log messages of the NOTICE level or higher. However, unlike :class:`~stem.response.events.LogEvent` these contain well formed data.')

    def _GUARD_Desc(self):
        self.ui.Description.setText('Event that indicates that our guard relays have changed. The endpoint could be either a fingerprint, fingerprint=nickname pair.')

    def _CIRC_MINOR_Desc(self):
        self.ui.Description.setText('Event providing information about minor changes in our circuits.')

    def _BW_Desc(self):
        self.ui.Description.setText('Event emitted every second with the bytes sent and received by tor.')

    def _NEWCONSENSUS_Desc(self):
        self.ui.Description.setText('Event for when we have a new consensus.')

    def _DESCCHANGED_Desc(self):
        self.ui.Description.setText('Event that indicates that our descriptor has changed.')

    def _CIRC_BW_Desc(self):
        self.ui.Description.setText('Event emitted every second with the bytes sent and received by tor on a per-circuit basis.')

    def _CONN_BW_Desc(self):
        self.ui.Description.setText('Event emitted every second with the bytes sent and received by tor on a per-connection basis.')

    def _STREAM_Desc(self):
        self.ui.Description.setText('Event that indicates that a stream has changed.')

    def _NS_Desc(self):
        self.ui.Description.setText('Event for when our copy of the consensus has changed.')

    def _HS_DESC_CONTENT_Desc(self):
        self.ui.Description.setText('Provides the content of hidden service descriptors we fetch.')

    def _STREAM_BW_Desc(self):
        self.ui.Description.setText('Event (emitted approximately every second) with the bytes sent and received by the application since the last such event on this stream.')

    def _CONF_CHANGED_Desc(self):
        self.ui.Description.setText('Event that indicates that our configuration changed, either in response to a SETCONF or RELOAD signal.')

    def _STATUS_SERVER_Desc(self):
        self.ui.Description.setText('Notification of a change in tor\'s state. These are generally triggered for the same sort of things as log messages of the NOTICE level or higher. However, unlike :class:`~stem.response.events.LogEvent` these contain well formed data.')

    def _STATUS_CLIENT_Desc(self):
        self.ui.Description.setText('Notification of a change in tor\'s state. These are generally triggered for the same sort of things as log messages of the NOTICE level or higher. However, unlike :class:`~stem.response.events.LogEvent` these contain well formed data.')

    def _CLIENTS_SEEN_Desc(self):
        self.ui.Description.setText('Periodic event on bridge relays that provides a summary of our users.')

    def _NEWDESC_Desc(self):
        self.ui.Description.setText(' Event that indicates that a new descriptor is available.')

    def _HS_DESC_Desc(self):
        self.ui.Description.setText('Event triggered when we fetch a hidden service descriptor that currently is not in our cache.')

    def _TRANSPORT_LAUNCHED_Desc(self):
        self.ui.Description.setText('Event triggered when a pluggable transport is launched.')

    def _SIGNAL_Desc(self):
        self.ui.Description.setText('Event that indicates that tor has received and acted upon a signal being sent to the process.')

    def _CELL_STATS_Desc(self):
        self.ui.Description.setText('Event emitted every second with a count of the number of cells types broken down by the circuit. These events are only emitted if TestingTorNetwork is set.')

    def _BUILDTIMEOUT_SET_Desc(self):
        self.ui.Description.setText('Event indicating that the timeout value for a circuit has changed.')

    def _NETWORK_LIVENESS_Desc(self):
        self.ui.Description.setText('Event for when the network becomes reachable or unreachable.')
