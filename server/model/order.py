
class Order:

    def __init__(self, dict):
        self.name        = dict['name']
        self.description = dict['description']
        self.price       = dict['price']
        self.pharmacy    = dict['pharmacy']
