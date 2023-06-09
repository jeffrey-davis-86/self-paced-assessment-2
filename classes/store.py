from classes.customer import Customer
from classes.inventory import Inventory
import os
import csv

class Store:
    def __init__(self, name):
        #instance attributes
        self.name = name
        # calls Customer method to load customers from csv file
        self.customers = Customer.load_all_customers()
        # calls Inventory method to load inventory from csv file
        self.inventory = Inventory.load_all_inventory()
    
    # View video inventory from runner file 
    def list_inventory(self):
        print("\nHere is the current video inventory:")
        print("------------------------------------------------------------")
        for inventory_info in self.inventory:
            print(inventory_info)
    
    # View customer's rented videos from runner file 
    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == (customer_id):
                #print(customer)
                return customer
        return None
        
    # Add new customer
    def add_customer(self, customer_data):
        new_customer = Customer(**customer_data)
        self.customers.append(new_customer)
        self.write_all_customers()
    
    # Write all customers helper method    
    def write_all_customers(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, "../data/customers.csv")
        
        with open(file, mode="w") as csvfile:
            fieldnames = ['customer_id','first_name','last_name','current_video_rentals']
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(fieldnames)
            for customer in self.customers:
                csv_writer.writerow([customer.customer_id, customer.first_name, customer.last_name, customer.current_video_rentals])
    
    # Write all customers helper method    
    def write_all_inventory(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, "../data/inventory.csv")
        
        with open(file, mode="w") as csvfile:
            fieldnames = ['video_id','title','rating','copies_available']
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(fieldnames)
            for inventory in self.inventory:
                csv_writer.writerow([inventory.video_id, inventory.title, inventory.rating, inventory.copies_available])
    
    # Determine next available customer_id number to prevent dupllicates
    def next_customer_id(self):
        next_customer_id = 0
        for customer in self.customers:
            if int(customer.customer_id) >= next_customer_id:
                next_customer_id = int(customer.customer_id) + 1
                #print(next_customer_id)
        return next_customer_id
    
    # Rent a video    
    def rent_video(self, customer_id, video_id):
        customer = self.find_customer_by_id(customer_id)
        current_videos = (customer.current_video_rentals).split('/')
        #print(current_videos)
        if len(current_videos)>=3:
            print('Customer can only rent a maximum of 3 videos at once.')
        else:
            video = self.find_video_by_id(video_id)
            print(f"Video: {video.title}\n")
            if int(video.copies_available) == 0:
                print("Video not available")
            else:    
                correct_video = input('Is this correct? <Y/N>')
                if correct_video == "Y" or "y":
                    video.copies_available = int(video.copies_available) - 1
                    print(f"\n{video.copies_available} copies remaining\n")
                    if video:
                        #print(current_videos)
                        if current_videos == [""]:
                            current_videos = video.title
                            customer.current_video_rentals = current_videos
                        else:
                            current_videos.append(video.title)
                            video_str = "/".join(current_videos)
                            #print(s)
                            customer.current_video_rentals = video_str #current_videos
                        #print(video.title)
                        #print(current_videos)
                        
                        #print(current_videos)
                        #customer.current_video_rentals = current_videos
                        print(customer)
                        self.write_all_customers()
                        self.write_all_inventory()
                    else:
                        print(current_videos)
                else:
                    print("\nNo video added for this customer.\n")
        
    
    # Return a video
    def return_video(self, customer_id, video_id): 
        #print('return test')
        customer = self.find_customer_by_id(customer_id)
        current_videos = (customer.current_video_rentals).split('/')
        #print(current_videos)
        video = self.find_video_by_id(video_id)
        print(f"Video: {video.title}\n")
        correct_video = input('Is this correct? <Y/N>')
        if correct_video == "Y" or "y":
            print(video.title)
            print(current_videos)
            if video.title in current_videos:
                current_videos.remove(video.title)
                print(current_videos)
                customer.current_video_rentals = "/".join(current_videos)
                video.copies_available = int(video.copies_available) + 1
                print(f"\n{video.copies_available} copies available\n")
                self.write_all_customers()  
                self.write_all_inventory()
            else:
                print("Customer didn't rent that movie!")
        else:
            print("\nVideo not returned\n")
        
    # Find video name and number of copies
    def find_video_by_id(self, video_id):
        for video in self.inventory:
            if video.video_id == (video_id):
                if int(video.copies_available) > 0:
                    print(f"\n{video.copies_available} copies available")
                    #video.copies_available = int(video.copies_available) - 1
                    #print(f"\n{video.copies_available} copies remaining")
                    return video
                else:
                    print("No copies of that movie are currently available.")
                    return video
        return None