import pandas as pd
import random
from DataSet import Data
import matplotlib as plt
import matplotlib.pyplot as plt1
import plotly.express as px


class exploratory_analysis:
    
    def __init__(self):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.analysis_results_summary = None
        self.analysis_results_head = pd.DataFrame()
        self.database = None
        self.ds_size = 10000
        self.data = None
        
    def dataset(self):
        self.data = Data(self.ds_size)
        random.seed(10)
        self.data.generate_dataset()
        self.database = self.data.get_dataset()

    def exploratory_analysis(self):

        if self.database == None:
            raise ValueError("data has not been generated yet.")
        data = pd.DataFrame(self.database)
        self.analysis_results_summary = data.describe(include = 'all')
        self.analysis_results_head = data.head()
        print("Exploratory Analysis completed.")
        
    def analysis_histogram(self):
        data = pd.DataFrame(self.database)
        data.hist(bins=50, figsize=(20,15))
        plt1.savefig('hist.png')
        
    def corelation_matrix(self):
        if self.database == None:
            raise ValueError("data has not been generated yet.")
        data = pd.DataFrame(self.database)
        corr_matrix = data[["age", "salary","gender","online_shopping"]].corr()
        
        return corr_matrix

    # Main function to execute the class
def main():

    analysis = exploratory_analysis()    
    analysis.dataset()
    analysis.exploratory_analysis()
    analysis.analysis_histogram()
    analysis.corelation_matrix()

if __name__ == "__main__":
    main()