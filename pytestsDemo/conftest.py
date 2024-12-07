import pytest
@pytest.fixture(scope='class')
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataload():
    print("user profile data being created")
    return ["shaima","anvar","shaima@gmail.com"]

@pytest.fixture(params=[("chrome","shaima"),("firefox","EK"),"IE"])
def crossBrowser(request):
    return request.param