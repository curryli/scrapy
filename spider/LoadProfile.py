 # -*- coding: utf-8 -*-
 #该程序能够打开自己的带有各种配置的浏览器  profile，这样可以直接加载一些cookies之类的
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from bs4 import BeautifulSoup
import requests
import urllib2  # 网络访问模块
import codecs  #解决编码问题的关键 ，使用codecs.open打开文件
import re

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class News(object):
    def __init__(self):
        self.url = None
        self.title = None
        self.date = None
        self.content = None



def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr)
  return content[startIndex:endIndex]


def main():
    option = webdriver.ChromeOptions()
    #加载默认的数据。注意这时候电脑上不要开启其他的chrome，否则会报错：selenium unable to move the cache
    option.add_argument('--user-data-dir=C:\Users\lixurui\AppData\Local\Google\Chrome\User Data')
#   这里的文件路径是webdriver的文件路径
    
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", chrome_options=option)
     
#   打开网页
    driver.get("https://www.zhihu.com/")
  
    time.sleep(1)
   
    
    print "done"
      
if __name__ == '__main__':
    main()
    
    
    
    
    
     