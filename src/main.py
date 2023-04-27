from meal_mate_functions import view_ingr, add_ingr, remove_ingr, staple_view_ingr, staple_edit_ingr
from search_functions import get_recipes
from colored import fg, bg, attr  # https://pypi.org/project/colored/
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
# c = canvas.Canvas('ex.pdf')
# c.drawImage('ar.jpg', 0, 0, 10*cm, 10*cm)
# c.showPage()
# c.save()  # https://www.reportlab.com/docs/reportlab-userguide.pdf
# https://stackoverflow.com/questions/2252726/how-to-create-pdf-files-in-python
import time

print(f"{fg(64)}Welcome to Meal Mate{attr(0)} \n{fg(18)}'The recipe finder for your pantry items you don't know what to with!' {attr(0)}")

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
Bay Leaves,True
Parsley,True
Thyme,True
Chilli Powder,True
Ground Cumin,True
Smoked Paprika,True
Turmeric,True
Cinnamon,True
Curry Powder,True
Honey,True
Garlic,True
Onion,True
Ginger,True""")
    staple_file.close()


def create_menu():
    print(f"{bg(5)}Pantry items{attr(0)}")
    print(f"{fg(28)}1.{attr(0)} to {fg(28)}view{attr(0)} you ingredient list")
    print(f"{fg(2)}2.{attr(0)} to {fg(2)}add{attr(0)} a new item to your list")
    print(f"{fg(1)}3.{attr(0)} to {fg(1)}remove{attr(0)} item from your list")
    print(f"{bg(50)}Staple items ie. salt, pepper, oil, vinegar{attr(0)}")
    print(f"{fg(28)}4.{attr(0)} to {fg(28)}view{attr(0)} you ingredient list")
    print(f"{fg(90)}5.{attr(0)} to {fg(90)}adjust{attr(0)} an item on your list")
    print(f"{bg(90)}Search{attr(0)}")
    print(f"{fg(111)}6.{attr(0)} to {fg(111)}search{attr(0)} for recipes")
    print(f"{fg(4)}Exit{attr(0)}")
    print(f"{fg(2)}7.{attr(0)} to {fg(2)}exit{attr(0)}")
    # local variable
    choice = input("Enter your selection: ")
    return choice


# global variable
user_choice = ""

while user_choice != "7":
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
            get_recipes(ingr_file_name, staple_file_name)
        case "7":
            continue
        case _:
            print(f"{bg(1)}Invalid input{attr(0)}\n")
            time.sleep(1)
            continue

    input(f"{bg(177)}Press Enter to continue...{attr(0)}\n")

print(f"{bg(2)}Thank you for using Meal Mate{attr(0)}")
