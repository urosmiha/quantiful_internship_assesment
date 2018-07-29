#!/bin/bash
# Create a new folder if data folder does not exists #
if [ ! -d data ]; then #
    echo "Creating a data directory..." #
    mkdir -p data; #
fi #
# Fetch new data if the csv files do not exist #
# if [ ! -d data/apple.csv ] | [ ! -d data/alphabet.csv ] | [ ! -d data/amazon.csv ]; then #
echo "Fetching data..." #
URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=3IAFG5IWH0P5UW5G&outputsize=full&datatype=csv" #
curl -k --request GET $URL > data/apple.csv #
URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=3IAFG5IWH0P5UW5G&outputsize=full&datatype=csv" #
curl -k --request GET $URL > data/alphabet.csv #
URL="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=3IAFG5IWH0P5UW5G&outputsize=full&datatype=csv" #
curl -k --request GET $URL > data/amazon.csv #
echo "Done" #
#fi #
# Insety data from the csv files into db for the specified date, stocks and csv file #
function insertdata() { #
    DATE="$1" #
    STOCK="$2" #
    CSV="$3" #
    echo "Retrieving Data for '$STOCK'" #
    # get data from specified csv file #
    # cat opens the file, grep gets the row, awk gets the column we know in which column which value is stored #
    OPEN=$(cat "$CSV" | grep "$DATE" | awk -F',' '{ print $2 }') #
    HIGH=$(cat "$CSV" | grep "$DATE" | awk -F',' '{ print $3 }') #
    LOW=$(cat "$CSV" | grep "$DATE" | awk -F',' '{ print $4 }') #
    CLOSE=$(cat "$CSV" | grep "$DATE" | awk -F',' '{ print $5 }') #
    VOLUME=$(cat "$CSV" | grep "$DATE" | awk -F',' '{ print $6 }') #
    # Print out the data you got just to varify the correctness #
    echo "OPEN: $OPEN" #
    echo "HIGH: $HIGH" #
    echo "LOW: $LOW" #
    echo "CLOSE: $CLOSE" #
    echo "VOLUME: $VOLUME" #
# Create a table if it does not exists, and add values to the table #
sqlite3 test2_db.db << EOF
CREATE TABLE IF NOT EXISTS stock_data (DATE varchar(255) not null, STOCK varchar(255) not null, OPEN float not null, HIGH float not null, LOW float not null, CLOSE_VALUE float not null, VOLUME integer not null);
INSERT INTO stock_data (DATE, STOCK, OPEN, HIGH, LOW, CLOSE_VALUE, VOLUME) VALUES ('$DATE', '$STOCK', $OPEN, $HIGH, $LOW, $CLOSE, $VOLUME);
EOF
    echo "Data stored in db" #
} #
# Main function keeps getting recursively called until user terminates or enters 'q' #
function welcome() { #
    echo "Please enter the date you wish to retrieve data from."
    echo "But note that it cannot be before 1990-01-02."
    echo "Also please use YYYY-MM-DD format."
    echo "You can enter q if you wish to quit"
    echo "Your input> "
    read response #
    if [ "$response" == "q" ]; then #
        echo "Bye"
        exit #
    else # insert values in db for each stock for specified date #
        insertdata "$response" "AAPL" "data\apple.csv" #
        insertdata "$response" "GOOGL" "data\alphabet.csv" #
        insertdata "$response" "AMZN" "data\amazon.csv" #
        welcome #
    fi #
} #
welcome #
echo "bye..." #
exit # 
#
