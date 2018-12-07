
class Product:

    def __init__(self, dict):
        self.name        = dict['name']
        self.description = dict['description']
        self.pharmacy    = dict['pharmacy']
        self.price       = dict['price']
