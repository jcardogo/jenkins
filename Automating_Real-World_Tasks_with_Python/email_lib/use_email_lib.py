import os.path
attachement_path = "/tmp/example.png"
attachement_filename = os.path.basename(attachement_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachement_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split("/", 1)
print(mime_type)
print(mime_subtype)

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

with open(attachement_path, "rb") as ap:
  message.add_attachement(ap.read(),
                         maintype=mime_type,
                         subtype=mime_subtype,
                         filename=os.path.basename(attachement_path))
print(message)
