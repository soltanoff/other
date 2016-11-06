# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resourcedialog.ui'
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

class Ui_ResourceDialog(object):
    def setupUi(self, ResourceDialog):
        ResourceDialog.setObjectName(_fromUtf8("ResourceDialog"))
        ResourceDialog.resize(826, 414)
        self.gridLayout_2 = QtGui.QGridLayout(ResourceDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(ResourceDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lstAvailableResources = QtGui.QListWidget(self.groupBox)
        self.lstAvailableResources.setObjectName(_fromUtf8("lstAvailableResources"))
        self.gridLayout_4.addWidget(self.lstAvailableResources, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(ResourceDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(290, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lstUsefullResources = QtGui.QTreeWidget(self.groupBox_2)
        self.lstUsefullResources.setObjectName(_fromUtf8("lstUsefullResources"))
        self.gridLayout_5.addWidget(self.lstUsefullResources, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.btnOk = QtGui.QPushButton(ResourceDialog)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.gridLayout_2.addWidget(self.btnOk, 1, 1, 1, 1)

        self.retranslateUi(ResourceDialog)
        QtCore.QObject.connect(self.btnOk, QtCore.SIGNAL(_fromUtf8("clicked()")), ResourceDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ResourceDialog)

    def retranslateUi(self, ResourceDialog):
        ResourceDialog.setWindowTitle(_translate("ResourceDialog", "Таблица ресурсов", None))
        self.groupBox.setTitle(_translate("ResourceDialog", "Список всех доступных ресурсов", None))
        self.groupBox_2.setTitle(_translate("ResourceDialog", "Монитор использования ресурсов", None))
        self.lstUsefullResources.headerItem().setText(0, _translate("ResourceDialog", "Процессы", None))
        self.btnOk.setText(_translate("ResourceDialog", "ОК", None))

