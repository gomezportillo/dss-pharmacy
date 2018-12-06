import os

from flask import Flask
from flask import send_from_directory
from flask import jsonify

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
VERSION = 0.2
authors = {}
authors['server'] = '@gomezportillo'
authors['mobile-app'] = '@xenahort'

# App definition
app = Flask(__name__)

# MongoDB URI
MONGODB_URI = 'mongodb://user:user123@ds123584.mlab.com:23584/pharmacy'

# DAOs
daoproduct = DAOProduct(MONGODB_URI)
daouser    = DAOUser(MONGODB_URI)
daopharm   = DAOPharmacy(MONGODB_URI)
daoorder   = DAOOrder(MONGODB_URI)

html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(html_dir, 'index.html')

@app.route('/rest/status', methods=['GET'])
def status():
    data = {}
    data['status'] = 'OK'
    data['version'] = VERSION
    data['authors'] = authors

    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route('/rest/pharmacies/all', methods=['GET'])
def get_pharmacies():
    pharmacies = daopharm.readAll()
    resp = jsonify(pharmacies)
    resp.status_code = 200
    return resp

@app.route('/rest/users/all', methods=['GET'])
def get_users():
    users = daouser.readAll()
    resp = jsonify(users)
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    return send_from_directory(html_dir, '404.html')

@app.errorhandler(405)
def not_allowed(error=None):
    return send_from_directory(html_dir, '405.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
