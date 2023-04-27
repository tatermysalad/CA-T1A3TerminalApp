import requests  # https://pypi.org/project/requests/
from colored import fg, bg, attr
import time
import random
import pdfkit


def get_recipes(ingr_file_name, staple_file_name):
    p = ""  # pantry + staples
    with open(ingr_file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            p = p + row[0] + ","
    with open(staple_file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if row[1] == "True":
                p = p + row[0] + ","
    print(f'{fg(111)}Searching for recipes with {len(p.split(","))} items{attr(0)}')
    r = requests.get(
        'https://api.spoonacular.com/recipes/findByIngredients?apiKey=3e06d892f3044bab8b766176ccd0e18c&ingredients=' + p)
    # r.headers['content-type'] = 'application/json; charset=utf8'
    json = r.json()
    i = 0
    if len(json) > 0:
        for recipe in json:
            if recipe["usedIngredientCount"] == len(p.split(",")):
                print(
                    f'{fg(random.randrange(0,256))}{i}. {recipe["title"]} contains all of your ingredients!{attr(0)}')
                i += 1
            else:
                if i < 1:
                    print(
                        f"{bg(1)}Here are some recipes which may require a trip to the shops{attr(0)}")
                    time.sleep(2)
                    i += 1
                print(
                    f'{fg(random.randrange(0,256))}{i}. {recipe["title"]}{attr(0)}')
                print(
                    f'Utilises: {recipe["usedIngredientCount"]} items, Requires: {recipe["missedIngredientCount"]} items')
                i += 1
                time.sleep(0.1)
    elif len(json) == 0:
        print("No recipes found\nPlease use remove some ingredients or consider changing the prioritisation")
        return

    def search_menu():
        print(f'{bg(random.randrange(0, 256))}Recipe options{attr(0)}')
        print(
            f"{fg(random.randrange(0,256))}1. View more details{attr(0)} about a recipe")
        print(f"{fg(random.randrange(0,256))}2. Export{attr(0)} a recipe")
        print(f"{bg(1)}Exit{attr(0)}")
        print(f"{fg(1)}3.{attr(0)} to {fg(1)}exit{attr(0)}")
        # local variable
        choice = input("Enter your selection: ")
        return choice

    def recipe_menu(json):
        try:
            recipe_int = int(input(
                "Press q to return to search options menu\nView more details about which recipe: "))
            recipe_id = json[recipe_int - 1]["id"]
            return requests.get(
                'https://api.spoonacular.com/recipes/' + recipe_id + '/information?apiKey=3e06d892f3044bab8b766176ccd0e18c&ingredients=')
        except ValueError:
            return

    def recipe_export(recipe_menu):
        pass

    def specific_recipe(recipe_menu):
        recipe_item = requests.get(
            'https://api.spoonacular.com/recipes/' + recipe_menu + '/information?apiKey=3e06d892f3044bab8b766176ccd0e18c&ingredients=')
    # r.headers['content-type'] = 'application/json; charset=utf8'
    json = r.json()
    search_choice = ""
    while search_choice != "3":
        search_choice = search_menu()
        match search_choice:
            case "1":
                recipe_menu(json)
            case "2":
                pass
            case "3":
                continue
        input(f"{bg(177)}Press Enter to continue...{attr(0)}\n")
