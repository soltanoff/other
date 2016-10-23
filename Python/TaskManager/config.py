#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

VERSION = 'v0.0.1'


TASK_PRIORITY = [
    u'Высокий',     # 1
    u'Средний',     # 2
    u'Низкий'       # 3
]

TASK_STATUS = [
    'born',         # 0
    'ready',        # 1
    'execute',      # 2
    'waiting',      # 3
    'finish'        # 4
]

DEFAULT_TASK_NAME = u'Процесс #%s'

RESOURCES_PATH = os.getcwd() + '\\resources'
RESOURCES_LIST = os.listdir(RESOURCES_PATH)
