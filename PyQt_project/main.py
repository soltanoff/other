#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from main_form import Ui_ClientInfo
from db_connection import create_connection


class Main(QMainWindow):
    search_id = []

    gender_name = {
        0: "Неопределено",
        1: "Мужчина",
        2: "Женщина"
    }

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ClientInfo()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.get_user_info)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.searchResult.doubleClicked.connect(self.select_client)
        create_connection()

    @staticmethod
    def show_dialog(text):
        msg = QMessageBox()
        msg.setText(str(text))
        msg.setWindowTitle("Информация")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def select_client(self):
        for item in self.ui.searchResult.selectedIndexes():
            self.ui.lineEdit.setText(str(self.search_id[item.row()]))
            self.get_user_info()

    def set_search_fields(self, query_string):
        if len(self.ui.searchLastName.text()) > 0:
            query_string += " and C.lastName = :lastname"

        if len(self.ui.searchFirstName.text()) > 0:
            query_string += " and C.firstName = :firstname"

        if len(self.ui.searchPatrName.text()) > 0:
            query_string += " and C.patrName = :patrname"

        if len(self.ui.searchDocSerial.text()) > 0:
            query_string += " and CD.serial = :docserial"

        if len(self.ui.searchDocNumber.text()) > 0:
            query_string += " and CD.number = :docnumber"

        if len(self.ui.searchDocType.text()) > 0:
            query_string += " and DT.name = :doctype"

        if len(self.ui.searchOmcSerial.text()) > 0:
            query_string += " and CP.serial = :omcserial"

        if len(self.ui.searchOmcNumber.text()) > 0:
            query_string += " and CP.number = :omcnumber"

        if len(self.ui.searchOmcType.text()) > 0:
            query_string += " and PK.name = :omctype"
        return query_string

    def set_query_fields(self, query):
        if len(self.ui.searchLastName.text()) > 0:
            query.bindValue(":lastname", self.ui.searchLastName.text())

        if len(self.ui.searchFirstName.text()) > 0:
            query.bindValue(":firstname", self.ui.searchFirstName.text())

        if len(self.ui.searchPatrName.text()) > 0:
            query.bindValue(":patrname", self.ui.searchPatrName.text())

        if len(self.ui.searchDocSerial.text()) > 0:
            query.bindValue(":docserial", self.ui.searchDocSerial.text())

        if len(self.ui.searchDocNumber.text()) > 0:
            query.bindValue(":docnumber", self.ui.searchDocNumber.text())

        if len(self.ui.searchDocType.text()) > 0:
            query.bindValue(":doctype", self.ui.searchDocType.text())

        if len(self.ui.searchOmcSerial.text()) > 0:
            query.bindValue(":omcserial", self.ui.searchOmcSerial.text())

        if len(self.ui.searchOmcNumber.text()) > 0:
            query.bindValue(":omcnumber", self.ui.searchOmcNumber.text())

        if len(self.ui.searchOmcType.text()) > 0:
            query.bindValue(":omctype", self.ui.searchOmcType.text())
        return query

    def search(self):
        self.search_id.clear()
        query_string = "SELECT " \
                       "C.id, C.lastName, C.firstName, C.patrName" \
                       " FROM " \
                       " client as C, " \
                       " clientpolicy as CP, " \
                       " rbpolicykind as PK," \
                       " clientdocument as CD," \
                       " rbdocumenttype as DT" \
                       " WHERE" \
                       " C.id = CP.client_id and" \
                       " C.id = CD.client_id and" \
                       " PK.id = CP.policykind_id and" \
                       " DT.id = CD.documentType_id"

        query = QSqlQuery()

        query_string = self.set_search_fields(query_string)
        query.prepare(query_string)
        query = self.set_query_fields(query)

        query.exec_()

        model = QStandardItemModel(self.ui.searchResult)
        while query.next():
            item = QStandardItem()
            item.setEditable(False)
            item.setText(query.value(1) + " " + query.value(2) + " " + query.value(3) + " " +
                         "[id:" + str(query.value(0)) + "]")
            self.search_id.append(query.value(0))
            model.appendRow(item)

        self.ui.searchResult.setModel(model)
        if model.rowCount() == 0:
            self.show_dialog("Записи не найдены.")


    def get_user_info(self):
        if self.ui.lineEdit.text().isdigit():
            query = QSqlQuery()
            query.prepare(
                "SELECT "
                " C.lastName, C.firstName, C.patrName, C.birthDate, C.sex,"
                " CP.serial, CP.number, CP.begDate, CP.endDate,"
                " PK.name,"
                " DT.name, CD.serial, CD.number, CD.date"
                " FROM "
                " client as C, "
                " clientpolicy as CP, "
                " rbpolicykind as PK,"
                " clientdocument as CD,"
                " rbdocumenttype as DT"
                " WHERE"
                " C.id = CP.client_id and"
                " C.id = CD.client_id and"
                " PK.id = CP.policykind_id and"
                " DT.id = CD.documentType_id and"
                " C.id = :id"
            )
            query.bindValue(":id", self.ui.lineEdit.text())
            query.exec_()
            if query.next():
                self.ui.lastName.setText(query.value(0))
                self.ui.firstName.setText(query.value(1))
                self.ui.patrName.setText(query.value(2))
                self.ui.birthDate.setDate(query.value(3))
                self.ui.sex.setText(self.gender_name[query.value(4)])
                self.ui.omcSerial.setText(query.value(5))
                self.ui.omcNumber.setText(query.value(6))
                self.ui.omcBegDate.setDate(query.value(7))
                self.ui.omcEndDate.setDate(query.value(8))
                self.ui.omcKind.setText(query.value(9))
                self.ui.docType.setText(query.value(10))
                self.ui.docSerial.setText(query.value(11))
                self.ui.docNumber.setText(query.value(12))
                self.ui.docDate.setDate(query.value(13))
            else:
                self.show_dialog("Пациент не найден.")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    main()
