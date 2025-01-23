#!/usr/bin/env Python3

import os
import datetime
import report
import emails

dt = datetime.date.today().strftime("%B %d, %Y")
date = "Processed Update on" + dt
names = []
weights = []
path = "./supplier-data/descriptions/"
for file in os.listdir("./supplier-data/descriptions"):
    with open (path + file) as f:
        for ln in f:
            line = ln.strip()
            if len(line) <= 10 and len(line) > 0 and "lb" not in line:
                fruit_name = "name: " + line
                names.append(fruit_name)
            if "lbs" in line:
                fruit_weight = "weight: " + line
                weights.append(fruit_weight)

summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == "__main__":
    report.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    reciever = "jcardogo@gmail.com".format(os.enviton.get('USER'))
    subject = "Upload Completed -Online Fruit Store"
    body = "All fruits are uploaded to our website succesfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, reciever, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

