'''Test suite for the Flask application routes.'''

import unittest
from unittest.mock import patch
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
            b"<h1>Welcome to Flavor Finder, your Digital Recipe Generator!</h1>"
            b"<p>This is the Homepage. To discover a random recipe, simply use the URL format '/random/n', where <em>n</em> is a number of desired recipes between 1 and 10.</p>"
            b"<p>For example, use '/random/2' to view two randomly generated recipes.</p>"
        )
        self.assertIn(expected_content, response.data, "Homepage content " \
        "should match the expected text.")

    def test_random_valid_input(self):
        with patch('ProductionCode.data.get_data', return_value=[["id", "title", "desc"], [1, "Pasta", "Yummy"], [2, "Soup", "Hot"]]):
            with patch('ProductionCode.random_recipe.get_random_recipes', return_value=[[1, "Pasta", "Yummy"]]):
                response = self.client.get('/random/1')
                self.assertIn(b"Returning 1 random recipes", response.data)
                self.assertIn(b"Pasta", response.data)

    def test_random_input_too_small(self):
        response = self.client.get('/random/0')
        self.assertIn(b"Please enter a number between 1 and 10.", response.data)

    def test_random_input_too_large(self):
        response = self.client.get('/random/11')
        self.assertIn(b"Please enter a number between 1 and 10.", response.data)

    def test_invalid_input_format(self):
        response = self.client.get('/random/abc')
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)

    def test_500_error(self):
        with patch('ProductionCode.data.get_data', side_effect=Exception("Simulated error")):
            response = self.client.get('/random/1')
            self.assertIn(b"A bug occurred! Simulated error", response.data)
