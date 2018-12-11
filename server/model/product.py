
class Product:

    def __init__(self, name=None, description=None, pharmacy=None, price=None, dict=None):
        if dict is None:
            self.name        = name
            self.description = description
            self.pharmacy    = pharmacy
            self.price       = price
        else:
            self.name        = dict['name']
            self.description = dict['description']
            self.pharmacy    = dict['pharmacy']
            self.price       = dict['price']


    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__)
        return {'name':self.name,'description':self.description,'pharmacy':self.pharmacy,'price':self.price}
