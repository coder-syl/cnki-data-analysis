# coding:utf-8

import pymysql
from .config import db_config as df
# from config import db_config as df

class dbHandle():

    def __init__(self,):
        try:
            self.conn = pymysql.connect(host=df['host'],  user=df['user'], password=df['password'],database=df['database'],unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",charset='utf8')
        except:
            print("连接数据库失败")
        self.cur = self.conn.cursor()

    def dbClose(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()

    def dbQuery(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
    def dbInsert(self, sql):
        print('开始插入');
        try:
            self.cur.execute(sql)
            print("插入成功！！！")
            self.conn.commit()

        except Exception as e:
            print(e)
            print('插入失败！！！')

    def dbUpdate(self, sql):
        try:
            self.cur.execute(sql)
            print("更新状态成功！！！")
            self.conn.commit()

        except Exception as e:
            print(e)
            print('更新状态失败！！！')