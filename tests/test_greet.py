import pytest

from my_project.greet import greet


def test_greet_returns_formatted_message():
    assert greet("World") == "Hello, World!"


def test_greet_strips_whitespace():
    assert greet("  Alice  ") == "Hello, Alice!"


@pytest.mark.parametrize("invalid_name", ["", "   ", None])
def test_greet_rejects_empty_name(invalid_name):
    with pytest.raises(ValueError, match="non-empty"):
        greet(invalid_name)
