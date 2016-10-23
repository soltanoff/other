#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from config import DEFAULT_TASK_NAME, TASK_PRIORITY, RESOURCES_LIST
from ui.ui_taskdialog import Ui_TaskDialog


class CTaskDialog(QtGui.QDialog, Ui_TaskDialog):
    def __init__(self, parent):
        # initialize ui
        QtGui.QDialog.__init__(self)
        Ui_TaskDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.setWindowTitle(u'Добавить процесс...')

        self.edtTaskName.setText(DEFAULT_TASK_NAME % parent.taskIndex)
        self.cmbTaskPriority.addItems(TASK_PRIORITY)
        self.cmbTaskPriority.setCurrentIndex(1)

        self.lstAvailableResources.addItems(RESOURCES_LIST)
