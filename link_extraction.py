import time
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')

links = open('link.txt', 'w')
def individual_product(url):
    driver.get(url)
    while True:
        try:
            table = driver.find_element_by_xpath('//*[@id="review-body"]/div[1]')
            products = table.find_elements_by_tag_name('a')
            for product in products:
                print(product.text)
                print(product.get_attribute('href'))
                links.write(product.get_attribute('href') + '\n')
        except:
            print('Retrying......')
            continue
        try:
            nest_page = driver.find_element_by_xpath('//*[@id="body"]/div/div[3]/div[2]/a[2]')
            time.sleep(1)
            nest_page.click()
            time.sleep(1)
        except:
            break





driver.get('https://www.gsmarena.com/makers.php3')
table = driver.find_element_by_xpath('//*[@id="body"]/div/div[2]/table')
brands = table.find_elements_by_tag_name('a')
brand_link = list()
for brand in brands:
    if brand.text.split('\n')[0] == 'ONEPLUS' or brand.text.split('\n')[0] == 'REALME':
        continue
    print(brand.text.split('\n')[0])
    brand_link.append(brand.get_attribute('href'))
    # print(brand.get_attribute('href'))

for brand in brand_link:
    individual_product(brand)
# individual_product('https://www.gsmarena.com/philips-phones-11.php')
# individual_product('https://www.gsmarena.com/acer-phones-59.php')