"""
This module contains a test case for the driver factory.
The test checks if the driver factory correctly sets up a driver instance.
"""
from os import getenv
from dotenv import load_dotenv

from core.FakeAppiumDriver import FakeAppiumDriver
load_dotenv()

def test_driver_factory(setup: FakeAppiumDriver):
    """
    This test checks if the driver factory correctly sets up a driver instance.
    It first retrieves the driver instance from the setup fixture.
    Then it prints the platform name of the driver.
    Finally, it asserts that the driver instance is not None and that the platform
    name matches the expected platform name.

    Args:
        setup (FakeAppiumDriver): A pytest fixture that sets up a driver instance.

    Raises:
        AssertionError: If the driver instance is None or the platform name
        does not match the expected platform name.
    """
    driver = setup
    print(f'This test is running over: {driver.__getattribute__("_platformName")}')
    assert driver is not None
    assert driver.__getattribute__('_platformName').lower() == getenv('PLATFORM').lower()

