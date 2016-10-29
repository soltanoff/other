#!/usr/bin/env python
# -*- coding: utf8 -*-


class Process(object):
    def __init__(
            self,
            thread=None,
            name='none',
            processor='- none -',
            eventStart=None,
            eventFinish=None,
            priority=0,
            status=1,
            time=4,
            resources=list()
    ):
        self.thread = thread
        self.name = name
        self.processor = processor
        self.eventStart = eventStart
        self.eventFinish = eventFinish
        self.priority = priority
        self.status = status
        self.time = time
        self.resources = resources
