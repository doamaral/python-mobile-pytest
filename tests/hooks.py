import pytest
import logging
from core.driver_factory import DriverFactory
from utils.logger import logger

log = logger(logging.DEBUG)


@pytest.fixture(scope='module', autouse=True)
def setup_driver():
    """
    This is a pytest fixture that sets up a driver instance before each module.
    It uses the DriverFactory to get an instance of the driver.
    After the test module finishes, it cleans up the driver instance.

    Yields:
        driver: An instance of the driver.
    """
    log.info('setup driver before all tests in the module')
    driver = DriverFactory.get_instance()
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def before_each(request):
    log.info('running test: %s', request.node.name)
