from flask import Blueprint, render_template, g

blog = Blueprint('blog', __name__, url_prefix='/')  # news蓝图


@blog.route('/', methods=['GET'])
def index():
    """首页"""
    return render_template('index.html', user_data=g.user_data)
