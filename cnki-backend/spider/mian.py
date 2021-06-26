from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import csv
from celery import task




@task
def start_spider(page):
    print("爬虫启动")
    # 设置谷歌驱动器的环境
    options = webdriver.ChromeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # 创建一个谷歌驱动器
    browser = webdriver.Chrome('/Applications/chromedriver', chrome_options=options)
    url = 'http://wap.cnki.net/touch/web/guide'

    # 声明一个全局列表，用来存储字典
    data_list = []
    # 请求url
    browser.get(url)
    # 显示等待输入框是否加载完成
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.ID, 'keyword')
        )
    )
    # 找到输入框的id，并输入python关键字
    browser.find_element_by_id('keyword').click()
    browser.find_element_by_id('keyword_ordinary').send_keys('python')
    # 输入关键字之后点击搜索
    browser.find_element_by_class_name('btn-search ').click()
    # print(browser.page_source)
    # 显示等待文献是否加载完成
    WebDriverWait(browser, 1000).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'g-search-body')
        )
    )

    # 声明一个标记，用来标记翻页几页
    count = 1
    while True:
        # 显示等待加载更多按钮加载完成
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'c-company__body-item-more')
            )
        )
        # 获取加载更多按钮
        Btn = browser.find_element_by_class_name('c-company__body-item-more')
        # 显示等待该信息加载完成
        WebDriverWait(browser, 1000).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2*count-1))
            )
        )
        # 获取在div标签的信息，其中format(2*count-1)是因为加载的时候有显示多少条
        # 简单的说就是这些div的信息都是奇数
        divs = browser.find_elements_by_xpath('//div[@id="searchlist_div"]/div[{}]/div[@class="c-company__body-item"]'.format(2*count-1))
        # 遍历循环
        for div in divs:
            # 获取文献的题目
            name = div.find_element_by_class_name('c-company__body-title').text
            # 获取文献的作者
            author = div.find_element_by_class_name('c-company__body-author').text
            # 获取文献的摘要
            content = div.find_element_by_class_name('c-company__body-content').text
            # 获取文献的来源和日期、文献类型等
            text = div.find_element_by_class_name('c-company__body-name').text.split()
            if (len(text) == 3 and text[-1] == '优先') or len(text) == 2:
                # 来源
                source = text[0]
                # 日期
                datetime = text[1]
                # 文献类型
                literature_type = None
            else:
                source = text[0]
                datetime = text[2]
                literature_type = text[1]
            # 获取下载数和被引数
            temp = div.find_element_by_class_name('c-company__body-info').text.split()
            # 下载数
            download = temp[0].split('：')[-1]
            # 被引数
            cite = temp[1].split('：')[-1]

            # 声明一个字典存储数据
            data_dict = {}
            data_dict['name'] = name
            data_dict['author'] = author
            data_dict['content'] = content
            data_dict['source'] = source
            data_dict['datetime'] = datetime
            data_dict['literature_type'] = literature_type
            data_dict['download'] = download
            data_dict['cite'] = cite

            data_list.append(data_dict)
            print(data_dict)
        # 如果Btn按钮（就是加载更多这个按钮）没有找到（就是已经到底了），就退出
        if not Btn:
            break
        else:
            Btn.click()
        # 如果到了爬取的页数就退出
        if count == page:
            break

        count += 1

        # 延迟两秒，我们不是在攻击服务器
        time.sleep(2)


# def main():
#
#     start_spider(eval(input('请输入要爬取的页数（如果需要全部爬取请输入0）：')))
#
#     # 将数据写入json文件中
#     # with open('data_json.json', 'a+', encoding='utf-8') as f:
#     #     json.dump(data_list, f, ensure_ascii=False, indent=4)
#     # print('json文件写入完成')
#     #
#     # # 将数据写入csv文件
#     # with open('data_csv.csv', 'w', encoding='utf-8', newline='') as f:
#     #     # 表头
#     #     title = data_list[0].keys()
#     #     # 声明writer对象
#     #     writer = csv.DictWriter(f, title)
#     #     # 写入表头
#     #     writer.writeheader()
#     #     # 批量写入数据
#     #     writer.writerows(data_list)
#     # print('csv文件写入完成')
#
#
# if __name__ == '__main__':
#
#     main()

