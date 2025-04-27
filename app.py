import csv
import os
from flask import Flask
import unittest


app = Flask(__name__)
data = []


def load_data():
   # Path to the CSV file
   file_path = 'final_data.csv'
  
   if not os.path.exists(file_path):
       # File not found, using dummy data
       print(f"Warning: The file '{file_path}' was not found. Using hardcoded data instead.")
       data.append(["Recipe Title", "Instructions", "Cleaned Ingredients"])
       data.append(["Miso-Butter Roast Chicken", "Instructions", "Ingredients List"])
   else:
       # Read from the CSV file if it exists
       with open(file_path, newline='') as f:
           reader = csv.reader(f)
           next(reader) 
           for row in reader:
               data.append(row)


@app.route('/')
def homepage():
   return """
   <h1> Hello, Welcome to Flavor Finder, your Digital Recipe Generator!</h1>
   <p>This is the homepage. Use '/recipe/recipe_id' to view a recipe.</p>
   <p>For now, use '/recipe/1' to view recipe 1.</p>
   """


@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
   try:
       # Adjust for zero-based indexing (recipe_id 1 should be index 0, etc.)
       recipe = data[recipe_id - 1]  # Subtract 1 to match recipe_id with list index
       return f"<h1>{recipe[0]}</h1><p><strong>Title:</strong><br>{recipe[1]}</p><p>\
        <strong>Instructions:</strong><br>{recipe[2]}</p><strong>Ingredients:</strong><br>{recipe[3]}</p>"
   except IndexError:
       return "Invalid recipe ID."


@app.errorhandler(404)
def page_not_found(e):
   return "Sorry, wrong format, do this instead...."


@app.errorhandler(500)
def python_bug(e):
   return "Eek, a bug!"


# Load data on startup
load_data()


if __name__ == '__main__':
   app.run(debug=True)



