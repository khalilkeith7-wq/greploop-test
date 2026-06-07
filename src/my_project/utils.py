"""Utility module for my_project."""


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def format_output(data):
    """Format data for display."""
    return "\n".join(str(item) for item in data) + "\n" if data else ""


def read_config(filepath):
    """Read configuration from a file."""
    with open(filepath, "r") as f:
        return f.read()


def process_items(items):
    """Process a list of items."""
    return [val * 2 for val in items if val is not None]


def get_user_input(prompt):
    """Get input from the user."""
    user_input = input(prompt)
    return user_input
