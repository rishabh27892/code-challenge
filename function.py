import datetime
import calendar
from datetime import timedelta
mm = 0
dd = 0
yyyy = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']


#date parsing of the initial input to break it into dd, mm, yyyy element and checking basic date restrictions(months with 30 days are checked by datetime lib)
def parsfun(date):
    fail = False
    postdate = date.split("-")
    mm = int(postdate[0])
    dd = int(postdate[1])
    yyyy = int(postdate[2])
    if dd < 1 or dd > 31:
        print ("invalid date")
        fail = True
    if mm < 1 or mm > 12:
        print ("invalid month")
        fail = True
    if yyyy < 1 or len(postdate[2]) < 4:
        print ("invalid year")
        fail = True
    if fail is True:
        print ("try again with valid dates")
        exit()
    return [mm, dd, yyyy]

# leap year condition check via  library
def leaplib(year):
    return calendar.isleap(year)

# leap year condition check without library
def leapfun(year):
    if year%4 == 0 and year%100!=0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

# weekly price change based on the week of the month
def weeklyprice(date):
    if 0 < date < 8:
        price = 0.05
    elif 7 < date < 15:
        price = 0.10
    elif 14 < date < 22:
        price = 0.15
    elif 21 < date < 29:
        price = 0.20
    elif 28 < date < 32:
        price = 0.25
    else:
        price = 0
    return price

# final date function to perform corner condition (February 28/29 based on the leap year)
def final_dates(date):
    dates = parsfun(date)
    condition = leapfun(dates[2])
    if dates[0] == 2:
        if condition is False and int(dates[1]) > 28:
            print ("Since it is not a leap year, Feb must have only 28 days")
            exit()
        elif condition is True and int(dates[1]) > 29:
            print ("Since it is a leap year, Feb must have only 29 days")
            exit()
    return [dates[0], dates[1], dates[2]]

# checks if it is a weekday or not
def check_day(date):
    # format is yyyy, mm, dd
    day = datetime.date(date[2], date[0], date[1]).weekday()
    return day

# finds the next valid date after adding certain number of days
def date_add(date, days):
    dates = date
    d1 = datetime.date(dates[2], dates[0], dates[1])
    d0 = d1 + timedelta(int(days))
    return d0
# reformatting due to different formats of python inbuilt library and input taken by the user
def reformat(date):
    date = str(date)
    postdate = date.split("-")
    yyyy = postdate[0]
    mm = postdate[1]
    dd = postdate[2]
    f_date = mm + "-" + dd + "-" + yyyy
    return f_date

# bob's tool calculating the total cost of bananas
def bob_tool(date, days):
    P = 0
    new_date = date
    while days != 0:
        f_date = final_dates(new_date)
        # check to ignore weekends
        if check_day(f_date) == 5 or check_day(f_date) == 6:
            pass
        else:
            P = weeklyprice(f_date[1]) + P
        new_date = reformat(date_add(f_date, 1))
        days = days - 1
    return P

