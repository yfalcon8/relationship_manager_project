"""The muscle of my database. Models and database functions for contacts db."""

# SQLAlchemy is a popular and powerful Python-based Object
# Relational Model/Mapper (ORM). Helps me navigate my relational database.
# SQLAlchemy is a powerful software that transforms Python into SQL.

import datetime

from flask_sqlalchemy import SQLAlchemy

# Here's where the idea of my database is created. This is pulled from my
# Flask-SQLAlchemy library. db allows me to find the 'session' object where
# the majority of my database interactions will occur (such as committing,
# querying, etc.)

db = SQLAlchemy()


##############################################################################
# Create my ORM. Allows for object-orientation into SQL.

# All of my models will subclass db.Model.
# This declares that a class will be managed by SQLAlchemy.
# db is the object and Model is a class.
# The Model class contains the __init__() method, so I don't need to include it.
class User(db.Model):
    """Stores information about my users."""

    # The instances of this class will be stored in a table named users.
    __tablename__ = "users"

    # db.Column creates a column in the users table called user_id. db.Integer
    # specifies the type of column. This column sets my primary key to be
    # an automatically increasing number.
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    # If the user signs up with Facebook, grab their Facebook_user_id.
    # This field is useful for when users who didn't store their email with
    # FB wants to sign-in to my app. FB may not return an email address, but
    # the user will have an email address stored in my database.
    fb_id = db.Column(db.String(20),
                      unique=True)

    # 'String' is the SQLAlchemy-managed version of the data type.
    # It indicates that the data type of this column can contain
    # letters, numbers and special characters.
    # The (30) indicates that this field will fit a max of 30 characters.
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

    def __repr__(self):
        return "<User: {} {}, {}, {}>".format(self.first_name,
                                              self.last_name,
                                              self.email,
                                              self.fb_id)


class Recommendation(db.Model):
    """Stores information about my users."""

    __tablename__ = "recommendations"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    # The default is for those users who do not feel like specifying the type
    # relationship they have with the contact they just imported. There will
    # be a default set of tips on how to reach out.
    relatp_type = db.Column(db.String(3),
                            default='fr')

    rcmdn = db.Column(db.Text,
                      nullable=False,
                      unique=True)

    # Join the recommendation table and relationship table through the
    # relatp_code. This allows me to navigate from the a user's contact to his/her
    # associated recommendations and vice versa.
    relatp = db.relationship("Relationship",
                             secondary='rcmdns_relatps')

    def __repr__(self):

        return "<Recommendation: relatp_type={}, rcmdn={}>".format(self.relatp_type,
                                                                   self.rcmdn)


class Event(db.Model):
    """Stores information about each event."""

    __tablename__ = "events"

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    scheduled_at = db.Column(db.DateTime)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.id'))

    rcmdn = db.Column(db.Text,
                      nullable=False)

    user = db.relationship('User', backref=db.backref('event'))

    relationship = db.relationship('Relationship', backref=db.backref('events'))

    def __repr__(self):
        return "<Event: id={}, user_id={}, scheduled_at={}, relatp_id={}, rcmdn={}>".format(self.id,
                                                                                            self.user_id,
                                                                                            self.scheduled_at,
                                                                                            self.relatp_id,
                                                                                            self.rcmdn)


class Relationship(db.Model):
    """Stores all of a users' contacts info."""

    __tablename__ = "relationships"

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)

    first_name = db.Column(db.String(30),
                           nullable=False)

    last_name = db.Column(db.String(30))

    relatp_type = db.Column(db.String(3),
                            nullable=False,
                            default='fr')

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    created_date = db.Column(db.DateTime,
                             default=datetime.datetime.now())

    rcmdn_list = db.Column(db.Text)

    email = db.Column(db.String(50))

    bday = db.Column(db.Date)

    phone = db.Column(db.String(15))

    work = db.Column(db.String(50))

    edu = db.Column(db.String(50))

    fb = db.Column(db.String(50))

    linked_in = db.Column(db.String(50))

    twitter = db.Column(db.String(50))

    google_plus = db.Column(db.String(50))

    github = db.Column(db.String(50))

    pinterest = db.Column(db.String(50))

    word_press = db.Column(db.String(50))

    yelp = db.Column(db.String(50))

    skype = db.Column(db.String(50))

    other_social_media = db.Column(db.String(50))

    gift_idea = db.Column(db.Text)

    goal = db.Column(db.Text)

    note = db.Column(db.Text)

    pet = db.Column(db.Text)

    family = db.Column(db.Text)

    hobby = db.Column(db.Text)

    likes = db.Column(db.Text)

    dislike = db.Column(db.Text)

    pet_peeve = db.Column(db.Text)

    fav_food = db.Column(db.Text)

    fav_drink = db.Column(db.Text)

    fav_restaurant = db.Column(db.Text)

    sports_team = db.Column(db.Text)

    fav_brand = db.Column(db.Text)

    other_fav = db.Column(db.Text)

    convo = db.Column(db.Text)

    trait = db.Column(db.Text)

    user = db.relationship("User", backref=db.backref("relationships"))

    recommendations = db.relationship("Recommendation",
                                      secondary='rcmdns_relatps')

    def __repr__(self):
        """Provide useful information about the relationship."""

        return "<Relationship: id={}, first_name={}, last_name={}, created_date={}\
        relatp_type={}, user_id={}, rcmdn_list={}, email={}, bday={}, phone={},\
        work={}, edu={}, fb={}, linked_in={}, twitter={}, google_plus={},\
        github={}, pinterest={}, word_press={}, yelp={}, skype={},\
        other_social_media={}, gift_idea={}, goal={}, note={}, pet={},\
        family={}, hobby={}, likes={}, dislike={}, pet_peeve={}, fav_food={},\
        fav_drink={}, fav_restaurant={}, sports_team={}, fav_brand={},\
        other_fav={}, convo={}, trait={}>".format(
        self.id, self.first_name, self.last_name, self.created_date,
        self.relatp_type, self.user_id, self.rcmdn_list, self.email, self.bday,
        self.phone, self.work, self.edu, self.fb, self.linked_in, self.twitter,
        self.google_plus, self.github, self.pinterest, self.word_press,
        self.yelp, self.skype, self.other_social_media, self.gift_idea,
        self.goal, self.note, self.pet, self.family, self.hobby, self.likes,
        self.dislike, self.pet_peeve, self.fav_food, self.fav_drink,
        self.fav_restaurant, self.sports_team, self.sports_team, self.fav_brand,
        self.other_fav, self.convo, self.trait)


class RecommendationRelationship(db.Model):
    """Association table between recommendation and relationship table.

    Describes the method of reaching out that's tied to each contact.
    """

    __tablename__ = "rcmdns_relatps"

    rcmdnRelatp_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)

    rcmdn_id = db.Column(db.Integer,
                         db.ForeignKey('recommendations.id'),
                         nullable=False)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.id'),
                          nullable=False)


def example_data():
    """This function exists to populate testable data in the database.

    It is safer to test a sample database instead of testing an apps actual
    database."""

    user = User(id=1,
                first_name='Gabriel',
                last_name='Macht',
                email='gabriel@gmail.com',
                password='gabriel#1')

    recommendation = Recommendation(relatp_type='fr',
                                    rcmdn='Send a text')

    friend = Relationship()

    db.session.add(user)
    db.session.commit()


# This set up allows my app the ability to talk to SQLite, PostgreSQL, MySQL
# among others.

##########################
#### Helper Functions ####
##########################

# When running my actual db, db_uri="postgresql:///contacts".
# For testing purposes, db_uri="postgresql:///testdb".
def connect_to_db(app, db_uri="postgresql:///contacts"):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    from server import app
    connect_to_db(app)
    print "Connected to DB."
