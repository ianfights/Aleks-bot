from selenium import webdriver
from time import sleep
username = raw_input("Username: ")
password = raw_input("Password: ")

class AleksBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://connected.mcgraw-hill.com/connected/login.do')

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="loginUserName"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="loginPassword"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginLink"]')
        login_btn.click()

        sleep(15)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="NG8D8OGC6M5G2Z5C"]/div/div/div[2]/button')
        popup_1.click()
        sleep(5)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="rotatorContent"]/table/tbody/tr/td[1]/div/div/div/a')
        popup_2.click()
        sleep(3)
        popup_3 = self.driver.find_element_by_xpath('//*[@id="lessonSearchResults"]/div/div[3]/div')
        popup_3.click()
        
    
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(20)
        try:
            popup_4 = self.driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_assignment_home_auto_db_c2ed66a_quiz#1104_2530"]')
            popup_4.click()
        except:
            
            popup_5 = self.driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_start_learning"]')
            popup_5.click()
       
        sleep(5)
        
                    

        while True:
            sleep(20)
            popup_8 = self.driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_requestExplain"]')
            popup_8.click()
            sleep(40)
            popup_9 = self.driver.find_element_by_xpath('//*[@id="smt_bottomnav_button_input_learning"]')
            popup_9.click()
        
    
bot = AleksBot()
bot.login()
