from model import order
from model.interfacedao import InterfaceDAO
from model.singleton import Singleton


@Singleton
class DAOOrder(InterfaceDAO):

    def __init__(self):
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
        self.orders = []
