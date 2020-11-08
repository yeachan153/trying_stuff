import pytest


@pytest.fixture
def fixture_1():
    return ["a"]


# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     """Remove requests.sessions.Session.request for all tests."""
#     monkeypatch.delattr("requests.sessions.Session.request")
