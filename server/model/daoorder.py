import pymongo

from model import order
from model.interfacedao import InterfaceDAO

PRIMARY_KEY = 'id'
COLLECTION_NAME = 'orders'

class DAOOrder(InterfaceDAO):

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.set_up_ddbb()


    def insert(self, order):
        self.orders.append( order )


    def update(self, product):
        pass


    def readAll(self):
        return [ order.toJSON() for order in self.orders ]


    def delete(self, product):
        pass


    def deleteAll(self):
        self.orders = []


    def find(self, product):
        pass


    def set_up_ddbb(self):
        # self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
        self.orders = []
