import datetime

def getTenYearsAgoDate():
    # Get date 10 years ago from today
    ten_years_later = datetime.datetime.now() - datetime.timedelta(days=10*365.24)
    return ten_years_later.date()