"""Send user an email about their contact and recommend how to reach out."""

import smtplib
# Built-in Simple Mail Transfer Protocol (SMTP) module

import schedule

import arrow

from model import Event, User, Relationship, connect_to_db, db

from flask import Flask

#######################
#### Configuration ####
#######################
app = Flask(__name__)
connect_to_db(app)

# Sets make the most sense here, as it's faster than a list and there's
# no need for a key.
past_events = set()


def call_function():
    """Query the Events table to check who needs to be emailed and email them."""

    # Grab the current time in datetime format.
    current_time_arrowed = arrow.now('US/Pacific')
    current_time_datetimed = current_time_arrowed.datetime

    # Grab all of the Events that passed the current time.
    all_events = db.session.query(Event).filter(Event.scheduled_at < current_time_datetimed).all()

    # Check to see if the email has already been sent regarding that event.
    # If not, send the email.
    for event in all_events:
        if event.id not in past_events:

            # Grab the user info.
            user_info = db.session.query(User.first_name, User.last_name, User.email).filter_by(id=event.user_id).one()
            recipient_name = user_info.first_name[0], user_info.last_name[0]

            # Grab the relationship info.
            relatp_info = db.session.query(Relationship.first_name, Relationship.last_name).filter_by(id=event.relatp_id)
            relatp_name = relatp_info.first_name, relatp_info.last_name

            # Send the email.
            send_event_notification(recipient_name, relatp_name, user_info.email, event.rcmdn)

            # Make sure the user doesn't get notified about that event again.
            past_events.add(event.id)

        else:
            return


def send_event_notification(recipient_name, relatp_name, recipient_email, recommendation):
    """Send an email to the user reminding them to reach out to their friends."""

    content = """From: Relationship Manager App <RelationshipManagerHB@gmail.com>
    To: {}
    Subject: SMTP e-mail test

    Hiya, {}!
    Time to reach out to {}. Your python email worked!! {}""".format(recipient_email, recipient_name, relatp_name, recommendation)

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
    mail.sendmail("yfalcon8@gmail.com", recipient_email, content)

    # Disconnect from teh SMTP server
    mail.quit()


if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    schedule.every().hour.do(call_function)

    while True:
        schedule.run_pending()
    # print "Connected to DB."
