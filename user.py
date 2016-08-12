"""Users of my app."""
from model import db


class User(object):
    """Unique user."""

    def __init__(self, first_name, last_name, bday, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.bday = bday
        self.email = email
        self.password = password

    def __repr__(self):
        """Show useful information about user."""

        return "<Customer: %s %s, %s, %s>" % (self.first_name,
                                              self.last_name,
                                              self.bday,
                                              self.email)


def grab_user_from_db(email):
    """Grab user info from users table in contacts database given an email."""

    user = db.session.query(User).filter_by(email=email).all()

    return user



