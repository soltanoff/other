#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread

# from config import TASK_STATUS
from lib.threadqueue import CThreadQueue


def createProcess(name, target, priority=1, time=4, resources=[]):
    eStart = Event()
    eFinish = Event()
    thread = Thread(target=target, args=(name, eStart, eFinish, time))

    return {
        'thread':       thread,
        'name':         name,
        'eventStart':   eStart,
        'eventFinish':  eFinish,
        'priority':     priority,
        'status':       1,          # ready
        'time':         time,
        'resources':    resources   # list of id's of available resources
    }


class SJF(object):
    def __init__(self):
        self.queue = CThreadQueue()
        self.finishedThreads = []
        # self.allThreads = []

        self.sjfThread = Thread(target=self.sjfRoutine)
        self.sjfFinishThreadEvent = Event()
        self.sjfNewThreadEvent = Event()
        self.sjfFinishThreadEvent.clear()
        self.sjfNewThreadEvent.clear()

        self.currentThread = None
        self.suspended = False
        self.enable = True

    # TODO: 1) execute planning with available resources of all thread
    # TODO: 2) write selecting and changing priority level
    # TODO: 3) write timer, whos run a little process in query
    def startPlanning(self):
        self.queue.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))
        self.changeStatus()
        self.queue.data.sort(key=lambda k: (k['status'], k['priority'], k['time']))

    def changeStatus(self, pos=1):
        for x in self.queue.data[pos:]:
            if x['status'] != 4:
                x['status'] = 3

    def sjfRoutine(self):
        while self.enable:
            self.sjfFinishThreadEvent.wait()    # wait current executed thread
            if self.currentThread:
                self.currentThread['eventFinish'].wait()
                self.currentThread['status'] = 4    # set finish status
                self.startPlanning()
                # self.startPlanning()

            self.currentThread = self.queue.pop()   # can return None

            if self.currentThread:
                self.currentThread['status'] = 2
                self.currentThread['thread'].start()

                if not self.suspended:
                    self.currentThread['eventStart'].set()

                self.currentThread['eventFinish'].clear()
            else:
                self.sjfNewThreadEvent.clear()  # all threads in queue are finished
                self.sjfNewThreadEvent.wait()   # wait a new thread in queue

        # if self.currentThread and self.currentThread['thread'].isAlive():
        #    self.currentThread['thread'].terminate()
        print u'[TaskManager] Closing...'

    def suspendCurrentThread(self):
        self.suspended = True
        self.sjfFinishThreadEvent.clear()
        if self.currentThread and self.currentThread['thread'].isAlive():
            self.currentThread['eventStart'].clear()
            self.currentThread['status'] = 1    # ready

    def resumeCurrentThread(self):
        self.suspended = False
        self.sjfFinishThreadEvent.set()
        self.sjfNewThreadEvent.set()
        if self.currentThread and self.currentThread['thread'].isAlive():
            self.currentThread['eventStart'].set()
            self.currentThread['status'] = 2    # execute

    def start(self):
        self.sjfThread.start()
