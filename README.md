# Quantiful Data Engineering Internship Program Assessment

# Question 1

### Pre-requirements:
- Python 3
- requests library for python

For this task, I used python and 'requests' library which usually does not come with standard python libraries so you'll probably have to add it.
- In Linux use _sudo easy_install requests_ or _pip install requests_
- In Windows use _[Path]\easy_install.exe requests_ where [path] is where easy_install.exe is (usually where your python.exe is and then in Scripts directory)
- For more info: https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests

### Necessary Files:
- _test1.py_

## How does the code work
- The code is commented where ever I felt necessary.
- I left some commented code that mostly just prints some value, to show the process I went through.
- I did not use standard try and catch to check if the response was successful but I rather just used if statement to check for response 200 (i.e. success).
- I first searched all states and got _locationid_ for Florida and then I used that _locationid_ to find all the precipitation reading from all the stations in that location (i.e. Florida).
- After tonnes of API documentation reading, I decided to use PRECIP_HLY as _datasetid_ which should (from my understanding) return the hourly precipitation reading.
- For the start date I used '2000-07-14T14:00:00' while for end I used '2000-07-24T15:00:00' because the maximum number of results you can get back  is 1000 so in (very unlikely) case where there are more than 1000 results for that specific hour we can request the second lot. Although I am not quite sure how to do that yet. Maybe not necessary step but good practice I guess.

- __INTERESTING OBSERVATION__:
According to HOAA API datasheet when the returned value is 99999 that means the value is missing.
However, that is only the case if you do not specify the __unit__ parameter in URL
If the __unit__ is specified as _standard_ (inches) the incomplete value seems to be returned as __999.99__
If the __unit__ is specified as _metric_ (mm) the incomplete value seems to be returned as __25399.75__

- Since my European heritage prevents me to understand the imperial measurements I have set the unit parameter as a metric.
Therefore I will assume that anything above 25000 is an error and will not be accounted for reading.

- The returned value is also in tenths of a millimetre so the accumulated result should be multiplied by 0.1 to get mm, before it gets divided with the total number of readings, to get the average value.

## Running the script
- Simply run the __test1.py__ scripts
- The output should display '_Average precipitation: 1.5833 mm_'

__End of Question 1__
_________________________________________________________________________________________________________________

# Question 2
### Pre-requirements:
- Python 3
- requests library for pythoon
- SQLite
### Necessary Files
- _test2.py_ - handles all API calls and data filtering
- _helper_func.py_  - has a simple function to calculate the date 10 years ago from today
- _dbh.py_  - handles all database connections and setup
## How does the code work
### Getting data from APIs
- API documentation: https://www.alphavantage.co/documentation/#daily
- I could not find the way to specify that I want a data not older than 10 years.
- The only 2 options were compact (only latest 100 results) or full (all data from last 20 years)
- So I had to use full and filter data, so I have a function that calculates the date 10 years ago from today. So this code will always get data for the last 10 years from the date you run it.
- Initially, I used compact just to test that my logic works for storing and accessing data.
- Then I used _full_ parameter to get data from the last 20 years. (This took a long time)
### Database setup and storing data
- When the script is run it tries to connect to __test2_db.db__ database and if it cannot find it then it creates it.
- Upon that the table __stock_data__ is created if not existent already.
- Therefore there is no need to have a database already set up, the script will create it.
- __I assume that you do not want me to share the database with you, since it's quite large__ I can't even push it to git anyways because of its size.
- Data returned from API requests is added to this table )
- For __STOCK__ files in the table, I used NSDAQ (i.e. AAPL, GOOGL, AMZN)

## Executing the script
- __Make sure you have _helper_func.py_ and _dbh.py_ files in the same directory as the scrip file__
- Simply run __test2.py__
- The dates for each stock should be printed on the screen.
- Go make yourself a cup of coffee cause this will take a while

__End of Question 2__
____________________________________________________________________________________________________

