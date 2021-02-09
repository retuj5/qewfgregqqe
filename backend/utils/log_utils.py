from flask import g


def login_log():
    print(u'用户登录：%s' % g.login_data)


def login_ip_log(ip):
    pass
