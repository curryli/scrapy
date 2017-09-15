from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

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
        print (hlink.get_attribute('href'))  
        
    showmore = parent.find_element_by_xpath("/html/body/div[3]/div[1]/div[32]")
    
    time.sleep(1)
    
    showmore.click()
    time.sleep(2)
    
    for i in range(5):
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