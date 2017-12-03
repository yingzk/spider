#!usr/bin/env python  
#-*- coding:utf-8 -*- 

""" 
@author:yzk13 
@time: 2017/12/03 
"""
from urllib.parse import urlencode

import pymongo
from pyquery import PyQuery as pq
from conf import *
import requests

proxy = None
# MongoDB
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_proxy():
    try:
        response = requests.get(PROXYPOOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('获取代理失败，重试中...')
        get_proxy()

# 获取页面代码
def get_html(url):
    global proxy
    try:
        # 是否有代理
        if proxy:
            proxies = {
                'proxy' : 'http://' + proxy
            }
            # allow_redirects= False   禁止重定向
            response = requests.get(url, allow_redirects=False, headers=HEADERS, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=HEADERS)

        if response.status_code == 200:
            return response.text
        # 需要代理
        elif response.status_code == 302:
            print('IP unavailable')
            proxy = get_proxy()
            if proxy:
                print('获取代理', proxy)
                return get_html(url)
            else:
                print('获取代理失败')
                return None
    except ConnectionError:
        print('获取连接失败, 正在重试...')
        get_html(url)


def get_index(page):
    data = {
        'type' : 2,
        'query' : KEYWORD,
        'page' : 1
    }
    queries = urlencode(data)
    url = BASE_URL + queries
    return get_html(url)

# 获取文章的url
def get_articles_url(html):
    doc = pq(html)
    articles_url = doc('#main > div.news-box > ul > li > div.txt-box > h3 > a').items()
    for u in articles_url:
        yield u.attr('href')

def get_article_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        get_article_html(url)

# 解析文章
def parse_html(url, html):
    doc = pq(html)
    yield {
        'article url' : url,
        'title' : doc('#activity-name').text(),
        'date' : doc('#post-date').text(),
        'official account' : doc('#post-user').text(),
        'html' : doc('html').html()
    }

# 存储到MongoDB
def save2mongo(result):
    if db[MONGO_TABLE].insert(result):
        print(result)
        print ('存储到MongoDB成功')
        return True
    print('存储到MongoDB失败')
    return False

if __name__ == '__main__':
    for page in range(1, 101):
        html =get_index(page)
        articles_url = get_articles_url(html)

        for url in articles_url:
            html = get_article_html(url)
            results = parse_html(url, html)
            for result in results:
                save2mongo(result)