#!/usr/bin/env python
# -*- coding: utf8 -*-
# logger.py
import emoji

MESSAGE_HISTORY = 'cfg/ignore_msgs.cfg'

# newspapaer.py
BASE_URL = 'http://www.yandex.ru'

# botmath.py
SAVE_LIST = [
    'math',
    'acos',
    'asin',
    'atan',
    'atan2',
    'ceil',
    'factorial'
    'cos',
    'cosh',
    'degrees',
    'e',
    'exp',
    'fabs',
    'floor',
    'fmod',
    'frexp',
    'hypot',
    'ldexp',
    'log',
    'log10',
    'modf',
    'pi',
    'pow',
    'radians',
    'sin',
    'sinh',
    'sqrt',
    'tan',
    'tanh'
]

# dbconnect.py
DBSETTINGS = {
    'user':     'dbuser',
    'password': 'dbpassword',
    'host':     'localhost',
    'port':     3306,
    'database': 'db_bot'
}

# bot.py
RESTART_TIME = 7200
BOT_SIGN_IN = {
    'login': u'+79531472458',
    'password': u'huluna2013'
}
LITERALS = {
    'db_error': emoji.emojize(u'Я не умею разговаривать. :shit:', use_aliases=True),
    'remember_data':    emoji.emojize(u"{user_name}, океюшки :ok_hand:. Теперь я запомнил: \"{message}\" :)", use_aliases=True),
    'forget_data':      emoji.emojize(u"{user_name}, океюшки. :pensive: Пожалуй забуду: \"{message}\"", use_aliases=True),
    'commands': {
        'bot_off':      {
            'cmd':      u"{bot_name} завали ебало",
            'answer':   emoji.emojize(u"{user_name}, океюшки! Уебываю... :running:", use_aliases=True)
        },
        'bot_on':       {
            'cmd':      u"{bot_name} камбекнись",
            'answer':   emoji.emojize(u"{user_name}, Я вернулся! :stuck_out_tongue_winking_eye:", use_aliases=True)
        },
        'help':         {
            'cmd':      u"{bot_name} команды"
        },
        'forget':       {
            'cmd':      u"{bot_name} забудь "
        },
        'remember':     {
            'cmd':      u"{bot_name} запомни "
        },
        'probability':  {
            'cmd':      u"{bot_name} инфа ",
            'answer':   {
                'max':  emoji.emojize(u"Инфа :100:, бро :thumbsup:", use_aliases=True),
                'high': u"Вероятность крайне высока - {percent}%",
                'min':  emoji.emojize(u"Вероятность никакущая, бро :thumbsdown: - {percent}%", use_aliases=True),
                'low':  u"Вероятность крайне мала - {percent}%",
                'mid':  u"Вероятность - {percent}%"
            }
        },
        'change_mod':   {
            'cmd':      u"{bot_name} смени режим",
            'answer':   {
                 'intelligency': emoji.emojize(u"{user_name}, океюшки! Теперь я интеллигент. :performing_arts:", use_aliases=True),
                'default':       emoji.emojize(u"{user_name}, океюшки! Теперь я обычный. :ghost:", use_aliases=True)
            }
        },
        'current_mod':  {
            'cmd':      u"{bot_name} режим",
            'answer': {
                'intelligency':     emoji.emojize(u"{user_name}, я интеллигент. :performing_arts:", use_aliases=True),
                'default':          emoji.emojize(u"{user_name}, я обычный. :ghost:", use_aliases=True)
            }
        },
        'news':         {
            'cmd':      u"{bot_name} новости"
        },
        'tv_list':       {
            'cmd':      u"{bot_name} телепрограмма"
        },
        'math':         {
            'cmd':      {
                'help': u"{bot_name} м помощь",
                'calc': u"{bot_name} м ",
            },
            'answer':   emoji.emojize(u"{user_name}, вот тебе справка по моей математике. :sunglasses:\n{help}", use_aliases=True)
        },
        'who_is':       {
            'cmd':      u"{bot_name} кто",
            'answer':   [
                emoji.emojize(u'да это же :point_right: {user_name}', use_aliases=True),
                u'я считаю, что это {user_name}',
                emoji.emojize(u'инфа :100:, что это {user_name}', use_aliases=True),
                emoji.emojize(u'полагаю, что это {user_name} :smiling_imp:', use_aliases=True),
                emoji.emojize(u'это {user_name}, зуб даю :point_up:', use_aliases=True)
            ]
        },
        'date': {
            'cmd': u"{bot_name} когда",
            'answer': [
                emoji.emojize(u'хм, наверно :point_right: {date}', use_aliases=True),
                u'я считаю, что {date}',
                emoji.emojize(u'инфа :100:, что {date}', use_aliases=True),
                emoji.emojize(u'полагаю, что это {date} :smiling_imp:', use_aliases=True)
            ]
        }
    }
}
DATE_MONTH = [
    'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
    'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'
]
ADMIN_LIST = [96996256, 77698338, 299314896, 141004290, 25306994, 148006413]
VERSION = 'v1.3.0'

