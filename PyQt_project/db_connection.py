#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
from PyQt4 import QtSql
from PyQt4.QtGui import *

CFG_FILENAME = 'settings.ini'


def parse_cfg():
    cfg = configparser.ConfigParser()
    cfg['DB_SETTINGS'] = {
        'dbms': 'QMYSQL',
        'hostname': '127.0.0.1',
        'db_name': 'db_vista',
        'db_user': 'root',
        'db_pass': ''
    }
    cfg.read(CFG_FILENAME)
    return cfg


def create_connection():
    cfg = parse_cfg()
    db = QtSql.QSqlDatabase.addDatabase(cfg['DB_SETTINGS']['dbms'])
    db.setHostName(cfg['DB_SETTINGS']['hostname'])
    db.setDatabaseName(cfg['DB_SETTINGS']['db_name'])
    db.setUserName(cfg['DB_SETTINGS']['db_user'])
    db.setPassword(cfg['DB_SETTINGS']['db_pass'])
    if db.open() == False:
        QMessageBox.critical(None, "Database Error", db.lastError().text())