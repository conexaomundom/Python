import seaborn as sns
import os
import webbrowser
from datetime import date


class generate_report():
    def __init__(self):
        """Creates a report with the results."""
        self.filename = "Report Results"
        self.today = date.today()
        self.author = "Marina Rodrigues de Oliveira"
        
        self.page_title_text='Results Report Python Project'
        self.author_name = 'Author: ' + self.author
        self.title_text = ''
        self.text = 'Hello, welcome an analysis about some data!'
        self.prices_text = 'Historical prices of S&P 500'
        self.stats_text = 'Historical prices summary statistics'
        
        
    def generate_report(self):
        # 2. Combine them together using a long f-string
        html = f'''
            <html>
                <head>
                    <title>{self.page_title_text}</title>
                </head>
                <body>
                    <h1>{self.title_text}</h1>
                    <p>{self.author_name}</p>
                    <p>{self.today}</p>
                    <p>{self.text}</p>
                    <img src='hist.png' width="700">
                    <h2>{self.prices_text}</h2>
                    <h2>{self.stats_text}</h2>
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
        
        print(f"Report generated at {self.filename}")