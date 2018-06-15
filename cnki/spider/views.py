from django.shortcuts import render

from spider.get_cookies import getCookies
import time
from bs4 import BeautifulSoup
import requests


def spider():
    cookies, total_num = getCookies('大数据')
    cookies = dict(cookies)
    urls = [
        'http://kns.cnki.net/kns/brief/brief.aspx?curpage={0}&RecordsPerPage=50&QueryID=0&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER&'.format(
            page) for page in range(1, int(total_num/20))]
    k=1
    for url in urls:
        r = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.select('.GridTableContent tr')
        print(k);
        k=k+1
        print('requesting ' + url)
        if not results:
            print('请到 ' + url + ' 输入验证码, 输入完毕且正确后请打y')
            is_success = input()
            if is_success == 'y':
                continue
            else:
                print('请重新输入验证码')
        else:
            for r in results:
                if r.has_attr('bgcolor'):
                    record = r.select('td')[1].find('a')
                    print(record.text)
                    year = r.select('td')[4].text
                    url = 'http://kns.cnki.net' + record.attrs['href']
                    title = record.text
        time.sleep(3)


spider()
