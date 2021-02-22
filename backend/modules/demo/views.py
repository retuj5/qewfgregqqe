from flask import Blueprint, jsonify, render_template

demo = Blueprint('demo', __name__, url_prefix='/demo')  # news蓝图

@demo.route('/', methods=['GET'])
def index():
    return render_template('demo.html')


@demo.route('/demo', methods=['POST'])
def demo_request():
    return jsonify({"code": 200, "msg": "请求成功", "data": {"username": "周杰伦"}})
