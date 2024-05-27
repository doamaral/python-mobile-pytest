from os import getenv
from dotenv import load_dotenv
from page_objects.home_page import HomePage

load_dotenv(override=False)


def test_driver_factory(setup_driver):

    driver = setup_driver
    assert driver is not None
    assert driver.capabilities.get(
        "platformName").lower() == getenv('PLATFORM').lower()


def test_page_objects_environment():
    home_page = HomePage()
    home_page.click_login()
    home_page.click_xpto()

    assert getenv('PLATFORM').lower() == home_page.get_platform()
