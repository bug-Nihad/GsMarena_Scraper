import json
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(10)

def log_in():
    driver.get('https://techweu.com/secure_admin')
    username = driver.find_element_by_xpath('//*[@id="user_login"]')
    username.send_keys('Michael@techweu')
    password = driver.find_element_by_xpath('//*[@id="user_pass"]')
    password.send_keys('bqPbS4MB*VcI7rbF9)nG27G5')
    submit = driver.find_element_by_xpath('//*[@id="wp-submit"]')
    submit.click()

def compulsory_input(xpath, key):
    while True:
        try:
            driver.find_element_by_xpath(xpath).send_keys(key)
            break
        except:
            try:
                driver.find_element_by_xpath('//*[@id="components-form-token-input-0"]').send_keys(key)
                break
            except:
                pass
            pass

def compulsory_click(xpath):
    while True:
        try:
            driver.find_element_by_xpath(xpath).click()
            break
        except:
            time.sleep(1)
            pass
k = 0
def upload_data(product):
    global k

    for key in product:
        model_name = key
        break
    # driver.find_element_by_xpath('//*[@id="post-title-0"]').send_keys(model_name + '\n' + model_name +  " on of " + product[model_name]['DISPLAY']['Resolution'] + "   . " + model_name +  " is powered by a " + product[model_name]['PLATFORM']['Chipset'] + " processor.\nAs far as the cameras are concerned, the " + model_name +  " on the rear packs " + product[model_name]['cam'] + " camera. It sports a " + product[model_name]['SELFIE CAMERA']['Single'] + " camera on the front for selfies.")
    #compulsory_click('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/h2/button')
    driver.find_element_by_xpath('//*[@id="post-title-0"]').send_keys(model_name)
    if k == 0:
        elem = driver.find_element_by_xpath('//*[@id="editor"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/h2/button')
        driver.execute_script('arguments[0].click()', elem)
        k = 1
    elem = driver.find_element_by_xpath('//textarea[@placeholder="Add title"]')
    elem.send_keys(model_name.split(' ')[0] + '\n')

    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[4]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/textarea').send_keys(model_name +  " on of " + product[model_name]['DISPLAY']['Resolution'] + "   . " + model_name +  " is powered by a " + product[model_name]['PLATFORM']['Chipset'] + " processor.\n As far as the cameras are concerned, the " + model_name +  " on the rear packs " + product[model_name]['cam'] + " camera. It sports a " + product[model_name]['SELFIE CAMERA']['Single'] + " camera on the front for selfies.)")
    #Features
    driver.execute_script("window.scrollTo(0, 1080)")
    elem = driver.find_element_by_xpath('//*[@id="aps_products_meta_box"]/div[2]/div/div/ul/li[2]')
    driver.execute_script('arguments[0].click()', elem)

    try:
        driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[1]/div[2]/input[3]').send_keys(product[model_name]['PLATFORM']['Chipset'])
    except:
        try:
            driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[1]/div[2]/input[3]').send_keys(product[model_name]['PLATFORM']['CPU'])
        except:
            driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[1]/div[2]/input[3]').send_keys("Unknown")

    driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[2]/div[2]/input[3]').send_keys(product[model_name]['disp'])
    driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[3]/div[2]/input[3]').send_keys(product[model_name]['cam'])
    try:
        driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[4]/div[2]/input[3]').send_keys(product[model_name]['ram'])
    except:
        try:
            driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[4]/div[2]/input[3]').send_keys(product[model_name]['MEMORY']['Internal'])
        except:
            driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[4]/div[2]/input[3]').send_keys("Unknown")

    driver.find_element_by_xpath('//*[@id="aps-tb-features"]/ul/li[5]/div[2]/input[3]').send_keys(product[model_name]['battry'])
    #Ratings
    driver.find_element_by_xpath('//*[@id="aps_products_meta_box"]/div[2]/div/div/ul/li[5]').click()
    driver.find_element_by_xpath('//*[@id="aps-tb-ratings"]/div/div[1]/p/label/input').click()
    #Attributes
    driver.find_element_by_xpath('//*[@id="aps_products_meta_box"]/div[2]/div/div/ul/li[6]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-375"]').send_keys(product[model_name]['NETWORK']['2G bands'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-376"]').send_keys(product[model_name]['NETWORK']['3G bands'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-377"]').send_keys(product[model_name]['NETWORK']['4G bands'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13172"]').send_keys(product[model_name]['NETWORK']['5G bands'])
    except:
        pass

    try:
        driver.find_element_by_xpath('//*[@id="attr-input-481"]').send_keys(product[model_name]['NETWORK']['Speed'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-418"]').send_keys(product[model_name]['NETWORK']['GPRS'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-408"]').send_keys(product[model_name]['NETWORK']['EDGE'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[2]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-23101"]').send_keys(model_name)
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-380"]').send_keys(product[model_name]['LAUNCH']['Announced'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[3]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-402"]').send_keys(product[model_name]['BODY']['Dimensions'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-502"]').send_keys(product[model_name]['BODY']['Weight'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13156"]').send_keys(product[model_name]['BODY']['Build'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-478"]').send_keys(product[model_name]['BODY']['SIM'])
    except:
        pass

    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[4]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-406"]').send_keys(product[model_name]['DISPLAY']['Type'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-479"]').send_keys(product[model_name]['DISPLAY']['Size'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-469"]').send_keys(product[model_name]['DISPLAY']['Resolution'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-405"]').send_keys(product[model_name]['DISPLAY']['Protection'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[5]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-447"]').send_keys(product[model_name]['PLATFORM']['OS'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-395"]').send_keys(product[model_name]['PLATFORM']['Chipset'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-397"]').send_keys(product[model_name]['PLATFORM']['CPU'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-420"]').send_keys(product[model_name]['PLATFORM']['GPU'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[6]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-394"]').send_keys(product[model_name]['MEMORY']['Card slot'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13170"]').send_keys(product[model_name]['MEMORY']['Internal'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25120"]').send_keys(product[model_name]['MEMORY']['Phonebook'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25121"]').send_keys(product[model_name]['MEMORY']['Call records'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[7]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13161"]').send_keys(product[model_name]['MAIN CAMERA']['Single'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13160"]').send_keys(product[model_name]['MAIN CAMERA']['Dual'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13159"]').send_keys(product[model_name]['MAIN CAMERA']['Triple'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13158"]').send_keys(product[model_name]['MAIN CAMERA']['Quad'])
    except:
        pass

    try:
        driver.find_element_by_xpath('//*[@id="attr-input-414"]').send_keys(product[model_name]['MAIN CAMERA']['Features'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-494"]').send_keys(product[model_name]['MAIN CAMERA']['Video'])
    except:
        pass
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[8]').click()
    try:
        driver.find_element_by_xpath('//input[@name="aps-attr[13163][13161]"]').send_keys(product[model_name]['SELFIE CAMERA']['Single'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//textarea[@name="aps-attr[13163][13160]"]').send_keys(product[model_name]['SELFIE CAMERA']['Dual'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//textarea[@name="aps-attr[13163][13159]"]').send_keys(product[model_name]['SELFIE CAMERA']['Triple'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//textarea[@name="aps-attr[13163][13158]"]').send_keys(product[model_name]['SELFIE CAMERA']['Quad'])
    except:
        pass

    try:
        driver.find_element_by_xpath('//textarea[@name="aps-attr[13163][414]"]').send_keys(product[model_name]['SELFIE CAMERA']['Features'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//input[@name="aps-attr[13163][494]"]').send_keys(product[model_name]['SELFIE CAMERA']['Video'])
    except:
        pass
    #Sound
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[9]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-439"]').send_keys(product[model_name]['SOUND']['Loudspeaker'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-379"]').send_keys(product[model_name]['SOUND']['Alert types'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-427"]').send_keys(product[model_name]['SOUND']['3.5mm jack'])
    except:
        pass
    #Connectivity
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[10]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-503"]').send_keys(product[model_name]['COMMS']['WLAN'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-388"]').send_keys(product[model_name]['COMMS']['Bluetooth'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-419"]').send_keys(product[model_name]['COMMS']['GPS'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-445"]').send_keys(product[model_name]['COMMS']['NFC'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-417"]').send_keys(product[model_name]['COMMS']['Radio'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-490"]').send_keys(product[model_name]['COMMS']['USB'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-424"]').send_keys(product[model_name]['COMMS']['HDMI'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-433"]').send_keys(product[model_name]['COMMS']['Infrared'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-411"]').send_keys(product[model_name]['COMMS']['Ethernet Port'])
    except:
        pass


    #Features
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[11]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-475"]').send_keys(product[model_name]['FEATURES']['Sensors'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25116"]').send_keys(product[model_name]['FEATURES']['Messaging'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25117"]').send_keys(product[model_name]['FEATURES']['Browser'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25118"]').send_keys(product[model_name]['FEATURES']['Games'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-25119"]').send_keys(product[model_name]['FEATURES']['Java'])
    except:
        pass
    #Battery
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[12]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-387"]').send_keys(product[model_name]['BATTERY']['Type'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-393"]').send_keys(product[model_name]['BATTERY']['Capacity'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13165"]').send_keys(product[model_name]['BATTERY']['Charging'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-482"]').send_keys(product[model_name]['BATTERY']['Standby'])
    except:
        pass

    #MISC
    driver.find_element_by_xpath('//*[@id="aps-tb-attributes"]/ul/li[13]').click()
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-396"]').send_keys(product[model_name]['MISC']['Colors'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-454"]').send_keys(product[model_name]['MISC']['Price'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13474"]').send_keys(product[model_name]['MISC']['SAR'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="attr-input-13475"]').send_keys(product[model_name]['MISC']['SAR EU'])
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="wds_focus"]').send_keys( model_name + '  specs and features, ' +  model_name + '  specs and price, ' +  model_name + '  specs and price in india, ' +  model_name + '  specs battery mah, ' +  model_name + '  specs camera, ' +  model_name + '  specs 128gb, ' +  model_name + '  specs front camera, ' +  model_name + '  specs apple, ' +  model_name + '  specs battery, ' +  model_name + '  specs battery life, ' +  model_name + '  specs body, ' +  model_name + '  buy online, ' +  model_name + '  buy india, ' +  model_name + '  buy online emi, ' +  model_name + '  buying options, ' +  model_name + '  buy amazon, ' +  model_name + '  buy apple, ' +  model_name + '  full phone specs, ' +  model_name + '  on discount ')
    except:
        pass
    time.sleep(2)
    elem = driver.find_element_by_xpath('//*[@id="editor"]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/button[2]')
    driver.execute_script('arguments[0].click()', elem)
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="editor"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/div[1]/button')
    driver.execute_script('arguments[0].click()', elem)
    x = 1
    while True:
        try:
            if x == 10:       # Time to wait
                break
            driver.find_element_by_xpath('//*[@id="inspector-text-control-0"]')
            print('Finished ' + model_name)
            break
        except:
            x = x + 1
            time.sleep(1)
            pass

def main():
    log_in()
    for line in open('product_data.txt', 'r').readlines():
        driver.get('https://techweu.com/wp-admin/post-new.php?cat_id=613&post_type=aps-products')
        product = json.loads(line)
        upload_data(product)
        driver.execute_script("window.open('https://google.com');")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



    # print(product)

if __name__ == '__main__':
    main()