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
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)

    def test_500_error(self):
        '''Verify behavior when a 500 error occurs.'''
        with patch('ProductionCode.data.get_data', side_effect=Exception("Simulated error")):
            response = self.client.get('/random/1')
            self.assertIn(b"A bug occurred! Simulated error.", response.data)

    def test_load_recipe_data_function(self, mock_get_data):
        '''Verify that load_recipe_data returns the expected data from get_data.'''
        mock_get_data.return_value = [
            ["id", "name", "description"], 
            [1, "Spaghetti", "Tasty Italian pasta"],
            [2, "Sushi", "Fresh seafood rolls"]
        ]
        from data.recipe_data_1 import recipe_data
        result = recipe_data()
        self.assertEqual(result, mock_get_data.return_value)
        mock_get_data.assert_called_once()
    
    def test_random_recipes_function(self):
        '''Verify that random_recipes returns the expected output.'''
        with patch('ProductionCode.random_recipe.get_random_recipes') as mock_get_random_recipes:
            mock_get_random_recipes.return_value = [
                [1, "Spaghetti", "Tasty Italian pasta"],
                [2, "Sushi", "Fresh seafood rolls"]
            ]
            response = self.client.get('/random/2')
            self.assertIn(b"Returning 2 random recipes...", response.data)
            self.assertIn(b"Spaghetti: Tasty Italian pasta", response.data)
            self.assertIn(b"Sushi: Fresh seafood rolls", response.data)
        
        
    def test_random_recipes_none_found(self, mock_load_data, mock_get_random):
        '''Verify behavior when no recipes are returned.'''
        mock_load_data.return_value = []
        mock_get_random.return_value = []
        response = self.client.get('/random/1')
        self.assertIn(b"No recipes found.", response.data)

    def test_404_error(self):
        '''Verify behavior when a 404 error occurs.'''
        response = self.client.get('/nonexistent_route')
        self.assertIn(b"Sorry, wrong format. Do this instead:", response.data)

if __name__ == '__main__':
    unittest.main()
    app.run(debug=True)
# This test suite uses the unittest framework to test the Flask application routes.
