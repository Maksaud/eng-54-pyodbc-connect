import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
server = 'localhost,1433'
database = 'Northwind'
user_id = 'SA'
passwords = 'Passw0rd2018'

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user_id + ';PWD=' + passwords)

# the DSN value should be the name of the entry in odbc.ini, not freetds.conf

# Making the connecting
conn = pyodbc.connect('DSN=MYMSSQL;UID='+ user_id + ';PWD=' + passwords +';DATABASE='+database)

# creating a cursor objct from connection
# Imagine like a real cursor on your azure data studio
# This will maintain state
crsr = conn.cursor()
#
# # Running SQL Queries using .execute()
# crsr.execute("select * FROM Orders")# get the next entry in the cursor
#
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
#
# # each row, has all the columns of that entry.
# # getting individual data is easy from this row
#
# p
# print(row.ContactName)
# print(row.Fax)
#
# # Checking the headers of the columns
# print(crsr.description)

# using the .fetchall()
# Using fetchall is dangerous because you can stall/crash your servers
# if there is a lot of data :)
# crsr.execute("SELECT * FROM Customers")
# all_rows = crsr.fetchall()
# print_rows = crsr.fetchall()
# print(all_rows)
# print(type(all_rows))
#
# counter = 0
# for item in all_rows:
#     # print(item)
#     print(item.ContactName, '-', 'Fax', item.FAX)
#     counter += 1


#Best practices is to use a while loop and fetchone()
# until your entry is none.
rows = crsr.execute("select*from customers")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.ContactName)

rows = crsr.execute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    new_values = []
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

print(new_values)

