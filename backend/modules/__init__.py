from flask import Flask
from flask.helpers import get_env
from flask_cors import CORS

from modules.blog.views import blog
from modules.demo.views import demo
from modules.auth.views import auth
from modules.news.views import news
from modules.product.views import product


def init_app(app: Flask) -> None:
    app.register_blueprint(demo)
    app.register_blueprint(blog)
    app.register_blueprint(auth)
    app.register_blueprint(news)
    app.register_blueprint(product)

    # if get_env() == 'development':
    #     CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
