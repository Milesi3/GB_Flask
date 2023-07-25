from flask import Flask, render_template

app = Flask(__name__)

products_data = [
    {'id': 1, 'name': 'Product 1', 'description': 'Description of Product 1', 'price': 19.99, 'category': 'clothing',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 2, 'name': 'Product 2', 'description': 'Description of Product 2', 'price': 29.99, 'category': 'clothing',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 3, 'name': 'Product 3', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 4, 'name': 'Product 4', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 5, 'name': 'Product 5', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 6, 'name': 'Product 6', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    {'id': 7, 'name': 'Product 7', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'https://avatars.dzeninfra.ru/get-zen_doc/4460346/pub_6085d3c1e2c7114111efc2a2_6085e4803b735b52f85124ce/scale_1200'},
    # Add more products with their respective categories here
]


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/category/<string:category_name>')
def category_page(category_name):
    category_products = [product for product in products_data if product['category'] == category_name]
    return render_template('category.html', category_name=category_name, products=category_products)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    product = next((product for product in products_data if product['id'] == product_id), None)
    return render_template('product.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
