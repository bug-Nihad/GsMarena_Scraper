import json
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://google.com')
driver.switch_to.window(driver.window_handles[0])
driver.close()
