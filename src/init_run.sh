#!/bin/bash

printf "Installing required packages"
sleep 1

# Install required packages
python3 -m pip install -r requirements.txt
# MacOS homebrew install for wkhtmltopdf
brew install homebrew/cask/wkhtmltopdf

printf "Install complete"

python3 main.py
