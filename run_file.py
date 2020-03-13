from db_products_oop import *

products_tb = NWProducts()

##### One Product Input Function

def one_or_all(add_method):
    data=add_method
    print(data)
    while True:
        record = data.fetchone()
        if record is None:
            break
        print(record.ProductName)

while True:
    print('select 1 for all products\n Select 2 for one product\n Select 3 to create a product\n Select 4 to create a product')
    user_input = input('>>> ')
    if user_input == '1':
        # get all our product using our new method
        # Iterate and display nicely
        one_or_all(products_tb.all())
    elif user_input == '2':
        data = products_tb.one_product()
        print(data)
        while True:
            one_or_all(products_tb.one_product())
    elif user_input == '3':
        data = products_tb.create()
    elif user_input == '4':
        data = products_tb.delete()
    else:
        break

            # test each function so you know it works