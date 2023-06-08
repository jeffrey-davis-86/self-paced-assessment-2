# Setup a video store management system

# Manage customer information:
#     customer id, first name, last name, current list of video rentals (by title)
#   Create a customer class
#   customer.csv file

# Manage the store's video inventory:
#     video id, video title, video rating, number of copies currently available in-store
#   Create an inventory class
#   inventory.csv file

# Welcome to Code Platoon Video!
# 1. View video inventory
# 2. View customer's rented videos
# 3. Rent video
# 4. Return video
# 5. Add new customer
# 6. Exit

from classes.store import Store

store = Store('Code Platoon Video')

mode = input("\nWelcome to Code Platoon Video!\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n")

if mode == '1':
    store.list_inventory()
    # for inventory_info in store.inventory:
    #     print(inventory_info)
if mode == '2':
    customer_id = input('Enter customer ID: ')
    customer = store.find_customer_by_id(customer_id)
    if customer:
        print(customer)
    else:
        print("Customer ID does not exist")
    # print(customer_id)
    # for customer_info in store.customers:
    #     print('test')
    #     print(store.customers[customer_id])
    #     if customer_id == store.customers.customer_id:
    #         print(customer_info)
    #     else:
    #         print("Customer ID does not exist")
else:
    pass

# TESTING SECTION
#print(store.name)
#Interface('Code Platoon Video').run()
#for customer_info in store.customers:
#   print(customer_info)
   
#print("=========================================================================")

#for inventory_info in store.inventory:
#    print(inventory_info)
# customer_info = {
#     "customer_id" : 6,
#     "first_name" : "Jeff",
#     "last_name" : "Davis", 
#     "current_video_rentals" : "The Princess Bride"
#     }
    
# customer = Customer(**customer_info)

# print(customer.last_name)