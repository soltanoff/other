#!/usr/bin/env python
# -*- coding: utf8 -*-
# logger.py
MESSAGE_HISTORY = 'ignore_msgs.cfg'

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

# bot.py
BOT_SIGN_IN = {
    'login': u'login@login',
    'password': u'password'
}
LITERALS = {
    'remember_data':    u"{user_name}, океюшки. Теперь я запомнил: \"{message}\" :)",
    'forget_data':      u"{user_name}, океюшки :( Пожалуй забуду: \"{message}\"",
    'commands': {
        'bot_off':      {
            'cmd':      u"{bot_name} завали ебало",
            'answer':   u"{user_name}, океюшки! Уебываю..."
        },
        'bot_on':       {
            'cmd':      u"{bot_name} камбекнись",
            'answer':   u"{user_name}, Я вернулся! :)"
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
                'max':  u"Инфа сотка, бро :) ! {percent}%",
                'high': u"Вероятность крайне высока - {percent}%",
                'min':  u"Вероятность никакущая, бро :( - {percent}%",
                'low':  u"Вероятность крайне мала - {percent}%",
                'mid':  u"Вероятность - {percent}%"
            }
        },
        'change_mod':   {
            'cmd':      u"{bot_name} смени режим",
            'answer':   {
                'intelligency': u"{user_name}, океюшки! Теперь я интеллигент.",
                'default':      u"{user_name}, океюшки! Теперь я обычный."
            }
        },
        'current_mod':  {
            'cmd':      u"{bot_name} режим",
            'answer': {
                'intelligency': u"{user_name}, я интеллигент.",
                'default': u"{user_name}, я обычный."
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
            'answer':   u"{user_name}, вот тебе справка по моей математике.\n{help}"
        },
        'who_is':       {
            'cmd':      u"{bot_name} кто",
            'answer':   [
                u'да это же {user_name}',
                u'я считаю, что это {user_name}',
                u'инфа сотка, что это {user_name}',
                u'полагаю, что это {user_name}',
                u'это {user_name}, зуб даю'
            ]
        }
    }
}
ADMIN_LIST = [77698338, 96996256]
VERSION = 'v1.0.3'
