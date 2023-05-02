import pytest

# testing try, except block for error handling
# Could not import the function as it needed an input
def exception(recipe_int_value):
    recipe_int = int(recipe_int_value)
    return recipe_int

# handles the value
def test_exception():
    with pytest.raises(ValueError):
        exception("q")


