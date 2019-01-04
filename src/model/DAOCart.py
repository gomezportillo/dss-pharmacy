from model.ProductCart import ProductCart
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton


@Singleton
class DAOCart(InterfaceDAO):

    def __init__(self):
        self.shopping_cart = []


    def insert(self, new_product):
        if self.find( new_product.name ) is None:
            self.shopping_cart.append( new_product )
        else:
            for product in self.shopping_cart:
                if product.name == new_product.name:
                    product.quantity += 1


    def update(self, product):
        pass


    def readAll(self):
        return [ product.toJSON() for product in self.shopping_cart ]


    def delete(self, product_name):
        for product in self.shopping_cart:
            if product.name == product_name:
                self.shopping_cart.remove( product )


    def deleteAll(self):
        self.shopping_cart = []


    def find(self, product_name):
        for product in self.shopping_cart:
            if product.name == product_name:
                return product
        return None
