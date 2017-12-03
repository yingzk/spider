#!usr/bin/env python  
#-*- coding:utf-8 -*- 

""" 
@author:yzk13 
@time: 2017/11/29 
"""
from selenium.webdriver.common.by import By

def is_element_exist(browser, class_sector):
    if browser.find_element_by_class_name(class_sector):
        return True
    return False