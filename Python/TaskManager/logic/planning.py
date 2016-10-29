#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread

from config import DEFAULT_PROCESSOR_NAME, MAIN_MUTEX


class Processor(object):
    def __init__(self, queue, sjfNewThreadEvent=Event()):
        self.queue = queue
        self.finishedThreads = []

        self.sjfThread = Thread(target=self.sjfRoutine)
        self.sjfFinishThreadEvent = Event()
        self.sjfNewThreadEvent = sjfNewThreadEvent
        self.sjfFinishThreadEvent.clear()
        self.sjfNewThreadEvent.clear()

        self.currentThread = None
        self.secondCurrentThread = None
        self.suspended = False
        self.enable = True
        self.name = DEFAULT_PROCESSOR_NAME

        self.firstThread = None
        self.lastThread = None

    def getProcess(self, process, isLast=False):
        if process:
            process.status = 4  # set finish status
        MAIN_MUTEX.acquire()
        try:
            self.queue.startPlanning()
            result = self.queue.last() if isLast else self.queue.pop()  # can return None
        except Exception as e:
            print '[PROCESSOR_ERROR] %s: %s' % (
                self.name,
                e.msg if hasattr(e, 'msg') else e.message
            )
            result = None
        finally:
            MAIN_MUTEX.release()
        return result

    def execProcess(self, process):
        if process:
            process.status = 2
            process.processor = self.name
            process.thread.start()

            if not self.suspended:
                process.eventStart.set()

            process.eventFinish.clear()

    def waitNewProcess(self):
        MAIN_MUTEX.acquire()
        try:
            self.queue.startPlanning()
            if self.enable:
                self.sjfNewThreadEvent.clear()  # all threads in queue are finished
                self.sjfNewThreadEvent.wait()  # wait a new thread in queue
        except Exception as e:
            print '[PROCESSOR_ERROR] %s: %s' % (
                self.name,
                e.msg if hasattr(e, 'msg') else e.message
            )
            result = None
        finally:
            MAIN_MUTEX.release()

    def firstProcess(self):
        self.sjfFinishThreadEvent.wait()  # wait current executed thread
        if self.firstThread and not self.firstThread.eventFinish.isSet():
            # TODO: wait by timeouts. See signature of wait()
            self.firstThread.eventFinish.wait(timeout=1)
            print 'Timeout'
        else:
            self.firstThread = self.getProcess(self.firstThread)
            self.execProcess(self.firstThread)

        if self.firstThread is None:
            self.waitNewProcess()

    def lastProcess(self):
        self.sjfFinishThreadEvent.wait()  # wait current executed thread
        if self.lastThread and not self.lastThread.eventFinish.isSet():
            sleep(1)
        else:
            self.lastThread = self.getProcess(self.lastThread, isLast=True)
            self.execProcess(self.lastThread)

        if self.lastThread is None:
            self.waitNewProcess()

    # SJF planning
    # TODO: 1) execute planning with available resources of all thread
    # TODO: 2) задать минимальный квант времени выполнения задач в приоритете
    # TODO: 3) организовать работу с файлами, повышение приоритетов задач
    def sjfRoutine(self):
        while self.enable:
            self.firstProcess()

    def suspendCurrentThread(self):
        self.suspended = True
        self.sjfFinishThreadEvent.clear()
        if self.currentThread and self.currentThread.thread.isAlive():
            self.currentThread.eventStart.clear()
            self.currentThread.status = 1    # ready

    def resumeCurrentThread(self):
        self.suspended = False
        self.sjfFinishThreadEvent.set()
        self.sjfNewThreadEvent.set()
        if self.currentThread and self.currentThread.thread.isAlive():
            self.currentThread.eventStart.set()
            self.currentThread.status = 2    # execute

    def start(self):
        self.sjfThread.start()
