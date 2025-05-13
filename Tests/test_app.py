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
        '''Verify behavior when the random input is too small.'''
        response = self.client.get('/random/0')
        self.assertIn(b"Please enter a number between 1 and 10.", response.data)

    def test_random_input_too_large(self):
        '''Verify behavior when the random input is too large.'''
        response = self.client.get('/random/11')
        self.assertIn(b"Please enter a number between 1 and 10.", response.data)

    def test_invalid_input_format(self):
        '''Verify behavior when the input format is invalid.'''
        response = self.client.get('/random/abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)

    def test_500_error(self):
        '''Verify behavior when a 500 error occurs.'''
        with patch('ProductionCode.data.get_data', side_effect=Exception("Simulated error")):
            response = self.client.get('/random/1')
            self.assertEqual(response.status_code, 500)
            self.assertIn(b"A bug occurred! Simulated error.", response.data)

    def test_random_valid_input(self):
        '''Verify behavior with a valid random input.'''
        fake_data = [
            ['ID', 'Name', 'Description'],  # header
            ['1', 'Pizza', 'Cheesy delight'],
            ['2', 'Pasta', 'Italian classic'],
            ['3', 'Salad', 'Fresh and crispy'],
        ]
        with patch('ProductionCode.data.get_data', return_value=fake_data):
            with patch('ProductionCode.random_recipe.get_random_recipes',
                       return_value=fake_data[1:3]):
                response = self.client.get('/random/2')
                self.assertEqual(response.status_code, 200)
                self.assertIn(b"Returning 2 random recipes", response.data)
                self.assertIn(b"Pizza", response.data)

    def test_404_error(self):
        '''Verify custom 404 error handler.'''
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Sorry, wrong format. Do this instead", response.data)


if __name__ == '__main__':
    unittest.main()
