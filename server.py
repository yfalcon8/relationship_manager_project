"""My web app's online structure."""

#################
#### imports ####
#################

# Jinja is a popular template system for Python, used by Flask.
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, session, flash, redirect
# Flask: A class that we import. An instance of this class will be the
# WSGI application.
# session: A Flask object (class) that allows you to store information specific to a
# user from one request to the next. It's a dictionary that preserves type.
# It is a customized cookie.

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Recommendation, Relationship, Event

import arrow

#######################
#### configuration ####
#######################

# Instantiates Flask. "__name__" is a special Python variable for the name of
# the current module. This is needed so that Flask knows where to look for
# templates, static files, and so on.
app = Flask(__name__)

# Required to use Flask sessions and the debug DebugToolbarExtension. The user could look at
# the contents of your cookie but not modify it, unless they know the secret key
# used for signing.
app.secret_key = "ILoveStephenColbert"
# Another way of generating a secret key:
# >>>import os
# >>>os.urandom(24)

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined


# @app.route('/') is a Python decorator. '/' in the decorator maps directly
# to the URL the user requested which is the homepage. The index function
# is triggered when the URL is visited.
@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


# GET: The browser tells the server to just get the information stored on
# that page and send it.
# POST: The browser tells the server that it wants to post some new
# information to that URL and that the server must ensure the data is stored and
# only stored once. This is how HTML forms usually transmit data to the server.
@app.route('/login')
def display_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def handle_login():
    """Process login."""

    # Add email and password to the dictionary 'form'
    email = request.form['email']
    password = request.form['password']

    # Check to see if the email is in the database.
    user = User.query.filter_by(email=email).first()

    # If it doesn't, redirect them to the login page.
    if not user:
        flash("That user does not exist.")
        return redirect("/")

    # If the password doesn't match the email, let the user know.
    if user.password != password:
        flash("Incorrect password.")
        return redirect("/")

    # Grab the user_id and assign it to the session dictionary.
    session["user_id"] = user.id

    # Take the user to the landing page when their login credentials match.
    flash("Login successful!")
    return redirect("/landing-page/{}".format(user.id))


@app.route('/register')
def register():
    """Page where users registers for my app."""

    return render_template('registration_form.html')


@app.route('/registration-success', methods=['POST'])
def registration_success():
    """Inform new user that they've been added."""

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    # Add the user as long as the email isn't already taken.
    email_exists = db.session.query(User).filter_by(email=email).first()

    if email_exists is None:
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    else:
        flash("Email {} is taken.".format(email))
        return redirect('/register')

    # Grab the id of the user that just signed in.
    user_id = db.session.query(User.id).filter_by(email=email).first()[0]

   # Add the user to the session.
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    session["user_id"] = user.id

    return render_template('registration_success.html',
                           first_name=first_name,
                           email=email,
                           user_id=user_id)


@app.route('/add-contacts/<int:user_id>')
def add_contacts(user_id):
    """User manually adds contacts and categorizes them as friend, family, or
    professional contact."""

    return render_template("add_contact.html",
                           user_id=user_id)


@app.route('/contact-added/<int:user_id>', methods=['POST'])
def contact_added(user_id):
    """Confirmation page that user has been added."""

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    relatp = request.form.get('relatp')

    relatp_type = ''

    # Change the relapt_type to match the table it will be committed to.
    if relatp == 'friend':
        relatp_type = 'fr'
    elif relatp == 'family':
        relatp_type = 'fam'
    else:
        relatp_type = 'prf'

    # Add the new contact to the db.
    new_contact = Relationship(user_id=user_id, first_name=first_name, last_name=last_name, relatp_type=relatp_type)
    db.session.add(new_contact)
    db.session.commit()

    # Grab the id of the relationship that was just created.
    new_contact_info = db.session.query(Relationship.id).filter_by(user_id=user_id, first_name=first_name, last_name=last_name, relatp_type=relatp_type).all()[0][0]

    return render_template("contact_added.html",
                           first_name=first_name,
                           last_name=last_name,
                           relatp=relatp,
                           user_id=user_id,
                           relatp_id=new_contact_info)


@app.route('/methods-of-reaching-out/<int:user_id>/<int:relatp_id>')
def specify_methods_of_reaching_out(user_id, relatp_id):
    """User can select methods of reaching out from a list."""

    # Given the relatp_id, grab the relationship type (friend, family, or professional).
    relatp_type = db.session.query(Relationship.relatp_type).filter_by(id=relatp_id).all()[0][0]

    # Grab the recommendation list associated with the relationship type.
    rcmdn_list = db.session.query(Recommendation).filter_by(relatp_type=relatp_type).all()

    return render_template('reach_out.html',
                           user_id=user_id,
                           relatp_id=relatp_id,
                           rcmdn_list=rcmdn_list)


@app.route('/methods-success/<int:user_id>/<int:relatp_id>', methods=['POST'])
def method_specification_success(user_id, relatp_id):
    """Add the methods specified to the relationship."""

    # Grab the recommendation list specified for the relationship.
    desired_list = request.form.getlist('rcmdn')

    # Add the customized list to the respective relationship.
    update_relatp = Relationship.query.filter_by(user_id=user_id, id=relatp_id).first()
    update_relatp.rcmdn_list = desired_list

    # The created_at column should be placed in the Relationship table.
    created_at = db.session.query(Relationship.created_date).filter_by(id=relatp_id).one()

    # Turn the query result (a tuple) into an Arrow friendly format.
    arrow_created_at = arrow.get(created_at[0])

    # The start date of all events will be a month from the date he/she was added.
    start_date = arrow_created_at.replace(months=+1)

    # Events will be scheduled for a max of a year for demo purposes.
    yr_from_now = start_date.replace(years=+1)

    # Create events for the duration of the year.
    # Friends and family should have an event a month.
    # Professional contacts should have an event per quarter.
    while start_date < yr_from_now:

        for desired_item in desired_list:

            if update_relatp.relatp_type == 'fr' or update_relatp.relatp_type == 'fam':

                # Convert from arrow format to datetime format for db storage.
                new_event = Event(user_id=user_id, relatp_id=relatp_id, rcmdn=desired_item, scheduled_at=start_date.datetime)
                db.session.add(new_event)

                start_date = start_date.replace(months=+1)

            else:
                new_event = Event(user_id=user_id, relatp_id=relatp_id, rcmdn=desired_item, scheduled_at=start_date.datetime)
                db.session.add(new_event)

                start_date = start_date.replace(months=+4)

    db.session.commit()

    return render_template('reach_out_added.html',
                           user_id=user_id,
                           desired_list=desired_list)


@app.route('/landing-page/<int:user_id>')
def landing_page(user_id):
    """Page where users land after logging in or signing up."""

    # Display the name of all of the reltionships a user has.
    # A list of tuples are returned.
    # The relationships id will be used to create a link to their profile.
    # The user_id is needed in the query results to pass into my Jinja for loop.
    contact_name_and_id = db.session.query(Relationship.user_id, Relationship.id, Relationship.first_name, Relationship.last_name).filter_by(user_id=user_id).all()

    return render_template("landing_page.html",
                           user_id=user_id,
                           contact_name_and_id=contact_name_and_id)


@app.route('/contact-display/<int:user_id>/<int:relatp_id>')
def contact_display(user_id, relatp_id):
    """Display a selected contacts profile."""

    # Query for all the data related to a relationship.
    # Returns a list of objects.
    relatp_info = db.session.query(Relationship).filter_by(id=relatp_id).all()

    return render_template("contact_display.html",
                           user_id=user_id,
                           relatp_info=relatp_info)


@app.route('/event-display/<int:user_id>')
def event_display(user_id):
    """Display a selected contacts profile."""

    # Store all of a users events in a list.
    all_events = []

    # Grab the text and time of all of the users relationship.
    # Returns a list of tuples.
    rcmdn_and_date = db.session.query(Event.rcmdn, Event.scheduled_at, Event.relatp_id).filter_by(user_id=user_id).all()

    # Grab the name of the relationship.
    # Store the name, text, and time in the all_events list.
    for rcmdn in rcmdn_and_date:
        relatp_id = rcmdn.relatp_id
        relatp_name = db.session.query(Relationship.first_name, Relationship.last_name).filter_by(id=relatp_id).one()
        all_events.append([relatp_name.first_name, relatp_name.last_name, rcmdn[0], rcmdn[1].date()])

    return render_template("event.html",
                           user_id=user_id,
                           all_events=all_events)


@app.route('/logout')
def process_logout():
    """Log user out."""

    del session["user_id"]
    flash("Logged out.")
    return render_template('logout.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('page_not_found.html', 404)


# App will only run if we ask it to run.
if __name__ == "__main__":

    # Setting this to be true so that I can invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # debug=True runs Flask in "debug mode". It will reload my code when it
    # changes and provide error messages in the browser.
    # The host makes the server publicly available by adding 0.0.0.0. This
    # tells my operating system to listen on all public IPs.
    # Port 5000 required for Flask.
    app.run(debug=True, host='0.0.0.0', port=5000)
