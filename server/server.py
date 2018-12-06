import os

from flask import Flask
from flask import send_from_directory
from flask import jsonify
from flask import request
from flask import abort

import pymongo

from model.daouser import DAOUser
from model.daopharmacy import DAOPharmacy
from model.daoproduct import DAOProduct
from model.daoorder import DAOOrder

from model.order import Order
from model.pharmacy import Pharmacy
from model.product import Product
from model.user import User

# Metadata
VERSION = 0.3
authors = {}
authors['server'] = '@gomezportillo'
authors['mobile-app'] = '@xenahort'

# App definition
app = Flask(__name__)

# MongoDB URI
MONGODB_URI = 'mongodb://user:user123@ds123584.mlab.com:23584/pharmacy'

# DAOs
daos = {}
daos['products']   = DAOProduct(MONGODB_URI)
daos['users']      = DAOUser(MONGODB_URI)
daos['pharmacies'] = DAOPharmacy(MONGODB_URI)
daos['orders']     = DAOOrder(MONGODB_URI)

html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'html')
css_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'css')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(html_dir, 'index.html')

@app.route('/products', methods=['GET'])
def products():
    return send_from_directory(html_dir, 'products.html')


@app.route('/css/main.css', methods=['GET'])
def get_css():
    return send_from_directory(css_dir, 'main.css')

@app.route('/rest/status', methods=['GET'])
def status():
    data = {}
    data['status'] = 'OK'
    data['version'] = VERSION
    data['authors'] = authors

    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route('/rest/<string:resource_name>/all', methods=['GET'])
def get_resource(resource_name):
    if resource_name in daos:
        result = daos[resource_name].readAll()
        resp = jsonify(result)
        resp.status_code = 200
        return resp
    else:
        abort(404)

@app.route('/rest/products', methods=['POST'])
def post_product():
    params = request.form.to_dict()
    product = Product(params['name'], params['description'], params['price'])
    daos['products'].insert(product)
    
    resp = jsonify({'status':'201'})
    resp.status_code = 201
    return resp


@app.errorhandler(404)
def not_found(error=None):
    return send_from_directory(html_dir, '404.html')

@app.errorhandler(405)
def not_allowed(error=None):
    data = {}
    data['status'] = '405'
    data['message'] = 'URL {} not allowed from {} HTTP method'.format(request.url, request.method)
    resp = jsonify(data)
    resp.status_code = 405
    return resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
