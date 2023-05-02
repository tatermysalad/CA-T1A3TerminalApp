#!/bin/bash

# check if python is installed
python3 -m venv meal_mate
# check if venv already exists
source3 meal_mate/bin/activate
python3 -m pip3 install -r requirements.txt
# macOS homebrew install for wkhtmltopdf
brew install homebrew/cask/wkhtmltopdf
clear
python3 src/main.py