
class Order:

    def __init__(self, user='email@dss', type='Purchase', cart={}):
        self.user = user
        self.type = type
        self.cart = cart


    def toJSON(self):
        json_msg             = {}
        json_msg['email']    = self.user
        json_msg['type']     = self.type
        json_msg['products'] = self.cart
        return json_msg