#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

from PyQt4 import QtGui

from config import VERSION
from lib.taskmanager import CTaskManager


def main():
    try:
        print u'[TaskManager] Current programm version: %s' % VERSION

        QtGui.qApp = QtGui.QApplication(sys.argv)
        win = CTaskManager(processorCount=5)
        win.show()
        QtGui.qApp.exec_()
    except Exception as e:
        QtGui.QMessageBox.warning(
            None,
            u'Предупреждение',
            u'Непредвиденная ошибка:\n%s' % e.msg if hasattr(e, 'msg') else e.message,
            QtGui.QMessageBox.Ok
        )
    finally:
        sys.exit()

if __name__ == '__main__':
    main()
