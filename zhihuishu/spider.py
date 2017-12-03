#!usr/bin/env python  
#-*- coding:utf-8 -*- 

""" 
@author:yzk13 
@time: 2017/11/29 
"""
import re
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf import *
from utils import *
from pyquery import PyQuery as pq

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('start-maximized')

browser = webdriver.Chrome(chrome_options=option)
wait = WebDriverWait(browser, 100)

def login():
    """
    登陆智慧树
    """
    try:
        browser.get(LOGIN_URL)
        s_no = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#lUsername')))
        s_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#lPassword')))
        ok_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#f_sign_up > div > span')))

        s_no.send_keys(PHONE)
        s_pwd.send_keys(PASSWORD)
        ok_button.click()

        change_to_chinese = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#myBody > div.headerMenuOutside > div > div.headerMenu.clearfix > div.i18nSwitchBtn')))
        change_to_chinese.click()

        # list_all_course = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#course_studied')))
        # list_all_course.click()
        return browser.page_source
    except TimeoutException:
        login()

def get_course_id(html):
    """
    获取课程编号
    :param html:
    :return:
    """
    return None

def open_one_course(course_id):
    """
    打开课程，开始自动看课程
    :param course_id:
    :return:
    """
    start_url = COURSE_URL + str(course_id)
    # 打开新的窗口
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[1])
    browser.get(start_url)

    # 关闭警告
    if is_element_exist(browser, 'wrap_popboxes'):
        close_alarm1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'popbtn_yes')))
        close_alarm1.click()

    # 获取视频进度
    progress = browser.find_element_by_css_selector('div.progressbar_box_tip')
    print(progress.text)

    end_point = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'div.progressbar_box_tip'), '0%'))
    print(end_point.text)
        # progress_result = 0     # 设置默认进度
        # while progress_result != 1:
        #     pass
        # if re.compile('(\d+(\.\d+)?)').search(progress.text) == None:
        #     progress_result = 0
        #
        # while progress_result != float(100):
        #     print ('当前进度: ', progress_result)
        #     progress = browser.find_element_by_css_selector('div.progressbar_box_tip')
        #     print(progress.text)

if __name__ == '__main__':
    html = login()
    open_one_course(COURSE_ID)
