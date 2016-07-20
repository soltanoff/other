#!/usr/bin/env python
# -*- coding: utf8 -*-
from dbconnector import DBConnector
from logger import Logger
import random
import vk_api
import time
# import re

BOT_SIGN_IN = {
    'login': u'+79531472458',
    'password': u'huluna2013'
}
ADMIN_LIST = [77698338, 96996256]
VERSION = 'v0.8.3'


class MainBot(object):
    def __init__(self):
        self._vk_session = vk_api.VkApi(
            BOT_SIGN_IN['login'],
            BOT_SIGN_IN['password'],
            captcha_handler=self.__captcha_handler
        )

        try:
            self._vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return

        self._vk = self._vk_session.get_api()
        self._bot_name = self._get_user_name(None)
        self._db = DBConnector()
        self._logger = Logger()
        self._ignore_msgs = self._logger.read_history()
        self._ans_list = self._db.select_ids()

        self._disable = False

    @staticmethod
    def __captcha_handler(captcha):
        """
            При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    def _add_msg_to_ignore(self, msg):
        if 'chat_id' in msg:
            self._ignore_msgs.append('%s-%s-%s' % (msg['chat_id'], msg['id'], msg['user_id']))
        else:
            self._ignore_msgs.append('NONE-%s-%s' % (msg['id'], msg['user_id']))
        self._logger.write_history(self._ignore_msgs)

    def _is_msg_in_ignore(self, msg):
        # result = False
        if 'chat_id' in msg:
            result = '%s-%s-%s' % (msg['chat_id'], msg['id'], msg['user_id']) in self._ignore_msgs
        else:
            result = 'NONE-%s-%s' % (msg['id'], msg['user_id']) in self._ignore_msgs
        return result

    def _send(self, msg, text):
        if 'chat_id' in msg:
            self._vk.messages.send(
                chat_id=msg['chat_id'],
                message=text
            )
        else:
            self._vk.messages.send(
                user_id=msg['user_id'],
                message=text
            )

    def _send_message_from_db(self, msg):
        self._send(
            msg,
            '%s, %s' % (
                self._get_user_name(msg['user_id']),
                self._db.get_message(self._ans_list[random.randint(0, len(self._ans_list)-1)][0])
            )
        )

    @staticmethod
    def _prepare_msg(msg):
        return msg.replace('\'', '\\\'')

    def _remember_new_data(self, msg):
        self._db.add_new_row(msg['user_id'], self._prepare_msg(msg['body'][13:]))
        self._send(
            msg,
            u"%s, океюшки. Теперь я запомнил: \"%s\" :)" % (
                self._get_user_name(msg['user_id']),
                self._prepare_msg(msg['body'][13:])
            )
        )
        print(u'Remember new data: from %s, msg: %s' % (msg['user_id'], self._prepare_msg(msg['body'][13:])))
        self._ans_list = self._db.select_ids()

    def _forget_data(self, msg):
        self._db.del_row(self._prepare_msg(msg['body'][12:]))
        self._send(
            msg,
            u"%s, океюшки :( Пожалуй забуду: \"%s\"" % (
                self._get_user_name(msg['user_id']),
                self._prepare_msg(msg['body'][12:])
            )
        )
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
        """.replace('name', self._bot_name).replace('version', VERSION)

    def _get_user_name(self, user_id):
        return u'%s' % self._vk.users.get(user_ids=[user_id])[0]['first_name']

    def __command_bot_off(self, msg):
        if msg['body'][:17] == u'%s завали ебало' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            if msg['user_id'] in ADMIN_LIST:
                self._send(msg, u'%s, океюшки! Уебываю...' % self._get_user_name(msg['user_id']))
                self._disable = True
            return True
        return False

    def __command_bot_on(self, msg):
        if msg['body'][:17] == u'%s камбекнись' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            if msg['user_id'] in ADMIN_LIST:
                self._send(msg, u'%s, Я вернулся!' % self._get_user_name(msg['user_id']))
                self._disable = False
            return True
        return False

    def __command_bot_help(self, msg):
        if msg['body'][:12] == u'%s команды' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            self._send(msg, '%s, %s' % (self._get_user_name(msg['user_id']), self._get_help()))
            return True
        return False

    def __command_bot_forget(self, msg):
        if msg['body'][:12] == u'%s забудь ' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            if msg['user_id'] in ADMIN_LIST:
                self._forget_data(msg)
            return True
        return False

    def __command_bot_remember(self, msg):
        if msg['body'][:13] == u'%s запомни ' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            self._remember_new_data(msg)
            return True
        return False

    def __command_bot_probability(self, msg):
        if msg['body'][:10] == u'%s инфа ' % self._bot_name and not self._is_msg_in_ignore(msg):
            self._add_msg_to_ignore(msg)
            probability = random.randint(0, 100)
            # text = u''
            if probability == 100:
                text = u'Инфа сотка, бро :) ! %s%s' % (probability, '%')
            elif probability > 75:
                text = u'Вероятность крайне высока - %s%s' % (probability, '%')
            elif probability == 0:
                text = u'Вероятность никакущая, бро :( - %s%s' % (probability, '%')
            elif probability < 15:
                text = u'Вероятность крайне мала - %s%s' % (probability, '%')
            else:
                text = u'Вероятность - %s%s' % (probability, '%')
            self._send(msg, u'%s, %s' % (self._get_user_name(msg['user_id']), text))
            return True
        return False

    def __command_bot_message(self, msg):
        if msg['body'][:4] == self._bot_name and not self._is_msg_in_ignore(msg) and len(msg['body']) > 5:
            self._add_msg_to_ignore(msg)
            self._send_message_from_db(msg)
            return True
        return False

    def __analyze_messages(self, msg_list=None):
        if msg_list:
            for msg in msg_list:
                if not self._disable:
                    self.__command_bot_off(msg)
                    self.__command_bot_help(msg)
                    self.__command_bot_forget(msg)
                    self.__command_bot_remember(msg)
                    self.__command_bot_probability(msg)
                    self.__command_bot_message(msg)
                else:
                    self.__command_bot_on(msg)

    def __main(self):
        while True:
            self.__analyze_messages(self._vk.messages.get(count=5)['items'])
            # current_chat_title = vk.messages.getChat(chat_id=target_chat_id)['title']
            # if current_chat_title != target_chat_title:
            #     print('Changed:', current_chat_title, 'to', target_chat_title)
            #     vk.messages.editChat(chat_id=target_chat_id, title=target_chat_title)
            time.sleep(2)

    def start_bot(self, debug=False):
        print(u"Starting work...")
        while True:
            if debug:
                self.__main()
            else:
                try:
                    self.__main()
                except Exception as error_msg:
                    print('Oops! I\'m restarting. Error: %s' % error_msg)
