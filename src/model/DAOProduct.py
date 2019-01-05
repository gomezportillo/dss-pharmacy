from model.Product import Product
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton

import MySQLdb

@Singleton
class DAOProduct(InterfaceDAO):

    def __init__(self):
        self.set_up_ddbb()


    def insert(self, product):
        query = """INSERT INTO
                   Products(name, description, pharmacy, price)
                   VALUES('{0}', '{1}', '{2}', '{3}')"""

        query = query.format(product.name, product.description, product.pharmacy, product.price)

        try:
            self.execute_query( query )
        except MySQLdb.IntegrityError:
            self.update( product )


    def update(self, product):
        query = "UPDATE Products SET description='{0}', pharmacy='{1}', price='{2}' WHERE name='{3}'"

        query = query.format(product.description, product.pharmacy, product.price, product.name)

        self.execute_query( query )


    def readAll(self):
        products = []
        query = "SELECT * FROM Products"
        rows = self.execute_query( query )

        for row in rows:
            p = Product(row[0], row[1], row[2], row[3])
            products.append( p )

        return [ product.toJSON() for product in products ]


    def delete(self, name):
        query = "DELETE FROM Products WHERE name='{}'".format( name )
        self.execute_query( query )


    def deleteAll(self):
        query = "TRUNCATE TABLE Products"
        self.execute_query( query )


    def find(self, product_name):
        query = "SELECT * FROM Products WHERE name='{}'".format( product_name )
        row = self.execute_query( query )

        if row:
            p = Product(row[0][0], row[0][1], row[0][2], row[0][3])
            return p

        return None



    def set_up_ddbb(self):

        query = "DROP TABLE IF EXISTS Products"
        self.execute_query( query )

        query = """ CREATE TABLE Products (
                    name        CHAR(30) NOT NULL PRIMARY KEY,
                    description CHAR(30),
                    pharmacy    CHAR(30),
                    price       INT) """
        self.execute_query( query )


        query = """INSERT INTO Products
                   VALUES('Ibuprofen', 'Cures headache', 'Pharmacy 1', 7)"""
        self.execute_query( query )

        query = """INSERT INTO Products
                   VALUES('Frenadol', 'Cures flu', 'Pharmacy 2', 12)"""
        self.execute_query( query )

        query = """INSERT INTO Products
                   VALUES('Bandage', 'Cures wounds', 'Pharmacy 1', 10)"""
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
