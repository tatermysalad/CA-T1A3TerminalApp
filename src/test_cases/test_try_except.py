import pytest

# testing try, except block for error handling
# Could not import the function as it needed an input
def exception(recipe_int_value):
    recipe_int = int(recipe_int_value)
    return recipe_int

# handles the value and throws the ValueError, this will return the person back to the menu
def test_exception():
    with pytest.raises(ValueError):
        exception("q")

def test_success():
    try:
        exception("1")
    except:
        pytest.fail("Unexpected MyError ..")


