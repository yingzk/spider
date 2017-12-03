# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:34:31 2017

@author: YingJoy
"""

import requests
import re

content = requests.get('https://book.douban.com/latest').text
pattern = re.compile('<div class="detail-frame">.*?<h2.*?<a href="(.*?)">(.*?)</a>.*?<p class="color-gray">(.*?)</p>', re.S)
results = re.findall(pattern, content)

if (results):
    for result in results:
        print (result[0], result[1], result[2].strip())