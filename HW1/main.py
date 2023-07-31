from flask import Flask, render_template

app = Flask(__name__)

products_data = [
    {'id': 1, 'name': 'Product 1', 'description': 'Description of Product 1', 'price': 19.99, 'category': 'clothing',
     'image_url': 'img/foto.jpg'},
    {'id': 2, 'name': 'Product 2', 'description': 'Description of Product 2', 'price': 29.99, 'category': 'clothing',
     'image_url': 'img/foto.jpg'},
    {'id': 3, 'name': 'Product 3', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'img/foto.jpg'},
    {'id': 4, 'name': 'Product 4', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'img/foto.jpg'},
    {'id': 5, 'name': 'Product 5', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'img/foto.jpg'},
    {'id': 6, 'name': 'Product 6', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'img/foto.jpg'},
    {'id': 7, 'name': 'Product 7', 'description': 'Description of Product 3', 'price': 39.99, 'category': 'footwear',
     'image_url': 'img/foto.jpg'},
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
