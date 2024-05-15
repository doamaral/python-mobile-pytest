import pytest
import os
from dotenv import load_dotenv
load_dotenv()

def test_driver_factory(setup):
    """
    This test checks if the driver factory correctly sets up a driver instance.
    It first retrieves the driver instance from the setup fixture.
    Then it prints the platform name of the driver.
    Finally, it asserts that the driver instance is not None and that the platform name matches the expected platform name.

    Args:
        setup: A pytest fixture that sets up a driver instance.

    Raises:
        AssertionError: If the driver instance is None or the platform name does not match the expected platform name.
    """
    driver = setup
    print(f'This test is running over: {driver.__getattribute__("_platformName")}')
    assert driver is not None
    assert driver.__getattribute__('_platformName').lower() == os.getenv('PLATFORM').lower()
    