import psutil, getpass
import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets

thread_count = 0
proc_count = 0
time = time.time()
count = 0
count1 = 0
pid = 0

PRIVELEGED_USERS = [
    'root',
    'administrator',
    'parul'
]

INVALID_PROCESSES = [
	'zombie'
]

SYSTEM_USERS = []

_currentSystemUser = getpass.getuser()

class _Resources():

    def __init__(self, ui):
        self.ui = ui

    def Resources_Stats(self):
        for proc in psutil.process_iter():
            global count
            global thread_count
            global proc_count

            if proc.name() in ["Python", "python.exe", "python3"] and count == 0:
                count = 1

            elif proc.name() in ["Python", "python.exe", "python3"] and count == 1:
                count = 0
                time_delta = time - proc.create_time()
                proc_info = {}
                proc_info['id'] = proc.pid
                proc_info['name'] = proc.name()

                p = psutil.Process(proc.pid)
                proc_info['user'] = p.username()

                #if ((proc_info['user'] == _currentSystemUser) or (_currentSystemUser in PRIVELEGED_USERS)) and p.status() not in INVALID_PROCESSES:
                #if p.status() not in INVALID_PROCESSES:
                delta = datetime.timedelta(seconds=(time - p.create_time()))
                proc_info['rawtime'] = time - p.create_time()
                proc_info['time'] =  delta
                proc_info['command'] = ' '.join(p.cmdline())
                thread_count += p.num_threads()
                proc_info['cpu'] = p.cpu_percent()
                proc_info['memory'] = round(p.memory_percent(),2)
                proc_info['local_ports'] = [x.laddr[1] for x in p.connections()]
                proc_info['open_files'] = p.open_files()
                proc_count += 1

                self.ui.Resources_Tracktor.clear()
                for i in proc_info.items():
                    if (str(i[0]) == 'cpu'):
                        self.ui.CPU_Tracktor.setText(str(i[1]) + ' %')
                    elif (str(i[0]) == 'memory'):
                        self.ui.RAM_Tracktor.setText(str(i[1]) + ' %')
                    item3 = QtWidgets.QListWidgetItem('')
                    item = QtWidgets.QListWidgetItem((str(i[0])).upper() + " : " + str(i[1]))
                    self.ui.Resources_Tracktor.addItem(item3)
                    self.ui.Resources_Tracktor.addItem(item)

                if proc_info['user'] not in SYSTEM_USERS:
                    SYSTEM_USERS.append(proc_info['user'])

            elif proc.name() in ["tor.real", "tor.exe", "tor"]:

                try :
                    time_delta = time - proc.create_time()
                    proc_info = {}
                    proc_info['id'] = proc.pid
                    proc_info['name'] = proc.name()

                    p = psutil.Process(proc.pid)
                    proc_info['user'] = p.username()

                    if p.status() not in INVALID_PROCESSES:
                        delta = datetime.timedelta(seconds=(time - p.create_time()))
                        proc_info['rawtime'] = time - p.create_time()
                        proc_info['time'] =  delta
                        proc_info['command'] = ' '.join(p.cmdline())

                        thread_count += p.num_threads()
                        proc_info['cpu'] = p.cpu_percent()
                        proc_info['memory'] = round(p.memory_percent(),2)
                        proc_info['open_files'] = p.open_files()
                        proc_count += 1

                    self.ui.Resources_Tor.clear()
                    for i in proc_info.items():
                        if (str(i[0])== 'memory'):
                            self.ui.RAM_Tor.setText(str(i[1]) + ' %')
                        item3 = QtWidgets.QListWidgetItem('')
                        item = QtWidgets.QListWidgetItem((str(i[0])).upper() + " : " + str(i[1]))
                        self.ui.Resources_Tor.addItem(item3)
                        self.ui.Resources_Tor.addItem(item)

                    if proc_info['user'] not in SYSTEM_USERS:
                        SYSTEM_USERS.append(proc_info['user'])

                except:
                    global count1
                    if count1 == 0:
                        self.ui.Resources_Tor.clear()
                        item = QtWidgets.QListWidgetItem('')
                        item1 = QtWidgets.QListWidgetItem('Data Not Found! Do not have Permission!')
                        self.ui.Resources_Tor.addItem(item)
                        self.ui.Resources_Tor.addItem(item1)
                        count1 = 1
                    else:
                        continue
