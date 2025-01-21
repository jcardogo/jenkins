import os.path
attachement_path = "/tmp/example.png"
attachement_filename = os.path.basename(attachement_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachement_path)
mime_type, mime_subtype = mime_type.split("/", 1

from email.message import EmailMessage
message = EmailMessage()
sender = "jcardogo@gmail.com"
recipient = "jairoalejandrocardoso@gmail.com"

message["From"] = sender
message["To"] = recipient

message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)

body = """Hey there!

Im learning to send emails using python!"""

message.set_content(body)

import smtplib

mail_server= smtplib.SMTP("smtp.gmail.com", 587)
mail_server.set_debuglevel(1)

import getpass
mail_pass = getpass.getpass("Password? ")
mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()
