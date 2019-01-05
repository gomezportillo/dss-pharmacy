from model.Order import Order
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton

import MySQLdb

@Singleton
class DAOOrder(InterfaceDAO):

    def __init__(self):
        self.set_up_ddbb()


    def insert(self, order):
        query = """INSERT INTO
                   Orders(user, type, date, cart)
                   VALUES('{0}', '{1}', '{2}', '{3}')"""

        query = query.format(order.user, order.type, order.date, order.cart)

        self.execute_query( query )

    def update(self, order):
        query = "UPDATE Orders SET user='{0}', type='{1}', date='{2}', cart='{3}' WHERE id='{4}'"

        query = query.format(order.user, order.type, order.date, order.cart, order.id)
        self.execute_query( query )

    def readAll(self):
        orders = []
        query = "SELECT * FROM Orders"
        rows = self.execute_query( query )

        for row in rows:
            print(row)
            o = Order(row[1], row[2], row[3], row[4], row[0])
            orders.append( o )

        return [ order.toJSON() for order in orders ]

    def delete(self, id):
        query = "DELETE FROM Orders WHERE id='{}'".format( id )
        self.execute_query( query )


    def deleteAll(self):
        query = "TRUNCATE TABLE Orders"
        self.execute_query( query )


    def find(self, id):
        query = "SELECT * FROM Orders WHERE id={}".format( id )
        row = self.execute_query( query )

        if row:
            row = row[0]
            o = Order(row[1], row[2], row[3], row[4], row[0])
            return o

        return None


    def set_up_ddbb(self):

        query = "DROP TABLE IF EXISTS Orders"
        self.execute_query( query )

        query = """ CREATE TABLE Orders (
                    id   MEDIUMINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    user CHAR(30),
                    type CHAR(30),
                    date CHAR(30),
                    cart CHAR(150))"""
        self.execute_query( query )

        query = """INSERT INTO Orders(user, type, date, cart)
                   VALUES('admin', 'Purchase', '1-1-2019', 'Bandage. Cures wounds. Pharmacy 1. 10EUR x 1u;')"""
        self.execute_query( query )

    def execute_query(self, query):
        db = MySQLdb.connect(host='us-cdbr-gcp-east-01.cleardb.net',
                             user='b761ae150766d3',
                             passwd='4bcf3d10',
                             db='gcp_ca2ad2566039a3f0f01c',
                             port=3306)

        cursor = db.cursor()

        try:
            cursor.execute(query)
        except Exception as error:
            cursor.close()
            db.close()
            raise error

        db.commit()
        result = cursor.fetchall()
        cursor.close()
        db.close()

        return result
