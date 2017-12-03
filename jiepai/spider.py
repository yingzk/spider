#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yzk13 
@time: 2017/11/11
"""
import json
import re
from _md5 import md5
from json import JSONDecodeError
from urllib.parse import urlencode

import os
import pymongo

from config import *
import requests

# 获取页面索引页
from bs4 import BeautifulSoup

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

def get_page_index(offset, KEYWORD):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': KEYWORD,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }
    params = urlencode(data)
    base = 'https://www.toutiao.com/search_content/?'
    url = base + '?' + params
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('连接错误')
        return None


# 解析文章页面地址
def parse_page_index(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                if 'article_url' in item:
                    yield item.get('article_url')
    except JSONDecodeError:
        pass


# 获取文章详细页面
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('连接错误')
        return None


# 解析详细页面
def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    if result:
        title = result[0].get_text()
    else:
        return None

    pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)
    result = re.search(pattern, html)
    if result:
        try:
            data = json.loads(json.loads(result.group(1)))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                for image in images:
                    save_image(download_image(image))
                return {
                    'title': title,
                    'url': url,
                    'images': images
                }
        except JSONDecodeError:
            return None

# 存储到mongodb
def save_to_mongodb(result):
    if db[MONGO_TABLE].insert(result):
        print('成功保存到MongoDB中')
        return True
    return False

# 下载图片
def download_image(url):
    print('Downloading', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None
    except ConnectionError:
        print('连接错误')
        return None

# 保存图片
def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd() + '/images', md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

if __name__ == '__main__':
    groups = [x * 20 for x in range(GROUP_START, GROUP_END)]
    for group in groups:
        text = get_page_index(group, '街拍')
        urls = parse_page_index(text)
        for url in urls:
            html = get_page_detail(url)
            result = parse_page_detail(html, url)
            if result:
                save_to_mongodb(result)