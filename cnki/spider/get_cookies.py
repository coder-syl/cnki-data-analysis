from selenium import webdriver
import time
def getCookies(keyWord):
    driver = webdriver.Chrome('/Users/syl/node_modules/chromedriver/lib/chromedriver/chromedriver')
    driver.get('http://www.cnki.net/')
    print(driver.title)
    search_text = driver.find_element_by_id('txt_SearchText')
    search_text.send_keys(keyWord)
    driver.find_element_by_class_name('input-box').find_element_by_class_name('search-btn').click()
    driver.refresh()
    time.sleep(1)
    cookies = {}
    for cookie in driver.get_cookies():
        cookies[cookie['name']] = cookie['value']
    driver.switch_to.frame('iframeResult')
    total_num=int(str(driver.find_element_by_class_name('pagerTitleCell').text).replace(' 找到 ','').replace(' 条结果','').replace(',',''))
    return cookies,total_num

