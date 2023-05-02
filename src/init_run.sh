#!/bin/bash

printf "Installing required packages"
sleep 1

# Install required packages
python3 -m pip install -r requirements.txt
# MacOS homebrew install for wkhtmltopdf
brew install homebrew/cask/wkhtmltopdf

clear
printf "Install complete"

python main.py
