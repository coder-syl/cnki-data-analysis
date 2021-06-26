from selenium import webdriver
import time


from .db_handle import dbHandle
# from db_handle import dbHandle
def getAuthors(driver, keywordID):
    print('点击作者链接')
    print(driver.find_element_by_link_text('作者').text)
    driver.find_element_by_link_text('作者').click()
    time.sleep(5)
    li_div = driver.find_element_by_class_name('hide')
    ul = li_div.find_element_by_tag_name('ul')
    lis = ul.find_elements_by_tag_name('li')
    print(lis)
    for li in lis:
        print('作者', str(li.text).replace('\n', ''))
        author = str(li.text).split('(')[0].replace('\n', '')
        number = str(li.text).split('(')[1].replace('\n', '').replace(')', '')
        print(author)
        print(number)
        dbhandle = dbHandle()
        # 插入年的信息
        in_author_sql = "INSERT INTO analyse_author ( author ) values('%s')" % (author)
        dbhandle.dbInsert(in_author_sql)

        query_authorID_sql = "select id from analyse_author where author='%s' " % (author)
        print(query_authorID_sql)
        author_id = dbhandle.dbQuery(query_authorID_sql)[0][0]
        print(author, 'author_id', author_id)

        in_author_to_keyword = "INSERT INTO analyse_authortokeyword(author_id_id,keyword_id_id,counts)" \
                             "values('%d','%d','%d')" \
                             % (author_id, keywordID, int(number))
        dbhandle.dbInsert(in_author_to_keyword)
    time.sleep(5)
