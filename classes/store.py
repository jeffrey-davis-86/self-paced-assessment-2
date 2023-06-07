from classes.customer import Customer

class Store:
    def __init__(self, name):
        self.name = name
        self.customers = Customer.load_all_customers()
        self.inventory = []
        