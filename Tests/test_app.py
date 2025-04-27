import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    def test_homepage(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b'Hello, this is the homepage. Use \'/recipe/<recipe_id>\' to view a recipe.', response.data)

    def test_get_recipe_valid(self):
        self.app = app.test_client()
        response = self.app.get('/recipe/1', follow_redirects=True)
        self.assertIn(b'Miso-Butter Roast Chicken', response.data)  # Checks if the recipe title is present

    def test_get_recipe_invalid(self):
        self.app = app.test_client()
        response = self.app.get('/recipe/10', follow_redirects=True)  # Invalid ID
        self.assertEqual(b'Invalid recipe ID.', response.data)