from classes.customer import Customer
from classes.inventory import Inventory

class Store:
    def __init__(self, name):
        #instance attributes
        self.name = name
        self.customers = Customer.load_all_customers()
        self.inventory = Inventory.load_all_inventory()
     
    def list_inventory(self):
        for inventory_info in self.inventory:
            print(inventory_info)
        
    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
        