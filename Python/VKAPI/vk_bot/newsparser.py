#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

BASE_URL = 'http://www.yandex.ru'


class NewsParser(object):
    @staticmethod
    def __get_html(url):
        return urllib2.urlopen(url).read()

    def __parse_news(self):
        soup = BeautifulSoup(self.__get_html(BASE_URL), "html.parser")
        table = soup.find('div', class_="news")

        rf_news = table.contents[0].contents[0].contents[1].contents[0].contents
        spb_news = table.contents[0].contents[0].contents[2].contents[0].contents
        news = []
        for row in rf_news + spb_news:
            news.append(
                {
                    'NEWS': row.contents[0].text,
                    'LINK': row.contents[0].get('href')
                }
            )
        return news

    def __parse_tvlist(self):
        soup = BeautifulSoup(self.__get_html(BASE_URL), 'html.parser')
        y = soup.find('ul', class_="list tv-list")

        tvlist = []
        for x in y.find_all('li'):
            tvlist.append(
                {
                    'TIME': x.contents[0].text,
                    'TVSHOW': x.contents[1].text
                }
            )
        return tvlist

    def get_news(self):
        news = self.__parse_news()
        count = 0
        text = u'Новости РФ:'
        for obj in news:
            count += 1
            if count == 6:
                count = 1
                text += u'\nНовости СПб: '
            text += u'\n%s) %s\nПРУВ: %s\n' % (count, obj['NEWS'], obj['LINK'])
        return text

    def get_tvlist(self):
        tvlist = self.__parse_tvlist()
        count = 0
        text = u'Телепрограмма:'
        for obj in tvlist:
            count += 1
            text += u'\n%s) %s - %s' % (count, obj['TIME'], obj['TVSHOW'])
        return text
