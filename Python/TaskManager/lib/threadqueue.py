#!/usr/bin/env python
# -*- coding: utf8 -*-
from config import TASK_STATUS


class CThreadQueue(object):
    u"""
    item of queue:
    {
        'thread': thread,               Thread
        'name': name,                   str
        'eventStart': eStart,           Event
        'eventFinish': eFinish,         Event
        'priority': priority,           int
        'status': status,               int
        'time': time,                   int
        'resources': []                 list
    }
    """
    def __init__(self, queue=list(dict())):
        self.data = queue

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data and self.data[0]['status'] != 4:
            return self.data[0]
        else:
            return None

    # def sort(self):
    #    self.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))
    #    self.changeStatus()

    # def changeStatus(self, pos=1):
    #    for x in self.data[pos:]:
    #        if x['status'] != 4:
    #            x['status'] = 3

    def __len__(self):
        return len(self.data)
