#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import pymysql
from practice_P2P.tools import project_path
import configparser
config_path = project_path.test_config_path
cf = configparser.ConfigParser()
cf.read(config_path,encoding='utf-8')
host = cf.get('DATABASE','host')
port = cf.get('DATABASE','port')
user = cf.get('DATABASE','user')
passwd = cf.get('DATABASE','passwd')
db_name = cf.get('DATABASE','db_name')


class OperateDb:
    """数据库操作封装"""

    def __init__(self):
        # 连接数据库
        self.connection = pymysql.connect(host=host,
                            port=int(port),
                            user=user,
                            passwd=passwd,
                            db=db_name,
                            cursorclass=pymysql.cursors.DictCursor)
        # 使用cursor()方法创建一个游标对象cur
        self.cur = self.connection.cursor()

    def select_db(self, selete_sql,state='all'):    #state=all是有多条记录，=1是只有1条记录
        """查询数据"""
        # 使用 execute()方法执行SQL查询
        self.cur.execute(selete_sql)
        if state == 1:
            # 使用fetchall()方法获取查询结果
            data = self.cur.fetchone()       #元祖类型，针对一条数据
        else:
            data = self.cur.fetchall()       #列表嵌套元祖，针对多行数据

        # 关闭数据库连接
        self.connection.close()
        return data

    def operate_db(self, sql):
        """删除/更新/新增数据"""
        try:
            self.cur.execute(sql)
            self.connection.commit()  # 提交操作
        except Exception as e:
            print("操作异常：{}".format(e))
            self.connection.rollback()  # 回滚操作
        finally:
            self.connection.close()


if __name__ == "__main__":
    sql1 = "select amount from incent_reward_record where id<=3"
    print(OperateDb().select_db(sql1))
    # sql2 = "update incent_reward_record set amount=55 where id=2"
    # OperateDb().operate_db(sql2)
    # print(OperateDb().select_db(sql1))