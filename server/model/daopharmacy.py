import pymongo

from model.pharmacy import Pharmacy
from model.interfacedao import InterfaceDAO

PRIMARY_KEY = 'name'
COLLECTION_NAME = 'pharmacies'

class DAOPharmacy(InterfaceDAO):

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.pharmacies = []
        self.set_up_ddbb()


    def insert(self, new_pharmacy):
        if self.find( new_pharmacy.name ) is None:
            self.pharmacies.append( new_pharmacy )
        else:
            self.update( new_pharmacy )


    def update(self, new_pharmacy):
        for pharmacy in self.pharmacies:
            if pharmacy.name == new_pharmacy.name:
                self.pharmacies.remove( pharmacy )
                self.pharmacies.append( new_pharmacy )


    def readAll(self):
        return [ pharmacy.toJSON() for pharmacy in self.pharmacies ]


    def delete(self, pharmacy_name):
        for pharmacy in self.pharmacies:
            if pharmacy.name == pharmacy_name:
                self.pharmacies.remove( pharmacy )


    def deleteAll(self):
        self.pharmacies = []


    def find(self, pharmacy_name):
        for pharmacy in self.pharmacies:
            if pharmacy.name == pharmacy_name:
                return pharmacy
        return None


    def set_up_ddbb(self):
        # self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
        pharmacy1 = Pharmacy(name='Pharmacy 1', latitude=37.198366, longitude=-3.624976)
        pharmacy2 = Pharmacy(name='Pharmacy 2', latitude=37.195993, longitude=-3.622784)

        self.pharmacies.append( pharmacy1 )
        self.pharmacies.append( pharmacy2 )
