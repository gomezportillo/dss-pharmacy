from model.User import User
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton

import MySQLdb

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
        users = []
        query = "SELECT * FROM USERS"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        for row in rows:
            u = User(row[0], row[1], row[2])
            users.append( u )

        return [ user.toJSON() for user in users ]


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

        db = MySQLdb.connect(host='us-cdbr-gcp-east-01.cleardb.net',
                             user='b6c862ade2902a',
                             passwd='f05cd157',
                             db='gcp_1e27e3d6e920e92796e6',
                             port=3306)

        self.cursor = db.cursor()
        self.cursor.execute ("SELECT VERSION()")
        row = self.cursor.fetchone()
        print("server version:", row[0])


        query = "DROP TABLE USERS"
        self.cursor.execute(query)

        query = """ CREATE TABLE USERS (
                    EMAIL    CHAR(30) NOT NULL PRIMARY KEY,
                    NAME     CHAR(30),
                    PASSWORD CHAR(30) )"""

        self.cursor.execute(query)

        self.cursor.execute("""INSERT INTO USERS VALUES
                            ('admin', 'Adminstrator', 'admin')""")

        self.cursor.execute("""INSERT INTO USERS VALUES
                            ('gomezportillo@dss.com', 'Pedro Manuel Gomez-Portillo', '1234')""")

        self.cursor.execute("""INSERT INTO USERS VALUES
                            ('xenahort@dss.com', 'Juan Carlos Serrano', 'secretpassworkd')""")
