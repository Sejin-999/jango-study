from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Safari()
#browser.implicitly_wait(5) #대기시간
browser.get("https://www.naver.com")
time.sleep(3)
find = browser.find_element_by_id



#def crow ():
    #n =1
    #browser.get(url+n)

    #saveinfo = browser.find_elements(By.CLASS_NAME , "up")
    #for info in saveinfo:
        #print(info)