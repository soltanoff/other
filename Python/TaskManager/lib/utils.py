#!/usr/bin/env python
# -*- coding: utf8 -*-
from threading import Event, Thread

from PyQt4 import QtGui

from config import RESOURCES_LIST
from logic.processing import Process


def setResources(lar, lur, process=list()):
    if lar is not None:
        lar.clear()
        lar.addItems(RESOURCES_LIST)

    lur.clear()
    for x in process:
        parentItem = QtGui.QTreeWidgetItem()
        parentItem.setText(0, x.name)
        lur.insertTopLevelItem(0, parentItem)
        for x in x.resources:
            childItem = QtGui.QTreeWidgetItem()
            childItem.setText(0, x)
            parentItem.insertChild(0, childItem)


def createProcess(name, target, priority=1, time=4, resources=list()):
    task = Process(
        name=name,
        eventFinish=Event(),
        eventStart=Event(),
        priority=priority,
        time=time,
        resources=resources
    )
    task.thread = Thread(
        target=target,
        args=(name, task.eventStart, task.eventFinish, time)
    )
    return task