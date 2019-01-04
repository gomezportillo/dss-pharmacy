from model import Order
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton


@Singleton
class DAOOrder(InterfaceDAO):

    def __init__(self):
        self.set_up_ddbb()


    def insert(self, order):
        self.orders.append( order )


    def update(self, products):
        pass


    def readAll(self):
        return [ order.toJSON() for order in self.orders ]


    def delete(self, user):
        for order in self.orders:
            if order.user == user:
                self.orders.remove( order )

    def deleteAll(self):
        self.orders = []


    def find(self, email):
        for order in self.orders:
            if order.user == email:
                yield order
        return None


    def set_up_ddbb(self):
        self.orders = []
