#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
from threading import Thread, Condition, Lock

from PyQt4.QtCore import pyqtSignal

from logic.planning import createProcess, Processor
from logic.threadroutines import routine_1


class TmThread(Thread):
    def __init__(self, target, args):  # name, event_for_wait, event_for_set
        Thread.__init__(self)  # , target=target, args=args)

        self.__target = target
        self.__args = args
        self.__kwargs = None
        self.priority = 0
        self.time = 0
        #flag to Finish thread
        self.Finishd = False
        # Explicitly using Lock over RLock since the use of self.Finishd
        # break reentrancy anyway, and I believe using Lock could allow
        # one thread to Finish the worker, while another resumes; haven't
        # checked if Condition imposes additional limitations that would
        # prevent that. In Python 2, use of Lock instead of RLock also
        # boosts performance.
        self.Finish_cond = Condition(Lock())


    def Finish(self):
        self.Finishd = True
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.Finishd
        # and begin waiting until it's set back to False
        self.Finish_cond.acquire()

    #should just resume the thread
    def resume(self):
        self.Finishd = False
        # Notify so thread will wake after lock released
        self.Finish_cond.notify()
        # Now release the lock
        self.Finish_cond.release()


def ti():
    import time

    # старт таймера
    begin_time = time.time()

    # выполняем продолжительное действие
    time.sleep(1)

    # получаем время окончания действия с начала запуска таймера
    end_time = time.time()
    print end_time - begin_time


def main1():
    ThreadList = [
        createProcess('Thread #1', routine_1),
        createProcess('Thread #2', routine_1),
        createProcess('Thread #3', routine_1)
    ]
    # ============================================================
    f = Processor()
    for x in ThreadList:
        f.queue.push(x)
    f.start()
    # ============================================================
    f.ProcessorThread.join()


def main2():
    g = [
        {
            'priority': 0,
            'time': 50,
            'finished': 1
        },
        {
            'priority': 0,
            'time': 30,
            'finished': 0
        },
        {
            'priority': 1,
            'time': 10,
            'finished': 1
        },
        {
            'priority': 1,
            'time': 3,
            'finished': 1
        },
        {
            'priority': 2,
            'time': 2,
            'finished': 0
        },
        {
            'priority': 0,
            'time': 10,
            'finished': 0
        }
    ]
    # print sorted(g, key=lambda k: k['time'])
    print sorted(g, key=lambda k: (k['finished'], k['priority'], k['time']))
    g.sort(key=lambda k: (k['finished'], k['priority'], k['time']))
    print g


def main3():
    f =  os.listdir(os.getcwd() + '\\resources')
    pass


def main4():
    q = []

    class A(object):
        def __init__(self, q):
            self.w = q

    a = A(q)

    def f(g):
        g()

    # f = lambda x, y: x = y
    # pass


def main5():
    # FIXME: have some troubles when use 3 process
    def mainFunc(self):
        if self.currentThread:
            while not self.currentThread['eventFinish'].isSet():
                self.queue.changeStatus(checkFinished=True)
                self.queue.startPlanning()
                if self.currentThread['time'] <= TASK_TIME_QUANTUM[self.currentThread['priority']]:
                    return  # wait current executed thread
                else:
                    MAIN_MUTEX.acquire()
                    try:
                        self.secondCurrentThread = self.queue.last()
                    except Exception as e:
                        print '[PROCESSOR_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
                    finally:
                        MAIN_MUTEX.release()

                    if self.secondCurrentThread is None:
                        return

                    currentQuantum = TASK_TIME_QUANTUM[self.currentThread['priority']]
                    secondQuantum = TASK_TIME_QUANTUM[self.secondCurrentThread['priority']]
                    while not self.currentThread['eventFinish'].isSet():
                        if currentQuantum:  # and self.currentThread['status'] != 4:
                            self.currentThread['eventStart'].set()
                            self.currentThread['status'] = 2
                            if not secondQuantum:
                                secondQuantum = TASK_TIME_QUANTUM[self.secondCurrentThread['priority']]
                            currentQuantum -= 1
                            sleep(1)
                        else:
                            self.currentThread['eventStart'].clear()
                            self.currentThread['status'] = 3
                            if not self.secondCurrentThread['thread'].isAlive() and not self.secondCurrentThread['eventFinish'].isSet():
                                try:
                                    self.secondCurrentThread['thread'].start()
                                except:
                                    pass

                            self.secondCurrentThread['processor'] = self.name
                            self.secondCurrentThread['status'] = 2
                            self.secondCurrentThread['eventStart'].set()
                            if secondQuantum:
                                secondQuantum -= 1
                                sleep(1)
                            else:
                                self.secondCurrentThread['eventStart'].clear()
                                if self.secondCurrentThread['eventFinish'].isSet():
                                    self.secondCurrentThread['status'] = 4
                                else:
                                    self.secondCurrentThread['status'] = 3
                                currentQuantum = TASK_TIME_QUANTUM[self.currentThread['priority']]
                        self.queue.changeStatus(checkFinished=True)
                    self.currentThread['status'] = 3

    def sjfRoutine1(self):
        while self.enable:
            self.queue.changeStatus(checkFinished=True)
            self.sjfFinishThreadEvent.wait()    # wait current executed thread
            # self.mainFunc()
            if self.currentThread:
                self.currentThread['eventFinish'].wait()
                self.currentThread['status'] = 4    # set finish status
                self.queue.startPlanning()
                # self.startPlanning()
            # elif self.secondCurrentThread:
            #     self.secondCurrentThread['eventFinish'].wait()
                # self.secondCurrentThread['status'] = 4    # set finish status


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

                # if not self.currentThread['thread'].isAlive():
                #     try:
                self.currentThread['thread'].start()
                #    except:
                #        print '[START_PROCESS] pew pew'

                if not self.suspended:
                    self.currentThread['eventStart'].set()

                self.currentThread['eventFinish'].clear()
            else:
                # MAIN_MUTEX.acquire()
                # try:
                #    if self.enable:
                self.queue.changeStatus(checkFinished=True)
                self.sjfNewThreadEvent.clear()  # all threads in queue are finished
                self.sjfNewThreadEvent.wait()   # wait a new thread in queue
                # except Exception as e:
                #    print '[PROCESSOR_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
                # finally:
                #    MAIN_MUTEX.release()

        # if self.currentThread and self.currentThread['thread'].isAlive():
        #    self.currentThread['thread'].terminate()
        print u'[TaskManager] Closing...'

    def sjfRoutine_(self):
        while self.enable:
            self.sjfFinishThreadEvent.wait()  # wait current executed thread
            self.mainFunc()
            if self.currentThread:
                self.currentThread['eventFinish'].wait()
                self.currentThread['status'] = 4  # set finish status
                # self.queue.startPlanning()
                # self.startPlanning()

            MAIN_MUTEX.acquire()
            try:
                self.queue.startPlanning()
                self.currentThread = self.queue.pop()  # can return None
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
                        self.sjfNewThreadEvent.wait()  # wait a new thread in queue
                except Exception as e:
                    print '[PROCESSOR_ERROR] %s' % e.msg if hasattr(e, 'msg') else e.message
                finally:
                    MAIN_MUTEX.release()

                    # if self.currentThread and self.currentThread['thread'].isAlive():
                    #    self.currentThread['thread'].terminate()
        print u'[TaskManager] Closing...'


def main():
    def callback(name, address):
        print("Name=%s and address=%s" % (name, address))

    signal = pyqtSignal()
    signal.connect(callback)

    # Mistake the first argument for a tuple.
    signal.emit(names=('marcus', 'ottosson'), address='earth')
    # TypeError: callback() got an unexpected keyword argument 'names'

    # When actually, its a single string value.
    signal.emit(name='marcus ottosson', address='earth')
    # Name=marcus ottosson and address=earth

    # Of course, non-keyword arguments works too.
    signal.emit('marcus ottosson', 'earth')


if __name__ == '__main__':
    main()
