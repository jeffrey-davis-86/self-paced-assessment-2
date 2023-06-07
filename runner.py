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
from classes.customer import Customer

store = Store('Code Platoon Video')

print(store.name)
#Interface('Code Platoon Video').run()
for customer_info in store.customers:
    print(customer_info)

print("=======================")
for inventory_info in store.inventory:
    print(inventory_info)
# customer_info = {
#     "customer_id" : 6,
#     "first_name" : "Jeff",
#     "last_name" : "Davis", 
#     "current_video_rentals" : "The Princess Bride"
#     }
    
# customer = Customer(**customer_info)

# print(customer.last_name)