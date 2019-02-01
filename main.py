import sys
from function import *
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
numberofdays = int(argument[2])
print bob_tool(date, numberofdays)
 
