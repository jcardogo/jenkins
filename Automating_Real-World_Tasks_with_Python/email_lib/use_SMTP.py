import smtplib

mail_server= smtplib.SMTP("smtp.gmail.com")
mail_server.set_debuglevel(1)

import getpass
mail_pass = getpass.getpass("Password? ")
mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()
