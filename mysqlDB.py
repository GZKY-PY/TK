# -*- coding:utf-8 -*-
import pymysql
import json


class Mysql():
    '''
    mysql数据库的一些常用操作
    '''

    def __init__(self, database_name):

        self.db = pymysql.connect(host='127.0.0.1', user='root', password='710727', port=3306, db=database_name)
        self.cursor = self.db.cursor()

    # def create_database(self,database_name):
    #     sql = "CREATE DATABASE {database_name} DEFAULT CHARACTER SET utf8".format(database_name=database_name)
    #     self.cursor.execute(sql)

    def create_table(self, table_name):

        sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
        self.cursor.execute(sql)

    def insert_data(self, table_name, data):

        sql = f'INSERT INTO {table_name}(id, content_name, content,fenci_words,key_words) values(%s, %s, %s, %s, %s)'
        for i in data:
            try:
                self.cursor.execute(sql, (i["id"], i["content_name"], i["content"], i["fenci_words"], i["key_words"]))
                self.db.commit()
                print("ok .......")
            except:
                self.db.rollback()

    def query_data(self, table_name):
        data_list = []
        sql = f'SELECT * FROM {table_name}'

        try:
            self.cursor.execute(sql)
            # 全部数据列表
            results = self.cursor.fetchall()
            for row in results:
                data_list.append(row)
            return data_list
        except:
            print('Error')

    def delete_data(self, table_name, condition):
        sql = f"DELETE FROM  {table_name} WHERE {condition}"  # 删除条件
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def update_data(self, table_name, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))

        sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE"
        update = ','.join([" {key} = %s".format(key=key) for key in data])
        sql += update
        try:
            if self.cursor.execute(sql, tuple(data.values()) * 2):
                print('Successful')
                self.db.commit()
        except:
            print('Failed')
            self.db.rollback()

    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    M = Mysql("test")
    data_list = M.query_data("law_content")
    for data in data_list:
        print(data)

# ccc = input("请输入关键字:")
#
# select_result = []
# for data in data_list:
#     fenci_words_list = [i for i in data[3].split(' ') if i != '']
#     if ccc in fenci_words_list:
#         print("Content:",data[1])
