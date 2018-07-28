import urllib
import requests
import json
import datetime
from datetime import datetime
from helper_func import getTenYearsAgoDate
from dbh import *

conn = setupConnetion()
# Create database and table if not existent
dbSetup(conn)

addTestData(conn)

# get 10 years ago date
oldest_date = getTenYearsAgoDate()
print ('Oldest data date: ', oldest_date)

token = '3IAFG5IWH0P5UW5G'
nsdaqs = ['AAPL', 'GOOGL', 'AMZN']      # NASDAQ identifier
main_url = 'https://www.alphavantage.co/query?'

function = 'function=TIME_SERIES_DAILY'     
pre_symbol = 'symbol='                      # different NSDAQ numbers will be added to this later
out_size = 'outputsize=compact'            # full is last 20 years
datatype = 'datatype=json'      
api_key = 'apikey=' + token

# For each stock (nsdaq) get data and update database
for stock in nsdaqs:
    # Format URL
    symbol = pre_symbol + stock
    url = main_url + '&' + function + '&' + symbol + '&' + out_size + '&' + datatype + '&' + api_key
    # print(url) #debug

    response = requests.get(url)
    # print(response)

    if(response.status_code != 200):
        print('Oops something went wrong. Error: ', response.status_code)
    else:

        json_response = response.json()
        # print(json_response)
        # print(type(json_response)) # Seems like the response is a dictionary

        response_data = json_response['Time Series (Daily)']

        date_id = 0     # We can see that date is store in a 1st column (i.e. index 0)
        data_id = 1     # and other info in 2nd column (i.e. index 1)

        for dataset in response_data.items():
            # print(dataset)
            date = dataset[date_id]
            ot_date = datetime.strptime(date, '%Y-%M-%d').date()    #convert string to datetime object
            # print(ot_date)

            # Only use data that is not older than 10 year
            if(ot_date > oldest_date):
                opens = dataset[data_id]['1. open']
                high = dataset[data_id]['2. high']
                low = dataset[data_id]['3. low']
                close = dataset[data_id]['4. close']
                volume = dataset[data_id]['5. volume']

                addData(conn, ot_date, stock, opens, high, low, close, volume)

                # addData(conn, ot_date, stock, opens, high, low, close, volume)
                # print(stock, feedback)
                # print('-----------------------------')
        
conn.close()    #close connection when finished
    


