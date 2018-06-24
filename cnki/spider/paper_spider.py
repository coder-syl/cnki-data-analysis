#coding:utf8

from spider.get_cookies import getCookies
import time
from bs4 import BeautifulSoup
import requests

import time

from celery import task

import redis


# this is celery settings


# this is a function about need many time

@task
def paperSpider(keyWord):
    print('爬虫启动')
    conn = redis.Redis(host='127.0.0.1', port=6379,db=1,charset='utf-8',)
    print('reids 连接成功')
    key_word=keyWord
    cookies, total_num = getCookies(key_word)
    cookies = dict(cookies)
    urls = [
        'http://kns.cnki.net/kns/brief/brief.aspx?curpage={0}&RecordsPerPage=50&QueryID=0&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER&'.format(
            page) for page in range(1, int(total_num / 20))]
    k = 1
    for url in urls:
        num = 0
        r = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.select('.GridTableContent tr')
        print(k);
        k = k + 1
        print('requesting ' + url)
        if not results:
            # print('请到 ' + url + ' 输入验证码, 输入完毕且正确后请打y')
            # is_success = input()
            # if is_success == 'y':
            #     continue
            # else:
            #     print('请重新输入验证码')
            break
        else:
            for r in results:
                if r.has_attr('bgcolor'):
                    record = r.select('td')[1].find('a')

                    year = str(r.select('td')[4].text)
                    paper_url = 'http://kns.cnki.net' + str(record.attrs['href']).replace('kns', 'KCMS')
                    title = str(record.text)
                    num = num + 1;
                    # paper_detail = {
                    #     title: title,
                    # }
                    conn.sadd(key_word,record.text)
                    spider_data = conn.smembers('大数据')
        time.sleep(3)
# paperSpider()