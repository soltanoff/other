#!/usr/bin/env python
# -*- coding: utf8 -*-
import mysql.connector as db_bot


class DBConnector(object):
    def __init__(self, user='root', pwd=None, host='localhost', port=3306, database='db_bot'):
        self._db = db_bot.connect(user=user, password=pwd, host=host, port=port, database=database)
        self._cursor = self._db.cursor()

    def _query(self, stmt):
        self._cursor.execute(stmt)
        return self._cursor.fetchall()

    def get_message(self, idx):
        try:
            result = self._query(u'''
                SELECT
                    `message`
                  FROM
                    messages
                  WHERE
                    id = %s
                    AND deleted = 0;
                ''' % idx)

            return result[0][0]
        except Exception as error_msg:
            print u'[DB ERROR]: %s' % error_msg
            return u'ой да, ошибка 42'

    def get_exists(self, text):
        try:
            result = self._query(u'''
                SELECT
                    `id`
                  FROM
                    messages
                  WHERE
                    message = '%s'
                    AND deleted = 0;
                ''' % text)
            return result[0][0]
        except Exception as error_msg:
            print u'[DB ERROR]: %s' % error_msg
            return None

    def del_row(self, text):
        self._cursor.execute(u'''
            UPDATE messages m SET `deleted` = 1
            WHERE message = '%s';
            ''' % text)
        self._db.commit()

    def add_new_row(self, user_id, text, is_intelligent=False):
        if not self.get_exists(text):
            self._cursor.execute(u'''
                INSERT INTO
                    messages(creator_id, message, create_date, is_intelligent)
                VALUES(%s, '%s', CURRENT_DATE(), %s)
                ''' % (user_id, text, 1 if is_intelligent else 0)
            )
            self._db.commit()

    def select_ids(self, is_intelligent=False, is_question_answer=False):
        stmt = u'''
            SELECT
                id
            FROM
                messages
            WHERE
                deleted = 0
                %s
                %s
            ;
        ''' % (
            u'AND is_intelligent = 1' if is_intelligent else '',
            u'AND is_question_answer = 1' if is_question_answer else ''
        )
        return self._query(stmt)
