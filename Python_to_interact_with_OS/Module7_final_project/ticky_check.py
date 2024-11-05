#/usr/bin/env python3
import sys
import re
import operator
import csv

#Dictionary counting the number of event for user
per_user = {} #splitting between INFO and ERROR

#Dictionary witn the number of different ERROR messages 
errors = {} 

#Section_1: Read the file and populate Dictionaries
 
log_file = "/var/log/messages"

with open(log_file, 'r') as file:
    for line in file:
        #Regular expression search
        # * Sample Line of log file
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"        
        event_pattern = r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$" #regular expression separate sections
        match = re.search(event_pattern, line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)
        
        # Populates error dict with ERROR messages from log file
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] =+1
        
        #Populate per_user dict with user and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        #Populate user dictionary with per user logs entry
        if code == "INFO":
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]["INFO"] = 0
            else:
                per_user[user]["INFO"] =+ 1
        if code == "ERROR":
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]["ERROR"] = 0
            else:
                per_user[user]["ERROR"] =+ 1

#Sorted by VALUE (most common to least common)
error_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

#Sorted by USERNAME
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()

#Insert at the beginning of the list
error_list.insert(0, ('ERROR', 'Count'))
#per_user_list.insert(0, ("USER", "Event"))

# * Create CSV file user_statistics
with open('user_statistics.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' + str(value['INFO']) + ',' + str(value['ERROR']) + '\n')

#create CSV file for error_message
with open('error_message.csv', 'w', newline='') as error_csv:
    for key, value in error_list:
        error_csv.write(str(key)+','+str(value)+'\n')



