"""Greet feature — first vertical slice."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name or not name.strip():
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name.strip()}!"
