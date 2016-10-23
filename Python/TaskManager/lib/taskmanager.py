#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


from config import VERSION
from lib.resourcedialog import CResourceDialog
from lib.tablemodel import CTableModel
from lib.taskdialog import CTaskDialog
from lib.utils import setResources
from logic.planning import SJF, createProcess
from logic.threadroutines import routine_1
from ui.ui_taskmanager import Ui_MainDialog


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
        # self.tblProxyModel = QtGui.QSortFilterProxyModel(self)
        # self.tblProxyModel.setSourceModel(self.tblModel)

        self.tblTask.setModel(self.tblModel)  # tblProxyModel)
        self.tblTask.verticalHeader().setVisible(True)

        # self.tblTask.resizeColumnsToContents()
        self.tblTask.autoFillBackground()
        self.tblTask.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblTask.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        # self.tblTask.row
        self.tblTask.setAlternatingRowColors(True)

        for col in xrange(self.tblTask.model().columnCount()):
            if col in [3, 1]:
                self.tblTask.horizontalHeader().resizeSection(col, 60)
                self.tblTask.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.ResizeToContents)
            elif col == 0:
                self.tblTask.horizontalHeader().resizeSection(col, 500)
                self.tblTask.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.Stretch)
            elif col == 2:
                self.tblTask.horizontalHeader().resizeSection(col, 65)
                self.tblTask.horizontalHeader().setResizeMode(col, QtGui.QHeaderView.Custom)

        self.taskIndex = 0

        self.manager = SJF()
        self.manager.suspended = self.chkPauseAll.isChecked()
        self.manager.start()

        self.resources = CResourceDialog(None)

    @QtCore.pyqtSlot(bool)
    def on_chkPauseAll_toggled(self, checked):
        if checked:
            self.manager.suspendCurrentThread()
        else:
            self.manager.resumeCurrentThread()
        self.tblTask.model().layoutChanged.emit()

    @QtCore.pyqtSlot()
    def on_btnNewTask_clicked(self):
        dlg = CTaskDialog(self)
        # dlg.setResources(self.resources.resourceList)
        if dlg.exec_():
            x = createProcess(
                dlg.edtTaskName.text(),
                routine_1,
                dlg.cmbTaskPriority.currentIndex(),
                dlg.spbTaskTime.value(),
                [x.text() for x in dlg.lstAvailableResources.selectedItems()]
            )
            self.manager.queue.push(x)
            self.manager.startPlanning()
            # self.manager.startPlanning()
            if not self.manager.sjfNewThreadEvent.isSet():
                self.manager.sjfNewThreadEvent.set()
            # self.manager.allThreads.append(x)
            self.tblTask.model().body = self.manager.queue.data
            self.tblTask.model().layoutChanged.emit()
            # self.tblTask.resizeColumnsToContents()
            self.taskIndex += 1

            self.setResources(self.manager.queue.data)
        del dlg

    @QtCore.pyqtSlot()
    def on_btnResourceTable_clicked(self):
        self.resources.setResources(self.manager.queue.data)
        self.resources.exec_()

    def setResources(self, process=list()):
        setResources(None, self.lstUsefullResources, process[::-1])

    def closeEvent(self, event):
        self.manager.enable = False

        if self.manager.suspended:
            self.manager.resumeCurrentThread()
        elif not self.manager.sjfNewThreadEvent.isSet():
            self.manager.sjfNewThreadEvent.set()

        event.accept()
