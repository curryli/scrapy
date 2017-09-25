# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from tutorial.items import TestspiderItem
from selenium import webdriver
import time

class ZhihuSpider(scrapy.Spider):
    name = "zhihu_login"
    allowed_domains = ["zhihu.com", "baidu.com"]
    #allowed_domains = ["scrapy.org"]
    start_urls = [
        'https://www.zhihu.com/'
     ]

    def parse(self, response):
        my_cookies = self.post_login()
        after_log_url = "https://www.zhihu.com/explore"   #不能直接抓 "https://www.zhihu.com/"   登录后直接抓https://www.zhihu.com/   发现抓到的页面还是登录前的，必须换个链接抓，可能是哟缓存？
        #after_log_url = "https://www.baidu.com"
        #after_log_url = "https://doc.scrapy.org/en/latest/_static/selectors-sample1.html"
        yield scrapy.Request(after_log_url, callback=self.after_login)

        #return scrapy.Request(url=self.start_urls[0], cookies=self.get_cookies(), callback=self.after_login)

    def post_login(self):
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver.get(self.start_urls[0])
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_class_name("signin-switch-password").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("471954797@qq.com") #修改为自己的用户名
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1234567") #修改为自己的密码
        time.sleep(5)
        print "I have click the captcha by hand."
        driver.find_element_by_css_selector("button.sign-button.submit").click()
        time.sleep(1)
        # driver.find_element_by_xpath(u'//*[@id="root"]/div/div[2]/header/div/nav/a[1]').click()
        # time.sleep(1)
        cookies = driver.get_cookies()
        print cookies
        return cookies

    def after_login(self, response):
        sel = scrapy.Selector(response)
        text2 = response.xpath(u'/html/head/title/text()').extract()[0].encode("utf-8")
        print text2

        text3 = response.xpath(u'//title/text()').extract()[0].encode("utf-8")
        print text3

        # text5 = response.xpath(u'//h2[@*]').extract()[0].encode("utf-8")
        # print text5
        #
        # text4 = response.xpath(u"//h2[@class='ContentItem-title']").extract()[0].encode("utf-8")
        # print text4

        time.sleep(2)
        yield scrapy.Request("https://www.zhihu.com/", callback=self.back_main)


    def back_main(self, response):
        sel = scrapy.Selector(response)
        text2 = response.xpath(u'/html/head/title/text()').extract()[0].encode("utf-8")
        print text2
        time.sleep(1000)



