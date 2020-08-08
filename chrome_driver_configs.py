# IMPORTS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome Driver Setup Functions

def get_chrome_driver(options):
    return webdriver.Chrome(chrome_options=options)

def get_chromdriver_options():
    return webdriver.ChromeOptions()
    
     
def set_ignore_certificate_error(options):
    return options.add_argument('--ignore-certifictae-errors')

def set_incognito_mode(options):
    return options.add_argument('--incognito')