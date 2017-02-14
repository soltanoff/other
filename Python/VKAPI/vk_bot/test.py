#!/usr/bin/env python
# -*- coding: utf8 -*-
from grab.base import Grab


def main():
    g = Grab()
    g.go('http://yandex.ru')

    # Ищем слово "Новости" на странице
    print(u"На этой странице есть слово \"Новости\"? %s" % u'Да' if g.doc.text_search(u'Новости') else u'Нет')
    # выводим тайтл страницы
    print(u"Заголовок страницы: '%s'" % g.doc.select('//title').text())

    g.doc.set_input('text', 'grab python')
    g.doc.submit()
    # получаем первую ссылку из запроса яндекса) Ссылку на годную статейку
    print(u"Годная ссылочка на хабр про грабик: %s" % g.doc.select('//li[@class="serp-item"]//a').attr('href'))


if __name__ == '__main__':
    main()
