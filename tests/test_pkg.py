from package_1.one import f, is_palindrome, getssh
from pathlib import Path
import pytest
import requests


def test_f():
    assert isinstance(f(), dict)


def test_fixture(fixture_1):
    print(fixture_1)
    assert isinstance(fixture_1, list)


@pytest.mark.parametrize(
    "palindrome",
    ["", "a", "bob"],
)  # All list items are tested
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", False),
        ("Never odd or even", False),
        ("Do geese see God?", False),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


def test_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():  # Some function to return what we want
        return Path("/abc")

    # Set Path.home() to the same as calling mockreturn()
    monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn now
    x = getssh()
    requests.get("http://google.com")
    assert x == Path("/abc/.ssh")
