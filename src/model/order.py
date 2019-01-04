
class Order:

    def __init__(self, user='email@dss', type='Purchase', date='01/01/2019', cart={}):
        self.user = user
        self.type = type
        self.cart = cart
        self.date = date


    def toJSON(self):
        json_msg             = {}
        json_msg['email']    = self.user
        json_msg['type']     = self.type
        json_msg['date']     = self.date
        json_msg['products'] = self.cart
        return json_msg
