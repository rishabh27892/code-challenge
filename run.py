# !/usr/bin/env python
# Author: Rishabh Chauhan
# Location for Bob's tool to perform tests
# Test case count: 5

from function import *
import sys
import traceback
import os
import requests
import random
import unittest
import xmlrunner
import json

params = {
        'endpoint' : "https://bananabudget.azurewebsites.net/",
        'date' : "startDate=",
        'days' : "numberOfDays="
}

input_date = {
            'example' : "10-12-2017",
            'feb29leap' : "02-29-2020",
            'feb29nonleap' : "02-29-2019",
            'aug27bday' : "08-27-1992",
            'sept30' : "09-30-1892",
}

input_day = {
            'example' : 20,
            'feb29leap' : 45,
            'feb29nonleap' : 76,
            'aug27bday' : 5,
            'sept30' : 31
}


class bobsbudget_test(unittest.TestCase):

    def setUp(self):
        pass


    def test_01_codechallenegexample(self):
        try:
            response = GETf(input_date['example'], input_day['example'])
            response2 = bob_tool(input_date['example'], input_day['example'])
            data = response.json()
            TotalCost = data['totalCost']
            TotalCost = TotalCost[1:]
            print "Rest Price: " + str(TotalCost) + " Function price: " +  str(response2)
            assert str(TotalCost) == str(response2), "Value mismatch"
        except:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")



    def test_02_feb29_leapyear(self):
        try:
            response = GETf(input_date['feb29leap'], input_day['feb29leap'])
            response2 = bob_tool(input_date['feb29leap'], input_day['feb29leap'])
            data = response.json()
            TotalCost = data['totalCost']
            TotalCost = TotalCost[1:]
            print "Rest Price: " + str(TotalCost) + " Function price: " +  str(response2)
            assert str(TotalCost) == str(response2), "Value mismatch"
        except:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")


    def test_03_feb29_nonleapyear(self):
        try:

            response = GETf(input_date['feb29nonleap'], input_day['feb29nonleap'])
            response2 = bob_tool(input_date['feb29leap'], input_day['feb29nonleap'])
            data = response.json()
            TotalCost = data['totalCost']
            TotalCost = TotalCost[1:]
            print "Rest Price: " + str(TotalCost) + " Function price: " +  str(response2)
            assert str(TotalCost) == str(response2), "Value mismatch"
        except:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")


    def test_04_aug27_mybirthday(self):
        try:
            response = GETf(input_date['aug27bday'], input_day['aug27bday'])
            response2 = bob_tool(input_date['aug27bday'], input_day['aug27bday'])
            data = response.json()
            TotalCost = data['totalCost']
            TotalCost = TotalCost[1:]
            print "Rest Price: " + str(TotalCost) + " Function price: " +  str(response2)
            assert str(TotalCost) == str(response2), "Value mismatch"
        except:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

# This must fail due to invalid date
    def test_05_sept30(self):
        try:
            response = GETf(input_date['sept30'], input_day['sept30'])
            response2 = bob_tool(input_date['sept30'], input_day['sept30'])
            data = response.json()
            TotalCost = data['totalCost']
            TotalCost = TotalCost[1:]
            print "Rest Price: " + str(TotalCost) + " Function price: " +  str(response2)
            assert str(TotalCost) == str(response2), "Value mismatch"
        except:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")



if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports',  verbosity=2),
        failfast=False, buffer=False, catchbreak=False)
