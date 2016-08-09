"""The muscle of my database. Models and database functions for contacts db."""

# What is SQLAlchemy? It is a popular and powerful Python-based Object
# Relational Model/Mapper (ORM). Helps me navigate my relational database.

from flask_sqlalchemy import SQLAlchemy

# Here's where the idea of my database is created. This is pulled from my
# Flask-SQLAlchemy library. db allows me to find the 'session' object where
# the majority of my database interactions will occur (such as committing,
# querying, etc.)

db = SQLAlchemy()

# This set up allows my app the ability to talk to SQLite, PostgreSQL, MySQL
# and more.


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///contacts'
    db.app = app
    db.init_app(app)

connect_to_db(app)

##############################################################################
# Create my ORM. Allows for object-orientation into SQL.

# All of my models will subclass db.Model. What is db.Model?


class User(db.Model):
    """Stores information about my users."""

    # Specifies table name.
    __tablename__ = "users"

    # db.Column creates a column in the users table called user_id. db.Integer
    # specifies the type of column. This column sets my primary key to be
    # an automatically increasing number.
    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)

    # db.String(30) indicates that the data type of this column can contain
    # letters, numbers and special characters. As it would not make sense to
    # have numbers and special characters in a first name, the HTML form that
    # will collect the first name from the user will specity that only letters
    # are allowed. The (30) indicates that this field will fit a max of
    # 30 characters.
    first_name = db.Column(db.String(30),
                          nullable=False)


    # The nullability of this field is set to False, as I want to require my
    # users to input their name.
    last_name = db.Column(db.String(30),
                          nullable=False)

    # The users email address will be their username for their login. Users
    # must have different usernames, meaning they must be unique.
    email = db.Column(db.String(50),
                      nullable=False,
                      unique=True)

    password = db.Column(db.String(20),
                         nullable=False)

    bday = db.Column(db.Date(20),
                         nullable=False)


# class Recommendation(db.Model):
#     """Stores information about my users."""

#     # Specifies table name.
#     __tablename__ = "recommendations"

#     # db.Column creates a column in the users table called user_id. db.Integer
#     # specifies the type of column. This column sets my primary key to be
#     # an automatically increasing number.
#     rcmdn_id = db.Column(db.Integer,
#                         primary_key=True,
#                         autoincrement=True)

#     relat_code = db.Column()



# def connect_to_db(app):
#     """Conenct the database to the Flask app."""

#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///contacts'
#     db.app = app
#     db.init_app(app)

if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
