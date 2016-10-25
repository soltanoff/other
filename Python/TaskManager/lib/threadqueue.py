#!/usr/bin/env python
# -*- coding: utf8 -*-
# from config import TASK_STATUS


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
        self.pos = 1

    def push(self, x):
        self.data.append(x)

    def pop(self):
        index = 0
        if self.data:
            while index < len(self.data):
                if self.data[index]['status'] not in [4, 2]:
                    self.data[index]['status'] = 2
                    return self.data[index]
                index += 1
            return None
        else:
            return None

    # SJF sorting
    def startPlanning(self):
        self.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))
        self.changeStatus()
        self.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))

    def changeStatus(self):
        for x in self.data[self.pos:]:
            if x['status'] not in [4, 2]:  # and not (x['status'] == 1 and x['processor'] == '- none -'):
                x['status'] = 3

    def removeFinished(self):
        self.data = [i for i in self.data if i['status'] != 4]

    # def sort(self):
    #    self.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))
    #    self.changeStatus()

    # def changeStatus(self, pos=1):
    #    for x in self.data[pos:]:
    #        if x['status'] != 4:
    #            x['status'] = 3

    def __len__(self):
        return len(self.data)
