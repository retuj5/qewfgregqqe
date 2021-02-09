from flask import Blueprint, render_template, session, redirect, url_for, request, g
import time
from utils.log_utils import login_log

account = Blueprint('account', __name__)  # news蓝图


@account.route('/login')
def login():
    """登录"""
    return render_template('login.html')


@account.route('/logout')
def do_logout():
    """登出"""
    session['username'] = ''
    session['login_time'] = ''
    return redirect(url_for('index'))


@account.route('/loginProcess', methods=['POST', 'GET'])
def do_login():
    """登录"""
    data = request.form
    nm = data['nm']
    session['username'] = nm
    session['login_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    g.login_data = session
    login_log()
    return redirect(url_for('index'))
