from DataSet import *
import random
import pandas as pd
import statistics as s

#data = pd.DataFrame()

if __name__ == "__main__":
    ds_size = 10000
    generator = Data(ds_size)
    random.seed(10)
    generator.generate_dataset()
    data = pd.DataFrame(generator.get_dataset())
    

print(data.head())
print(s.mean(data['salary'])) # 69501.51183
print(data.describe())
print(data.describe(include = 'all'))