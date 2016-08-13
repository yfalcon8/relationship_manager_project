"""Send user an email about their contact and recommend how to reach out."""

import smtplib
# Built-in Simple Mail Transfer Protocol (SMTP) module


from model import db, User

# FIXME: How do I query my db from this file?
all_users = db.session.query(User).all()
print all_users


def send_event_notification(name, email):
    sender = "relationshipmanagerhb@gmail.com"
    # recipient_email = ["yfalcon8@gmail.com"]
    # recipient_name = ["Yuki Falcon"]

    content = """From: Relationship Manager App <RelationshipManagerHB@gmail.com>
    To: <%s>
    Subject: SMTP e-mail test

    Hiya, %s!
    your python email worked! mmm!""" % (email, name)

    # Create an SMTP object that specifices the server & port (465 or 587 for Gmail).
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # Identify yourself to server by helo (regular) or ehlo (esmtp server).
    mail.ehlo()

    # Start TLS mode (transport layer security).
    # Any smtp command that comes after this code will be encrypted.
    mail.starttls()

    # Log in to the account that email will come from.
    mail.login(sender, "fulfillinspiremotivate")

    # Specify sender, receiver and content of email.
    mail.sendmail(sender, email, content)

    # Disconnect from teh SMTP server
    mail.quit()