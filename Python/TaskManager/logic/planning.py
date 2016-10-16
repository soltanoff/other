#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread

from config import TASK_STATUS
from lib.threadqueue import CThreadQueue


def createProcess(name, target, priority=1, time=4):
    eStart = Event()
    eFinish = Event()
    thread = Thread(target=target, args=(name, eStart, eFinish, time))

    return {
        'thread': thread,
        'name': name,
        'eventStart': eStart,
        'eventFinish': eFinish,
        'priority': priority,
        'status': TASK_STATUS[0],
        'time': time
    }


class SJF(object):
    def __init__(self):
        self.queue = CThreadQueue()
        self.finishedThreads = []
        self.allThreads = []
        self.sjfThread = Thread(target=self.sjfRoutine)
        self.currentThread = None
        self.suspended = False

    def sjfRoutine(self):
        while True:
            if self.suspended or \
                    (not len(self.queue.getList())) or \
                    (self.currentThread and self.currentThread['eventStart'].is_set()):
                continue
            elif self.currentThread:
                self.finishedThreads.append(self.currentThread)

            self.currentThread = self.queue.pop()
            self.currentThread['thread'].start()

            if not self.suspended:
                self.currentThread['eventStart'].set()

            self.currentThread['eventFinish'].clear()

    def suspendCurrentThread(self):
        self.suspended = True
        if self.currentThread and self.currentThread['thread'].isAlive():
            self.currentThread['eventStart'].clear()

    def resumeCurrentThread(self):
        self.suspended = False
        if self.currentThread and self.currentThread['thread'].isAlive():
            self.currentThread['eventStart'].set()

    def start(self):
        self.sjfThread.start()
