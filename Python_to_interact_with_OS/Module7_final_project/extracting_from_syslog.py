#!/usr/bin/env python

import re

#pattern = r"(\w\w\w \d\d \d\d:\d\d:\d\d) ([\w-\.]+) (\w+\[\d+\]): ([^:]+): ([^\/]+)\/([^@]+)@([\d\.]+):(\d+) (.*$)"
#event_pattern = re.compile(r'<\d{1,2}>.?(ERROR|INFO):?(.*)$')
event_pattern = re.compile(
    r"(?:\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) "  # Date and time
    r"localhost "  # Hostname
    r"jenkins\[\d+\]: "  # Jenkins process name and PID
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) "  # Timestamp
    r"\[(.*?)\] "  # Log ID
    r"([A-Z]+) "  # Log level (INFO, ERROR, etc.)
    r"(.*)$")  # Log message
log_file = ""
def extract_events(log_file):
    events = []
    with open(log_file, 'r') as f:
        print("oppening file:" + log_file)
        for line in f.readlines():
            match = event_pattern.match(line)
            if match:
                #extract
                event_level = match.group(1)
                event_message = match.group(2).strip()
                events.append((event_level, event_message))
            return events
    f.close()
    print(events)
