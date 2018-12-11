from model.product import Product
from model.interfacedao import InterfaceDAO


class DAOProduct(InterfaceDAO):

    def __init__(self):
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
        product1 = Product('Ibuprofen', 'Cures headache', 'Pharmacy 1', 7)
        product2 = Product('Frenadol', 'Cures flu', 'Pharmacy 2', 12)
        product3 = Product('Bandage', 'Cures wounds', 'Pharmacy 1', 10)

        self.products.append( product1 )
        self.products.append( product2 )
        self.products.append( product3 )
