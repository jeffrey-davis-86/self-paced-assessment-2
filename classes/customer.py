import csv
import os

class Customer:
    def __init__(self, customer_id, first_name, last_name, current_video_rentals):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals
        
    def __str__(self):
        return f"{self.customer_id}: {self.first_name} {self.last_name}\n-----------------------------\n{self.current_video_rentals}"
    
    # method to read in all of the customers from the csv file
    @classmethod
    def load_all_customers(cls):
        all_customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, "../data/customers.csv")
        
        with open(file, mode="r") as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                #print(row)
                customer = Customer(**row)
                all_customers.append(customer)
        return all_customers