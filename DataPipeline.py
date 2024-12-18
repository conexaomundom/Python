import pandas as pd
#from faker import Faker
import random
from DataSet import Data

class DataPipeline:
    
    def __init__(self):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.analysis_results = None
        self.model_results = None
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
        self.analysis_results = data.describe(include = 'all')
        print("Exploratory Analysis completed.")
        
    def model_run(self):
        if self.database == None:
            raise ValueError("data has not been generated yet.")
        #self.model_results = "Not done yet." #self.database
        pass
    
    def generate_report(self):
        """Creates a report with the results."""
        filename = "Report Results"
        with open(filename, "w") as f:
            f.write("Results Report\n")
            f.write("\nExploratory Analysis:\n")
            f.write(self.analysis_results.to_string())
            f.write("\n\nModel Results:\n")
            f.write("Not done yet.\n")
            #f.write(self.model_results.to_string())
        print(f"Report generated at {filename}")
    
    # Main function to execute the pipeline
def main():

    pipeline = DataPipeline()    
    pipeline.dataset()
    pipeline.exploratory_analysis()
    pipeline.model_run()
    pipeline.generate_report()

if __name__ == "__main__":
    main()
    
    

        
    
