import requests  # https://pypi.org/project/requests/

print("Welcome to Meal Mate \n'The recipe finder for your pantry items you don't know what to with!'")

# Check if pantry_items.csv exists
file_name = "./pantry_list.csv"

try:
    meal_mate_file = open(file_name, "r")
    meal_mate_file.close()

except FileNotFoundError as e:
    meal_mate_file = open(file_name, "w")
    meal_mate_file.write("Ingredient,completed\n")
    meal_mate_file.close()

def get_recipes(ingr):
    r = requests.get(
        'https://api.edamam.com/api/recipes/v2?type=public&q=' + ingr + '&app_id=fbfe9bd1&app_key=0f3153405e76a862a72d02b718d7e722')  # , query={'app_id': 'fbfe9bd1', 'app_key': '0f3153405e76a862a72d02b718d7e722'})
    # r.headers['content-type'] = 'application/json; charset=utf8'
    return r.json()

print(get_recipes("meatball, chicken, pasta, lamb")["hits"][0]["recipe"]["label"])
