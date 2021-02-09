from flask import Flask, render_template, session, g

from modules.news.news import news
from modules.account.account import account
from modules.product.product import product
from modules.api.api import api

app = Flask(__name__)  # 实例化并命名为app实例
app.secret_key = 'lsadfklsjdoijzxclkvnj12312'
urls = [news, account, product, api]
for url in urls:
    app.register_blueprint(url)


@app.before_request
def common():
    # 全局变量每次请求时赋值
    g.user_data = session
    print(f'当前用户 ：{session}')


@app.route('/')
def index():
    """首页"""
    return render_template('index.html', user_data=g.user_data)


with app.test_request_context():
    print(app.config)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(port=2020, host="127.0.0.1", debug=True)
