from flask import Flask, session, g

import modules
from flask_cors import CORS
from common import templating

app = Flask(__name__)  # 实例化并命名为app实例
app.secret_key = 'lsadfklsjdoijzxclkvnj12312'
CORS(app)
modules.init_app(app)
templating.init_app(app)


def load_site_config():
    # 全局变量每次请求时赋值
    if "site" not in g:
        # user = User.get_admin()
        user = {
            'settings': {
                "locale": "zh",
                "start_from": "2020",
                "name": "唐哼哼博客",
                "cover_url": "/static/images/cover.jpg",
                "avatar": "/static/images/avatar.jpeg",
                "description": "A simple blog powered by Flask",
            }
        }
        g.site = user['settings']
    if "user_data" not in g:
        g.user_data = session
    print(f'当前用户 ：{session}')


if __name__ == "__main__":
    app.debug = True
    app.env = 'development'  # 区分开发环境与生产环境
    app.config['JSON_AS_ASCII'] = False
    app.before_request(load_site_config)
    app.run(port=2020, host="127.0.0.1", debug=True)
    print(app.config)
