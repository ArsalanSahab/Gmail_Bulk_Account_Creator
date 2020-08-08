# IMPORTS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configs as conf


# Chrome Driver Setup Functions


def get_chrome_driver(options):
    return webdriver.Chrome(chrome_options=options)

def get_chromdriver_options():
    return webdriver.ChromeOptions()
    
     
def set_ignore_certificate_error(options):
    return options.add_argument('--ignore-certifictae-errors')

def set_incognito_mode(options):
    return options.add_argument('--incognito')


def open_gmail_signup(my_driver):
    
    # Open Gmail Signup Page 
    
    BASE_URL = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
    
    my_driver.get(BASE_URL)
    time.sleep(2)
    

    
    
def enter_details(my_driver):
    
    first_name = my_driver.find_element_by_xpath('//*[@id="firstName"]')
    first_name.send_keys(conf.FIRST_NAME)
    
    last_name = my_driver.find_element_by_xpath('//*[@id="lastName"]')
    last_name.send_keys(conf.LAST_NAME)
    
    gmail_id = my_driver.find_element_by_xpath('//*[@id="username"]')
    gmail_id.send_keys(conf.USER_ID)
    
    password = my_driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
    password.send_keys(conf.PASSWORD)
    
    confirm_password = my_driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
    confirm_password.send_keys(conf.PASSWORD)
    
    time.sleep(2)
    
    next_button = my_driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/span')
    next_button.click()
    
    time.sleep(2)
    
    phone_number = my_driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
    phone_number.send_keys(conf.PHONE)
    
   
    
    next_button_2 = my_driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
    next_button_2.click()
    
    phone_code = input("Enter Verification Code : ")
    phone_verify = my_driver.find_element_by_xpath('//*[@id="code"]')
    phone_verify.send_keys(phone_code)
    phone_verify.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    month = my_driver.find_element_by_xpath('//*[@id="month"]')
    month.send_keys("j")
    
    day = my_driver.find_element_by_xpath('//*[@id="day"]')
    day.send_keys("1")
    
    year = my_driver.find_element_by_xpath('//*[@id="year"]')
    year.send_keys("1995")
    
    gender = my_driver.find_element_by_xpath('//*[@id="gender"]')
    gender.click()
    gender.click()
    
    time.sleep(1)
    
    next_button_3 = my_driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
    next_button_3.click()
    
    skip_button = my_driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]')
    skip_button.click()
    
    agree_button = my_driver.find_element_by_xpath('//*[@id="termsofserviceNext"]/span/span')
    time.sleep(1)
    agree_button.click()
    
    time.sleep(2)
                                                
                                            
def main():
    
    options = get_chromdriver_options()
    set_ignore_certificate_error(options)
    set_incognito_mode(options)
    driver = get_chrome_driver(options)
    
    open_gmail_signup(driver)
    enter_details(driver)
    
    driver.quit()
    
      
    
if __name__ == "__main__":
    
    main()