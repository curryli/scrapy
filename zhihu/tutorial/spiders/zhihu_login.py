# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from tutorial.items import TestspiderItem
from selenium import webdriver
import time

class ZhihuSpider(scrapy.Spider):
    name = "zhihu_login"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'https://www.zhihu.com/',
    )



    def get_cookies(self):
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver.get(self.start_urls[0])
        time.sleep(2)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(2)
        driver.find_element_by_class_name("signin-switch-password").click()
        time.sleep(1)
        driver.find_element_by_name("account").clear()
        time.sleep(1)
        driver.find_element_by_name("account").send_keys("471954797@qq.com") #修改为自己的用户名
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("1234567") #修改为自己的密码
        time.sleep(20)
        print "I have click the captcha by hand."
        driver.find_element_by_css_selector("button.sign-button.submit").click()
        time.sleep(2)
        cookies = driver.get_cookies()
        print cookies
        #driver.close()
        return cookies

    def after_login(self, response):
        sel = scrapy.Selector(response)
        #print response.body
        for i in range(1,10):
            xml = r'//*[@id="feed-%d"]/div[1]/div[2]/div[2]/h2/a/text()' %(i)
            titile = sel.xpath(xml).extract()
            if len(titile):
                print str(titile[0])

    def parse(self, response):
        return scrapy.Request(url=self.start_urls[0], cookies=self.get_cookies(), callback=self.after_login)
