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
import pyinputplus as pyip
from classes.store import Store

# creates the store instance
store = Store('Code Platoon Video')

mode = None
while mode != 6:
    # pyip let's me specify an integer between 1 and 6
    mode = pyip.inputInt(prompt = "\nWelcome to Code Platoon Video!\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n", min = 1, max = 6)
    #print(mode)
    
    # View video inventory
    if mode == 1:
        store.list_inventory()
    
    # View customer's rented videos
    if mode == 2:
        customer_id = input('Enter customer ID: ')
        customer = store.find_customer_by_id(customer_id)
        if customer:
            print(customer)
        else:
            print("Customer ID does not exist")
            
    # Rent video
    if mode == 3:
        pass
    
    # Return video
    if mode == 4:
        pass
    
    # Add new customer
    if mode == 5:
        next_customer_id = store.next_customer_id()
        print(next_customer_id)
        customer_data = {}
        customer_data['customer_id'] = str(next_customer_id)
        customer_data['first_name'] = input('Enter first name: ')
        customer_data['last_name'] = input('Enter last name: ')
        customer_data['current_video_rentals'] = ""
        print(customer_data)
        store.add_customer(customer_data)
        
    if mode == 6:
        # Exit
        print("Exit complete. Have a great day!")



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