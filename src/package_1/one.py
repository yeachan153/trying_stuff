import json
from package_2.two import g
from pathlib import Path


def f():
    with open("src/test.json") as f:
        file = json.load(f)
    return file


def is_palindrome(s):
    return s == s[::-1]


def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"