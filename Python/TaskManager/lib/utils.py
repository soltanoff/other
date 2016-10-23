#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtGui

from config import RESOURCES_LIST


def setResources(lar, lur, process=list()):
    if lar is not None:
        lar.clear()
        lar.addItems(RESOURCES_LIST)

    lur.clear()
    # parentItem = QtGui.QTreeWidgetItem('P')
    # self.addTopLevelItem(parentItem)
    # childItem = QtGui.QTreeWidgetItem('C')
    # parentItem.insertChild(0, childItem)
    for x in process:
        parentItem = QtGui.QTreeWidgetItem()
        parentItem.setText(0, x['name'])
        lur.insertTopLevelItem(0, parentItem)
        for x in x['resources']:
            childItem = QtGui.QTreeWidgetItem()
            childItem.setText(0, x)
            parentItem.insertChild(0, childItem)
