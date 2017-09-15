 # -*- coding: utf-8 -*-
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
 
#   这里的文件路径是webdriver的文件路径
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

#   打开网页
    driver.get("http://www.mpaypass.com.cn/digest.html")
    
    WebDriverWait(driver, 15).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[3]/div[1]").is_displayed())
     
    time.sleep(1)
    
 
    
    
    parent=driver.find_element_by_class_name("main-left")
    listbody = parent.find_elements_by_class_name("newslist")
    for news in listbody:
        pic = news.find_element_by_id("pic")
        hlink = pic.find_element_by_css_selector("#pic > a")
        url = hlink.get_attribute('href')
        print (url)  
        
        request = urllib2.Request(url)
        html = urllib2.urlopen(request).read().decode('utf8')
         
       # html = urllib2.urlopen(hlink).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        page = soup.find('div', attrs={'class':'newsbody'})
        content = page.get_text()
        #http://www.mpaypass.com.cn/news/201709/15163009.html
        name_reg = "^.*\/(.*?)\.html$"
        match = re.findall(name_reg, url)
        fname = "d:/spider_file/" + match[0] + ".txt"
        
        File_out = codecs.open(fname,"a+") #文件操作
        File_out.write(content)
        File_out.close()
          
    showmore = parent.find_element_by_xpath("/html/body/div[3]/div[1]/div[32]")
    
    time.sleep(1)
    
    showmore.click()
    time.sleep(2)
    
    for i in range(2):
        print i
        parent=driver.find_element_by_class_name("main-left")
        listbody = parent.find_elements_by_class_name("newslist")
        for news in listbody:
            pic = news.find_element_by_id("pic")
            hlink = pic.find_element_by_css_selector("#pic > a")
            print (hlink.get_attribute('href'))  
        
        WebDriverWait(driver, 5).until(lambda the_driver: the_driver.find_element_by_class_name("newsmore-page").is_displayed())
        #showmore =driver.find_element_by_class_name("newsmore-page")
        #time.sleep(1)
        next_btn = driver.find_element_by_class_name("newsmore-page-b")
        time.sleep(1)
        next_btn.click()
        time.sleep(2)
    
    
    print "done"
      
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
#import time
#import random
#
#def main():
# 
##   这里的文件路径是webdriver的文件路径
#    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#
##   打开网页
#    driver.get("http://www.mpaypass.com.cn/digest.html")
#    
#    WebDriverWait(driver, 15).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[3]/div[1]").is_displayed())
#     
#    time.sleep(1)
#    
#    
#    parent=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]")
#    listbody = parent.find_element_by_id("listbody")
#    pic = listbody.find_element_by_id("pic")
#    hlink = pic.find_element_by_css_selector("#pic > a")
#    
#    print (hlink.get_attribute('href'))  
#      
#if __name__ == '__main__':
#    main()


#url = "http://www.mpaypass.com.cn/news/201709/15163009.html"
#pattern = "^.*\/(.*?)\.html$"
#match = re.findall(pattern, url)
#print(match[0])
#15163009