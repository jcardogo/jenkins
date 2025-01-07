from email.message import EmailMessage
message = EmailMessage()
print(message)

sender = "jcardogo@gmail.com"
recipient = "jairoalejandrocardoso@gmail.com"

message["From"] = sender
message["To"] = recipient

print(message)

message["Subject"] = "Greetings from {}"
