import csv
import requests  # https://pypi.org/project/requests/
from colored import fg, bg, attr


def add_ingr(file_name):
    print(f"{fg(2)}Add item{attr(0)}")
    ingr_title = input("Enter your ingredient: ")
    with open(file_name, "a") as ingr_file:
        writer = csv.writer(ingr_file)
        writer.writerow([ingr_title, "False"])


def remove_ingr(file_name):
    print(f"{fg(1)}Remove item{attr(0)}")
    view_ingr(file_name)
    ingr_title = input("Enter the ingredient that you want to remove: ")
    ingr_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (ingr_title != row[0]):
                ingr_lists.append(row)
    # print(ingr_lists[1:])
    # We will write that down in the file again
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(ingr_lists)
    view_ingr(file_name)
    


def prior_ingr(file_name):
    print(f"{fg(90)}Mark item to prioritise{attr(0)}")
    view_ingr(file_name)
    ingr_title = input("Enter the item that you want to prioritise for use")
    ingr_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (ingr_title == row[0]):
                ingr_lists.append([row[0], "True"])
            else:
                ingr_lists.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(ingr_lists)
    view_ingr(file_name)


def view_ingr(file_name):
    print(f"{fg(28)}View items{attr(0)}") # dark green color
    with open(file_name, "r") as f: 
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if row[1] == "True":
                print(f"{row[0]} {fg(58)}(prioritised){attr(0)}") # orange 
            else:
                print(f"{row[0]}")




def get_recipes(file_name):
    print(f"{fg(111)}Searching for recipes...{attr(0)}")
    c = ""
    prior = ""
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            c = c + row[0] + ","
            if row[1] == "True":
                prior = prior + row[0] + ","
                print(prior)
        
    r = requests.get(
        'https://api.edamam.com/api/recipes/v2?type=public&q=' + c + '&app_id=fbfe9bd1&app_key=0f3153405e76a862a72d02b718d7e722')
    # r.headers['content-type'] = 'application/json; charset=utf8'
    json = r.json()
    # recipes = []
    if len(json["hits"]) < 0:
        for recipe in json["hits"]:
            print(recipe["recipe"]["label"])
    else:
            r=requests.get(
        'https://api.edamam.com/api/recipes/v2?type=public&q=' + prior + '&app_id=fbfe9bd1&app_key=0f3153405e76a862a72d02b718d7e722')
            json = r.json()
            for recipe in json["hits"]:
                print(recipe["recipe"]["label"])
            print("no recipes found")

    # print(recipes)
        