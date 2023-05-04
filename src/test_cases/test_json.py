import pytest
import requests

# testing parsing of API information
r = requests.get(
    'https://api.spoonacular.com/recipes/findByIngredients?apiKey=3e06d892f3044bab8b766176ccd0e18c&ingredients=chicken,noodles&ranking=2&number=5')
json = r.json()


# retrieval of information to use within the displayed application
def test_json_parser():
    assert type(json[0]["id"]) == int


# calculations for if statements in the application
def test_json_length():
    assert len(json) > 0

# checking status code for request
def test_response():
    assert r.status_code == 200