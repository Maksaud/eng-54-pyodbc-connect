from db_products_oop import *
products_tb = NWProducts()


print('This function should return the output of one of the selected  item in the databse using a query')
try:
    the_product = products_tb.one_product()
    print(the_product.fetchone())
except ValueError as err:
    print("Check if the method is a valid method")
    print(err)

try:
    all_products = products_tb.all()
    print(all_products.fetchone())
except ValueError as err:
    print("Check argument")
    print(err)

create_products = products_tb.create()

delete_products = products_tb.delete()