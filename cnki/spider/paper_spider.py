# coding:utf8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import time
from celery import task
import redis
import pymysql
#
from .get_cookies import getCookies
from .db_handle import dbHandle
from .paper_detail import paperDetail


#
# from get_cookies import getCookies
# from db_handle import dbHandle


# this is a function about need many time

@task
def paperSpider(keyWord):
    print('爬虫启动')
    # conn = redis.Redis(host='127.0.0.1', port=6379,db=1,charset='utf-8',)
    # print('reids 连接成功')
    DB = dbHandle();
    # 接收用户输入的关键词
    key_word = keyWord
    # 获取到cookies，以便登录，同时获取到该关键词下有多少篇文章
    cookies, total_num = getCookies(key_word)  # 获取到
    # cookies字典化
    cookies = dict(cookies)
    urls = [
        'http://kns.cnki.net/kns/brief/brief.aspx?curpage={0}&RecordsPerPage=50&QueryID=0&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER&'.format(
            page) for page in range(1, int(total_num / 20))]
    # k是用来记录爬取了多少页
    k = 1
    for url in urls:
        num = 0
        r = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.select('.GridTableContent tr')
        print("正在爬取第%d页*************************************************************" % k);
        k = k + 1
        # print('requesting ' + url)
        if not results:
            driver = webdriver.Chrome('/Applications/chromedriver')
            for key in cookies:
                print(key, cookies[key])
                driver.add_cookie({key: cookies[key]})
            driver.get(url)
            break
        else:
            num = 0
            for r in results:
                if r.has_attr('bgcolor'):
                    # 解析出标题
                    record = r.select('td')[1].find('a')
                    paper_title = str(record.text).replace('\n', '')
                    # 文章详情链接页
                    paper_url = 'http://kns.cnki.net' + str(record.attrs['href']).replace('kns', 'KCMS')
                    # 作者
                    paper_author = str(r.select('td')[2].text).replace('\n', '')
                    authors = paper_author.split(';')
                    # 文章发表的期刊
                    paper_magazine = str(r.select('td')[3].text).replace('\n', '')
                    # 年份
                    paper_year = str(r.select('td')[4].text)
                    # .replace(' ', '')[0:5]
                    # 文章的类型
                    paper_source_type = str(r.select('td')[5].text).replace(' ', '').replace('\n', '')
                    title = str(record.text).replace('\n', '')
                    local_url = "http://localhost:8000/cnki/paperDetail?title="
                    local_url = str(local_url + title)
                    print(local_url)
                    print('论文发表年限------------', paper_year)

                    paper_description, paper_funds, paper_keywords=paperDetail(cookies, paper_url)
                    print(paper_description,paper_funds,paper_keywords)
                    # 存储数据库的信息
                    dbhandle = dbHandle()
                    # 插入文章的信息
                    in_paper_sql = "INSERT INTO analyse_paper(title,url,sch_key,description,paper_funds,paper_keywords,public_year,local_url,source_type)" \
                                   "values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                   % (paper_title, paper_url, key_word, paper_description,paper_funds,paper_keywords,paper_year, local_url, paper_magazine)
                    print(in_paper_sql)
                    dbhandle.dbInsert(in_paper_sql)
                    query_paperID_sql = "select id from analyse_paper where title='%s' " % (paper_title)
                    print(query_paperID_sql)
                    paper_id = dbhandle.dbQuery(query_paperID_sql)[0][0]
                    print('paper id', paper_id)
                    # 插入作者的信息
                    for author in authors:
                        author = author.replace(' ', '')
                        print(author)
                        in_author_sql = "INSERT INTO analyse_author(author)" \
                                        "values('%s')" \
                                        % (author)
                        dbhandle.dbInsert(in_author_sql)
                        query_authorID_sql = "select id from analyse_author where author='%s'" % (author)

                        print(query_authorID_sql)
                        author_id = dbhandle.dbQuery(query_authorID_sql)[0][0]
                        print('author id ', author_id)
                        # 插入作者与文章的信息的信息
                        in_author_to_paper = "INSERT INTO analyse_papertoauthor(author_id_id,paper_id_id)" \
                                             "values('%d','%d')" \
                                             % (author_id, paper_id)
                        dbhandle.dbInsert(in_author_to_paper)

                    num = num + 1

                print('第{}页抓取了{}条数据'.format(k, num))

        time.sleep(3)

# paperSpider('大数据')
