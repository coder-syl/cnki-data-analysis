from selenium import webdriver
import time

from .db_handle import dbHandle
# from db_handle import dbHandle

def insertKeywordID(keyword):
    dbhandle = dbHandle()
    # 插入关键词的信息
    in_keyword_sql = "INSERT INTO analyse_keyword ( keyword ) values('%s')" % (keyword)
    dbhandle.dbInsert(in_keyword_sql)

    query_KeywordCount_sql = "select counts from analyse_keyword where keyword='%s' " % (keyword)
    print(query_KeywordCount_sql)
    KeywordCount = dbhandle.dbQuery(query_KeywordCount_sql)[0][0]

    in_keyword_sql = "UPDATE analyse_keyword  SET counts='%d' where keyword='%s'" % (int(KeywordCount),keyword)
    dbhandle.dbInsert(in_keyword_sql)

def getKeywordID(keyword):
    dbhandle = dbHandle()
    query_KeywordID_sql = "select id from analyse_keyword where keyword='%s' " % (keyword)
    print(query_KeywordID_sql)
    KeywordID = dbhandle.dbQuery(query_KeywordID_sql)[0][0]
    print(KeywordID, 'KeywordID', KeywordID)
    return KeywordID
