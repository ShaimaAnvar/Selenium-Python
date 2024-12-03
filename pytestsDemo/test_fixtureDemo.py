import pytest


@pytest.fixture
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo method")
