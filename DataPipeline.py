import pandas as pd
from datetime import date
import random
from DataSet import Data
from model import run_models
from exploratory_analysis import exploratory_analysis
#---------------------#
# Report
import matplotlib.pyplot as plt
import seaborn as sns
import os
import webbrowser


class DataPipeline:
    
    def __init__(self):
        #Initiazlizate an empty Data frame to enter to be feed with customer data
        self.analysis_results_summary = None
        self.analysis_results_head = pd.DataFrame()
        #self.analysis_results_summary = None
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
        self.analysis_results = exploratory_analysis(data = self.database)
        self.analysis_results.exploratory_analysis()
        self.analysis_results.analysis_histogram()
        self.analysis_results.corelation_matrix()
        
        print("DataPipeline Exploratory Analysis completed.")
        
    def model_run(self):
        if self.database == None:
            raise ValueError("data has not been generated yet.")
        self.model_results = run_models(self.database, test_ratio=0.2)    
        self.model_results.split_train_test()
        
    
    def generate_report(self):
        """Creates a report with the results."""
        filename = "Report Results"
        today = date.today()
        author = "Marina Rodrigues de Oliveira"
        
        page_title_text='Results Report Python Project'
        author_name = 'Author: ' + author
        title_text = ''
        text = 'Hello, welcome an analysis about some data!'
        prices_text = 'Historical prices of S&P 500'
        stats_text = 'Historical prices summary statistics'


        # 2. Combine them together using a long f-string
        html = f'''
            <html>
                <head>
                    <title>{page_title_text}</title>
                </head>
                <body>
                    <h1>{title_text}</h1>
                    <p>{author_name}</p>
                    <p>{today}</p>
                    <p>{text}</p>
                    <img src='hist.png' width="700">
                    <h2>{prices_text}</h2>
                    <h2>{stats_text}</h2>
                </body>
            </html>
            '''
        # 3. Write the html string as an HTML file
        with open('html_report.html', 'w') as f:
            f.write(html)
            
        if os.path.exists('html_report.html'):
            print("File successfully created!")
        else:
            print("File was not created.")
        
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
    
    

        
    
