'''Flask web application for digital recipe generator'''
from flask import Flask
from ProductionCode.random_recipe import get_random_recipes
import ProductionCode.data as data_module

app = Flask(__name__)

def load_recipe_data():
    """
    This function imports the `get_data` function from the `ProductionCode.data` module
    to retrieve the recipe data. The import is performed inside the function to avoid
    potential circular import issues. The function also skips the header of the data
    before returning it.
    """
    recipe_data = data_module.get_data()
    print("Loaded Recipe Data:", recipe_data)  # For debugging
    return recipe_data

@app.route('/')
def homepage():
    ''' This function returns the homepage of the application. 
    It provides an introduction to Flavor Finder and  instructions on how to use the 
    app to discover random recipes by specifying a number in the URL.'''
    return"""
   <h1>Welcome to Flavor Finder, your Digital Recipe Generator!</h1>
   <p>This is the Homepage. To discover a random recipe, simply use the URL format '/random/n', where <em>n</em> is a number of desired recipes between 1 and 10.</p>
   <p>For example, use '/random/2' to view two randomly generated recipes.</p>
"""

@app.route('/random/<num_recipes>')
def random_recipes(num_recipes):
    '''Function returns random recipes from recipe_data.csv'''
    try:
        num_recipes = int(num_recipes)
    except ValueError:
        return "Sorry, wrong format. Do this instead: /random/3", 400

    if num_recipes < 1 or num_recipes > 10:
        return "Please enter a number between 1 and 10.", 400

    recipe_data = load_recipe_data()
    randrecipes = get_random_recipes(recipe_data, num_recipes)
    if not randrecipes:
        return "No recipes found."

    output = ""
    for recipe in randrecipes:
        output += f"<b>{recipe[1]}</b>: {recipe[2]}<br><br>"
    return f"Returning {num_recipes} random recipes...<br><br>{output}"


@app.errorhandler(404)
def page_not_found():
    '''Handles 404 errors by returning a custom error message.''' 
    return "Sorry, wrong format. Do this instead: /random/number_of_recipes"

@app.errorhandler(500)
def python_bug(e):
    '''Handles internal server errors (HTTP 500) by returning a formatted error message.'''
    return f"A bug occurred! Simulated error. {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
