from selenium import webdriver
import time

from .db_handle import dbHandle


# from db_handle import dbHandle


def getYear(driver, keywordID):
    print('点击发表年度链接')
    print(driver.find_element_by_link_text('发表年度').text)
    driver.find_element_by_link_text('发表年度').click()
    time.sleep(5)
    li_div = driver.find_element_by_class_name('hide')
    ul = li_div.find_element_by_tag_name('ul')
    lis = ul.find_elements_by_tag_name('li')
    print(lis)
    for li in lis:
        print('nian', str(li.text).replace('\n', ''))
        year = str(li.text).replace('\n', '')[0:4]
        number = str(li.text).replace('\n', '')[5:].replace(')', '')
        print(year)
        print(number)

        dbhandle = dbHandle()
        # 插入年的信息
        in_year_sql = "INSERT INTO analyse_year ( year ) values('%s')" % (year)
        dbhandle.dbInsert(in_year_sql)

        query_yearID_sql = "select id from analyse_year where year='%s' " % (year)
        print(query_yearID_sql)
        year_id = dbhandle.dbQuery(query_yearID_sql)[0][0]
        print(year, 'year_id', year_id)
        #queryCount_sql = "select count(*) from analyse_yeartokeyword where  keyword_id_id={}".format(keywordID)
        #print(queryCount_sql)
        # haveCount =0 #dbhandle.dbQuery(queryCount_sql)[0][0]
        # if (haveCount == 0):
        #     break;
        in_year_to_keyword = "INSERT INTO analyse_yeartokeyword(year_id_id,keyword_id_id,counts)" \
                             "values('%d','%d','%d')" \
                             % (year_id, keywordID, int(number))
        # else:
        #     print('数据库中已经存在该数据')
        dbhandle.dbInsert(in_year_to_keyword)
    time.sleep(5)
    # return 1;
