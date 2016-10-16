#!/usr/bin/env python
# -*- coding: utf8 -*-


class CThreadQueue(object):
    def __init__(self, queue=list(dict())):
        self._queue = queue

    def push(self, x):
        self._queue.append(x)

    def pop(self):
        return self._queue.pop(0)

    def __len__(self):
        return len(self._queue)

    def getList(self):
        return self._queue
