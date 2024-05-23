from os import getenv
from dotenv import load_dotenv
from page_objects.home_page import HomePage
from utils.mock_appium_driver import MockAppiumDriver

load_dotenv(override=False)


def test_driver_factory(setup_driver: MockAppiumDriver):

    driver = setup_driver
    print(f'[test_driver_factory] This test is running over: {
          driver.get_platform_name()}')
    assert driver is not None
    assert driver.get_platform_name().lower() == getenv('PLATFORM').lower()


def test_page_objects_environment():
    home_page = HomePage()
    home_page.click_login()
    assert getenv('PLATFORM').lower() == home_page.get_platform()
