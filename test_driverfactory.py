import pytest

def test_driver_factory(setup):
    print('Test')
    driver = setup
    assert driver is not None
    