from model.Pharmacy import Pharmacy
from model.InterfaceDAO import InterfaceDAO
from auxiliary.Singleton import Singleton

import MySQLdb

@Singleton
class DAOPharmacy(InterfaceDAO):

    def __init__(self):
        self.set_up_ddbb()


    def insert(self, pharmacy):
        query = """INSERT INTO
                   Pharmacies(name, latitude, longitude)
                   VALUES('{0}', {1}, {2})"""

        query = query.format(pharmacy.name, pharmacy.latitude, pharmacy.longitude)

        try:
            self.execute_query( query )
        except MySQLdb.IntegrityError:
            self.update( product )


    def update(self, pharmacy):
        query = "UPDATE Pharmacies SET latitude={0}, longitude={1} WHERE name='{3}'"

        query = query.format(pharmacy.latitude, pharmacy.longitude, pharmacy.name)

        self.execute_query( query )


    def readAll(self):
        pharmacies = []
        query = "SELECT * FROM Pharmacies"
        rows = self.execute_query( query )

        for row in rows:
            p = Pharmacy(row[0], row[1], row[2])
            pharmacies.append( p )

        return [ pharmacy.toJSON() for pharmacy in pharmacies ]


    def delete(self, pharmacy_name):
        query = "DELETE FROM Pharmacies WHERE name='{}'".format( pharmacy_name )
        self.execute_query( query )


    def deleteAll(self):
        query = "TRUNCATE TABLE Pharmacies"
        self.execute_query( query )


    def find(self, pharmacy_name):
        query = "SELECT * FROM Pharmacies WHERE name='{}'".format( pharmacy_name )
        row = self.execute_query( query )

        if row:
            p = Pharmacy(row[0][0], row[0][1], row[0][2])
            return p

        return None


    def set_up_ddbb(self):

        query = "DROP TABLE IF EXISTS Pharmacies"
        self.execute_query( query )

        query = """ CREATE TABLE Pharmacies (
                    name        CHAR(30) NOT NULL PRIMARY KEY,
                    latitude    DECIMAL(10, 8),
                    longitude   DECIMAL(10, 8) ) """
        self.execute_query( query )


        query = """INSERT INTO Pharmacies
                   VALUES('Pharmacy 1', 37.198366, -3.624976)"""
        self.execute_query( query )

        query = """INSERT INTO Pharmacies
                   VALUES('Pharmacy 2', 37.195993, -3.622784)"""
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
