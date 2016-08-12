"""My web app's online structure."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, redirect, session, current_app, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Connection

import os


# from flask.ext.social import Social, SQLAlchemyConnectionDatastore, login_failed
# from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
# from flask.ext.social.utils import get_provider_or_404, get_connection_values_from_oauth_response
# from flask.ext.social.views import connect_handler
# from flask.ext.sqlalchemy import SQLAlchemy

# from flask.ext.security import LoginForm, current_user, login_required, login_user, Security, SQLAlchemyUserDatastore

# from flask.ext.assets import Environment

# Instantiates Flask.
app = Flask(__name__)

# Required to use Flask sessions and the debug DebugToolbarExtension
app.secret_key = "ILoveStephenColbert"

# app.config['SOCIAL_GOOGLE'] = 'client_secrets.sh'

# app.config['SOCIAL_GOOGLE'] = {
#     'consumer_key': os.environ.get('GOOGLE_OAUTH2_CLIENT_ID'),
#     'consumer_secret': os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')
# }

# security_ds = SQLAlchemyUserDatastore(db, models.User, models.Role)
# social_ds = SQLAlchemyConnectionDatastore(db, models.Connection)

# app.security = Security(app, security_ds)
# app.social = Social(app, social_ds)

# fsocial = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

# app.config['SECRET_KEY'] = 'your-secret-key'

# REDIRECT_URI = '/import_contacts'

# oauth2 = UserOAuth2(app)

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined

# gd_client = gdata.contacts.client.ContactsClient(source='contacts')


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/login')
def login():
    """Page where users sign-in with oAuth from Google."""

    # if current_user.is_authenticated():
    #     return redirect(request.referrer or '/')

    # return render_template('login.html', form=LoginForm())
    return render_template('login_form.html')


@app.route('/register')
def register():
    """Page where users registers for my app."""

    return render_template('registration_form.html')
# class SocialLoginError(Exception):
#     def __init__(self, provider):
#         self.provider = provider


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


@app.route('/landing_page')
# @login_required
def landing_page():
    """Page where users land after logging in or signing up."""

    return render_template('landing_page.html')
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


if __name__ == "__main__":
    # Setting this to be true so that I can invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # fsocial.init_app(app)

    # port 5000 required for vagrant
    app.run(debug=True, host='0.0.0.0', port=5000)
