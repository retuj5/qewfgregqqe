from flask import Blueprint, render_template, request

product = Blueprint('product', __name__)  # news蓝图


@product.route('/product/detail/<id>')
def product_detail_page(id):
    """产品"""
    type = request.args.get("type", '')
    product_name = f'产品 {id} {type}'
    return render_template('product_detail.html', data=product_name)


@product.route('/product/list')
def product_page():
    """产品"""
    type = request.args.get("type", '')
    product_name = f'产品 {type}'
    return render_template('product_list.html', data=product_name)
