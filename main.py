import sys
from function import *
month_dict = {
"jan" : 31,
"feb" : 28,
"mar" : 31,
"apr" : 30,
"may" : 31,
"jun" : 30,
"jul" : 31,
"aug" : 31,
"sep" : 30,
"oct" : 31,
"nov" : 30,
"dec" : 31
}
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
weeklyPrice = {
    "first" : 0.05,
    "second" : 0.10
#    "third" :
}
argument = sys.argv

UsageMSG = """
Usage for %s:

main.py mm.dd.yyy number

Mandatory arguments:
<mm.dd.yyyy>                - Start date in MM.DD.YYYY format

<number>                    - Number of days (1 to 365)


""" % argument


if len(argument) < 3:
    print (UsageMSG)
    exit()
if int(argument[2]) > 365:
    print (UsageMSG)
    exit()

date = argument[1]
numberofdays = argument[2]
print (final_dates(date))

print ("it was a " +  weekday[check_day(final_dates(date))])

#bob_tool(final_dates(date), numberofdays)
temp_date_add(final_dates(date), numberofdays)
