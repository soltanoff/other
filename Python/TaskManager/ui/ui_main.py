# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(704, 429)
        self.gridLayout_3 = QtGui.QGridLayout(MainDialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gpbMain = QtGui.QGroupBox(MainDialog)
        self.gpbMain.setTitle(_fromUtf8(""))
        self.gpbMain.setObjectName(_fromUtf8("gpbMain"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gpbMain)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tblTask = QtGui.QTableView(self.gpbMain)
        self.tblTask.setObjectName(_fromUtf8("tblTask"))
        self.gridLayout_5.addWidget(self.tblTask, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gpbMain, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.btnNewTask = QtGui.QPushButton(MainDialog)
        self.btnNewTask.setObjectName(_fromUtf8("btnNewTask"))
        self.gridLayout_4.addWidget(self.btnNewTask, 0, 1, 1, 1)
        self.btnPauseCurrent = QtGui.QPushButton(MainDialog)
        self.btnPauseCurrent.setObjectName(_fromUtf8("btnPauseCurrent"))
        self.gridLayout_4.addWidget(self.btnPauseCurrent, 0, 3, 1, 1)
        self.btnResourceTable = QtGui.QPushButton(MainDialog)
        self.btnResourceTable.setEnabled(False)
        self.btnResourceTable.setObjectName(_fromUtf8("btnResourceTable"))
        self.gridLayout_4.addWidget(self.btnResourceTable, 0, 2, 1, 1)
        self.chkPauseAll = QtGui.QCheckBox(MainDialog)
        self.chkPauseAll.setCheckable(True)
        self.chkPauseAll.setChecked(True)
        self.chkPauseAll.setObjectName(_fromUtf8("chkPauseAll"))
        self.gridLayout_4.addWidget(self.chkPauseAll, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(_translate("MainDialog", "TaskManager v0.0.1", None))
        self.btnNewTask.setText(_translate("MainDialog", "Добавить процесс", None))
        self.btnPauseCurrent.setText(_translate("MainDialog", "Остановить текущий", None))
        self.btnResourceTable.setText(_translate("MainDialog", "Таблица ресурсов", None))
        self.chkPauseAll.setText(_translate("MainDialog", "Остановить все", None))

