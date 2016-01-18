# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://www.yandex.ru'
NEWS_COUNT = 10

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    news = []
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', class_ = "b-table widgets-table")
    
    row = table.find_all('div', class_ = "b-tabs__items")
    cols = row[0].find_all('li', class_ = "b-news-list__item")
    href = row[0].find_all('a', href = True)

    for i in range(NEWS_COUNT):
        news.append({
            'title' : cols[i].a.text,
            'href'  : href[i]['href']
        })
    print("News from Yandex")
    for x in news:
        print('#', x['title'], "\n(" + x['href'] + ')')

def main():
    parse(get_html(BASE_URL))

if __name__ == '__main__':
    main()
