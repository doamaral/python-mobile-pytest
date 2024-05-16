import pytest
from core.driver_factory import DriverFactory

@pytest.fixture(scope='module', autouse=True)
def setup():
    """
    This is a pytest fixture that sets up a driver instance before each module.
    It uses the DriverFactory to get an instance of the driver.
    After the test module finishes, it cleans up the driver instance.

    Yields:
        driver: An instance of the driver.
    """
    driver = DriverFactory.get_instance()
    yield driver