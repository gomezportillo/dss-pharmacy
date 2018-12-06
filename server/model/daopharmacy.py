import pymongo

from model import product

PRIMARY_KEY = 'name'
COLLECTION_NAME = 'pharmacies'

class DAOPharmacy:

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]

    def insert(self, product):
        pass

    def update(self, product):
        pass

    def readAll(self):
        pharms = {}
        pharms['Farmacia 1'] = {'latitude': 37.198366, 'longitude': -3.624976}
        pharms['Farmacia 2'] = {'latitude': 37.195993, 'longitude': -3.622784}
        return pharms

    def delete(self, product):
        pass

    def deleteAll(self, product):
        pass

    def find(self, product):
        pass

    def set_up_ddbb(self):
        self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
