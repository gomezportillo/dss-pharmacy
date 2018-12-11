import pymongo

from model.user import User

PRIMARY_KEY = 'email'
COLLECTION_NAME = 'users'

class DAOUser:

    def __init__(self, MONGODB_URI):
        self.mongo_client = pymongo.MongoClient(MONGODB_URI)
        self.apolo_ddbb = self.mongo_client.get_database()
        self.collection = self.apolo_ddbb[COLLECTION_NAME]
        self.users = []
        self.set_up_ddbb()


    def insert(self, user):
        if self.find( user.email ) is None:
            self.users.append( user )
        else:
            self.update(user)


    def update(self, new_user):
        for user in self.users:
            if user.email == new_user.email:
                self.users.remove( user )
                self.users.append( new_user )


    def readAll(self):
        return [ user.toJSON() for user in self.users ]


    def delete(self, email):
        for user in self.users:
            if user.email == email:
                self.users.remove( user )


    def deleteAll(self):
        self.users = []


    def find(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None


    def set_up_ddbb(self):
        # self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
        user1 = User('admin', 'Administrator', 'admin')
        user2 = User('gomezportillo@dss.com', 'Pedro Manuel Gómez-Portillo', 1234)
        user3 = User('xenahort@dss.com', 'Juan Carlos Serrano', 'secretpassword')

        self.users.append( user1 )
        self.users.append( user2 )
        self.users.append( user3 )
