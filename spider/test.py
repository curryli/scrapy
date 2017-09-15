# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from bs4 import BeautifulSoup
import requests
import urllib2  # 网络访问模块
import codecs  # 解决编码问题的关键 ，使用codecs.open打开文件
import re

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
url = "http://www.mpaypass.com.cn/news/201709/15163009.html"
pattern = "^.*\/(.*?)\.html$"
match = re.findall(pattern, url)
print(match[0])


