import os

from flask import Flask
from flask import send_from_directory

import pymongo

from model.product import Product
from model.daoproduct import DAOProduct
from model.user import User
from model.daouser import DAOUser

# App definition
app = Flask(__name__)

# MongoDB URI
MONGODB_URI = 'mongodb://user:user123@ds123584.mlab.com:23584/pharmacy'

# DAOs
# daoproduct = DAOProduct(MONGODB_URI)
# daouser = DAOUser(MONGODB_URI)

html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(html_dir, 'index.html')

@app.errorhandler(404)
def not_found(error=None):
    return send_from_directory(html_dir, '404.html')

@app.errorhandler(405)
def not_allowed(error=None):
    return send_from_directory(html_dir, '405.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)