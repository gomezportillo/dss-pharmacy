
class Order:

    def __init__(self, user, cart):
        pass


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
