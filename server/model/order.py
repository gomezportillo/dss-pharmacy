
class Order:

    def __init__(self, user, type, cart):
        self.user = user
        self.type = type
        self.cart = cart


    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        json_msg             = {}
        json_msg['email']    = self.user
        json_msg['type']     = self.type
        json_msg['products'] = self.cart
        return json_msg
