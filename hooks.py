import pytest
from core.DriverFactory import DriverFactory

@pytest.fixture(scope='module', autouse=True)
def setup():
    print('Before All')
    driver = DriverFactory.get_instance()
    yield driver