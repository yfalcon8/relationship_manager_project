"""Send user an email about their contact and recommend how to reach out."""

import smtplib
from model import Relationship, db, connect_to_db
import schedule
# Built-in Simple Mail Transfer Protocol (SMTP) module


def call_function():
    send_event_notification("Joys Place", "relationshipmanagerhb@gmail.com")


def send_event_notification(name, email):
    # Set datetime to 'start' when the user signs up.
    # add 4 months to sign_up_datetime for professional contacts
    # add 1 months to sign_up_datetime for friends/fam

    # recipient_email = ["yfalcon8@gmail.com"]

    content = """From: Relationship Manager App <RelationshipManagerHB@gmail.com>
    To: {}
    Subject: SMTP e-mail test

    Hiya, {}!
    Your python email worked!!""".format(email, name)

    # Create an SMTP object that specifices the server & port (465 or 587 for Gmail).
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # Identify yourself to server by helo (regular) or ehlo (esmtp server).
    mail.ehlo()

    # Start TLS mode (transport layer security).
    # Any smtp command that comes after this code will be encrypted.
    mail.starttls()

    # Log in to the account that email will come from.
    mail.login("yfalcon8@gmail.com", "yukilovesmarlonandmomo")

    # Specify sender, receiver and content of email.
    mail.sendmail("yfalcon8@gmail.com", email, content)

    # Disconnect from teh SMTP server
    mail.quit()

# Email every 4 months for professional contacts
schedule.every(13).weeks.do(call_function)

# Email every month for professional contacts
schedule.every(4).weeks.do(call_function)


if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    from server import app
    connect_to_db(app)
    relatp_type = db.session.query(Relationship.relatp_type).filter_by(id=1).all()[0][0]
    print "\n\n\n\n", relatp_type, "\n\n\n\n"

    while True:
        schedule.run_pending()
    # db.create_all()
    # print "Connected to DB."
