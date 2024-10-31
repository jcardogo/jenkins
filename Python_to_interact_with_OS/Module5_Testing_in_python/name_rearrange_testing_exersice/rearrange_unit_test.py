#!/usr/bin/env python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase): #with this code we create our own class by inherits from test case, thus inheritating those testing methods. we incluide the class from we want to inheritta in the parentheses
    
  def test_basic(self): #we define the function "test_basic" that will compare expected result with output
    testcase = "Lovelace, Ada" #string input to the rearrange method
    expected = "Ada Lovelace" #expected output from the rearrange method
    self.assertEqual(rearrange_name(testcase), expected)  #define the comparison between input applied on testcase string variable and the exptected strign
  
  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)
  
  def test_double_name(self):
    testcase = "Alejandro, Cardoso G."
    expected = "Cardoso G. Alejandro"
    self.assertEqual(rearrange_name(testcase), expected)
  
  def test_one_name(self):
    testcase = "Jairo"
    expected = "Jairo"
    self.assertEqual(rearrange_name(testcase), expected)


# Run the tests
unittest.main() #we call this main function to run this test for us

'''
chmod +x rearrange_test.py 
./rearrange_test.py 
'''
