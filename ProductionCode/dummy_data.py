import csv

# Dummy function to simulate loading the data from a CSV file
def load_recipes_data():
    # Simulating a CSV data structure (you'd typically load this from a file)
    recipes_data = [
        {
            "id": "recipe1",
            "title": "Miso-Butter Roast Chicken With Acorn Squash Panzanella",
            "instructions": "Pat chicken dry with paper towels, season all over with 2 tsp. salt...",
            "ingredients": [
                '1 (3½–4-lb.) whole chicken', '2¾ tsp. kosher salt, divided, plus more', '2 small acorn squash (about 3 lb. total)',
                '2 Tbsp. finely chopped sage', '1 Tbsp. finely chopped rosemary', '6 Tbsp. unsalted butter, melted, plus 3 Tbsp. room temperature'
            ]
        },
        {
            "id": "recipe2",
            "title": "Crispy Salt and Pepper Potatoes",
            "instructions": "Preheat oven to 400°F and line a rimmed baking sheet with parchment...",
            "ingredients": [
                '2 large egg whites', '1 pound new potatoes (about 1 inch in diameter)', '2 teaspoons kosher salt',
                '¾ teaspoon finely ground black pepper', '1 teaspoon finely chopped rosemary'
            ]
        }
    ]
    return recipes_data
