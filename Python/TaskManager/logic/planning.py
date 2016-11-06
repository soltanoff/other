#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread

from config import DEFAULT_PROCESSOR_NAME, MAIN_MUTEX, NEW_TASK_MUTEX, TASK_TIME_QUANTUM


class Processor(object):
    def __init__(self, queue, sjfNewThreadEvent=Event()):
        self.queue = queue
        self.finishedThreads = []

        self.sjfThread = Thread(target=self.sjfRoutine)
        self.sjfFinishThreadEvent = Event()
        self.sjfNewThreadEvent = sjfNewThreadEvent
        self.sjfFinishThreadEvent.clear()
        self.sjfNewThreadEvent.clear()

        self.suspended = False
        self.enable = True
        self.name = DEFAULT_PROCESSOR_NAME

        self.firstThread = None
        self.lastThread = None
        self.goNext = False

        # exec last task in queue where executing first task
        self.onlyFirst = False

    def getProcess(self, process, isLast=False):
        if process:
            process.status = 4  # set finish status
        MAIN_MUTEX.acquire()
        try:
            self.queue.startPlanning()
            result = self.queue.last() if isLast else self.queue.pop()  # can return None
            if result:
                result.status = 2
                result.processor = self.name
                result.thread.start()

        except Exception as e:
            print '[PROCESSOR_ERROR] %s: %s' % (
                self.name,
                e.msg if hasattr(e, 'msg') else e.message
            )
            result = None
        finally:
            MAIN_MUTEX.release()
            pass
        return result

    def execProcess(self, process):
        if process:
            if not self.suspended:
                process.eventStart.set()

            process.eventFinish.clear()

    def waitNewProcess(self):
        NEW_TASK_MUTEX.acquire()
        try:
            # self.queue.startPlanning()
            if self.enable:
                self.sjfNewThreadEvent.clear()  # all threads in queue are finished
                self.sjfNewThreadEvent.wait()  # wait a new thread in queue
        except Exception as e:
            print '[PROCESSOR_ERROR] %s: %s' % (
                self.name,
                e.msg if hasattr(e, 'msg') else e.message
            )
        finally:
            NEW_TASK_MUTEX.release()

    def firstProcess(self):
        self.sjfFinishThreadEvent.wait()  # wait current executed thread
        if self.firstThread and not self.firstThread.eventFinish.isSet():
            self.firstThread.status = 2
            self.firstThread.eventStart.set()
            self.firstThread.eventFinish.wait(timeout=TASK_TIME_QUANTUM[0])
            self.firstThread.eventStart.clear()
            if not self.firstThread.eventFinish.isSet():
                self.firstThread.status = 3
            # print 'Timeout firstThread'
            self.goNext = True
        else:
            self.firstThread = self.getProcess(self.firstThread)
            self.execProcess(self.firstThread)

        if self.firstThread is None:
            if self.lastThread is not None and not self.lastThread.eventFinish.isSet():
                self.firstThread = self.lastThread
            else:
            # elif self.firstThread.status == 4:
                self.waitNewProcess()

    def lastProcess(self):
        self.sjfFinishThreadEvent.wait()  # wait current executed thread
        if self.lastThread and not self.lastThread.eventFinish.isSet():
            self.lastThread.status = 2
            self.lastThread.eventStart.set()
            self.lastThread.eventFinish.wait(timeout=TASK_TIME_QUANTUM[1])
            self.lastThread.eventStart.clear()
            if not self.lastThread.eventFinish.isSet():
                self.lastThread.status = 3
            # print 'Timeout lastThread'
            self.goNext = False
        else:
            self.lastThread = self.getProcess(self.lastThread, isLast=True)
            if self.lastThread is None:
                self.goNext = False
            self.execProcess(self.lastThread)

    # SJF planning
    # TODO: 1) test resource filtration and task taking
    def sjfRoutine(self):
        while self.enable:
            if not self.goNext or self.onlyFirst:
                self.firstProcess()
            else:
                self.lastProcess()

    def _setEnable(self, thread, enable=True):
        if thread and thread.thread.isAlive():
            if enable:
                thread.eventStart.set()
                thread.status = 2    # execute
            else:
                thread.eventStart.clear()
                thread.status = 1  # ready

    def suspendCurrentThread(self):
        self.suspended = True
        self.sjfFinishThreadEvent.clear()
        self._setEnable(self.firstThread, not self.suspended)
        self._setEnable(self.lastThread, not self.suspended)

    def resumeCurrentThread(self):
        self.suspended = False
        self.sjfFinishThreadEvent.set()
        self.sjfNewThreadEvent.set()
        self._setEnable(self.firstThread)
        self._setEnable(self.lastThread)

    def start(self):
        self.sjfThread.start()
