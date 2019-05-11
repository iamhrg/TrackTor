"""
**Module Overview:**

This module will implement the funtionality of New Identity and Reload Tor

|- actions
	- NewIdentity: This function will generate new identity
	- ReloadTor: This function will reload tor
"""

import os
import time
import argparse
from stem import Signal
from stem.control import Controller
import stem.connection
from TrackTor.Home import DialogBox
from TrackTor.Utilities import StaticInfo

args = StaticInfo.args
control_port = StaticInfo.control_port
controller = StaticInfo.controller


class actions():
	def NewIdentity(self):

		"""
		Requests a new identity and provides information about the same.
		"""

		with Controller.from_port(port = control_port) as controllerr:

			if not controller:
				DialogBox.box.showMessageBox(DialogBox.box,'Message','Unable to connect to Tor. Are you sure it is running?')
			else :
				controller.authenticate()

				if not controller.is_newnym_available():
					DialogBox.box.showMessageBox(DialogBox.box,'Message','Sorry! New Relays are not available at the moment!')

				else:

					controller.signal(Signal.NEWNYM)
					DialogBox.box.showMessageBox(DialogBox.box,'Message','New Identity has been generated!')


	def ReloadTor(self):

		"""
		Reloads the torrc file.
		"""

		with Controller.from_port(port = control_port) as controller:
			if not controller:
				DialogBox.box.showMessageBox(DialogBox.box,'Message','Unable to connect to Tor. Are you sure it is running?')
			else:
				controller.authenticate()
				controller.signal(Signal.RELOAD)
				from TrackTor.Home.Edit_Torrc import _Edit_Torrc
				DialogBox.box.showMessageBox(DialogBox.box,'Message','Torrc has been reloaded!')
				_Edit_Torrc.Close_Edit_Torrc(_Edit_Torrc)
