from model.Product import Product

"""
Class inheriting from Product class
"""

class ProductCart(Product):

    def __init__(self, name=None, description=None, pharmacy=None, price=None, dict=None):
        super().__init__(name, description, pharmacy, price, dict)
        self.quantity = 1


    def toJSON(self):
        json_msg = super().toJSON()
        json_msg['quantity'] = self.quantity
        return json_msg


    def toXML(self):
        xml_price = '<price>{}</price>'.format( self.quantity )
        xml_msg = super().toXML()
        xml_msg = xml_msg.split('</product>')
        xml_msg = xml_msg[0] + xml_price + '</product>' + xml_msg[1]

        return xml_msg
