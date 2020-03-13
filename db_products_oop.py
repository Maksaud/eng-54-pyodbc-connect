from db_connect_oop import *

class NWProducts(MSDBConnection):
    def __init__(self):
        super().__init__()
        self.table = 'PRODUCTS'

    def __sql_query(self, query):
        return self.cursor.execute(query)

    # def __filter_sql_injection(self, query):
    #     # do some regular expression to filter bad sql attacks
    #     # return clean expression (like no DROP or DELETE with no WHERE)
    #     pass

    # write all the CRUD methods

    #R - READ ONE product :) (Select)
    def one_product(self):
        product_input = input("Eneter The productName ")
        rows = self.__sql_query(f"SELECT * FROM {self.table} WHERE ProductName = '{product_input}'")
        return rows

    # READ ALL PRUDUCTS (Select)
    def all(self):
        # return data with all products
        rows = self.__sql_query(f'SELECT * FROM {self.table}')
        return rows

    # Create One product (insert)
        # tip: search commit for pyodbc
    def create(self):
        product_input = input("What product you want to input ")
        rows = self.__sql_query(f"INSERT INTO {self.table} (ProductName) VALUES ('{product_input}')")
        self.conn.commit()
        return rows

    # Delete (delete)
    def delete(self):
        delete = input("What Product Name do you want to delete ")
        rows = self.__sql_query(f"DELETE FROM {self.table} WHERE ProductName = '{delete}'")
        self.conn.commit()
        return rows