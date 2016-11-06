#!/usr/bin/env python
# -*- coding: utf8 -*-
# from config import TASK_STATUS
from config import RESOURCES_LIST, RESOURCES_OWNERSHIP_PERSENT


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
        self.avgTime = 0

    def countOfActive(self):
        count = 0
        for x in self.data:
            if x.status not in [4]:
                count += 1
        return count

    def push(self, x):
        if self.countOfActive():
            x.status = 3
        self.data.append(x)

    def checkResources(self, element):
        for x in self.data:
            if x.processor != '- none -' and x.status in [2, 3]:
                for y in element.resources:
                    if y in x.resources:
                        return False
        return True

    def pop(self):
        index = 0
        if self.data:
            while index < len(self.data):
                if self.data[index].status not in [4, 2] and self.data[index].processor == '- none -':
                    if self.checkResources(self.data[index]):
                        self.data[index].status = 2
                        return self.data[index]
                index += 1
            return None
        else:
            return None

    def calculateAvgTime(self):
        self.avgTime = 0
        count = 0
        for x in self.data:
            if x.status != 4:
                self.avgTime += x.time
                count += 1
        if count:
            self.avgTime /= count

    def last(self):
        for x in range(-1, -len(self.data), -1):
            if self.data[x].status == 3 and self.data[x].processor == '- none -':
                if self.checkResources(self.data[x]):
                    return self.data[x]
        return None

    def reviewPriority(self):
        index = 0
        if self.data:
            while index < len(self.data):
                if len(self.data[index].resources) > RESOURCES_OWNERSHIP_PERSENT * len(RESOURCES_LIST) and \
                                self.data[index].priority != 0:
                    self.data[index].priority = 0
                index += 1

    # sorting (realize planing)
    def sort(self):
        self.data.sort(key=lambda k: (k.status, k.priority, k.time, -len(k.resources)))

    # SJF sorting
    def startPlanning(self):
        self.sort()
        self.reviewPriority()
        self.changeStatus()
        self.sort()
        self.calculateAvgTime()

    def changeStatus(self, checkFinished=False):
        if checkFinished:
            for x in self.data:
                if x.eventFinish.isSet():
                    x.status = 4
        else:
            for x in self.data[self.pos:]:
                if x.status not in [4, 2]:  # and not (x['status'] == 1 and x['processor'] == '- none -'):
                    x.status = 3
                elif x.eventFinish.isSet():
                    x.status = 4

    def removeFinished(self):
        self.data = [i for i in self.data if i.status != 4]

    def __len__(self):
        return len(self.data)
