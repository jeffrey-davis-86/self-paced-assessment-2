import csv
import os

class Inventory:
    
    def __init__(self, video_id, title, rating, copies_available):
        self.video_id = video_id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
        
    def __str__(self):
        return f"{self.video_id}: {self.title}, rated {self.rating}, {self.copies_available} copies available."
    
    @classmethod
    def load_all_inventory(cls):
        all_inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, "../data/inventory.csv")
        
        with open(file, mode="r") as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                #print(row)
                inventory = Inventory(**row)
                all_inventory.append(inventory)
        return all_inventory