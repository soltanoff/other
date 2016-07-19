#!/usr/bin/env python
# -*- coding: utf8 -*-
import mysql.connector as db_bot
import random
import vk_api
import time
# import re

login = u'+79531472458'
password = u'huluna2013'
admins = [77698338, 96996256]
version = 'v0.8.1'


class DBConnector(object):
    def __init__(self, user='root', pwd=None, host='localhost', port=3306, database='db_bot'):
        self._db = db_bot.connect(user=user, password=pwd, host=host, port=port, database=database)
        self._cursor = self._db.cursor()

    def _query(self, stmt):
        self._cursor.execute(stmt)
        return self._cursor.fetchall()

    def get_message(self, id):
        try:
            result = self._query(u'''
                SELECT
                    `message`
                  FROM
                    messages
                  WHERE
                    id = %s
                    AND deleted = 0;
                ''' % id)

            return result[0][0]
        except Exception:
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
        except Exception:
            return None

    def del_row(self, text):
        self._cursor.execute(u'''
            UPDATE messages m SET `deleted` = 1
            WHERE message = '%s';
            ''' % text)
        self._db.commit()

    def add_new_row(self, user_id, text):
        if not self.get_exists(text):
            self._cursor.execute(u'''
                INSERT INTO
                    messages(creator_id, message, create_date)
                VALUES(%s, '%s', CURRENT_DATE())
                ''' % (user_id, text)
            )
            self._db.commit()

    def select_ids(self):
        return self._query('''
            SELECT id FROM messages WHERE deleted = 0;
            ''')


class MainBot(object):
    def __init__(self):
        self._vk_session = vk_api.VkApi(login, password, captcha_handler=self._captcha_handler)

        try:
            self._vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return

        self._vk = self._vk_session.get_api()
        self._bot_name = self._get_user_name(None)
        self._db = DBConnector()
        self._ignore_msgs = self._read_history()
        self._ans_list = self._db.select_ids()

        self._disable = False

    @staticmethod
    def _captcha_handler(captcha):
        """
            При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    @staticmethod
    def _read_history():
        try:
            f = open('ignore_msgs.cfg', 'r')
            result = []
            for x in f:
                result.append(x[:len(x)-1])
            f.close()
            return result
        except Exception:
            return []

    @staticmethod
    def _write_history(ignore_msgs):
        try:
            f = open('ignore_msgs.cfg', 'w')
            for x in ignore_msgs:
                f.write(x + '\n')
            f.close()
        except Exception:
            pass

    def _get_user_name(self, user_id):
        return u'%s' % self._vk.users.get(user_ids=[user_id])[0]['first_name']

    def _add_msg_to_ignore(self, msg):
        if 'chat_id' in msg:
            self._ignore_msgs.append('%s-%s-%s' % (msg['chat_id'], msg['id'], msg['user_id']))
        else:
            self._ignore_msgs.append('NONE-%s-%s' % (msg['id'], msg['user_id']))
        self._write_history(self._ignore_msgs)

    def _is_msg_in_ignore(self, msg):
        result = False
        if 'chat_id' in msg:
            result = '%s-%s-%s' % (msg['chat_id'], msg['id'], msg['user_id']) in self._ignore_msgs
        else:
            result = 'NONE-%s-%s' % (msg['id'], msg['user_id']) in self._ignore_msgs
        return result

    def _send(self):
        pass

    def _send_message(self, user_id, text, is_chat=False, forward_messages=None):
        if is_chat:
            self._vk.messages.send(
                chat_id=user_id,
                message=text,
                forward_messages=forward_messages
            )
        else:
            self._vk.messages.send(
                user_id=user_id,
                message=text,
                forward_messages=forward_messages
            )

    def _send_message_from_db(self, msg):
        if 'chat_id' in msg:
            self._vk.messages.send(
                chat_id=msg['chat_id'],
                message='%s, %s' % (
                    self._get_user_name(msg['user_id']),
                    self._db.get_message(self._ans_list[random.randint(0, len(self._ans_list)-1)][0])
                )
            )
        else:
            self._vk.messages.send(
                user_id=msg['user_id'],
                message='%s, %s' % (
                    self._get_user_name(msg['user_id']),
                    self._db.get_message(self._ans_list[random.randint(0, len(self._ans_list)-1)][0])
                )
            )

    @staticmethod
    def _prepare_msg(msg):
        return msg.replace('\'', '\\\'')

    def _remember_new_data(self, msg):
        self._db.add_new_row(msg['user_id'], self._prepare_msg(msg['body'][13:]))
        if 'chat_id' in msg:
            self._send_message(
                msg['chat_id'],
                u"%s, океюшки. Теперь я запомнил: \"%s\" :)" % (
                    self._get_user_name(msg['user_id']),
                    self._prepare_msg(msg['body'][13:])
                ),
                is_chat=True
            )
        else:
            self._send_message(
                msg['user_id'],
                u"%s, океюшки. Теперь я запомнил: \"%s\" :)" % (
                    self._get_user_name(msg['user_id']),
                    self._prepare_msg(msg['body'][13:])
                )
            )
        print(u'Remember new data: from %s, msg: %s' % (msg['user_id'], self._prepare_msg(msg['body'][13:])))
        self._ans_list = self._db.select_ids()

    def _forget_data(self, msg):
        self._db.del_row(self._prepare_msg(msg['body'][12:]))
        if 'chat_id' in msg:
            self._send_message(
                msg['chat_id'],
                u"%s, океюшки :( Пожалуй забуду: \"%s\"" % (
                    self._get_user_name(msg['user_id']),
                    self._prepare_msg(msg['body'][12:])
                ),
                is_chat=True
            )
        else:
            self._send_message(
                msg['user_id'],
                u"%s, океюшки :( Пожалуй забуду: \"%s\"" % (
                    self._get_user_name(msg['user_id']),
                    self._prepare_msg(msg['body'][12:])
                )
            )
        # self._send_message(msg['user_id'], u"%s, океюшки :( Пожалуй забуду: \"\"" % (
        # self._get_user_name(msg['user_id']), self._prepare_msg(msg['body'][13:])))
        print(u'Remove data: from %s, msg: %s' % (msg['user_id'], self._prepare_msg(msg['body'][12:])))
        self._ans_list = self._db.select_ids()

    def _get_help(self):
        return u"""
            Моя текущая версия: version

            Список моих команд на сегодня:
              * Выучить что-то новое: name запомни <предложение/фраза>
              * [Для админов] Забыть что-то старое: name забудь <предложение/фраза>
              * Выдать вероятность события: name инфа <фраза/название/событие>
              * Просто попиздеть: name <предложение/фраза>
              * [Для админов] Выключить бота: name завали ебало
              * [Для админов] Включить бота : name камбекнись

            Список разработчиков:
              * Илья - http://vk.com/id96996256
            Список админов:
              * Илья - http://vk.com/id96996256
              * Дмитрий - http://vk.com/id77698338
        """.replace('name', self._bot_name).replace('version', version)

    def _analyze_messages(self, msg_list=None):
        # msg_answer = []
        if msg_list:
            for msg in msg_list:
                if not self._disable:
                    if msg['body'][:17] == u'%s завали ебало' % self._bot_name and not self._is_msg_in_ignore(msg):
                        self._add_msg_to_ignore(msg)
                        if msg['user_id'] in admins:
                            if 'chat_id' in msg:
                                self._send_message(
                                    user_id=msg['chat_id'],
                                    text=u'%s, океюшки! Уебываю...' % self._get_user_name(msg['user_id']),
                                    is_chat=True)
                            else:
                                self._send_message(
                                    user_id=msg['user_id'],
                                    text=u'%s, океюшки! Уебываю...' % self._get_user_name(msg['user_id']),
                                    is_chat=False)
                            self._disable = True
                        continue
                    if msg['body'][:12] == u'%s команды' % self._bot_name and not self._is_msg_in_ignore(msg):
                        self._add_msg_to_ignore(msg)
                        if 'chat_id' in msg:
                            self._send_message(
                                user_id=msg['chat_id'],
                                text='%s, %s' % (self._get_user_name(msg['user_id']), self._get_help()),
                                is_chat=True)
                        else:
                            self._send_message(
                                user_id=msg['user_id'],
                                text='%s, %s' % (self._get_user_name(msg['user_id']), self._get_help()),
                                is_chat=False)
                        continue
                    if msg['body'][:12] == u'%s забудь ' % self._bot_name and not self._is_msg_in_ignore(msg):
                        if msg['user_id'] in admins:
                            self._forget_data(msg)
                            self._add_msg_to_ignore(msg)
                        continue
                    if msg['body'][:13] == u'%s запомни ' % self._bot_name and not self._is_msg_in_ignore(msg):
                        self._remember_new_data(msg)
                        self._add_msg_to_ignore(msg)
                        continue
                    if msg['body'][:10] == u'%s инфа ' % self._bot_name and not self._is_msg_in_ignore(msg):
                        variable = random.randint(0, 100)
                        text = u''
                        if variable == 100:
                            text = u'Инфа сотка, бро :) ! %s%s' % (variable, '%')
                        elif variable > 75:
                            text = u'Вероятность крайне высока - %s%s' % (variable, '%')
                        elif variable == 0:
                            text = u'Вероятность никакущая, бро :( - %s%s' % (variable, '%')
                        elif variable < 15:
                            text = u'Вероятность крайне мала - %s%s' % (variable, '%')
                        else:
                            text = u'Вероятность - %s%s' % (variable, '%')

                        if 'chat_id' in msg:
                            self._send_message(
                                user_id=msg['chat_id'],
                                text='%s, %s' % (self._get_user_name(msg['user_id']), text),
                                is_chat=True)
                        else:
                            self._send_message(
                                user_id=msg['user_id'],
                                text='%s, %s' % (self._get_user_name(msg['user_id']), text),
                                is_chat=False)
                        self._add_msg_to_ignore(msg)
                        continue
                    if msg['body'][:4] == self._bot_name and not self._is_msg_in_ignore(msg) and len(msg['body']) > 5:
                        self._send_message_from_db(msg)
                        self._add_msg_to_ignore(msg)
                        continue
                else:
                    if msg['body'][:17] == u'%s камбекнись' % self._bot_name and not self._is_msg_in_ignore(msg):
                        self._add_msg_to_ignore(msg)
                        if msg['user_id'] in admins:
                            if 'chat_id' in msg:
                                self._send_message(
                                    user_id=msg['chat_id'],
                                    text=u'%s, Я вернулся!' % self._get_user_name(msg['user_id']),
                                    is_chat=True)
                            else:
                                self._send_message(
                                    user_id=msg['user_id'],
                                    text=u'%s, Я вернулся!' % self._get_user_name(msg['user_id']),
                                    is_chat=False)
                            self._disable = False
                        continue

    def _main(self):
        while True:
            self._analyze_messages(self._vk.messages.get(count=5)['items'])
            # current_chat_title = vk.messages.getChat(chat_id=target_chat_id)['title']
            # if current_chat_title != target_chat_title:
            #     print('Changed:', current_chat_title, 'to', target_chat_title)
            #     vk.messages.editChat(chat_id=target_chat_id, title=target_chat_title)
            time.sleep(2)

    def start_bot(self, debug=False):
        print(u"Starting work...")
        while True:
            if debug:
                self._main()
            else:
                try:
                    self._main()
                except Exception as error_msg:
                    print('Oops! I\'m restarting. Error: %s' % error_msg)


def main():
    bot = MainBot()
    bot.start_bot()


if __name__ == '__main__':
    main()
