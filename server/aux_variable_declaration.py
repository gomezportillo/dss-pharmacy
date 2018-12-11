"""
The objective of this class is to hold all the variable declarations of the
server in order to ease its readability and maintainability.
"""

import os

from model.daouser import DAOUser
from model.daopharmacy import DAOPharmacy
from model.daoproduct import DAOProduct
from model.daoorder import DAOOrder
from model.daocart import DAOCart

from model.order import Order
from model.pharmacy import Pharmacy
from model.product import Product
from model.user import User
from model.product_cart import ProductCart

# Metadata
VERSION = 0.7
server_info = {}
server_info['version']     = VERSION
server_info['server_dev']  = 'Pedro Manuel Gómez-Portillo'
server_info['android_dev'] = 'Juan Carlos Serrano'
server_info['repository']  = 'https://github.com/gomezportillo/dss-pharmacy'


# DAOs
daos = {}
daos['products']   = DAOProduct( )
daos['users']      = DAOUser( )
daos['pharmacies'] = DAOPharmacy( )
daos['orders']     = DAOOrder( )
daos['cart']       = DAOCart()


# Constructors
constructors = {}
constructors['products']   = Product
constructors['users']      = User
constructors['pharmacies'] = Pharmacy
constructors['orders']     = Order
constructors['cart']       = ProductCart


# HTML file directories
html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'html')
css_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'css')
img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'website', 'img')
