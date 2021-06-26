from selenium import webdriver
import time

from .db_handle import dbHandle
# from db_handle import dbHandle

def getFunds(driver, keywordID):
    print('点击基金链接')
    print(driver.find_element_by_link_text('基金').text)
    driver.find_element_by_link_text('基金').click()
    time.sleep(5)
    li_div = driver.find_element_by_class_name('hide')
    ul = li_div.find_element_by_tag_name('ul')
    lis = ul.find_elements_by_tag_name('li')
    print(lis)
    for li in lis:
        print('基金', str(li.text).replace('\n', ''))
        fund = str(li.text).split('(')[0].replace('\n', '')
        if(fund=='国家高技术研究发展计划'):
            fund=fund+'(863计划)'
        if(fund=='国家重点基础研究发展计划'):
            fund = fund + '(973计划)'
        if(fund=='江苏省教育厅人文社会科学研究基...'):
            fund='江苏省教育厅人文社会科学研究基金'
        number = str(li.text).replace('(97...', '').replace('(863...', '')
        number = number.split('(')[1].replace('\n', '').replace(')', '')

        print(fund)
        print(number)

        dbhandle = dbHandle()
        # 插入年的信息
        in_fund_sql = "INSERT INTO analyse_fund ( fund ) values('%s')" % (fund)
        dbhandle.dbInsert(in_fund_sql)

        query_fundID_sql = "select id from analyse_fund where fund='%s' " % (fund)
        print(query_fundID_sql)
        fund_id = dbhandle.dbQuery(query_fundID_sql)[0][0]
        print(fund, 'fund_id', fund_id)

        in_fund_to_keyword = "INSERT INTO analyse_fundtokeyword(fund_id_id,keyword_id_id,counts)" \
                               "values('%d','%d','%d')" \
                               % (fund_id, keywordID, int(number))
        dbhandle.dbInsert(in_fund_to_keyword)
    time.sleep(5)
