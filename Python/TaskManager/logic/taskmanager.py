#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from config import VERSION
from lib.tablemodel import CTableModel
from lib.taskdialog import CTaskDialog
from lib.threadqueue import CThreadQueue
from lib.threadroutines import routine_1
from logic.planning import SJF, createProcess
from ui.ui_main import Ui_MainDialog


class CTaskManager(QtGui.QDialog, Ui_MainDialog):
    def __init__(self):
        # initialize ui
        QtGui.QDialog.__init__(self)
        Ui_MainDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.setWindowTitle('TaskManager %s' % VERSION)

        self.tblModel = CTableModel(self)
        #self.tblProxyModel = QtGui.QSortFilterProxyModel(self)
        #self.tblProxyModel.setSourceModel(self.tblModel)

        self.tblTask.setModel(self.tblModel)  # tblProxyModel)
        self.tblTask.verticalHeader().setVisible(True)

        self.tblTask.resizeColumnsToContents()
        self.tblTask.autoFillBackground()
        self.tblTask.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblTask.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.tblTask.setAlternatingRowColors(True)

        for col in xrange(self.tblTask.model().columnCount()):
            if col in [3, 1, 2]:
                self.tblTask.horizontalHeader().resizeSection(col, 60)
                self.tblTask.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.ResizeToContents)
            elif col == 0:
                self.tblTask.horizontalHeader().resizeSection(col, 500)
                self.tblTask.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.Stretch)

        self.taskIndex = 0

        self.manager = SJF()
        self.manager.suspended = self.chkPauseAll.isChecked()
        self.manager.start()


    @QtCore.pyqtSlot(bool)
    def on_chkPauseAll_toggled(self, checked):
        if checked:
            self.manager.suspendCurrentThread()
        else:
            self.manager.resumeCurrentThread()

    @QtCore.pyqtSlot()
    def on_btnNewTask_clicked(self):
        dlg = CTaskDialog(self)
        if dlg.exec_():
            x = createProcess(
                    dlg.edtTaskName.text(),
                    routine_1,
                    dlg.cmbTaskPriority.currentIndex(),
                    dlg.spbTaskTime.value()
            )
            self.manager.queue.push(x)
            self.manager.allThreads.append(x)
            self.tblTask.model().body = self.manager.allThreads
            self.tblTask.model().layoutChanged.emit()
            self.taskIndex += 1
