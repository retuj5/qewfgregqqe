from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, url_prefix='/')  # news蓝图


@blog.route('/', methods=['GET'])
def index():
    """首页"""
    paginate = {
        'page': 1, 'per_page': 6, 'total': 3,
    }

    items = [
        {'title': '文章1', 'category': '分类', 'date': '2021-02-25', 'url': '/2021/0225/测试文章1',
         'last_modified': '2021-02-25'},
        {'title': '文章2', 'category': '分类', 'date': '2021-02-25', 'url': '/2021/0225/测试文章2',
         'last_modified': '2021-02-25'},
        {'title': '文章3', 'category': '分类', 'date': '2021-02-25', 'url': '/2021/0225/测试文章3',
         'last_modified': '2021-02-25'}
    ]

    return render_template('index.html', posts=items, paginate=paginate)


@blog.route('/<int:year>/<date>/<title>', methods=['GET'])
def post(year: str, date: str, title: str):
    post = {'title': '文章1', 'category': '分类', 'date': '2021-02-25', 'url': '/2021/0225/测试文章1',
            'last_modified': '2021-02-25', 'html': '阿黄是个变态'}
    return render_template("post.html", post=post)
