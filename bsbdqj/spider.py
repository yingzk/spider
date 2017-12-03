#!usr/bin/env python  
#-*- coding:utf-8 -*- 

""" 
@author:yzk13 
@time: 2017/11/15
@statement: spider all of videos from budejie
@link: http://www.budejie.com/
"""
import datetime
import os
from _md5 import md5

import pymongo
import requests
import time
from config import *
from bs4 import BeautifulSoup

# get index page response
def get_index_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

# parse index page html
# get title, video_url, date
def parse_index_page(html):
    time.sleep(1.4)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('.j-r-list-c-desc a')
    video_url = soup.select('.j-video')
    date = soup.select('.j-video-c')
    index = len(title)

    for i in range(index):
        yield {
            'title' : title[i].get_text(),
            'video_url' : video_url[i].get('data-mp4'),
            'date' : date[i].get('data-date')
        }

# save result to mongodb
def save_to_mongo(result):
    client = pymongo.MongoClient(MONGO_URL, connect=False)
    db = client[MONGO_DB]
    check_title = result.get('title')
    if not db[MONGO_TABLE].find_one({'title' : check_title}):
        if db[MONGO_TABLE].insert(result):
            print('------------------------成功保存至MongoDB')
            return True
        else:
            return False
    else:
        print('------------------------该记录已存在')
        pass

# get video content
def get_video_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None
    except ConnectionError:
        return None

def save_video(content):
    save_path = os.getcwd() + '/mp4/' + str(datetime.date.today())
    filepath = '{0}/{1}.{2}'.format(save_path, md5(content).hexdigest(), 'mp4')
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    with open(filepath, 'wb') as f:
        f.write(content)
        f.close()
    print('保存视频文件成功------------------------')

if __name__ == '__main__':
    for index in range(START_INDEX, END_INDEX):
        html = get_index_page(URL + str(index))
        result = parse_index_page(html)
        for i in result:
            print(i)
            content = get_video_content(i.get('video_url'))
            save_video(content)
            save_to_mongo(i)
