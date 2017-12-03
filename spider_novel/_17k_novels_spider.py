# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:44:30 2017

@author: YingJoy
"""
import requests
import re
import os

class _17Knovel:
    def __init__(self, bookID):
        self.__baseBooklURL = 'http://www.17k.com/list/'
        self.__basechapterURL = 'http://www.17k.com/'
        self.bookID = bookID
    
    # 获取小说章节列表页代码
    def getchapterCode(self):
        booklistURL = self.__baseBooklURL + str(self.bookID) + '.html'
        listPageCode = requests.get(booklistURL).text
        return listPageCode
    
    # 获取小说名
    def getBookName(self):
        listPageCode = self.getchapterCode()
        pattern = re.compile('<h1 class="Title">(.*?)</h1>', re.S)
        result = re.search(pattern, listPageCode).groups()[0]
        return result
    
    # 获取小说的卷数和每一卷的源码
    def getbookVolumeNums(self):
        listPageCode = self.getchapterCode()
        pattern = re.compile('<dl class="Volume".*?</dl>', re.S)
        results = re.findall(pattern, listPageCode)
        return len(results), results
        
    # 获取每卷的章节和章节地址的字典
    def getchapterPageDict(self):
        volumeNums, volumeCode = self.getbookVolumeNums()
        
        volume_name_pattern = re.compile('<span class="tit">(.*?)</span>', re.S)
        others_pattern = re.compile('<a target="_blank" href="(.*?)".*?<span class=(?:"ellipsis"|"ellipsis vip")>(.*?)</span>', re.S)
        
        result_dict = {}
        for i in range(volumeNums):
            volume_name_result = str(i) + '.' + re.search(volume_name_pattern, volumeCode[i]).groups()[0]
            others_results = re.findall(others_pattern, volumeCode[i])
            result_dict[volume_name_result] = others_results
        return result_dict
    
    # 创建相关文件夹保存小说
    def createFolder(self):
        result_dict = self.getchapterPageDict()
        for key in result_dict.keys():
            book_store_path = 'novels\\' + self.getBookName() + '\\' + key
            while not os.path.isdir(book_store_path):
                os.makedirs(book_store_path)
        
    
    # 提取页面的小说内容
    def getBookContent(self, url):
        pageCode = requests.get(url).text
        pattern = re.compile('(?:<h1>|<h1 class="title">)(.*?)</h1>.*?<div class="(?:p|content)".*?>(.*?)(?:<div class="author-say">|</div>)', re.S)
        result = re.search(pattern, pageCode).groups()
        title = result[0].strip()
        content = result[1].strip()
        content = re.sub('本书首发来自17K小说网，第一时间看正版内容！', '', content, re.S)
        conver_html = '<html><body><h1><p style="text-align: center">' + title + '</p></h1>' + content +'</body></html>'
        return conver_html
        
    # 下载每卷的html并保存到相应的路径
    def saveAllNovels(self):
        result_dict = self.getchapterPageDict()
        for key in result_dict.keys():
            index = 0
            for i in range(len(result_dict[key])):
                index += 1
                with open('novels\\' + self.getBookName() + '\\' + key + '\\' + str(index) + '.' + result_dict[key][i][1].strip() + '.html', 'w') as f:
                    text = self.getBookContent(self.__basechapterURL + result_dict[key][i][0].strip())
                    text.encode('utf-8')
                    f.write(text)
                    


print ('开始爬虫...')
s = _17Knovel(108821)
z = s.createFolder()
s.saveAllNovels()
print ('下载完毕...')
