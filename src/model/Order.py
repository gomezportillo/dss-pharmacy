
class Order:

    def __init__(self, user='email@dss', type='Purchase', date='now', products={}, id=0):
        self.user = user
        self.type = type
        self.date = date
        self.cart = products
        self.id   = id


    def toJSON(self):
        json_msg             = {}
        json_msg['id']       = self.id
        json_msg['email']    = self.user
        json_msg['type']     = self.type
        json_msg['date']     = self.date
        json_msg['products'] = self.cart
        return json_msg
