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
from flask.ext.sqlalchemy import SQLAlchemy

from sendnotif import *
from model import connect_to_db, db, User, Recommendation, Relationship

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
@app.route('/login', methods=['GET', 'POST'])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    email = request.form.get('email')
    password = request.form.get('password')

    return render_template('login_form.html')


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

    email_exists = db.session.query(User).filter_by(email=email).first()

    if email_exists is None:
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
    else:
        flash('Email taken.')
        return redirect('/register')

    return render_template('registration_success.html',
                           first_name=first_name,
                           email=email)


# route that my emails will be sent from
@app.route('/send_email')
def send_email():

    user = User.query.get(session['user_id'])

    send_event_notification(user.first_name, user.email)

    return "Success!"


@app.route('/add-contacts')
def add_contacts():
    """User manually adds contacts and categorizes them as friend, family, or
    professional contact."""

    return render_template("add_contact.html")


@app.route('/contact-added', methods=['POST'])
def contact_added():
    """Confirmation page that user has been added."""

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    relatp = request.form.get('relatp')

    relatp_type = ''

    if relatp == 'friend':
        relatp_type = 'fr'
    elif relatp == 'family':
        relatp_type = 'fam'
    else:
        relatp_type = 'prf'

    new_contact = Relationship(first_name=first_name, last_name=last_name, relatp_type=relatp_type)
    db.session.add(new_contact)
    db.session.commit()

    return render_template("contact_added.html",
                           first_name=first_name,
                           last_name=last_name,
                           relatp_type=relatp_type)


@app.route("/methods-of-reaching-out")
def methods_of_reaching_out():
    """User can select methods of reaching out from a list."""

    recommendations = db.session.query(Recommendation).all()
    return """<p>{}</p>""".format(recommendations)
    # return render_template('reach_out.html')


@app.route('/landing-page')
# @login_required
def landing_page():
    """Page where users land after logging in or signing up."""

    return render_template('landing_page.html')


@app.route('/contact-display')
def contact_display():
    """Display a selected contacts profile."""

    return render_template('contact_display.html')


@app.route('/event_display')
def event_display():
    """Display a selected contacts profile."""

    return render_template('event_display.html')


@app.route('/logout')
def process_logout():
    """Log user out."""

    session.pop('username', None)
    flash("Logged out.")
    return render_template('logout.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('page_not_found.html'), 404

# @app.context_processor
# def template_extras():
#     return dict(
#         google_analytics_id=app.config.get('GOOGLE_ANALYTICS_ID', None))


# @login_failed.connect_via(app)
# def on_login_failed(sender, provider, oauth_response):
#     app.logger.debug('Social Login Failed via %s; '
#                      '&oauth_response=%s' % (provider.name, oauth_response))

#     # Save the oauth response in the session so we can make the connection
#     # later after the user possibly registers
#     session['failed_login_connection'] = \
#         get_connection_values_from_oauth_response(provider, oauth_response)

#     raise SocialLoginError(provider)


# @app.errorhandler(SocialLoginError)
# def social_login_error(error):
#     return redirect(
#         url_for('register', provider_id=error.provider.id, login_failed=1))


# @app.route('/register', methods=['GET', 'POST'])
# @app.route('/register/<provider_id>', methods=['GET', 'POST'])
# def register(provider_id=None):
#     if current_user.is_authenticated():
#         return redirect(request.referrer or '/')

#     form = RegisterForm()

#     if provider_id:
#         provider = get_provider_or_404(provider_id)
#         connection_values = session.get('failed_login_connection', None)
#     else:
#         provider = None
#         connection_values = None

#     if form.validate_on_submit():
#         ds = current_app.security.datastore
#         user = ds.create_user(email=form.email.data, password=form.password.data)
#         ds.commit()

#         # See if there was an attempted social login prior to registering
#         # and if so use the provider connect_handler to save a connection
#         connection_values = session.pop('failed_login_connection', None)

#         if connection_values:
#             connection_values['user_id'] = user.id
#             connect_handler(connection_values, provider)

#         if login_user(user):
#             ds.commit()
#             flash('Account created successfully', 'info')
#             return redirect(url_for('profile'))

#         return render_template('thanks.html', user=user)

#     login_failed = int(request.args.get('login_failed', 0))

#     return render_template('register.html',
#                            form=form,
#                            provider=provider,
#                            login_failed=login_failed,
#                            connection_values=connection_values)



    # return render_template('profile.html',
    #                        google_conn=social.google.get_connection())


# @app.route('/profile/<provider_id>/post', methods=['POST'])
# @login_required
# def social_post(provider_id):

#     access_token = request.form.get('message', None)
#     print access_token
    # return redirect(url_for('profile'))



# # html that app.route should be the outermost decorator.
# @app.route('/needs_credentials')
# @oauth2.required
# def example():
#     # http is authorized with the user's credentials and can be used
#     # to make http calls.
#     http = oauth2.http()

# @app.route('/info')
# @oauth2.required
# def info():
#     return "Hello, {} ({})".format(oauth2.email, oauth2.user_id)

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
