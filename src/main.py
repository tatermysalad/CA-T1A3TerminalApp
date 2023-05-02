from meal_mate_functions import view_ingr, add_ingr, remove_ingr, staple_view_ingr, staple_edit_ingr, staple_ignore
from search_functions import get_recipes
from colored import fg, bg, attr  # https://pypi.org/project/colored/
import pdfkit
import time

print(f"\n{fg(64)}Welcome to Meal Mate{attr(0)} \n{fg(18)}'The recipe finder for your pantry items you don't know what to with!' {attr(0)}")

# Check if pantry_items.csv exists
ingr_file_name = "./pantry_list.csv"
staple_file_name = "./staple_list.csv"

try:
    ingr_file = open(ingr_file_name, "r")
    ingr_file.close()

except FileNotFoundError as e:
    ingr_file = open(ingr_file_name, "w")
    ingr_file.write("Ingredient\n")
    ingr_file.close()

try:
    staple_file = open(staple_file_name, "r")
    ingr_file.close()

except FileNotFoundError as e:
    staple_file = open(staple_file_name, "w")
    staple_file.write("""Staple,In_Stock
Olive oil,True
Vegetable oil,True
Vinegar,True
Salt,True
Pepper,True
Oregano,True
Parsley,True
Chilli Powder,True
Ground Cumin,True
Paprika,True
Cinnamon,True
Curry Powder,True
Garlic,True
Onion,True
Ginger,True""")
    staple_file.close()


def create_menu():
    print(f"\n{bg(5)}Pantry items{attr(0)}")
    print(f"{fg(28)}1.{attr(0)} to {fg(28)}view{attr(0)} you ingredient list")
    print(f"{fg(2)}2.{attr(0)} to {fg(2)}add{attr(0)} a new item to your list")
    print(f"{fg(1)}3.{attr(0)} to {fg(1)}remove{attr(0)} item from your list")
    print(f"\n{bg(58)}Staple items ie. salt, pepper, oil, vinegar{attr(0)}")
    print(f"{fg(28)}4.{attr(0)} to {fg(28)}view{attr(0)} you staple list")
    print(f"{fg(90)}5.{attr(0)} to {fg(90)}change{attr(0)} a staple item")
    print(f"{fg(104)}6. {attr(0)}to {fg(104)}ignore{attr(0)} staple items in search")
    print(f"\n{bg(90)}Search{attr(0)}")
    print(f"{fg(111)}7.{attr(0)} to {fg(111)}search{attr(0)} for recipes")
    print(f"\n{bg(4)}Exit{attr(0)}")
    print(f"{fg(2)}8.{attr(0)} to {fg(2)}exit{attr(0)}")
    # local variable
    choice = input("Enter your selection: ")
    return choice


# global variable
user_choice = ""

while user_choice != "8":
    user_choice = create_menu()

    match user_choice:
        case "1":
            view_ingr(ingr_file_name)
        case "2":
            add_ingr(ingr_file_name)
        case "3":
            remove_ingr(ingr_file_name)
        case "4":
            staple_view_ingr(staple_file_name)
        case "5":
            staple_edit_ingr(staple_file_name)
        case "6":
            staple_ignore_response = input(
                f"Use the staple items list in your search? (y/n): ")
            staple_setting = staple_ignore(staple_ignore_response)
            print(
                f"\nThe search function will now {fg(5)}{'use' if staple_setting else 'ignore'}{attr(0)} the staple list")
        case "7":
            try:
                get_recipes(ingr_file_name, staple_file_name, staple_setting)
            except NameError:
                get_recipes(ingr_file_name, staple_file_name, True)
        case "8":
            continue
        case _:
            print(f"{bg(1)}Invalid input{attr(0)}\n")
            time.sleep(1)
            continue

    input(f"\n{bg(177)}Press Enter to continue...{attr(0)}\n")

print(f"{bg(2)}Thank you for using Meal Mate{attr(0)}\n")
