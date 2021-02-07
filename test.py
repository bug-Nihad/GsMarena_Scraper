import json
from selenium import webdriver
import time

def log_in(driver):
    driver.get('https://techweu.com/secure_admin')
    time.sleep(1)
    username = driver.find_element_by_xpath('//*[@id="user_login"]')
    username.send_keys('Michael@techweu')
    time.sleep(1)
    password = driver.find_element_by_xpath('//*[@id="user_pass"]')
    password.send_keys('cl0DnKYbO#f3j@%UM9$Xd*Uh')
    submit = driver.find_element_by_xpath('//*[@id="wp-submit"]')
    submit.click()


# driver = webdriver.Chrome('chromedriver.exe')
log_in()
