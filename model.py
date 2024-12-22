import pandas as pd
import random
from DataSet import Data
import numpy as np

class run_models:
    
    def __init__(self, data, test_ratio):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.database = data
        self.ds_size = 10000
        self.data = None
        self.test_ratio = test_ratio
        
        
    def dataset(self):
        self.data = Data(self.ds_size)
        random.seed(10)
        self.data.generate_dataset()
        self.database = self.data.get_dataset()

    def split_train_test(self):

        #if self.database == None:
        #    raise ValueError("data has not been generated yet.")
        
        data = pd.DataFrame(self.database)
        
        shuffled_indices = np.random.permutation(len(data))
        test_set_size = int(len(data) + self.test_ratio)
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        print("Train and Test dataset complete.")

        return print(data.iloc[train_indices], data.iloc[test_indices])


    # Main function to execute the class
def main():

    analysis = run_models(test_ratio=0.2)    
    analysis.dataset()
    analysis.split_train_test()
    


if __name__ == "__main__":
    main()