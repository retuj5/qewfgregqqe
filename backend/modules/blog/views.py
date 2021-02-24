from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, url_prefix='/')  # news蓝图


@blog.route('/', methods=['GET'])
def index():
    """首页"""
    data = '你好，世界！'
    return render_template('index.html', data=data)
