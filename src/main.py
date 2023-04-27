from meal_mate_functions import add_ingr, remove_ingr, prior_ingr, view_ingr, get_recipes
from colored import fg, bg, attr  # https://pypi.org/project/colored/
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
# c = canvas.Canvas('ex.pdf')
# c.drawImage('ar.jpg', 0, 0, 10*cm, 10*cm)
# c.showPage()
# c.save()  # https://www.reportlab.com/docs/reportlab-userguide.pdf
# https://stackoverflow.com/questions/2252726/how-to-create-pdf-files-in-python

print(f"{fg(64)}Welcome to Meal Mate{attr(0)} \n{fg(18)}'The recipe finder for your pantry items you don't know what to with!' {attr(0)}")

# Check if pantry_items.csv exists
file_name = "./pantry_list.csv"

try:
    meal_mate_file = open(file_name, "r")
    meal_mate_file.close()

except FileNotFoundError as e:
    meal_mate_file = open(file_name, "w")
    meal_mate_file.write("Ingredient,completed\n")
    meal_mate_file.close()


def create_menu():
    print(f"{fg(2)}1.{attr(0)} Enter 1 to {fg(2)}add{attr(0)} a new item to your list")
    print(f"{fg(1)}2.{attr(0)} Enter 2 to {fg(1)}remove{attr(0)} item from your list")
    print(f"{fg(90)}3.{attr(0)} Enter 3 to {fg(90)}prioritise{attr(0)} an item on your list")
    print(f"{fg(28)}4.{attr(0)} Enter 4 to {fg(28)}view{attr(0)} you ingredient list")
    print(f"{fg(111)}5.{attr(0)} Enter 5 to {fg(111)}search{attr(0)} for recipes")
    print(f"{fg(2)}6.{attr(0)} Enter 6 to {fg(2)}exit{attr(0)}")
    # local variable
    choice = input("Enter your selection: ")
    return choice


# global variable
user_choice = ""

while user_choice != "6":
    user_choice = create_menu()

    match user_choice:
        case "1":
            add_ingr(file_name)
        case "2":
            remove_ingr(file_name)
        case "3":
            prior_ingr(file_name)
        case "4":
            view_ingr(file_name)
        case "5":
            get_recipes(file_name)
        case "6":
            continue
        case _:
            print("Invalid input")

    input(f"{bg(177)}Press Enter to continue...{attr(0)}")

print(f"{bg(2)}Thank you for using Meal Mate{attr(0)}")
