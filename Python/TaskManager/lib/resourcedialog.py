#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from lib.utils import setResources
from ui.ui_resourcedialog import Ui_ResourceDialog


class CResourceDialog(QtGui.QDialog, Ui_ResourceDialog):
    def __init__(self, parent):
        # initialize ui
        QtGui.QDialog.__init__(self)
        Ui_ResourceDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.setResources()
        self.resourceList = []

    def setResources(self, process=list()):
        setResources(self.lstAvailableResources, self.lstUsefullResources, process)
