"""
The objective of this class is to hold all the variable declarations of the
server in order to ease its readability and maintainability.
"""

import os
import datetime
import json

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

from flask import Flask
from flask import send_from_directory
from flask import jsonify
from flask import request
from flask import abort
from flask import Response


# Flask initialisation
app = Flask(__name__)


# Metadata
VERSION = 1.2
server_info = {}
server_info['version']     = VERSION
server_info['server_dev']  = 'Pedro Manuel Gómez-Portillo'
server_info['android_dev'] = 'Juan Carlos Serrano'
server_info['repository']  = 'https://github.com/gomezportillo/dss-pharmacy'


# HTML file directories
HTML_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'html')
CSS_DIR  = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'css')
IMG_DIR  = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'website', 'img')
