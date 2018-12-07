import pymongo

from model import pharmacy

PRIMARY_KEY = 'name'
COLLECTION_NAME = 'pharmacies'

class DAOPharmacy:

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.set_up_ddbb()

        self.pharmacies = {}
        self.pharmacies['Farmacia 1'] = {'latitude': 37.198366, 'longitude': -3.624976}
        self.pharmacies['Farmacia 2'] = {'latitude': 37.195993, 'longitude': -3.622784}

    def insert(self, pharmacy):
        self.pharmacies[pharmacy.name] = {'latitude': float(pharmacy.lat), 'longitude': float(pharmacy.lon)}

    def update(self, pharmacy):
        pass

    def readAll(self):
        return self.pharmacies

    def delete(self, key):
        self.pharmacies.pop(key)

    def deleteAll(self):
        pass

    def find(self, pharmacy):
        pass

    def set_up_ddbb(self):
        self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
