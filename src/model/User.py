
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


    def checkPassword(self, password):
        return self.password == password


    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        return {'email' : self.email, 'name' : self.name, 'password' : self.password}


    def toXML(self):
        xml_msg = '<user>'
        xml_msg += '<email>{}</email>'.format( self.email )
        xml_msg += '<name>{}</name>'.format( self.name )
        xml_msg += '<password>{}</password>'.format( self.password )
        xml_msg += '</user>'

        return xml_msg
