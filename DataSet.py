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
        
        

''' def add_customer(self):
        for i in list(range(1, self.ds_size+1)):
            id_customers_add = "ID_" + str(i)
            print(id_customers_add)
        
        
    
    def show_dataset(self):
        print(self.dataset)
'''

A = DataSet()
A.add_customer()