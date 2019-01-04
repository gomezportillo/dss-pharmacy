
class User:

    def __init__(self, email=None, name=None, password=None, dict=None):
        if dict is None:
            self.email    = email
            self.name     = name
            self.password = password
        else:
            self.email    = dict['email']
            self.name     = dict['name']
            self.password = dict['password']


    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        return {'email' : self.email, 'name' : self.name, 'password' : self.password}


    def checkPassword(self, password):
        return self.password == password
