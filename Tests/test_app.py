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
            b"In the url after the /, enter the word random, then a /, "
            b"followed by a number between 1 and 10. "
            b"This will return that many random recipes from the dataset. "
            b"For example: /random/3 will return 3 random recipes."
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
