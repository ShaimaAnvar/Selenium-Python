import pytest

@pytest.mark.usefixtures("dataload")
class TestExample2:
    def test_editProfile(self,dataload):
        print(dataload[0])
        print(dataload[2])