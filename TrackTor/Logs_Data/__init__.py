"""
**Module Overview:**

This module will implement the funtionality of collecting logs as well as showing it
- listener: This function will do funtionality of listening
- Collect_Logs: This function will do funtionality of collecting Logs
"""

from TrackTor.Utilities import StaticInfo
import sys
import time
import os
import pkg_resources

TrackTor_Events = ['BW', 'CIRC', 'ADDRMAP', 'BUILDTIMEOUT_SET', 'CELL_STATS', 'CIRC_BW',
'CIRC_MINOR', 'CLIENTS_SEEN', 'CONF_CHANGED', 'CONN_BW', 'DEBUG', 'DESCCHANGED', 'ERR',
'GUARD', 'HS_DESC', 'HS_DESC_CONTENT', 'INFO', 'NETWORK_LIVENESS', 'NEWCONSENSUS', 'NEWDESC',
'NOTICE', 'NS', 'ORCONN', 'SIGNAL', 'STREAM', 'STATUS_CLIENT', 'STATUS_GENERAL', 'STATUS_SERVER',
'STREAM_BW', 'TRANSPORT_LAUNCHED', 'WARN']

def listener(event):
    global file
    Uptime = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    if (TrackTor_Events == 'NEWCONSENSUS'):
        for line in event.splitlines():
            if line.startswith('r '):
                r_comp = line.split(' ')
                if '' in r_comp:
                    r_comp.remove('')
                address = r_comp[6]
                or_port = int(r_comp[7])
                fingerprint = stem.descriptor.router_status_entry._base64_to_hex(r_comp[2])
                nickname = r_comp[1]
                c.execute('INSERT OR REPLACE INTO relays(fingerprint, address, or_port, nickname) VALUES (?,?,?,?)', fingerprint, address, or_port, nickname)
    item = (Uptime, str(event))
    content = item[1].split(' ',1)
    category = content[0]
    message = content[1]
    file.write('{0:20}  {1:10}  {2}\n'.format(item[0],category, message))

import logging

def Collect_Logs(listener):
    global file
    if sys.platform == "win32":
        Uptime = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime())
        name = "Tor_" + Uptime
        name1 = "TrackTor_" + Uptime
    else:
        Uptime = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())
        name = "Tor_" + Uptime
        name1 = "TrackTor_" + Uptime

    if sys.platform == "win32":
        name = "Logs_Data\\" + name
        DATA_PATH = pkg_resources.resource_filename("TrackTor", name)
        file = open(DATA_PATH, "w")
        name1 = "Logs_Data\\" + name1
        DATA_PATH1 = pkg_resources.resource_filename("TrackTor", name1)
        logging.basicConfig(filename=DATA_PATH1, filemode='w', level=logging.ERROR)
    else:
        name = "Logs_Data/" + name
        DATA_PATH = pkg_resources.resource_filename("TrackTor", name)
        file = open(DATA_PATH, "w")
        name1 = "Logs_Data/" + name1
        DATA_PATH1 = pkg_resources.resource_filename("TrackTor", name1)
        logging.basicConfig(filename=DATA_PATH1, filemode='w', level=logging.ERROR)

    file.write('{0:20}  {1:10}  {2}\n'.format("Timestamp", "Category", "Message"))
    StaticInfo.controller.add_event_listener(listener, *TrackTor_Events)

Collect_Logs(listener)
