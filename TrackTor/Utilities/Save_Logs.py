"""
**Module Overview:**

This module will implement the funtionality of showing logs

|- _Save_Logs
    - openFileNameDialog: This function will give GUI for opening a file
    - openFileNamesDialog: This function will give GUI for opening a file
    - saveFileDialog: This function will give GUI for saving a file

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from TrackTor.Utilities import Logs
import logging
import os
import time

class _Save_Logs(QWidget):

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Logs to File","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            file = open(fileName, "w")
            file.write('{0:20}  {1:10}  {2}\n'.format("Timestamp", "Category", "Message"))
            for item in Logs.LogsArray:
                content = item[1].split(' ',1)
                category = content[0]
                message = content[1]
                file.write('{0:20}  {1:10}  {2}\n'.format(item[0],category, message))

if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    ex = _Save_Logs()
    #sys.exit(app.exec_())
