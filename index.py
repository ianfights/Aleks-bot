#!/usr/bin/env python
from selenium import webdriver
from pyvirtualdisplay import Display
from time import sleep
username = raw_input("Username: ")
password = raw_input("Password: ")
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#print 'Starting ...'
display = Display(visible=0, size=(1600, 1200))
display.start()
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
print 'webdriver loaded'


driver.get('https://connected.mcgraw-hill.com/connected/login.do')

sleep(2)

email_in = driver.find_element_by_xpath('//*[@id="loginUserName"]')
email_in.send_keys(username)
pw_in = driver.find_element_by_xpath('//*[@id="loginPassword"]')
pw_in.send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="loginLink"]')
login_btn.click()

sleep(15)
popup_1 = driver.find_element_by_xpath('//*[@id="NG8D8OGC6M5G2Z5C"]/div/div/div[2]/button')
popup_1.click()
sleep(5)
popup_2 = driver.find_element_by_xpath('//*[@id="rotatorContent"]/table/tbody/tr/td[1]/div/div/div/a')
popup_2.click()
sleep(3)
popup_3 = driver.find_element_by_xpath('//*[@id="lessonSearchResults"]/div/div[3]/div')
popup_3.click()
        
    
base_window = driver.window_handles[0]
driver.switch_to_window(driver.window_handles[1])
sleep(20)

#//*[@id="smt_hamburgermenu_button_input_start_learning_HB"]

menu = driver.find_element_by_xpath('//*[@id="smt_hbmenu_button_input"]')
menu.click()
sleep(1)
learn = driver.find_element_by_xpath('//*[@id="smt_hamburgermenu_button_input_start_learning_HB"]')
learn.click() 
    

                   

while True:
    try:
	    start = driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_learning"]')
            start.click()
    except:
        sleep(20)
	explain = driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_requestExplain"]')
	explain.click()
    sleep(40)
  
    popup_9 = driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_learning"]')
    popup_9.click()
    
    
    sleep(5)
    
        
    
