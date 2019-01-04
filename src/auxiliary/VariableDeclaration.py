"""
The objective of this class is to hold all the variable declarations of the
server in order to ease its readability and maintainability.
"""

import os
import datetime

from model.DAOUser import DAOUser
from model.DAOPharmacy import DAOPharmacy
from model.DAOProduct import DAOProduct
from model.DAOOrder import DAOOrder
from model.DAOCart import DAOCart

from model.Order import Order
from model.Pharmacy import Pharmacy
from model.Product import Product
from model.User import User
from model.ProductCart import ProductCart


# Metadata
VERSION = 1.1
server_info = {}
server_info['version']     = VERSION
server_info['server_dev']  = 'Pedro Manuel Gómez-Portillo'
server_info['android_dev'] = 'Juan Carlos Serrano'
server_info['repository']  = 'https://github.com/gomezportillo/dss-pharmacy'


# DAOs
daos = {}
daos['products']   = DAOProduct.instance()
daos['users']      = DAOUser.instance()
daos['pharmacies'] = DAOPharmacy.instance()
daos['orders']     = DAOOrder.instance()
daos['cart']       = DAOCart.instance()


# Constructors
constructors = {}
constructors['products']   = Product
constructors['users']      = User
constructors['pharmacies'] = Pharmacy
constructors['orders']     = Order
constructors['cart']       = ProductCart


# HTML file directories
html_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'html')
css_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'css')
img_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'img')
