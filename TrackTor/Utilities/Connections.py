"""
**Module Overview:**

This module will implement the funtionality of showing all the connections

- connections: This function will show all the connections

"""

import argparse
import collections
import time

import stem.connection
import stem.util.system
import stem.util.str_tools

from stem.control import Listener
from stem.util.connection import get_connections, port_usage, is_valid_ipv4_address
from TrackTor.Utilities import StaticInfo
from stem.util import datetime_to_unix

'''
INBOUND_OR = 'Inbound to our ORPort'
INBOUND_DIR = 'Inbound to our DirPort'
INBOUND_CONTROL = 'Inbound to our ControlPort'
OUTBOUND = 'Outbound to a relay'
'''

# categorize our connections

categories = collections.OrderedDict((
('INBOUND_OR', []),
('INBOUND_DIR', []),
('INBOUND_CONTROL', []),
('OUTBOUND', []),
('EXIT', []),
('CIRCUIT', [])
))


def connections():
    global controller
    args = StaticInfo.args
    control_port = StaticInfo.control_port
    controller = StaticInfo.controller

    if not (controller.is_alive()):
        return

    desc = controller.get_network_status(default = None)
    pid = StaticInfo.pid


    policy = controller.get_exit_policy()
    relays = {}  # address => [orports...]

    for desc in controller.get_network_statuses():
        relays.setdefault(desc.address, []).append(desc.or_port)

    exit_connections = {}  # port => [connections]

    for conn in get_connections(resolver = args.resolver, process_pid = pid):
        global categories
        if conn.protocol == 'udp':
            continue

        if conn.local_port in controller.get_ports(Listener.OR, []):
          categories['INBOUND_OR'].append(conn)
        elif conn.local_port in controller.get_ports(Listener.DIR, []):
          categories['INBOUND_DIR'].append(conn)
        elif conn.local_port in controller.get_ports(Listener.CONTROL, []):
          categories['INBOUND_CONTROL'].append(conn)
        elif conn.remote_port in relays.get(conn.remote_address, []):
          categories['OUTBOUND'].append(conn)
        elif policy.can_exit_to(conn.remote_address, conn.remote_port):
          categories['EXIT'].append(conn)
          exit_connections.setdefault(conn.remote_port, []).append(conn)
        else:
          categories['OUTBOUND'].append(conn)
    circ = controller.get_circuits([])
    for conn in circ:
        categories['CIRCUIT'].append(conn)


    if exit_connections:
        total_ipv4, total_ipv6 = 0, 0

        for port in sorted(exit_connections):
          connections = exit_connections[port]
          ipv4_count = len([conn for conn in connections if is_valid_ipv4_address(conn.remote_address)])
          ipv6_count = len(connections) - ipv4_count
          total_count = len(connections)
          total_ipv4, total_ipv6 = total_ipv4 + ipv4_count, total_ipv6 + ipv6_count

          usage = port_usage(port)
          label = '%s (%s)' % (port, usage) if usage else port

connections()
