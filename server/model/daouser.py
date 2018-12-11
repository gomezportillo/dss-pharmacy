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


    def insert(self, product):
        pass


    def update(self, product):
        pass


    def readAll(self):
        return [ user.toJSON() for user in self.users ]


    def delete(self, product):
        pass


    def deleteAll(self):
        pass


    def find(self, product):
        pass


    def set_up_ddbb(self):
        # self.collection.create_index([(PRIMARY_KEY, pymongo.ASCENDING)], unique=True)
        user1 = User('admin', 'Administrator Smith', 'admin')
        user2 = User('gomezportillo@dss.com', 'Pedro Manuel Gómez-Portillo', 1234)
        user3 = User('xenahort@dss.com', 'Juan Carlos Serrano', 'secretpassword')

        self.users.append( user1 )
        self.users.append( user2 )
        self.users.append( user3 )
