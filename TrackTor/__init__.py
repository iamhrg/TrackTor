"""
**Module Overview:**

This module is the initialization module of tracktor

|- Tracktor
    |- Home
        - __init__.py
        - Actions.py
        - DialogBox.py
        - Edit_Torrc.py
        - MessageBox.py

    |- Icons

    |- Logs_Data
        - __init__.py

    |- UI
        - Edit_Torrc.ui
        - trackTor.ui

    |- Utilities
        - __init__.py
        - Congigurations.py
        - Connections.py
        - Graphs.py
        - Interval_Change.py
        - Logs.py
        - Relay_Info.py
        - Resources.py
        - Save_Logs.py
        - StaticInfo.py

    - __main__.py
    - Consensus.db
    - Error.txt
    - main.py
    - New_Consensus
    - Tabs.py

"""

import argparse
import stem.connection
import sys
import os
import pkg_resources

DATA_PATH = pkg_resources.resource_filename("TrackTor", "Error.txt")

_stderr = sys.stderr
_stdout = sys.stdout

def TrackTor_Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ctrlport", help="default: 9051 or 9151")
    parser.add_argument("--resolver", help="default: autodetected")
    args = parser.parse_args()
    control_port = int(args.ctrlport) if args.ctrlport else 'default'
    sys.stdout = open(DATA_PATH, "r")
    try:
        controller = stem.connection.connect(control_port = ('127.0.0.1', control_port))
        import TrackTor.main
    except (OSError, IOError):
        from TrackTor.Start import _Start_Box
        _Start_Box.Open_Alert_Box(_Start_Box)
        sys.exit()

TrackTor_Main()
