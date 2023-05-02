#!/bin/bash

printf "Installing required packages in a virtual environment"
sleep 1

# check if venv is installed
python3 -m venv meal_mate
# check if venv already exists
source meal_mate/bin/activate
python3 -m pip3 install -r requirements.txt
# macOS homebrew install for wkhtmltopdf
brew install homebrew/cask/wkhtmltopdf

clear

python3 main.py