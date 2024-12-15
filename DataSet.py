import pandas as pd
import random
from faker import Faker

# Creating the class DataSet
#
#'ID','Name', 'Age', 'City','Work','AVG_Salary','Gender','Online_Shopping'
# Salary: Average Salary, Online Shopping: 1:Yes or 0:No
# n: number of records

class DataSet():
    def __init__(self,n):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.ds_size = n
        self.fake = Faker()
        self.database = []
        
    def generate_records(self, record_id):
        record = {
            "ID": record_id,
            "age": random.randint(18,70),
            "city": self.fake.city(),
            "salary": random(random.uniform(20000,120000), 2),
            "gender":random.choice(["Male","Female"]),
            "online_shopping": random.choice([True,False])
        }  
        
        return record

    def generate_dataset(self):
        for i in range(1, self.ds_size + 1):
            self.database.append(self.generate_records(i))
            
    def get_dataset(self):
        return self.database()


if __name__ == "__main__":
    n = 10
    generator = DataSet(n)
    generator.generate_records()
    generator.generate_dataset()
    for record in generator.get_dataset():
        print(record)
