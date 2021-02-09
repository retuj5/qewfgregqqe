from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')  # news蓝图


@api.route('/demo')
def demo():
    return jsonify({"code": 200, "data": {"msg": "请求成功"}})
