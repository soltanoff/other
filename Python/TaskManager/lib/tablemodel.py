#!/usr/bin/env python
# -*- coding: utf8 -*-
from PyQt4 import QtCore, QtGui

from config import TASK_PRIORITY, TASK_STATUS


class CTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, body=list()):
        QtCore.QAbstractTableModel.__init__(self)
        self.parent = parent
        self.header = [u'Имя процесса', u'Приоритет', u'Статус', u'Время выполнения']
        self.body = body

    def rowCount(self, parent=None):
        return len(self.body)

    def columnCount(self, parent=None):
        return len(self.header)

    def data(self, index, role):
        self.layoutChanged.emit()

        if role == QtCore.Qt.FontRole:
            row = index.row()
            col = index.column()
            if col == 2 and self.body[row]['status'] == 2:
                font = QtGui.QFont()
                font.setBold(True)
                font.setItalic(True)
                return QtCore.QVariant(font)
            if col == 2 and self.body[row]['status'] == 3:
                font = QtGui.QFont()
                font.setBold(True)
                return QtCore.QVariant(font)

        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return QtCore.QVariant()
        value = ''
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 0:
                value = self.body[row]['name']
            elif col == 1:
                value = TASK_PRIORITY[self.body[row]['priority']]
            elif col == 2:
                value = TASK_STATUS[self.body[row]['status']]
            elif col == 3:
                value = self.body[row]['time']

        return QtCore.QVariant(value)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.header[section])
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.QVariant(QtCore.Qt.AlignCenter)
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant("%s" % str(section + 1))
        return QtCore.QVariant()
