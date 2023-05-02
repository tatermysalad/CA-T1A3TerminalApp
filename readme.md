# T1A3 Python Terminal Application

## Links

---

[GitHub](https://github.com/tatermysalad/T1A3TerminalApp)
<br>

[Trello](https://trello.com/invite/b/FUrubUml/ATTI813af372e91184f1cef364b2ca77be1493A1819C/t1a3terminalapp)
<br>

[Video Presentation](https://youtube.com)

## Style guide

---

[Python Style Guide - Python Enhancement Proposal 8](https://peps.python.org/pep-0008/)

## Proposal

---

An application which can take an editable list of items and supply a list of recipes for those items

## App Features:

---

### Checklist of staple ingredients

Instead of having to add garlic, ginger, salt, pepper, etc. This will be a quick yes/no list for those ingredients

### Editable list of ingredients

This will be stored as a csv, with options to add, remove, view, clear. It will store the main ingredients, ie. protein, vegetables, etc.

### Fetch a list of recipes via API

The list of recipes from an external source

### Export recipe from CLI to PDF.

Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

-   use of variables and the concept of variable scope
-   loops and conditional control structures
-   error handling

Consult with your educator to check your features are sufficient .

## Help documentation

---

### System/Hardware requirements:

-   Requires Python Version 3.10.x or later to be installed
-   Requires MacOS
-   Requires an internet connection
-   Requires homebrew to install a dependency in the run.sh file
-   Tested working on MacOS 13.1.1

### Installation Instructions

1. Open a terminal window in your Macintosh computer
2. Navigate to the source (src) folder of the program
3. Run: (this will install the required modules and run the application)

```zsh
./init_run.sh
```

4. The application is now running.
5. Two '.csv' files which will be created on first run. These will be the location of staple and pantry ingredients. You can edit this either within the application or outside if preferred.

### Uninstall Instructions

1. Navigate to the source (src) folder of the program
2. Run: (this may require some user input)

```zsh
./uninstall.sh
```

3. The packages should now be uninstalled

### How to use

1. The main menu is navigated with numerical input, ie. entering the number 8 will exit the application.
   ![Main Menu](./docs/Main_menu.png)
2. Each heading has options below to view, add, and remove/ignore the lists.
3. Viewing the lists will present the overview of the Pantry items, or this will show the 'in stock' staple items.
   ![View staple list](./docs/staple_list.png)
4. After viewing you will need to press the 'Enter' key to return to the main menu.
5. To add a value to the ingredient list enter the name of the ingredient, make sure to spell this correctly.
6. To change a values availability enter its name as it is shown and the value with alternate between 'in stock' and 'out of stock'
   ![Edit staple list](./docs/staple_item_change.png)
7. To remove an ingredient enter the name as it is shown, similar to alternating a value in the staple items
8. To ignore the staple items in the search for recipes press number '6' from the main menu, then enter 'y' for yes and 'n' for no. The current option will be displayed after the entry.
9. To search for recipes with the options presented press number '7'. This will display 5 recipes ordered by the least amount of missing ingredients.
   ![Search](./docs/search.png)
10. After this list you can view more details about a particular recipe, from index 1 to 5.
11. You can also export the option in a similar way. This export will be created in the source (src) folder.

## References

---

All utilised sources:

https://pypi.org
https://docs.python.org
https://requests.readthedocs.io/en/latest/user/quickstart/#response-content
https://stackoverflow.com
https://www.w3schools.com/
