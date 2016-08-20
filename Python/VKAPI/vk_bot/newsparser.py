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

    def __parse_tv_list(self):
        soup = BeautifulSoup(self.__get_html(BASE_URL), 'html.parser')
        y = soup.find('ul', class_="list tv-list")

        tv_list = []
        html_list = y.find_all('li')
        for x in html_list:
            try:
                tv_list.append(
                    {
                        'TIME': x.contents[0].text,
                        'TV_SHOW': x.contents[1].text
                    }
                )
            except Exception as error_msg:
                print("[tv_list] %s" % error_msg)

        return tv_list

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

    def get_tv_list(self):
        tv_list = self.__parse_tv_list()
        count = 0
        text = u'Телепрограмма:'
        for obj in tv_list:
            count += 1
            text += u'\n%s) %s - %s' % (count, obj['TIME'], obj['TV_SHOW'])
        return text
