#!/usr/bin/env python34
# -*- coding: utf-8 -*-

import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://www.yandex.ru'
FILE_NAME = 'parse.csv'

def get_html(url):
    return urllib.request.urlopen(url).read()

def parse_news(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', class_="b-table widgets-table")

    news = []
    for row in table.find_all('a'):
        news.append(
            {
                'NEWS' : row.text,
                'LINK' : row.get('href')
            }
        )
    return news[3:-6]

def parse_tvlist(html):
    soup = BeautifulSoup(get_html(BASE_URL), 'html.parser')
    y = soup.find('ul', class_="b-tv-list")
    text = ""
    count = 0
    tvlist = []
    for x in y.find_all('td'):
        count+=1
        if count.__mod__(2) == 0:
            tvlist.append(
                {
                    'TIME' : text,
                    'TVSHOW' : x.text
                }
            )
            text = ""
        else:
            text = x.text
    return tvlist

def save_news(news, name_of_file, type):
    with open(name_of_file, type) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow((''))
        writer.writerow(('№', 'Новость', 'Ссылка'))
        count = 0
        for obj in news:
            count+=1
            writer.writerow((count, obj['NEWS'], obj['LINK']))

def save_tvlist(tvlist, name_of_file, type):
    with open(name_of_file, type) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow((''))
        writer.writerow(('№', 'Время', 'Передача'))
        count = 0
        for obj in tvlist:
            count += 1
            writer.writerow((count, obj['TIME'], obj['TVSHOW']))

def print_news(news):
    count = 0
    print('Новости РФ:',)
    for obj in news:
        count+=1
        if count == 6 :
            count = 1
            print('\nНовости СПб: ',)
        print(count, ') ', obj['NEWS'], ' | LINK: ', obj['LINK'], sep='')

def print_tvlist(tvlist):
    count = 0
    print('Телепрограмма:',)
    for obj in tvlist:
        count+=1
        print(count, ') ', obj['TIME'], ' - ', obj['TVSHOW'], sep='')

def main():
    html = get_html(BASE_URL)

    news = parse_news(html)
    save_news(news, FILE_NAME, 'w')
    print_news(news)

    print('')

    tvlist = parse_tvlist(html)
    save_tvlist(tvlist, FILE_NAME, 'a')
    print_tvlist(tvlist)

if __name__ == '__main__':
    main()

