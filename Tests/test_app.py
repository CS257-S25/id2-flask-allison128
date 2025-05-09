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
        expected_partial = b"Welcome to Flavor Finder"
        self.assertIn(expected_partial, response.data)

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
