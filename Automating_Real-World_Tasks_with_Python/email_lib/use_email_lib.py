from email.message import EmailMessage
message = EmailMessage()
print(message)

sender = "jcardogo@gmail.com"
recipient = "jairoalejandrocardoso@gmail.com"

message["From"] = sender
message["To"] = recipient

print(message)

message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)
print(message)

body = """Hey there!

Im learning to send emails using python!"""

message.set_content(body)

print(message)
