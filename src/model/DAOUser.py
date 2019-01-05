from model.User import User
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton

import MySQLdb
import traceback

@Singleton
class DAOUser(InterfaceDAO):

    def __init__(self):
        self.set_up_ddbb()


    def insert(self, user):
        query = """INSERT INTO
                   Users(email, name, password)
                   VALUES('{0}', '{1}', '{2}')"""

        query = query.format(user.email, user.name, user.password)

        try:
            self.execute_query( query )
        except MySQLdb.IntegrityError:
            self.update( user )


    def update(self, user):
        query = "UPDATE Users SET name='{0}', password='{1}' WHERE email='{2}'"

        query = query.format(user.name, user.password, user.email)
        self.execute_query( query )


    def readAll(self):
        users = []
        query = "SELECT * FROM Users"
        rows = self.execute_query( query )

        for row in rows:
            u = User(row[0], row[1], row[2])
            users.append( u )

        return [ user.toJSON() for user in users ]


    def delete(self, email):
        query = "DELETE FROM Users WHERE email='{}'".format( email )
        rows = self.execute_query( query )


    def deleteAll(self):
        query = "TRUNCATE TABLE Users"
        self.execute_query( query )


    def find(self, email):
        query = "SELECT * FROM Users WHERE email='{}'".format( email )
        row = self.execute_query( query )[0]
        u = User(row[0], row[1], row[2])
        return u


    def set_up_ddbb(self):

        query = "DROP TABLE Users"
        self.execute_query( query )

        query = """ CREATE TABLE Users (
                    email    CHAR(30) NOT NULL PRIMARY KEY,
                    name     CHAR(30),
                    password CHAR(30) )"""
        self.execute_query( query )

        query = "INSERT INTO Users VALUES('admin', 'Adminstrator', 'admin')"
        self.execute_query( query )

        query="""INSERT INTO Users VALUES
              ('gomezportillo@dss.com', 'Pedro Manuel Gomez-Portillo', '1234')"""
        self.execute_query( query )

        query= """INSERT INTO Users VALUES
               ('xenahort@dss.com', 'Juan Carlos Serrano', 'secretpassworkd')"""
        self.execute_query( query )


    def execute_query(self, query):
        db = MySQLdb.connect(host='us-cdbr-gcp-east-01.cleardb.net',
                             user='b6c862ade2902a',
                             passwd='f05cd157',
                             db='gcp_1e27e3d6e920e92796e6',
                             port=3306)

        cursor = db.cursor()

        try:
            cursor.execute(query)
        except Exception as error:
            cursor.close()
            db.close()
            raise error

        result = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()

        return result
