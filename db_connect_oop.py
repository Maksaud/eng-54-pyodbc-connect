import pyodbc

class MSDBConnection():
    # we need to connect to our D

    def __init__(self):
        # Variable for connections
        self.database = 'Northwind'
        self.user_id = 'SA'
        self.passwords = 'Passw0rd2018'

        # making the connection
        self.conn = pyodbc.connect('DSN=MYMSSQL;UID=' + self.user_id + ';PWD=' + self.passwords + ';DATABASE=' + self.database)

        # making cursor
        self.cursor = self.conn.cursor()

    def sql_query(self, query):
        return self.cursor.execute(query)

nw_db_obj = MSDBConnection()

rows = nw_db_obj.sql_query('SELECT * FROM Products')
# The keys do not come to the code.
print(rows.fetchone())