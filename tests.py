import unittest
from model import User, Relationship, Recommendation, Event, db, connect_to_db, example_data
from server import app


class AppTests(unittest.TestCase):
    """Integration tests to check that the app is working properly."""

    def setUp(self):
        """Method called before each test."""

        # Flask's test client is instantiated.
        self.client = app.test_client()

        # Flask's TESTING configuration variable is set so that any Flask error
        # will be printed in the same console as the tests. This makes it
        # easy to debug any errors that occur during tests.
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        # Required configuration for apps that use sessions.
        app.config['SECRET_KEY'] = 'key'

        # Assigns the test client a user_if of 1.
        # Useful for testing the parts of my app that require login.
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_homepage(self):
        """Tests that the homepage displays."""

        # Test client grabs my homepage route.
        result = self.client.get('/')

        # Asserts that the page loads fine, i.e., the HTTP response is OK.
        self.assertEqual(result.status_code, 200)

        # Asserts that the words "Facebook" appear on my page.
        # 'result.data' is the response string.
        self.assertIn("Facebook", result.data)

    def test_login(self):
        # 'data' is a dictionary of form key/value pairs.
        # follow_redirects should needs to be set to True so that the
        # self.client.post call won't give back the redirection result to
        # itself.
        result = self.client.post("/login",
                                  data={'email': 'harvey@gmail.com', 'password': 'blah'},
                                  follow_redirects=True)
        self.assertIn("Login successful!", result.data)


class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

if __name__ == "__main__":
    unittest.main()
