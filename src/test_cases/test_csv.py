import pytest
import csv

test_file = "./test_file.csv"
# check if test file exists
try:
    test_file = open(test_file, "r")
    test_file.close()
except FileNotFoundError as e:
    test_file = open(test_file, "w")
    test_file.write("""Staple,In_Stock
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
    test_file.close()

def test_staple_edit_ingr():
    print(f"Modify staple item")
    # staple_view_ingr(test_file)
    ingr_title =  "Onion" # input("Enter the item that you want to check/uncheck: ")
    staple_lists = []
    with open("./test_file.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (ingr_title == row[0]):
                if row[1] == "False":
                    staple_lists.append([row[0], "True"])
                else:
                    staple_lists.append([row[0], "False"])
            else:
                staple_lists.append(row)
    with open("./test_file.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(staple_lists)
    assert len(staple_lists) > 1
