#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = None
    for item in recipe:
        if item not in ingredients:
            return 0
        else:
            batches = ingredients[item] // recipe[item]
            if batches == 0:
                return 0
            elif max_batches is None or max_batches > batches:
                max_batches = batches
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(f"{recipe_batches(recipe, ingredients)} batches can be made from the"
          + f" available ingredients: {ingredients}.")
