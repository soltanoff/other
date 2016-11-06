#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
from multiprocessing import Lock

from PyQt4 import QtGui, QtCore

VERSION = 'v0.6.1'


MAIN_MUTEX = Lock()
NEW_TASK_MUTEX = Lock()
# TAKE_FIRST_TASK_MUTEX = Lock()
# TAKE_LAST_TASK_MUTEX = Lock()

TASK_PRIORITY = [
    u'Высокий',     # 0
    # u'Средний',     # 1
    u'Низкий'       # 2
]

TASK_TIME_QUANTUM = [
    # 3,              # 0
    2,              # 1
    1               # 2
]

TASK_STATUS = [
    'born',         # 0
    'ready',        # 1
    'execute',      # 2
    'waiting',      # 3
    'finish'        # 4
]

RESOURCES_OWNERSHIP_PERCENT = 0.5

DEFAULT_TASK_NAME = u'Процесс #%s'
DEFAULT_PROCESSOR_NAME = u'Процессор #%s'
DEFAULT_PRIORITY_COLOR =[
    QtGui.QColor(QtCore.Qt.red),        # 0
    QtGui.QColor(QtCore.Qt.blue),       # 1
    QtGui.QColor(QtCore.Qt.darkGreen)   # 2
]

try:
    RESOURCES_PATH = os.getcwd() + '\\resources'
    RESOURCES_LIST = os.listdir(RESOURCES_PATH)
except Exception as e:
    print '[CFG_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
    RESOURCES_PATH = ''
    RESOURCES_LIST = ''
