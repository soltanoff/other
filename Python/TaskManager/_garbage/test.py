#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
from threading import Thread, Condition, Lock

from logic.planning import createProcess, SJF
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
    f = SJF()
    for x in ThreadList:
        f.queue.push(x)
    f.start()
    # ============================================================
    f.sjfThread.join()


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


def main():
    pass


if __name__ == '__main__':
    main()
