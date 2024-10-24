#!/usr/bin/env python
import sys
import os
import re

'''
Make the file executable before running it.

sudo chmod +x find_error.py
Copied!
Now, run the file by passing the path to fishy.log as a parameter to the script.

./find_error.py ~/data/fishy.log
Copied!
This script will now prompt for the type of error to be searched. Continue by entering the following type of error:

CRON ERROR Failed to start
Copied!
On successful execution, this will generate an errors_found.log file, where you will find all the ERROR logs based on your search. You can view the ERROR log using the command below:

cat ~/data/errors_found.log
'''
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)