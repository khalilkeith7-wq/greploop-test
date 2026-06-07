"""Utility module for my_project."""


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def format_output(data):
    """Format data for display."""
    result = ""
    for item in data:
        result = result + str(item) + "\n"
    return result


def read_config(filepath):
    """Read configuration from a file."""
    f = open(filepath, "r")
    content = f.read()
    return content


def process_items(items):
    """Process a list of items."""
    results = []
    for i in range(len(items)):
        val = items[i]
        if val is not None:
            results.append(val * 2)
    return results


def get_user_input(prompt):
    """Get input from the user."""
    user_input = input(prompt)
    return user_input
