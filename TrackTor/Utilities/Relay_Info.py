"""
**Module Overview:**

This module will implement the funtionality of showing relay info

|- _Relay_Info
    - __init__: This function will initialize UI object and other class variables in all files
    - _Connections_All: This function will determine the values of Src_IP, Src_Country, Dest_IP, Dest_Country, time
    - _Inbound_Outbound: This function will determine the category and number of connections

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import pycountry
from TrackTor.Utilities import Connections
from TrackTor.Utilities import StaticInfo
import time
from datetime import datetime, timedelta
import calendar
import stem.util.str_tools

INBOUND_OR = Connections.categories['INBOUND_OR']
INBOUND_DIR = Connections.categories['INBOUND_DIR']
INBOUND_CONTROL = Connections.categories['INBOUND_CONTROL']
OUTBOUND = Connections.categories['OUTBOUND']
EXIT = Connections.categories['EXIT']
CIRCUIT = Connections.categories['CIRCUIT']
for i in CIRCUIT:
    if i.status == 'BUILT':
        continue
    else:
        CIRCUIT.remove(i)
length_all = len(INBOUND_OR) + len(INBOUND_DIR) + len(INBOUND_CONTROL) + len(OUTBOUND) + len(EXIT) + len(CIRCUIT)
Row_Count = 0

Node_Info = {}

class _Relay_Info():

    def __init__(self, ui):
        self.ui = ui
        self.controller = StaticInfo.controller

    def _Connections_All(self, Type, Row_Count, Name):
        Count = Row_Count
        if (Name != 'Circuit'):
            for Count in range (Row_Count, Row_Count + len(Type)):

                if (Name == 'Outbound' or Name == 'Exit'):
                    dest_address = Type[Count-Row_Count].remote_address
                    src_address = Type[Count-Row_Count][0]
                    Src_IP = str(src_address) + ':' + str(Type[Count-Row_Count][1])
                    Dest_IP = str(dest_address) + ':' + str(Type[Count-Row_Count][3])
                elif (Name == 'Control'):
                    dest_address = self.controller.get_info('address', None)
                    src_address = Type[Count-Row_Count][0]
                    Src_IP = str(src_address) + ':' + str(Type[Count-Row_Count][3])
                    Dest_IP = str(dest_address) + ':' + str(Type[Count-Row_Count][1])
                else:
                    dest_address = Type[Count-Row_Count][2]
                    src_address = Type[Count-Row_Count][0]
                    Src_IP = str(src_address) + ':' + str(Type[Count-Row_Count][1])
                    Dest_IP = str(dest_address) + ':' + str(Type[Count-Row_Count][3])

                Src_Country2 = str(self.controller.get_info('ip-to-country/%s' %src_address , None))
                Dest_Country2 = str(self.controller.get_info('ip-to-country/%s' %dest_address , None))

                if (Src_Country2.isalpha() == False or Src_Country2 == 'None'):
                    Src_Country = "None"
                else:
                    Src_Country1 = pycountry.countries.get(alpha_2 = str.upper(Src_Country2))
                    Src_Country = Src_Country1.name

                if (Dest_Country2.isalpha() == False or Dest_Country2 == 'None'):
                    Dest_Country = "None"
                else:
                    Dest_Country1 = pycountry.countries.get(alpha_2 = str.upper(Dest_Country2))
                    Dest_Country = Dest_Country1.name

                #Time = (StaticInfo.tor.create_time())
                Time = str(datetime.fromtimestamp(StaticInfo.tor.create_time()))
                Category = Name
                self.ui.Relay_Table.setItem(Count, 0, QtWidgets.QTableWidgetItem(Src_IP))
                self.ui.Relay_Table.setItem(Count, 1, QtWidgets.QTableWidgetItem(Src_Country))
                self.ui.Relay_Table.setItem(Count, 2, QtWidgets.QTableWidgetItem(Dest_IP))
                self.ui.Relay_Table.setItem(Count, 3, QtWidgets.QTableWidgetItem(Dest_Country))
                self.ui.Relay_Table.setItem(Count, 4, QtWidgets.QTableWidgetItem(Time[:19]))
                self.ui.Relay_Table.setItem(Count, 5, QtWidgets.QTableWidgetItem(Category))
            return Count

        else:
            global Node_Info
            Count = Row_Count
            count = Count
            for Count in range (Row_Count, Row_Count+len(Type)):
                if (Type[count-Row_Count].status == 'BUILT'):
                    if (('ONEHOP_TUNNEL' not in Type[count-Row_Count].build_flags)):
                        #print ("Something")
                        GuardNode_fingerprint = str((Type[count-Row_Count].path)[0][0])
                        MiddleNode_fingerprint = str((Type[count-Row_Count].path)[1][0])
                        EndNode_fingerprint = str((Type[count-Row_Count].path)[2][0])
                        Category = Name
                    else:
                        EndNode_fingerprint = str((Type[count-Row_Count].path)[0][0])
                        Category = 'OHT_Circuit'

                    Src_IP = self.controller.get_info('address', None)
                    if (Src_IP == None):
                        Src_IP = '127.0.0.1'

                    import sqlite3
                    import sys
                    import pkg_resources
                    DB_FILE = pkg_resources.resource_filename("TrackTor", "Consensus.db")
                    conn = sqlite3.connect(DB_FILE)
                    c = conn.cursor()
                    address = c.execute('SELECT address FROM Relay_Info WHERE fingerprint=?', (EndNode_fingerprint,)).fetchone()
                    if address:
                        Dest_IP = str(address[0])
                        locale = self.controller.get_info('ip-to-country/%s' %address , None)
                        if locale != '??':
                            locale1 = pycountry.countries.get(alpha_2 = str.upper(locale))
                            Dest_Country = locale1.name
                        else:
                            Dest_Country = 'NA'
                    else:
                        Dest_IP = EndNode_fingerprint
                        Dest_Country = 'NA'

                    if (('ONEHOP_TUNNEL' not in Type[count-Row_Count].build_flags)):
                        Node_Info[Dest_IP] = [GuardNode_fingerprint, MiddleNode_fingerprint, EndNode_fingerprint]
                    else:
                        Node_Info[EndNode_fingerprint] = ['None', 'None', EndNode_fingerprint]

                    Src_Country2 = str(self.controller.get_info('ip-to-country/%s' %Src_IP , None))
                    if (Src_Country2.isalpha() == False or Src_Country2 == 'None'):
                        Src_Country = "None"
                    else:
                        Src_Country1 = pycountry.countries.get(alpha_2 = str.upper(Src_Country2))
                        Src_Country = Src_Country1.name

                    TS = str(Type[0].created)
                    Time = str((datetime.strptime(TS[:19], '%Y-%m-%d %H:%M:%S')) + timedelta(hours = 5.5))
                    #print (Dest_IP)
                    self.ui.Relay_Table.setItem(count, 0, QtWidgets.QTableWidgetItem(Src_IP))
                    self.ui.Relay_Table.setItem(count, 1, QtWidgets.QTableWidgetItem(Src_Country))
                    self.ui.Relay_Table.setItem(count, 2, QtWidgets.QTableWidgetItem(Dest_IP))
                    self.ui.Relay_Table.setItem(count, 3, QtWidgets.QTableWidgetItem(Dest_Country))
                    self.ui.Relay_Table.setItem(count, 4, QtWidgets.QTableWidgetItem(Time))
                    self.ui.Relay_Table.setItem(count, 5, QtWidgets.QTableWidgetItem(Category))
                    count += 1
            return Count


    def _Inbound_Outbound(self):

        global Row_Count
        if not (self.controller.is_alive()):
            return

        else:

            #Length Calculation
            self.ui.Relay_Table.setRowCount(length_all)

            #Printng Connections
            if (len(CIRCUIT)):
                Row_Count = self._Connections_All(CIRCUIT, Row_Count, 'Circuit')

            if (len(INBOUND_CONTROL)):
                if (Row_Count):
                    Row_Count = self._Connections_All(INBOUND_CONTROL, Row_Count+1, 'Control' )
                else:
                    Row_Count = self._Connections_All(INBOUND_CONTROL, Row_Count, 'Control' )
            if (len(INBOUND_DIR)):
                if (Row_Count):
                    Row_Count = self._Connections_All(INBOUND_DIR, Row_Count+1, 'DIR')
                else:
                    Row_Count = self._Connections_All(INBOUND_DIR, Row_Count, 'DIR')
            if (len(INBOUND_OR)):
                if (Row_Count):
                    Row_Count = self._Connections_All(INBOUND_OR, Row_Count+1, 'OR')
                else:
                    Row_Count = self._Connections_All(INBOUND_OR, Row_Count, 'OR')
            if (len(OUTBOUND)):
                if (Row_Count):
                    Row_Count = self._Connections_All(OUTBOUND, Row_Count+1, 'Outbound')
                else:
                    Row_Count = self._Connections_All(OUTBOUND, Row_Count, 'Outbound')
            if (len(EXIT)):
                if (Row_Count):
                    Row_Count = self._Connections_All(EXIT, Row_Count+1, 'Exit')
                else:
                    Row_Count = self._Connections_All(EXIT, Row_Count, 'Exit')
