import datetime
import calendar
from datetime import timedelta
mm = 0
dd = 0
yyyy = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']

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

def leaplib(year):
    return calendar.isleap(year)

def leapfun(year):
    if year%4 == 0 and year%100!=0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False

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
    print (price)
    return price

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

def check_day(date):
    # format is yyyy, mm, dd
    day = datetime.date(date[2], date[0], date[1]).weekday()
    return day

def bob_tool(date, days):
    print ("here is where bob's tool will work with days: " +  str(date) + " and number of days: " + str(days))

def date_add(date, days):
    dates = date
    d1 = datetime.date(dates[2], dates[0], dates[1])
    d0 = d1 + timedelta(int(days))
    return d0


def while_fun(date, days):
    P = 0
    new_date = date
    while days != 0:
        f_date = final_dates(new_date)
        print f_date
        print (str(P) + " " + str(days))
        print (f_date[1])
        print (weeklyprice(f_date[1]))
        if check_day(f_date) == 5 or check_day(f_date) == 6:
            print "it is a weekend"
        else:
            P = weeklyprice(f_date[1]) + P
        new_date = reformat(date_add(f_date, 1))
        print new_date
        days = days - 1
    print ("The total price including weekends is: " + str(P))

def reformat(date):
    date = str(date)
    postdate = date.split("-")
    yyyy = postdate[0]
    mm = postdate[1]
    dd = postdate[2]
    f_date = mm + "-" + dd + "-" + yyyy
    return f_date
