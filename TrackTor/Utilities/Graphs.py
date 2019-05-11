"""
**Module Overview:**

This module will implement the funtionality of showing Graphs

|- Data_Statistics
    - __init__: This function will initialize UI object and other class variables in all files
    - Uploads:
    - Get_Uploads_Data:
    - Downloads:
    - Get_Downloads_Data:

|- Connections
    - __init__: This function will initialize UI object and other class variables in all files
    - Inbound: This function will show the inbound connections graph
    - outbound: This function will show the outbound connections graph

|- Resources
    - __init__: This function will initialize UI object and other class variables in all files
    - CPU: This function will show the CPU Usage Graph
    - Memory: This function will show the memory Usage Graph

"""

import collections
import numpy as np
import argparse
import stem.connection
import stem.util.system
import stem.util.str_tools
from TrackTor.Utilities import Interval_Change
from TrackTor.Utilities import StaticInfo

from stem.control import Listener, EventType, Controller
from stem.util.connection import get_connections, port_usage

#Getting Controller Information
args = StaticInfo.args
controller = StaticInfo.controller
pid = StaticInfo.pid
relays = {}


#Variables for Upload Data
uploads_sampleinterval=0.01
uploads_timewindow=10*((Interval_Change.Uploads_Interval)/1000)
uploads_bufsize = int(uploads_timewindow/uploads_sampleinterval)
uploads_databuffer = collections.deque([0.0]*uploads_bufsize, uploads_bufsize)
uploads_x = np.linspace(0.0, uploads_timewindow, num = uploads_bufsize)
uploads_y = np.zeros(uploads_bufsize, dtype=np.float)

#Variables for Downloads Data
downloads_sampleinterval=0.01
downloads_timewindow=10*((Interval_Change.Downloads_Interval)/1000)
downloads_bufsize = int(downloads_timewindow/downloads_sampleinterval)
downloads_databuffer = collections.deque([0.0]*downloads_bufsize, downloads_bufsize)
downloads_x = np.linspace(0.0, downloads_timewindow, num = downloads_bufsize)
downloads_y = np.zeros(downloads_bufsize, dtype=np.float)

class Data_Statistics():

    def __init__(self, ui):
        self.ui = ui

    def Uploads(self):

        if not (controller.is_alive()):
            return

        def Get_Uploads_Data(event):
            global uploads_y
            global uploads_databuffer
            uploads_databuffer.append(event.written)
            uploads_y[:] = uploads_databuffer
            self.ui.Uploads_Speed1.setText(str(event.written/1000) + " kB/s")

        #print (uploads_y)
        controller.add_event_listener(Get_Uploads_Data, EventType.BW)
        self.ui.uploads_curve.setData(uploads_x, uploads_y)


    def Downloads(self):

        if not (controller.is_alive()):
            return

        def Get_Downloads_Data(event):
            global downloads_y
            global downloads_databuffer
            downloads_databuffer.append(event.read)
            downloads_y[:] = downloads_databuffer
            self.ui.Downloads_Speed1.setText(str((event.read)/1000) + " kB/s")

        controller.add_event_listener(Get_Downloads_Data, EventType.BW)
        self.ui.downloads_curve.setData(downloads_x, downloads_y)


#Variable Definitions for Inbound
inbound_sampleinterval=0.05
inbound_timewindow=5.
inbound_bufsize = int(inbound_timewindow/inbound_sampleinterval)
inbound_databuffer = collections.deque([0.0]*inbound_bufsize, inbound_bufsize)
inbound_x = np.linspace(0.0, inbound_timewindow, num = inbound_bufsize)
inbound_y = np.zeros(inbound_bufsize, dtype=np.float)

#Variable Definitions for Outbound
outbound_sampleinterval=0.05
outbound_timewindow=5.
outbound_bufsize = int(outbound_timewindow/outbound_sampleinterval)
outbound_databuffer = collections.deque([0.0]*outbound_bufsize, outbound_bufsize)
outbound_x = np.linspace(0.0, outbound_timewindow, num = outbound_bufsize)
outbound_y = np.zeros(outbound_bufsize, dtype=np.float)

class Connections():

    def __init__(self, ui):
        self.ui = ui
        global controller
        global relays
        self.policy = controller.get_exit_policy()
        for desc in controller.get_network_statuses():
            relays.setdefault(desc.address, []).append(desc.or_port)

    def Inbound(self):

        if not (controller.is_alive()):
            return
        global inbound_y
        global inbound_databuffer
        inbound_count = 0
        for conn in get_connections(resolver = args.resolver, process_pid = pid):
            if conn.protocol == 'udp':
                continue
            if conn.local_port in controller.get_ports(Listener.OR, []):
                inbound_count+= 1
            elif conn.local_port in controller.get_ports(Listener.DIR, []):
                inbound_count+= 1
            elif conn.local_port in controller.get_ports(Listener.CONTROL, []):
                inbound_count+= 1
            inbound_databuffer.append(inbound_count)
            inbound_y[:] = inbound_databuffer
        self.ui.Inbound_Conn1.setText(str(inbound_count) + " /Sec")
        self.ui.inbound_curve.setData(inbound_x, inbound_y)

    def Outbound(self):

        if not (controller.is_alive()):
            return
        global outbound_y
        global outbound_databuffer
        global relays
        outbound_count = 0
        for conn in get_connections(resolver = args.resolver, process_pid = pid):
            if conn.protocol == 'udp':
                continue
            if conn.remote_port in relays.get(conn.remote_address, []):
                outbound_count+= 1
            elif self.policy.can_exit_to(conn.remote_address, conn.remote_port):
                outbound_count+= 1
            else:
                outbound_count+= 1
        self.ui.Outbound_Conn1.setText(str(outbound_count) + " /Sec")
        outbound_databuffer.append(outbound_count)
        outbound_y[:] = outbound_databuffer
        self.ui.outbound_curve.setData(outbound_x, outbound_y)

#Variable Definitions for CPU
cpu_sampleinterval=0.05
cpu_timewindow=5.
cpu_bufsize = int(cpu_timewindow/cpu_sampleinterval)
cpu_databuffer = collections.deque([0.0]*cpu_bufsize, cpu_bufsize)
cpu_x = np.linspace(0.0, cpu_timewindow, num = cpu_bufsize)
cpu_y = np.zeros(cpu_bufsize, dtype=np.float)

#Variable Definitions for Memory
memory_sampleinterval=0.05
memory_timewindow=5.
memory_bufsize = int(memory_timewindow/memory_sampleinterval)
memory_databuffer = collections.deque([0.0]*memory_bufsize, memory_bufsize)
memory_x = np.linspace(0.0, memory_timewindow, num = memory_bufsize)
memory_y = np.zeros(memory_bufsize, dtype=np.float)

class Resources():

    def __init__(self, ui):
        self.ui = ui

    def CPU(self):
        global cpu_y
        global cpu_databuffer
        cpu_databuffer.append(StaticInfo.CPU_Tor1)
        cpu_y[:] = cpu_databuffer
        self.ui.cpu_curve.setData(cpu_x, cpu_y)

    def Memory(self):
        global memory_y
        global memory_databuffer
        memory_databuffer.append(StaticInfo.RAM_Tor1)
        memory_y[:] = memory_databuffer
        self.ui.memory_curve.setData(memory_x, memory_y)
