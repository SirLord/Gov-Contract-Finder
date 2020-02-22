"""
Inert description

@author=SirLord 
"""

import sys, os, time, stat
from datetime import datetime, date
import logging
import csv
import requests
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.disable(logging.DEBUG)  #Disable Debug Messages
logging.debug('Start of program')


#-Add scripts to fetch Data
data_location = r'C:\Users\andre\Documents\Code\Gov-Contract-Finder/Data/data.csv'
url = 'https://s3.amazonaws.com/falextracts/Contract%20Opportunities/datagov/ContractOpportunitiesFullCSV.csv'
def retrieve_data(url, data_location):
    logging.debug('downloading data from ' + url)
    
    with open(data_location, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)
    return True

def load_data(data_location):
    dataframe = pd.read_csv(data_location,encoding='cp1252')
    return dataframe

def is_data_stale(data_location):
    logging.debug('checking data freshness')
    file_age = 0 #21601
    try:
        file_age = time.time() - os.stat(data_location)[stat.ST_MTIME]
        logging.debug('data from ' + str(file_age) + 'seconds ago')
        if file_age > 21600:
            return True
        else:
            logging.debug('data so fresh!')
            return False #data so fresh!
    except:
        logging.debug('data not found...')
        return True #no data to smell

def main(data_location,url):
    if is_data_stale(data_location):
        retrieve_data(url, data_location)
    dataframe = load_data(data_location)
    return True

    
#exampleFile = open('example.csv')
#exampleReader = csv.reader(exampleFile)



#-Munge Data and load into database
#-Initial Flask App to display data
#-Add queries and filters
#-Viz Engine to display geographics
#-Recommender Engine 
#-Setup Instructions
#-unit tests and coverage
#-pylint to prettify
if __name__ == '__main__':
    main(data_location,url)
logging.debug('End of program')