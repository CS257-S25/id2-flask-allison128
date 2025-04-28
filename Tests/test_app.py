'''Test suite for the Flask application routes.'''

import unittest
from app import app

class FlaskRouteTests(unittest.TestCase):
    '''Test suite for the routes in the Flask application.'''

    def setUp(self):
        '''Set up the test client for the Flask application.'''
        self.client = app.test_client()

    def test_homepage_content(self):
        '''Verify the content of the homepage route.'''
        response = self.client.get('/')
        expected_content = (
            b"Welcome to Flavor Finder, your Digital Recipe Generator!"
            b"This is the Homepage. To discover a random recipe, simply use the URL format '/random/n', where <em>n</em> is a number of desired recipes between 1 and 10."
            b"Foror example, use '/random/2' to view two randomly generated recipes."
        )
        self.assertIn(expected_content, response.data, "Homepage content " \
        "should match the expected text.")

    def test_invalid_input_handling(self):
        '''Test handling of invalid input on the random recipes route.'''
        # Test case for non-numeric input
        response = self.client.get('/random/abc', follow_redirects=True)
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)
        # Test case for negative number input
        response = self.client.get('/random/-1', follow_redirects=True)
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)
