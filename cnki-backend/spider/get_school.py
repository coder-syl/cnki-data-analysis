from selenium import webdriver
import time

from .db_handle import dbHandle
# from db_handle import dbHandle
def getSchools(driver, keywordID):
    print('点击机构链接')
    print(driver.find_element_by_link_text('机构').text)
    driver.find_element_by_link_text('机构').click()
    time.sleep(5)
    li_div = driver.find_element_by_class_name('hide')
    ul = li_div.find_element_by_tag_name('ul')
    lis = ul.find_elements_by_tag_name('li')
    print(lis)
    for li in lis:
        print('机构', str(li.text).replace('\n', ''))
        school = str(li.text).split('(')[0].replace('\n', '')
        number = str(li.text).split('(')[1].replace('\n', '').replace(')', '')
        print(school)
        print(number)
        dbhandle = dbHandle()
        # 插入年的信息
        in_school_sql = "INSERT INTO analyse_school ( school ) values('%s')" % (school)
        dbhandle.dbInsert(in_school_sql)

        query_schoolID_sql = "select id from analyse_school where school='%s' " % (school)
        print(query_schoolID_sql)
        school_id = dbhandle.dbQuery(query_schoolID_sql)[0][0]
        print(school, 'school_id', school_id)

        in_school_to_keyword = "INSERT INTO analyse_schooltokeyword(school_id_id,keyword_id_id,counts)" \
                             "values('%d','%d','%d')" \
                             % (school_id, keywordID, int(number))
        dbhandle.dbInsert(in_school_to_keyword)
    time.sleep(5)