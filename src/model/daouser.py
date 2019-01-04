from model.user import User
from model.interfacedao import InterfaceDAO
from auxiliary.singleton import Singleton


@Singleton
class DAOUser(InterfaceDAO):

    def __init__(self):
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
        user1 = User('admin', 'Administrator', 'admin')
        user2 = User('gomezportillo@dss.com', 'Pedro Manuel Gómez-Portillo', 1234)
        user3 = User('xenahort@dss.com', 'Juan Carlos Serrano', 'secretpassword')

        self.users.append( user1 )
        self.users.append( user2 )
        self.users.append( user3 )
