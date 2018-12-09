import pymongo

from model.product import Product

PRIMARY_KEY = 'name'
COLLECTION_NAME = 'products'

class DAOProduct:

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.products = []
        self.set_up_ddbb()


    def insert(self, product):
        if self.find( product.name ) is None:
            self.products.append( product )
        else:
            self.update(product)


    def update(self, new_product):
        for product in self.products:
            if product.name == new_product.name:
                self.products.remove( product )
                self.products.append( new_product )


    def readAll(self):
        return [ product.toJSON() for product in self.products ]


    def delete(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove( product )


    def deleteAll(self):
        self.products = []


    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None


    def set_up_ddbb(self):
        # self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
        product1 = Product('Ibuprofen', 'Cures headache', 'Pharmacy 1', 7)
        product2 = Product('Frenadol', 'Cures flu', 'Pharmacy 2', 12)
        product3 = Product('Bandage', 'Cures wounds', 'Pharmacy 1', 10)

        self.products.append( product1 )
        self.products.append( product2 )
        self.products.append( product3 )
