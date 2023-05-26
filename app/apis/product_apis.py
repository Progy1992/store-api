from app import app, jsonify, Product

products = Product()


@app.route('/v1/products')
def get_all_products():
    try:
        return jsonify({
            'data': products.get_all_products()
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch all products data.'
        }), 400


@app.route('/v1/products/<int:id>')
def get_product_by_id(id):
    try:
        return jsonify({
            'data': products.get_product_by_id(id)
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch product data with specified id.'
        }), 400
