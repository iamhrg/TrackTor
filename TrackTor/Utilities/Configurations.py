"""
**Module Overview:**

This module will implement the funtionality of showing Configurations of Tor

|- _Configurations
	- __init__: This function will initialize UI object and other class variables in all files
	- _Config_CurrentVal: This function will configure the current value
    - manual: This function will information from stem module
    - _Config_ChangeVal: This function will configure the changed value
    - _Config_Reset: This function will configure the changed value to its original version
    - _Config_DropDown: This function will configure the drop down window for time intervals
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from stem.control import Controller, EventType
from stem.util import enum
import stem
import threading
from TrackTor.Utilities import StaticInfo
from stem.util import conf, enum, log, str_tools
import stem.manual

try:
  # added in python 3.2
  from functools import lru_cache
except ImportError:
  from stem.util.lru_cache import lru_cache

Configurations = {}
Value_Type = {}


class _Configurations():
	def __init__(self, ui):
	    self.ui = ui
	    self.controller = StaticInfo.controller
	    if not self.controller.is_alive():
	        import sys
	        sys.stderr = open("Error.txt", "w")


	def _Config_CurrentVal(self):
	    self.ui.Conf_Label.hide()
	    name = self.ui.Config_Options.currentText()
	    self.ui.Config_CurrentVal.setText(Configurations[name])
	    @lru_cache()
	    def manual(option):
	        result = stem.manual.query('SELECT category, usage, summary, description, position FROM torrc WHERE key=?', option.upper()).fetchone()
	        item = QtWidgets.QListWidgetItem('Type :  ' + result[0])
	        item1 = QtWidgets.QListWidgetItem('Domain :  ' + result[1])
	        item2 = QtWidgets.QListWidgetItem('Description :  ' + result[2] + '.')
	        item3 = QtWidgets.QListWidgetItem('')
	        self.ui.Config_Desc.clear()
	        self.ui.Config_Desc.addItem(item3)
	        self.ui.Config_Desc.addItem(item3)
	        self.ui.Config_Desc.addItem(item)
	        self.ui.Config_Desc.addItem(item1)
	        self.ui.Config_Desc.addItem(item2)
	    manual(name)

	def _Config_ChangeVal(self):
		if not self.controller.is_alive():
		    import TrackTor.Home.MessageBox
		    MessageBox.box.showMessageBox(MessageBox.box,'Message','Unable to connect to Tor! Hence can not update Configurations!')

		else:
			self.ui.Conf_Label.hide()
			name = self.ui.Config_Options.currentText()
			new_val = self.ui.Config_NewVal.text()
			self.ui.Config_CurrentVal.setText(new_val)
			self.ui.Config_NewVal.setText('')
			if new_val != Configurations[name]:

				try:
					if Value_Type[name] == 'Boolean':
					    if new_val.lower() == 'true':
					     new_val = '1'
					    elif new_val.lower() == 'false':
					     new_val = '0'
					elif Value_Type[name] == 'LineList':
					    new_val = new_val.split(',')  # set_conf accepts list inputs
					self.controller.set_conf(name, new_val)
					self.Conf_Label.setText("<html><head/><body><p align=\"center\"><span style=\" color:#227319;\">Value has been updated</span></p></body></html>")
					self.ui.Conf_Label.show()
				except Exception as exc:
					self.ui.Conf_Label.setText(str(exc))
					self.ui.Conf_Label.show()


	def _Config_Reset(self):
	    if not self.controller.is_alive():
	        import MessageBox
	        MessageBox.box.showMessageBox(MessageBox.box,'Message','Unable to connect to Tor! Hence can not Reset Configurations')
	    else:
	        name = self.ui.Config_Options.currentText()
	        self.controller.reset_conf(name)

	def _Config_DropDown(self):
	    for line in self.controller.get_info('config/names').splitlines():
	        line_comp = line.split()
	        name, value_type = line_comp[0], line_comp[1]
	        values = self.controller.get_conf(name, [], True)

	        if not values:
	            Config = '<none>'
	        elif value_type == 'Boolean' and values[0] in ('0', '1'):
	            if values[0] == '0':
	                Config = 'False'
	            else:
	                Config = 'True'
	        elif value_type == 'DataSize' and values[0].isdigit():
	            Config = str_tools.size_label(int(values[0]))
	        elif value_type == 'TimeInterval' and values[0].isdigit():
	            Config = str_tools.time_label(int(values[0]), is_long = True)
	        else:
	            Config = values[0]
	        Value_Type.update({name:value_type})
	        Configurations.update({name:Config})
	        self.ui.Config_Options.addItem(name)
	    self._Config_CurrentVal()
