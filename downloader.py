import json
from selenium import webdriver
import time

def download_data(url):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    expand = driver.find_element_by_xpath('//*[@id="specs-list"]/table[1]/tbody/tr[1]/td[2]/a')
    expand.click()
    phone_name = driver.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/div[1]/h1').text
    element = driver.find_element_by_xpath('//*[@id="specs-list"]')
    no = 0
    product = dict()
    product_attr = dict()

    try:
        for table in element.find_elements_by_tag_name('table'):
            rows = table.find_elements_by_tag_name('tr')
            for row in rows:
                atrr_header = row.find_element_by_tag_name('th').text
                break
            product_attr_temp = dict()

            for row in rows:

                data = row.find_elements_by_tag_name('td')
                if not data[0].text == ' ':
                    # print(data[0].text, data[1].text)
                    product_attr_temp[data[0].text] = data[1].text
                    key = data[0].text
                else:
                    product_attr_temp[key] = product_attr_temp[key] +', ' + data[1].text
            product_attr[atrr_header] = product_attr_temp
    except Exception as er:
        print(type(er))
    try:
        product_attr['disp'] = driver.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/div[2]/ul/li[4]/strong/span').text
    except:
        product_attr['disp'] = " "

    try:
        product_attr['cam'] = driver.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/div[2]/ul/li[5]/strong/span[1]').text + 'MP'
    except:
        product_attr['cam'] = " "

    try:
        product_attr['ram'] = driver.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/div[2]/ul/li[6]/strong/span[1]').text + 'GB Ram'
    except:
        product_attr['ram'] = " "

    try:
        product_attr['battry'] = driver.find_element_by_xpath('//*[@id="body"]/div/div[1]/div/div[2]/ul/li[7]/strong/span[1]').text + 'mAh'
    except:
        product_attr['battry'] = " "




    product[phone_name] = product_attr
    # print(json.dumps(product, indent=1))
    driver.close()
    return product
