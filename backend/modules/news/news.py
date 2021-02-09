from flask import Blueprint, render_template

from utils.db_utils import DbUtils

news = Blueprint('news', __name__)  # news蓝图


@news.route('/news')
def news_page():
    """新闻"""
    db = DbUtils('web2020.db')  # 链接web2020数据库
    sql = 'select * from news'  # 组装查询sql语句
    newslist = db.db_action(sql, 1)  # 查询处理并返回列表
    return render_template('news.html', data=newslist)
