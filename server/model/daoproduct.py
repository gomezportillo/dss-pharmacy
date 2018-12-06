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

    def insert(self, product):
        pass

    def update(self, product):
        pass

    def readAll(self):
        products = {}
        products['Ibuprofen'] = {'description': 'Cures headache', 'price': 10}
        products['Frenadol']  = {'description': 'Cures flu', 'price': 12}
        products['Bandage']   = {'description': 'Cures wounds', 'price': 10}
        return products


    def delete(self, product):
        pass

    def deleteAll(self):
        pass

    def find(self, product):
        pass

    def set_up_ddbb(self):
        self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
