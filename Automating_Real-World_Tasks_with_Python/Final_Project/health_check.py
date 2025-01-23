#!/usr/bin/env Python3

import shutil
import psutil
import socket 
import emails
import os

sender = "automation@example.com"
reciever = "<USERNAME>@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

# Checks sisk usage and sends email if available space < 20%
du = shutil.disk_usage("/")
du_prsnt = du.free/du.total *100
if du_prsnt < 20:
    subject = "Error - Available disk space is less than 20%"
    message =  emails.generate_error_email(sender, reciever, subject, body)
    emails.send_email(message)

# Check CPU usage and sends email if usage > 80%
cpu_prsnt = psutil.cpu_percent(1)
if cpu_prsnt > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, reciever, subject, body)
    emails.send_email(message)

#Check for available memory, if < 100mb send and email
mem = psutil.virtual_memory()
trs = 100 * 1024 * 1024 #100MB
if mem.available < trs:
    subject = "Error - Available memory is less than 100MB"
    message = emails.generate_error_email(sender, reciever, subject, body)
    emails.send_email(message)

#Checks hostname and if cannot be resolved to "127.0.0.1" sends an email
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, reciever, subject, body)
    emails.send_email(message)