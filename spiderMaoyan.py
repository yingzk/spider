# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 23:16:09 2017

@author: YingJoy
"""

import requests
import re
import json
from requests.exceptions import RequestException

# 获取单页代码
def get_single_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    try:
        response = requests.get(url, headers = headers)
        if (response.status_code == 200):
            return response.text
        return None
    except RequestException:
        return None

# 解析单页
def parse_single_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?'
                        +'data-src="(.*?)".*?'
                        +'name">.*?">(.*?)</a>.*?'
                        +'star">(.*?)</p>.*?'
                        +'releasetime">(.*?)</p>.*?'
                        +'integer">(.*?)</i>.*?'
                        +'fraction">(.*?)</i>.*?'
                        +'.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
                'index': item[0],
                'name':item[2],
                'star':item[3].strip()[3:],
                'releasetime':item[4].strip()[5:],
                'score':item[5]+item[6],
                'image':item[1]
                }

# 将结果写入文件
def write_to_file(result):
    with open('Maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii = False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset) 
    html = get_single_page(url)
    for item in parse_single_page(html):
        write_to_file(item)
    
if __name__ == '__main__':
    for i in range(10):
        main(i * 10)