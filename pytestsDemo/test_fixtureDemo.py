import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("I will execute steps in fixture demo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture demo2 method")

    def test_fixtureDemo3(self):
            print("I will execute steps in fixture demo3 method")

    def test_fixtureDemo3(self):
                print("I will execute steps in fixture demo3 method")