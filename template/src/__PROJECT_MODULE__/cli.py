"""Command-line entry point."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="{{PROJECT_NAME}} command line")
    parser.add_argument("name", nargs="?", default="world", help="name to greet")
    return parser


def main(argv: list[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    print(f"Hello, {arguments.name}!")
    return 0
