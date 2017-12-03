# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:26:57 2017

@author: YingJoy

滕云阁文章爬虫
"""
import random
from collections import Counter

import jieba
import requests
from bs4 import BeautifulSoup
import pymongo
from multiprocessing import Pool

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

MONGO_URL = 'localhost'
MONGO_DB = 'tyg'
MONGO_TABLE = 'tyg'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

class TYG:
    # 初始化， 以文章的ID作为初始化参数
    def __init__(self, articleIndex):
        self.baseURL = 'https://www.qcloud.com/community/all/' + str(articleIndex)

    # 获取页面内容
    def get_page_index(self, url):
        try:
            response = requests.get(url)
            return response.text
        except ConnectionError:
            print('连接错误')
            return None

    # 获取一页所有文章 标题 地址 内容
    def get_one_page_all(self, url):
        try:
            html = self.get_page_index(self.baseURL)
            soup = BeautifulSoup(html, 'lxml')
            title = soup.select('.article-item > .title')
            address = soup.select('.article-item > .title > a[href]')
            for i in range(len(title)):
                random_num = random.randrange(0, 6500)
                content = self.parse_content('https://www.qcloud.com' + address[i].get('href').strip())
                yield {
                    'index' : random_num,
                    'title':title[i].get_text().strip(),
                    'address' : 'https://www.qcloud.com' + address[i].get('href').strip(),
                    'content' : content
                }
        except IndexError:
            pass

    # 解析文章内容
    def parse_content(self, url):
        html = self.get_page_index(url)
        soup = BeautifulSoup(html, 'lxml')
        content = soup.select('.J-article-detail')
        return content[0].get_text()

    # 将结果保存到MongoDB中
    def save__to_mongo(self, result):
        if db[MONGO_TABLE].insert(result):
            print('保存到MongoDB成功')
            return True
        return False

def main(index):
    for i in range(index):
        spider = TYG(i)
        s = spider.get_one_page_all(spider.baseURL)
        for i in s:
            print(i)
            spider.save__to_mongo(i)

def create_wordcloud():
    content = ''
    indexx = 0
    for item in db.tyg.find().sort([('index' , 1)]):
        indexx += 1
        content += item.get('content').strip()
        if (indexx % 100 == 0):
            with open('result' + str(indexx) + '.txt', 'a', encoding='utf-8') as f:
                f.write(content)
            f.close()
            content = ''
    return content

if __name__ == '__main__':

    create_wordcloud()
