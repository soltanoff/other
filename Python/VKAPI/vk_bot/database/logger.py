#!/usr/bin/env python
# -*- coding: utf8 -*-
from cfg.config import MESSAGE_HISTORY, get_time


class Logger(object):
    @staticmethod
    def read_history():
        try:
            f = open(MESSAGE_HISTORY, 'r')
            result = []
            for x in f:
                result.append(x[:len(x) - 1])
            f.close()
            return result
        except Exception as error_msg:
            print(get_time() + u'[BOT ERROR]: %s' % error_msg)
            return []

    @staticmethod
    def write_history(ignore_msgs):
        try:
            f = open(MESSAGE_HISTORY, 'w')
            for x in ignore_msgs:
                f.write(x + '\n')
            f.close()
        except Exception as error_msg:
            print(get_time() + u'[BOT ERROR]: %s' % error_msg)
