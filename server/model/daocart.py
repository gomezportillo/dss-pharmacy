import pymongo

from model import product

PRIMARY_KEY = 'id'

class DAOOCart:

    def __init__(self):
        self.shopping_cart = {}

    def insert(self, product):
        if product.name in self.shopping_cart:
            quantity = self.shopping_cart[ product.name ]['quantity']
            self.shopping_cart[ product.name ]['quantity'] = quantity+1
        else:
            self.shopping_cart[ product.name ] = {'description':product.description, 'pharmacy':product.pharmacy, 'price':product.price, 'quantity':1}

    def update(self, product):
        pass

    def readAll(self):
        pass

    def delete(self, product):
        pass

    def deleteAll(self):
        pass

    def find(self, product):
        pass
