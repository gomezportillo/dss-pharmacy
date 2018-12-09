
class User:

    def __init__(self, email, name, password):
        pass


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
