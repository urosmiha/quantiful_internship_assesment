# Quantiful Data Engineering Internship Program Assessment

# Question 1
________________________________________________
### Pre-requirements:
- Python 3
- requests library

For this task I used python and 'requests' library which usually does not come with standard python libraries so you'll probably have to add it.
- In Linux use _sudo easy_install requests_ or _pip install requests_
- In Windows use _[Path]\easy_install.exe requests_ where [path] is where easy_install.exe is (usually where your python.exe is and then in Scripts directory)
- For more info: https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests

## How does the code work
- Code is commented where ever I felt neccessery.
- I left some commented code that mostly just print some value, to show the process I went  through
- I did not use standard try and catch to check if the response was successful but I rather just used if statement to check for response 200 (i.e. success).
- I first searched all states and got _locationid_ for Florida and then I used that _locationid_ to find all the precipitation reading from all the stations in that location (i.e. Florida).
- After tonnes of API documentation reading I decided to use PRECIP_HLY as _datasetid_ which should (from my understanding) return the hourly precipitation reading.
- For the start date I used '2000-07-14T14:00:00' while for end I used '2000-07-24T15:00:00' because the maximum number of results you can get back  is 1000 so in (very unlikely) case where there are more than 1000 results for that specific hour we can request the second lot. Although I am not quite sure how to do that yet. Maybe not necessary step but good practice I guess.

- __INTERESTING OBSERVATION__:
According to HOAA API datasheet when the returned value is 99999 that means the value is missing.
However that is only the case if you do not specify the __unit__ parameter in url
If the __unit__ is specified as _standard_ (which is inch) the incomplete value seems to be returned as __999.99__
If the __unit__ is specified as _metric_ (which is mm) the incomplete value seems to be returned as __25399.75__

- Since my European heritage prevents me to understand the imperial measurements I have set unit parameter as metric.
Therefore I will assume that anything above 25000 is an error and will not be accounted for reading.

- Returned value is also in tenths of millimeter so the accumulated result should be multiplied by 0.1 to get mm, before it gets divided with the total number of readings, to get the average value.

## Running the script
- Simply run the __test1.py__ scripts
- The output should display '_Average precipitation: 1.5833 mm_'

__End of Question 1__
_________________________________________________________________________________________________________________



