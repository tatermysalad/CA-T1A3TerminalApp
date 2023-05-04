#!/bin/bash

printf "Thanks for using Meal Mate, the required packages are now uninstalling"
sleep 1

python3 -m pip uninstall -r requirements.txt
# MacOS homebrew install for wkhtmltopdf
brew uninstall homebrew/cask/wkhtmltopdf

printf "Uninstall complete. Have a nice day!"
