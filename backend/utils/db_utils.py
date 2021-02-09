"""
数据库sqlite 工具类
"""


class DbUtils:
    def __init__(self, dbName):  # 连接数据库
        import sqlite3
        self.conn = sqlite3.connect(dbName)

    def db_action(self, sql, actionType=0):  # 进行相关业务操作
        try:
            res = self.conn.execute(sql)
            if actionType == 1:  # 当操作类型为1时代表为查询业务，返回查询列表
                return res.fetchall()
            else:  # 当操作类型不为1时代表为新增、删除或更新业务，返回逻辑值
                return True
        except ValueError as e:
            print(e)

    def close(self):  # 关闭数据库
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    # 1.创建数据库
    db = DbUtils('web2020.db')

    # 2.创建新闻表
    sql = 'create table news (newsid int, content text, author text)'
    if db.db_action(sql, 0):
        print("创建新闻表成功！")
    else:
        print("try again1")

    # 3.新增新闻
    sql = "insert into news values (1,'武汉疫情非常严重，口罩等急需物品短缺','cao')," \
          "(2,'全国人民都给武汉加油，疫情肯定会控制住','cao')"
    if db.db_action(sql, 0):
        print("新增新闻表成功！")
    else:
        print("try again1")
    db.close()
