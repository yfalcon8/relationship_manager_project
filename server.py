"""My web app's online structure."""

# Jinja is a popular template system for Python, used by Flask.
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension

from sendnotif import *

# Instantiates Flask.
app = Flask(__name__)

# Required to use Flask sessions and the debug DebugToolbarExtension
app.secret_key = "ILoveStephenColbert"

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined


# @app.route('/') is a Python decorator. '/' in the decorator maps directly
# to the URL the user requested which is the homepage.
@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


# Tells Flask, "When you receive the request http://server/login, call the
# login function."
@app.route('/login')
def login():
    """Page where existing user inputs login info."""

    return render_template('login_form.html')


@app.route('/login', methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    email = request.form.get('email')
    password = request.form.get('password')

    user = db.session.query(User).filter_by(email=email).one()

    # user = customers.get_by_email(email)

    # if not user:
    #     flash("That email does not exist in the database.")
    #     return redirect('/login')

    # if user.password != password:
    #     flash("Incorrect password.")
    #     return redirect("/login")

    # session["logged_in_customer_email"] = user.email
    # flash("Logged in.")
    # return redirect("/melons")


@app.route('/register')
def register():
    """Page where users registers for my app."""

    return render_template('registration_form.html')
# class SocialLoginError(Exception):
#     def __init__(self, provider):
#         self.provider = provider

@app.route('/send_email')
def send_email():

    user = User.query.get(session['user_id'])

    send_event_notification(user.first_name, user.email)

    return "Success!"


@app.route('/add_contacts')
def add_contacts():
    """User manually adds contacts and categorizes them as friend, family, or
    professional contact."""

    return render_template('add_contact.html')


@app.route("/methods_of_reaching_out")
def methods_of_reaching_out():
    """User can select methods of reaching out from a list."""

    return render_template('reach_out.html')


@app.route('/landing_page')
# @login_required
def landing_page():
    """Page where users land after logging in or signing up."""

    return render_template('landing_page.html')


@app.route('/contact_display')
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

    # del session["logged_in_customer_email"]
    # flash("Logged out.")
    return render_template('logout.html')




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

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # fsocial.init_app(app)

    # Port 5000 required for vagrant.
    # debug=True runs Flask in "debug mode". It will reload my code when it
    # changes and provide error messages in the browser.
    app.run(debug=True, host='0.0.0.0', port=5000)
