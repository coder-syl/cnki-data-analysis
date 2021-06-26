# coding:utf8
# from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import time
# from celery import task
# import redis
# import pymysql
#
from .get_cookies import getCookies
from .db_handle import dbHandle

# from get_cookies import getCookies
# from db_handle import dbHandle
# this is a function about need many time

# @task
# paper_url='http://kns.cnki.net/KCMS/detail/11.2103.TN.20190422.1403.030.html?uid=WEEvREdxOWJmbC9oM1NjYkZCbDdrdW1QRWVHWlNKY2JNUkFVTThpbHZRbFU=$R1yZ0H6jyaa0en3RxVUd8df-oHi7XMMDo7mtKT6mSmEvTuk11l2gFA!!&v=MDA3NTN1WnJGQ3JsVUwzTUlWWT1JVFhBZHJHNEg5ak1xNDFIWk90Mll3OU16bVJuNmo1N1QzZmxxV00wQ0xMN1I3cWVi'
def paperDetail(cookies,paper_url):
    print('开始爬取详情页')
    # DB = dbHandle();
    # 接收用户输入的关键词
    paper_url=paper_url
    cookies = dict(cookies)
    print(paper_url,cookies)
    r = requests.get(paper_url, cookies=cookies)
    # print(r.text)
    paper_description=''
    paper_fund=''
    paper_keyword=''
    try:
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.select('.wxBaseinfo')
        paper_description=results[0].select('p')[0]
        paper_description=str(paper_description.text)
        paper_fund = results[0].select('p')[1]
        paper_fund=str(paper_fund.text).replace(' ','').replace('\r\n','')
        paper_keyword = results[0].select('p')[2]
        paper_keyword=str(paper_keyword.text).replace(' ','').replace('\r\n','')
        time.sleep(3)
    except Exception as e:
        print('数据为空',e)

    return paper_description, paper_fund, paper_keyword
#
# cookies= {'c_m_expire': '2019-04-23 12:51:27', '_pk_ses': '*', '_pk_ref': '%5B%22%22%2C%22%22%2C1555993936%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D', 'c_m_LinID': 'LinID=WEEvREcwSlJHSldRa1FhdkJkVG1BVmpTQUozQ2hhR21URFB6cDkxZU9YWT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=04/23/2019 12:51:27', 'SID_krsnew': '125131', 'Ecp_ClientId': '4190423123001492160', 'Ecp_LoginStuts': '%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22NJ0051%22%2C%22ShowName%22%3A%22%25E6%25B1%259F%25E8%258B%258F%25E5%25B8%2588%25E8%258C%2583%25E5%25A4%25A7%25E5%25AD%25A6%25E4%25B8%2580%25E5%25B8%25A6%25E4%25B8%2580%25E8%25B7%25AF%25E7%25A0%2594%25E7%25A9%25B6%25E9%2599%25A2%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22IB43OG%22%7D', 'SID_crrs': '125133', 'LID': 'WEEvREcwSlJHSldRa1FhdkJkVG1BVmpTQUozQ2hhR21URFB6cDkxZU9YWT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!', 'Ecp_session': '1', 'SID_klogin': '125143', 'KNS_SortType': '', 'cnkiUserKey': 'b18eb70d-b09a-71d5-28a1-bb3d7d9acb00', 'SID_kns': '123113', 'ASP.NET_SessionId': 'lllaehphb55hcugftjtnb2dv', 'RsPerPage': '20', 'Ecp_notFirstLogin': 'IB43OG'}
# paperDetail(cookies,paper_url)