#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread, Lock

# from config import TASK_STATUS
# from lib.threadqueue import CThreadQueue
from config import DEFAULT_PROC_NAME

MAIN_MUTEX = Lock()


def createProcess(name, target, priority=1, time=4, resources=list()):
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
        'resources':    resources,   # list of id's of available resources
        'processor':    '- none -'
    }


class Processor(object):
    def __init__(self, queue, sjfNewThreadEvent=Event()):
        self.queue = queue  # CThreadQueue()
        self.finishedThreads = []
        # self.allThreads = []

        self.sjfThread = Thread(target=self.sjfRoutine)
        self.sjfFinishThreadEvent = Event()
        self.sjfNewThreadEvent = sjfNewThreadEvent
        self.sjfFinishThreadEvent.clear()
        self.sjfNewThreadEvent.clear()

        self.currentThread = None
        self.suspended = False
        self.enable = True
        self.name = DEFAULT_PROC_NAME

    # SJF planning
    # TODO: 1) execute planning with available resources of all thread
    # TODO: 2) write selecting and changing priority level
    # TODO: 3) write timer, whos run a little process in query
    def sjfRoutine(self):
        while self.enable:
            self.sjfFinishThreadEvent.wait()    # wait current executed thread
            if self.currentThread:
                self.currentThread['eventFinish'].wait()
                self.currentThread['status'] = 4    # set finish status
                # self.queue.startPlanning()
                # self.startPlanning()

            MAIN_MUTEX.acquire()
            try:
                self.queue.startPlanning()
                self.currentThread = self.queue.pop()   # can return None
            except Exception as e:
                print '[PROCESSOR_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
            finally:
                MAIN_MUTEX.release()

            if self.currentThread:
                self.currentThread['status'] = 2
                self.currentThread['processor'] = self.name
                self.currentThread['thread'].start()

                if not self.suspended:
                    self.currentThread['eventStart'].set()

                self.currentThread['eventFinish'].clear()
            else:
                MAIN_MUTEX.acquire()
                try:
                    if self.enable:
                        self.sjfNewThreadEvent.clear()  # all threads in queue are finished
                        self.sjfNewThreadEvent.wait()   # wait a new thread in queue
                except Exception as e:
                    print '[PROCESSOR_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
                finally:
                    MAIN_MUTEX.release()

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
