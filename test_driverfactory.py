import pytest
import os
from dotenv import load_dotenv

load_dotenv()

def test_driver_factory(setup):
    driver = setup
    print(f'This test is running over: {driver.__getattribute__("_platformName")}')
    assert driver is not None
    assert driver.__getattribute__('_platformName').lower() == os.getenv('PLATFORM').lower()
    