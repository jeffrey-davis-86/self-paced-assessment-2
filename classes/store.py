from classes.customer import Customer
from classes.inventory import Inventory

class Store:
    def __init__(self, name):
        self.name = name
        self.customers = Customer.load_all_customers()
        self.inventory = Inventory.load_all_inventory()
        