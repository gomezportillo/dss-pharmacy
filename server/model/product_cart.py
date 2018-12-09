import json

from model.product import Product

class ProductCart(Product):

    def __init__(self, name=None, description=None, pharmacy=None, price=None, dict=None):
        super().__init__(name, description, pharmacy, price, dict)
        self.quantity = 1


    def toJSON(self):
        json_msg = super().toJSON()
        json_msg['quantity'] = self.quantity
        return json_msg
