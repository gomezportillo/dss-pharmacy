import os

from flask import Flask
from flask import send_from_directory
from flask import jsonify
from flask import request
from flask import abort

from model.daouser import DAOUser
from model.daopharmacy import DAOPharmacy
from model.daoproduct import DAOProduct
from model.daoorder import DAOOrder
from model.daocart import DAOCart

from model.order import Order
from model.pharmacy import Pharmacy
from model.product import Product
from model.user import User

# Metadata
VERSION = 0.5
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
daos['cart']       = DAOCart()

# Constructors
constructors = {}
constructors['products']   = Product
constructors['users']      = User
constructors['pharmacies'] = Pharmacy
constructors['orders']     = Order
constructors['cart']       = Product

html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'html')
css_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'css')
img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'img')

@app.route('/css/main.css', methods=['GET'])
def get_css():
    return send_from_directory(css_dir, 'main.css')

@app.route('/', methods=['GET'])
def get_html_index():
    return send_from_directory(html_dir, 'index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(img_dir, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/img/logo.jpg', methods=['GET'])
def get_logo():
    return send_from_directory(img_dir, 'logo.jpg')


@app.route('/<string:path>', methods=['GET'])
def get_html_products(path):
    return send_from_directory(html_dir, path + '.html')

@app.route('/rest/status', methods=['GET'])
def get_status():
    data = {}
    data['status'] = 'OK'
    data['version'] = VERSION
    data['authors'] = authors

    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route('/rest/<string:resource>/all', methods=['GET'])
def GET_ALL_resources(resource):
    if resource in daos:
        result = daos[resource].readAll()
        resp = jsonify(result)
        resp.status_code = 200
        return resp
    else:
        abort(404)

@app.route('/rest/<string:resource>', methods=['POST'])
def POST_resource(resource):
    if resource in daos and resource in constructors:
        print('POST ' + str(request.form.to_dict()) + ' on ' + resource)
        resource_obj = constructors[resource](dict=request.form.to_dict())
        daos[resource].insert(resource_obj)
        resp = jsonify({'status':'201'})
        resp.status_code = 201
        return resp
    else:
        abort(404)

@app.route('/rest/<string:resource>', methods=['DELETE'])
def DELETE_product(resource):
    name = request.form.to_dict()['name']
    daos[resource].delete(name)
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
