import pymongo

from model import product

PRIMARY_KEY = 'name'
COLLECTION_NAME = 'products'

class DAOProduct:

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.set_up_ddbb()

        self.products = {}
        self.products['Ibuprofen'] = {'description': 'Cures headache', 'pharmacy': 'Farmacia 1', 'price': 10}
        self.products['Frenadol']  = {'description': 'Cures flu', 'pharmacy': 'Farmacia 2',  'price': 12}
        self.products['Bandage']   = {'description': 'Cures wounds', 'pharmacy': 'Farmacia 1',  'price': 10}


    def insert(self, product):
        self.products[product.name] = {'description':product.description, 'pharmacy':product.pharmacy, 'price':product.price}

    def update(self, product):
        pass

    def readAll(self):
        return self.products

    def delete(self, key):
        self.products.pop(key)

    def deleteAll(self):
        pass

    def find(self, product):
        pass

    def set_up_ddbb(self):
        self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
