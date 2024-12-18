import pandas as pd
from faker import Faker
import random

class DataPipeline:
    
    def __init__(self,ds_size):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.ds_size = ds_size
        self.fake = Faker()
        self.database = []
        self.analysis_results = None
        self.model_results = None
        
    def generate_records(self, record_id):
        record = {
            "ID": record_id,
            "age": random.randint(18,70),
            "city": self.fake.city(),
            "salary": round(random.uniform(20000,120000), 2),
            "gender":random.choice(["Male","Female"]),
            "online_shopping": random.choice([True,False])
        }  
        
        return record

    def generate_dataset(self):
        for i in range(1, self.ds_size + 1):
            self.database.append(self.generate_records(i))
            
    def get_dataset(self):
        print("Data generated successfully!")
        return self.database

    def exploratory_analysis(self):
        if self.database == []:
            raise ValueError("data has not been generated yet.")
        data = pd.DataFrame(self.database)
        self.analysis_results = data.describe(include = 'all')
        print("Exploratory Analysis completed.")
        
    def model_run(self):
        if self.database == []:
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
    ds_size = 10000
    pipeline = DataPipeline(ds_size)
    random.seed(10)
    pipeline.generate_dataset()
    pipeline.exploratory_analysis()
    pipeline.model_run()
    pipeline.generate_report()

if __name__ == "__main__":
    main()
    
    

        
    
