# IMPORTS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configs as conf
import chromer_driver_configs as chronfigs


class GmailBulk :
    
    
        def __init__(self, base_url):
            
            self.base_url = base_url
            
            options = chronfigs.get_chrome_driver_options()
            chronfigs.set_ignore_certificate_error(options)
            chronfigs.set_incognito_mode(options)
            
            driver = chronfigs.get_chrome_driver()
            
            
    
        def open_gmail_signup(self):
            
            # Open Gmail Signup Page 
            self.driver.get(chronfigs.BASE_URL)
            time.sleep(2)
            
            
            
    
        def signup_page_1(self):
            
            first_name = self.driver.find_element_by_xpath('//*[@id="firstName"]')
            first_name.send_keys(conf.FIRST_NAME)
            
            last_name = self.driver.find_element_by_xpath('//*[@id="lastName"]')
            last_name.send_keys(conf.LAST_NAME)
            
            gmail_id = self.driver.find_element_by_xpath('//*[@id="username"]')
            gmail_id.send_keys(conf.USER_ID)
            
            password = self.driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
            password.send_keys(conf.PASSWORD)
            
            confirm_password = self.driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
            confirm_password.send_keys(conf.PASSWORD)
            
            time.sleep(2)
            
            next_button = self.driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/span')
            next_button.click()
    

        def signup_page_2(self):
            
    
            phone_number = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
            phone_number.send_keys(conf.PHONE)
            
            next_button_2 = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
            next_button_2.click()
            
            phone_code = input("Enter Verification Code : ")
            phone_verify = self.driver.find_element_by_xpath('//*[@id="code"]')
            phone_verify.send_keys(phone_code)
            phone_verify.send_keys(Keys.ENTER)
            
            time.sleep(2)
            
            
            
        def signup_page_3(self):
            
    
            month = self.driver.find_element_by_xpath('//*[@id="month"]')
            month.send_keys("j")
            
            day = self.driver.find_element_by_xpath('//*[@id="day"]')
            day.send_keys("1")
            
            year = self.driver.find_element_by_xpath('//*[@id="year"]')
            year.send_keys("1995")
            
        
            gender = self.driver.find_element_by_xpath('//*[@id="gender"]/option[3]')
            gender.click()

            time.sleep(1)
            
            next_button_4 = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
            next_button_4.click()
            
            next_button_3 = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
            next_button_3.click()
            
            skip_button = self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]')
            skip_button.click()
            
            time.sleep(2)
        
            
            agree_button = self.driver.find_element_by_xpath('//*[@id="termsofserviceNext"]/span/span')
            time.sleep(1)
            agree_button.click()
            
            time.sleep(2)
            
            
            
         def run(self):
            
            self.open_gmail_signup()
            self.signup_page_1()
            self.signup_page_2()
            self.signup_page_3()
            
            self.driver.quit()
                                                
                                        
    
      
    
if __name__ == "__main__":
    
    print("Initialising")
    gmail_bulk = GmailBulk(conf.BASE_URL)
    GmailBulk.run()