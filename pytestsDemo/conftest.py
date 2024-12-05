import pytest


@pytest.fixture
def setup(scope="class"):
    print("I will execute first")
    yield
    print("I will execute last")