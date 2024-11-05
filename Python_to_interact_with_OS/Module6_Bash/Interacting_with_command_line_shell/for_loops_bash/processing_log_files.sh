#!/bin/bash

#this script will list the top 10 most repeted logs on syslog

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
