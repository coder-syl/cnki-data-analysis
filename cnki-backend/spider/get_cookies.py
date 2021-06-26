from selenium import webdriver
import time
from .get_year import getYear
from .get_authors import getAuthors
from .get_school import getSchools
from .get_fund import getFunds
from .get_keyWordID import getKeywordID,insertKeywordID
#
# from get_year import getYear
# from get_authors import getAuthors
# from get_school import getSchools
# from get_fund import getFunds
# from get_keyWordID import getKeywordID,insertKeywordID


def getCookies(keyWord):
    driver = webdriver.Chrome(r"C:\Users\Administrator\Desktop\cnki\spider\chromedriver.exe")
    print('正在打开知网')
    driver.get('http://www.cnki.net/')
    # print(driver.title)
    print('正在获取cookies')
    search_text = driver.find_element_by_id('txt_SearchText')
    search_text.send_keys(keyWord)
    driver.find_element_by_class_name('input-box').find_element_by_class_name('search-btn').click()
    driver.refresh()
    time.sleep(5)
    # insertKeywordID(keyWord)
    # keyWord_id = getKeywordID(keyWord)
    keyWord_id=1
    getYear(driver, keyWord_id)

    # 因为只有上一个点击了下一个标签才会被加载
    print('点击研究层次')
    print(driver.find_element_by_link_text('研究层次').text)
    driver.find_element_by_link_text('研究层次').click()
    time.sleep(5)

    getAuthors(driver, keyWord_id)
    getSchools(driver, keyWord_id)
    getFunds(driver, keyWord_id)

    cookies = {}
    for cookie in driver.get_cookies():
        cookies[cookie['name']] = cookie['value']
    driver.switch_to.frame('iframeResult')
    total_num = int(
        str(driver.find_element_by_class_name('pagerTitleCell').text).replace(' 找到 ', '').replace(' 条结果', '').replace(
            ',', ''))
    # driver.find_element_by_link_text('50').click()
    print(cookies)
    time.sleep(5)
    return cookies, total_num


# getCookies('大数据')
