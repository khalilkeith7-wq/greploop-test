"""Command-line interface for my-project."""

import argparse
import sys

from my_project.greet import greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Greet someone by name.")
    parser.add_argument("name", help="Name to greet")
    args = parser.parse_args(argv)

    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
