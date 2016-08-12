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

    bday = db.Column(db.Date,
                     nullable=False)

    def __repr__(self):
        return "<User: %s %s, %s, %s>" (self.first_name,
                                        self.last_name,
                                        self.email,
                                        self.bday)


class Recommendation(db.Model):
    """Stores information about my users."""

    __tablename__ = "recommendations"

    rcmdn_id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True)

    # The default is for those users who do not feel like specifying the type
    # relationship they have with the contact they just imported. There will
    # be a default set of tips on how to reach out.
    relatp_code = db.Column(db.Integer,
                            db.ForeignKey('relationships.relatp_code'),
                            default=100)

    rcmdn_text = db.Column(db.Text,
                           nullable=False,
                           unique=True)

    # Join the recommendation table and relationship table through the
    # relatp_code. This allows me to navigate from the a user's contact to his/her
    # associated recommendations and vice versa.
    relatp = db.relationship("Relationship", backref=db.backref("rcmdn"))


class Event(db.Model):
    """Stores information about each event."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    scheduled_at = db.Column(db.DateTime,
                             nullable=False)

    relatp_id = db.Column(db.Integer)

    rcmdn_text = db.Column(db.Text,
                           nullable=False)

    user = db.relationship('User', backref='event')


class Relationship(db.Model):
    """Stores all of a users' contacts info."""

    __tablename__ = "relationships"

    relatp_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)

    relatp_code = db.Column(db.Integer,
                            nullable=False,
                            default=100)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))

    email = db.Column(db.String(50))

    bday = db.Column(db.Date)

    phone = db.Column(db.String(15))

    work = db.Column(db.String(50))

    edu = db.Column(db.String(50))

    fb = db.Column(db.String(50))

    linked_in = db.Column(db.String(50))

    twitter = db.Column(db.String(50))

    google_plus = db.Column(db.String(50))

    meet_up = db.Column(db.String(50))

    github = db.Column(db.String(50))

    pinterest = db.Column(db.String(50))

    reddit = db.Column(db.String(50))

    word_press = db.Column(db.String(50))

    yelp = db.Column(db.String(50))

    youtube = db.Column(db.String(50))

    skype = db.Column(db.String(50))

    other_social_media = db.Column(db.String(50))


    user = db.relationship("User", backref=db.backref("relationships"))

    recommendation = db.relationship("Recommendation",
                                     secondary='rcmdns_relatps',
                                     backref=db.backref("relationship"))


class RecommendationRelationship(db.Model):
    """Association table between recommendation and relationship table.

    Describes the method of reaching out that's tied to each contact.
    """

    __tablename__ = "rcmdns_relatps"

    rcmdnRelatp_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)

    rcmdn_id = db.Column(db.Integer,
                         db.ForeignKey('recommendations.rcmdn_id'),
                         nullable=False)

    relatp_code = db.Column(db.Integer,
                            db.ForeignKey('relationships.relatp_code'),
                            default=100,
                            nullable=False)


class Gift_Idea(db.Model):
    """Separately stores each gift idea a user has for his/her contact."""

    __tablename__ = "gift_ideas"

    gift_idea_id = db.Column(db.Integer,
                             nullable=False,
                             primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    gift_idea = db.Column(db.Text)

    # The backref is pluralized as gift_ideas because I'm expecting a list of
    # gift_ideas back. This is a one-to-many relationship so I'll be getting
    # one contact back.
    relatp = db.relationship("Relationship", backref=db.backref("gift_ideas"))


class Goal(db.Model):
    """Separately stores each goal a user has for his/her contact."""

    __tablename__ = "goals"

    goal_id = db.Column(db.Integer,
                        nullable=False,
                        primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    goal = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("goals"))


class Note(db.Model):
    """Separately stores a note a user has for his/her contact.

    For example, 'Paige is planning a vacation to the Bahamas in July.'"""

    __tablename__ = "notes"

    note_id = db.Column(db.Integer,
                        nullable=False,
                        primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    note = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("notes"))


class Pet(db.Model):
    """Separately stores pets a users contact has."""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer,
                       nullable=False,
                       primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    pet = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("pets"))


class Family(db.Model):
    """Separately stores a family member a user has noted for his/her contact."""

    __tablename__ = "family"

    family_id = db.Column(db.Integer,
                          nullable=False,
                          primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    family = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("family"))


class Hobby(db.Model):
    """Separately stores each gift idea a user has for his/her contact."""

    __tablename__ = "hobbies"

    hobby_id = db.Column(db.Integer,
                         nullable=False,
                         primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    hobby = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("hobbies"))


class Like(db.Model):
    """Separately stores each like that a user has noted for his/her contact."""

    __tablename__ = "likes"

    like_id = db.Column(db.Integer,
                        nullable=False,
                        primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    likes = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("likes"))


class Dislike(db.Model):
    """Separately stores each dislike a user has noted for his/her contact."""

    __tablename__ = "dislikes"

    dislike_id = db.Column(db.Integer,
                           nullable=False,
                           primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    dislike = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("dislikes"))


class Pet_Peeve(db.Model):
    """Separately stores each pet peeve a user has noted for his/her contact."""

    __tablename__ = "pet_peeves"

    pet_peeve_id = db.Column(db.Integer,
                             nullable=False,
                             primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    pet_peeve = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("pet_peeves"))


class Favorite_Food(db.Model):
    """Separately stores each favorite food a user has noted for his/her contact."""

    __tablename__ = "fav_foods"

    fav_food_id = db.Column(db.Integer,
                            nullable=False,
                            primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    fav_food = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("fav_foods"))


class Favorite_Drink(db.Model):
    """Separately stores favorite drink a user has noted for his/her contact."""

    __tablename__ = "fav_drinks"

    fav_drink_id = db.Column(db.Integer,
                             nullable=False,
                             primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    fav_drink = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("fav_drinks"))


class Favorite_Restaurant(db.Model):
    """Separately stores each favorite restaurant a user noted about his/her contact."""

    __tablename__ = "fav_restaurants"

    fav_restaurant_id = db.Column(db.Integer,
                                  nullable=False,
                                  primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    fav_restaurant = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("fav_restaurants"))


class Favorite_Sports_Team(db.Model):
    """Separately stores each favorite sports team a user noted for his/her contact."""

    __tablename__ = "fav_sports_teams"

    fav_sports_team_id = db.Column(db.Integer,
                                   nullable=False,
                                   primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    sports_team = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("fav_sports_teams"))


class Favorite_Brand(db.Model):
    """Separately stores each favorite brand a user has noted for his/her contact."""

    __tablename__ = "fav_brands"

    fav_brand_id = db.Column(db.Integer,
                             nullable=False,
                             primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    fav_brand = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("fav_sports_teams"))


class Other_Favorites(db.Model):
    """Separately stores other favorites a user noted for his/her contact."""

    __tablename__ = "other_favs"

    other_favs_id = db.Column(db.Integer,
                              nullable=False,
                              primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    other_fav = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("other_favs"))


class Conversation_Log(db.Model):
    """Separately stores each notable conversation a user had with his/her contact."""

    __tablename__ = "convo_log"

    convo_log_id = db.Column(db.Integer,
                             nullable=False,
                             primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    convo = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("convo_log"))


class Trait(db.Model):
    """Separately stores each trait a user noted about his/her contact."""

    __tablename__ = "traits"

    trait_id = db.Column(db.Integer,
                         nullable=False,
                         primary_key=True)

    relatp_id = db.Column(db.Integer,
                          db.ForeignKey('relationships.relatp_id'))

    trait = db.Column(db.Text)

    relatp = db.relationship("Relationship", backref=db.backref("traits"))


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)





def connect_to_db(app):
    """Conenct the database to the Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///contacts'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    """This is useful for running this module interactively. This will leave me
    in a state of being able to work with the database directly."""

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
